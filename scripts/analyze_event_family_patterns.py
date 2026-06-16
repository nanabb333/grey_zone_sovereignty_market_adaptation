#!/usr/bin/env python3
"""Summarize descriptive event-family patterns across events, news, and CARs."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
EVENTS_PATH = REPO_ROOT / "data" / "events_v2.csv"
NEWS_PATH = REPO_ROOT / "data" / "news" / "news_events.csv"
MARKET_PATH = REPO_ROOT / "results" / "event_abnormal_return_summary.csv"
RESULTS_DIR = REPO_ROOT / "results"
CSV_OUTPUT_PATH = RESULTS_DIR / "event_family_summary.csv"
JSON_OUTPUT_PATH = RESULTS_DIR / "event_family_summary.json"
MD_OUTPUT_PATH = RESULTS_DIR / "event_family_summary.md"

EVENT_REQUIRED_COLUMNS = ["date", "event_name", "event_family"]
NEWS_REQUIRED_COLUMNS = ["news_id", "date", "related_event_id", "event_family"]
MARKET_REQUIRED_COLUMNS = ["event_name", "event_date"]
PREFERRED_CAR_COLUMNS = [
    "tsmc_car_7",
    "car_percent",
    "car_value",
    "tsmc_car_3",
    "twse_car_7",
    "twse_car_3",
]


def read_csv(path: Path, required_columns: list[str], optional: bool = False) -> list[dict[str, str]]:
    if optional and not path.exists():
        return []
    if not path.exists():
        raise FileNotFoundError(f"Missing input file: {path}")

    with path.open("r", newline="", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames or []
        missing_columns = [column for column in required_columns if column not in fieldnames]
        if missing_columns:
            missing = ", ".join(missing_columns)
            raise ValueError(f"{path} is missing required column(s): {missing}")
        return list(reader)


def normalize_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def normalize_family(value: str) -> str:
    return value.strip().replace(" ", "_")


def event_lookup_keys(row: dict[str, str]) -> set[str]:
    date = row.get("date", "").strip()
    name = row.get("event_name", "").strip()
    event_id = row.get("event_id", "").strip()
    keys = {normalize_text(event_id), normalize_text(name), normalize_text(f"{date} {name}")}
    return {key for key in keys if key}


def news_lookup_keys(row: dict[str, str]) -> set[str]:
    date = row.get("date", "").strip()
    related = row.get("related_event_id", "").strip()
    keys = {normalize_text(related)}
    if related and not related.upper().startswith("E"):
        keys.add(normalize_text(f"{date} {related}"))
    return {key for key in keys if key}


def parse_float(value: str | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def select_car_column(market_rows: list[dict[str, str]]) -> str | None:
    if not market_rows:
        return None
    fieldnames = set(market_rows[0].keys())
    for column in PREFERRED_CAR_COLUMNS:
        if column in fieldnames:
            return column
    return None


def build_event_index(events: list[dict[str, str]]) -> tuple[dict[str, dict[str, str]], dict[str, list[dict[str, str]]]]:
    by_key: dict[str, dict[str, str]] = {}
    by_date: dict[str, list[dict[str, str]]] = defaultdict(list)
    for event in events:
        event["event_family"] = normalize_family(event["event_family"])
        for key in event_lookup_keys(event):
            by_key[key] = event
        by_date[event["date"]].append(event)
    return by_key, by_date


def link_news_to_events(
    news_rows: list[dict[str, str]],
    event_by_key: dict[str, dict[str, str]],
    events_by_date: dict[str, list[dict[str, str]]],
) -> dict[str, int]:
    linked_news_counts: Counter[str] = Counter()

    for news in news_rows:
        matched_event: dict[str, str] | None = None
        for key in news_lookup_keys(news):
            if key in event_by_key:
                matched_event = event_by_key[key]
                break

        if matched_event is None:
            same_day_events = events_by_date.get(news.get("date", "").strip(), [])
            if len(same_day_events) == 1:
                matched_event = same_day_events[0]

        if matched_event is not None:
            linked_news_counts[matched_event["event_family"]] += 1

    return dict(linked_news_counts)


def link_market_to_events(
    market_rows: list[dict[str, str]],
    event_by_key: dict[str, dict[str, str]],
    car_column: str | None,
) -> dict[str, list[float]]:
    family_cars: dict[str, list[float]] = defaultdict(list)
    if car_column is None:
        return family_cars

    for market in market_rows:
        event_id_key = normalize_text(market.get("event_id", ""))
        key = normalize_text(f"{market.get('event_date', '')} {market.get('event_name', '')}")
        event = (
            event_by_key.get(event_id_key)
            or event_by_key.get(key)
            or event_by_key.get(normalize_text(market.get("event_name", "")))
        )
        car = parse_float(market.get(car_column))
        if event is not None and car is not None:
            family_cars[event["event_family"]].append(car)

    return family_cars


def summarize(
    events: list[dict[str, str]],
    linked_news_counts: dict[str, int],
    family_cars: dict[str, list[float]],
    car_column: str | None,
) -> dict[str, Any]:
    event_counts = Counter(event["event_family"] for event in events)
    rows: list[dict[str, Any]] = []

    for family in sorted(event_counts):
        cars = family_cars.get(family, [])
        rows.append(
            {
                "event_family": family,
                "event_count": event_counts[family],
                "linked_news_count": linked_news_counts.get(family, 0),
                "car_observation_count": len(cars),
                "car_metric": car_column or "",
                "average_car": round(mean(cars), 4) if cars else "",
                "median_car": round(median(cars), 4) if cars else "",
                "min_car": round(min(cars), 4) if cars else "",
                "max_car": round(max(cars), 4) if cars else "",
                "positive_car_count": sum(1 for car in cars if car > 0),
                "negative_car_count": sum(1 for car in cars if car < 0),
                "interpretation_note": (
                    "Descriptive event-family summary for analyst review; not causal, "
                    "predictive, or investment guidance."
                ),
            }
        )

    return {
        "input_files": {
            "events": str(EVENTS_PATH.relative_to(REPO_ROOT)),
            "news": str(NEWS_PATH.relative_to(REPO_ROOT)),
            "market_reactions": str(MARKET_PATH.relative_to(REPO_ROOT))
            if MARKET_PATH.exists()
            else None,
        },
        "car_metric": car_column,
        "event_families_covered": len(rows),
        "summaries": rows,
        "method_note": (
            "Events are grouped by data/events_v2.csv event_family. News evidence "
            "is linked by related_event_id, dated event labels, or conservative "
            "single-event date matches. Market reactions are linked by event name "
            "and date where available."
        ),
        "use_limits": [
            "Descriptive pattern analysis only.",
            "Not a causal estimate or forecast.",
            "Not investment advice or trading guidance.",
            "Requires analyst review of event coding and news-source links.",
        ],
    }


def write_csv(rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "event_family",
        "event_count",
        "linked_news_count",
        "car_observation_count",
        "car_metric",
        "average_car",
        "median_car",
        "min_car",
        "max_car",
        "positive_car_count",
        "negative_car_count",
        "interpretation_note",
    ]
    with CSV_OUTPUT_PATH.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def render_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Event Family Analytics Summary",
        "",
        f"- Event families covered: {summary['event_families_covered']}",
        f"- CAR metric: `{summary['car_metric'] or 'not available'}`",
        "",
        str(summary["method_note"]),
        "",
        "| Event Family | Events | Linked News | Avg CAR | Median CAR | Min CAR | Max CAR | Positive | Negative |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary["summaries"]:
        lines.append(
            "| {event_family} | {event_count} | {linked_news_count} | {average_car} | "
            "{median_car} | {min_car} | {max_car} | {positive_car_count} | "
            "{negative_car_count} |".format(**row)
        )

    lines.extend(
        [
            "",
            "## Interpretation Boundary",
            "",
            "This output summarizes descriptive patterns by geopolitical event family. "
            "It does not estimate causality, predict markets, or provide investment advice.",
            "",
            "## Use Limits",
            "",
        ]
    )
    lines.extend(f"- {limit}" for limit in summary["use_limits"])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    events = read_csv(EVENTS_PATH, EVENT_REQUIRED_COLUMNS)
    news_rows = read_csv(NEWS_PATH, NEWS_REQUIRED_COLUMNS)
    market_rows = read_csv(MARKET_PATH, MARKET_REQUIRED_COLUMNS, optional=True)

    event_by_key, events_by_date = build_event_index(events)
    car_column = select_car_column(market_rows)
    linked_news_counts = link_news_to_events(news_rows, event_by_key, events_by_date)
    family_cars = link_market_to_events(market_rows, event_by_key, car_column)
    summary = summarize(events, linked_news_counts, family_cars, car_column)

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(summary["summaries"])
    JSON_OUTPUT_PATH.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    MD_OUTPUT_PATH.write_text(render_markdown(summary), encoding="utf-8")

    print(f"Analyzed {len(events)} events across {summary['event_families_covered']} families.")
    print(f"Linked news items counted: {sum(linked_news_counts.values())}")
    print(f"CAR metric: {car_column or 'not available'}")
    print(f"Wrote {CSV_OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"Wrote {JSON_OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"Wrote {MD_OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
