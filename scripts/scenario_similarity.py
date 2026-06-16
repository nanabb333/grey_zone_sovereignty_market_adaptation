#!/usr/bin/env python3
"""Compare example geopolitical scenarios with historical coded events."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
EVENTS_PATH = REPO_ROOT / "data" / "events_v2.csv"
NEWS_PATH = REPO_ROOT / "data" / "news" / "news_events.csv"
MARKET_PATH = REPO_ROOT / "results" / "event_abnormal_return_summary.csv"
RESULTS_DIR = REPO_ROOT / "results"
JSON_OUTPUT_PATH = RESULTS_DIR / "scenario_similarity_results.json"
MD_OUTPUT_PATH = RESULTS_DIR / "scenario_similarity_results.md"

EVENT_REQUIRED_COLUMNS = [
    "date",
    "event_name",
    "event_category",
    "brief_description",
    "surprise_rationale",
    "event_family",
    "event_repetition_level",
]
NEWS_REQUIRED_COLUMNS = [
    "news_id",
    "date",
    "related_event_id",
    "event_family",
    "actor",
    "geography",
    "summary",
]
MARKET_REQUIRED_COLUMNS = ["event_name", "event_date"]
PREFERRED_CAR_COLUMNS = ["tsmc_car_7", "tsmc_car_3", "twse_car_7", "twse_car_3"]

DASHBOARD_EVENT_ALIASES = {
    "e001": "Pelosi Visit",
    "e002": "Joint Sword 2023",
    "e003": "Joint Sword-2024A",
    "e004": "NVIDIA Taiwan AI Factory",
}

STOPWORDS = {
    "a",
    "an",
    "and",
    "around",
    "by",
    "for",
    "from",
    "in",
    "near",
    "new",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
}

SCENARIOS = [
    {
        "scenario_id": "S001",
        "scenario_text": "large-scale military exercises near Taiwan",
        "event_family": "Military_Exercise",
        "actors": ["PRC", "PLA", "China", "Taiwan"],
        "geographies": ["Taiwan Strait", "Taiwan"],
    },
    {
        "scenario_id": "S002",
        "scenario_text": "new semiconductor export control restrictions",
        "event_family": "Export_Control",
        "actors": ["United States", "China", "PRC"],
        "geographies": ["United States", "Global semiconductor supply chain"],
    },
    {
        "scenario_id": "S003",
        "scenario_text": "high-level diplomatic visit involving Taiwan",
        "event_family": "Diplomatic_Shock",
        "actors": ["United States", "Taiwan", "PRC"],
        "geographies": ["Taiwan", "Taiwan Strait"],
    },
    {
        "scenario_id": "S004",
        "scenario_text": "grey-zone naval and air pressure around Taiwan",
        "event_family": "Military_Exercise",
        "actors": ["PRC", "PLA", "China", "Taiwan"],
        "geographies": ["Taiwan Strait", "Taiwan"],
    },
    {
        "scenario_id": "S005",
        "scenario_text": "strategic chip investment or state support announcement",
        "event_family": "Strategic_Investment",
        "actors": ["TSMC", "United States", "Taiwan"],
        "geographies": ["United States", "Taiwan", "Global semiconductor supply chain"],
    },
    {
        "scenario_id": "S006",
        "scenario_text": "supply-chain disruption risk linked to cross-strait tensions",
        "event_family": "Economic_Coercion",
        "actors": ["PRC", "China", "Taiwan"],
        "geographies": ["Taiwan Strait", "Taiwan", "Global semiconductor supply chain"],
    },
]


def read_csv(
    path: Path,
    required_columns: list[str],
    optional: bool = False,
) -> list[dict[str, str]]:
    if optional and not path.exists():
        return []
    if not path.exists():
        raise FileNotFoundError(f"Missing input file: {path}")

    with path.open("r", newline="", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames or []
        missing = [column for column in required_columns if column not in fieldnames]
        if missing:
            raise ValueError(f"{path} is missing required column(s): {', '.join(missing)}")
        return list(reader)


def normalize_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def tokenize(value: str) -> set[str]:
    return {
        token
        for token in normalize_text(value).split()
        if len(token) > 2 and token not in STOPWORDS
    }


def normalize_family(value: str) -> str:
    return value.strip().replace(" ", "_")


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


def event_key(row: dict[str, str]) -> str:
    return normalize_text(f"{row.get('date', '')} {row.get('event_name', '')}")


def event_name_key(name: str) -> str:
    return normalize_text(name)


def news_candidate_keys(row: dict[str, str]) -> list[str]:
    related = row.get("related_event_id", "").strip()
    date = row.get("date", "").strip()
    alias = DASHBOARD_EVENT_ALIASES.get(related.lower())
    keys = []
    if alias:
        keys.append(event_name_key(alias))
    keys.append(event_name_key(related))
    keys.append(normalize_text(f"{date} {related}"))
    return [key for key in keys if key]


def build_event_indexes(
    events: list[dict[str, str]],
) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]], dict[str, list[dict[str, str]]]]:
    by_name: dict[str, dict[str, str]] = {}
    by_full_key: dict[str, dict[str, str]] = {}
    by_date: dict[str, list[dict[str, str]]] = defaultdict(list)

    for index, event in enumerate(events, start=1):
        event["event_family"] = normalize_family(event["event_family"])
        event["event_id"] = event.get("event_id", "").strip() or f"EV{index:03d}"
        by_name[event_name_key(event["event_name"])] = event
        by_full_key[event_key(event)] = event
        by_date[event["date"]].append(event)

    return by_name, by_full_key, by_date


def link_news_to_events(
    news_rows: list[dict[str, str]],
    events_by_name: dict[str, dict[str, str]],
    events_by_full_key: dict[str, dict[str, str]],
    events_by_date: dict[str, list[dict[str, str]]],
) -> dict[str, list[dict[str, str]]]:
    linked_news: dict[str, list[dict[str, str]]] = defaultdict(list)

    for news in news_rows:
        matched_event: dict[str, str] | None = None
        for key in news_candidate_keys(news):
            matched_event = events_by_name.get(key) or events_by_full_key.get(key)
            if matched_event is not None:
                break

        if matched_event is None:
            same_day_events = events_by_date.get(news.get("date", "").strip(), [])
            if len(same_day_events) == 1:
                matched_event = same_day_events[0]

        if matched_event is not None:
            linked_news[event_key(matched_event)].append(news)

    return dict(linked_news)


def build_market_context(
    market_rows: list[dict[str, str]],
    events_by_name: dict[str, dict[str, str]],
    events_by_full_key: dict[str, dict[str, str]],
) -> tuple[dict[str, dict[str, Any]], str | None]:
    car_column = select_car_column(market_rows)
    context: dict[str, dict[str, Any]] = {}
    if car_column is None:
        return context, None

    for market in market_rows:
        key = normalize_text(f"{market.get('event_date', '')} {market.get('event_name', '')}")
        event = events_by_full_key.get(key) or events_by_name.get(
            event_name_key(market.get("event_name", ""))
        )
        car_value = parse_float(market.get(car_column))
        if event is not None and car_value is not None:
            context[event_key(event)] = {
                "metric": car_column,
                "value": round(car_value, 4),
                "label": (
                    f"{car_column}={round(car_value, 4)} "
                    "(historical descriptive market reaction)"
                ),
            }

    return context, car_column


def linked_news_terms(news_items: list[dict[str, str]], column: str) -> set[str]:
    terms: set[str] = set()
    for item in news_items:
        values = re.split(r";|,", item.get(column, ""))
        terms.update(normalize_text(value) for value in values if normalize_text(value))
    return terms


def scenario_terms(scenario: dict[str, Any], column: str) -> set[str]:
    return {normalize_text(value) for value in scenario[column] if normalize_text(value)}


def score_event(
    scenario: dict[str, Any],
    event: dict[str, str],
    news_items: list[dict[str, str]],
    market_context: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    scenario_tokens = tokenize(scenario["scenario_text"])
    event_tokens = tokenize(
        " ".join(
            [
                event.get("event_name", ""),
                event.get("event_category", ""),
                event.get("brief_description", ""),
                event.get("surprise_rationale", ""),
                event.get("event_family", ""),
                " ".join(item.get("summary", "") for item in news_items),
            ]
        )
    )
    overlap = sorted(scenario_tokens & event_tokens)
    keyword_score = min(len(overlap) * 8, 40)

    family_match = scenario["event_family"] == event["event_family"]
    family_score = 25 if family_match else 0

    actor_overlap = sorted(
        scenario_terms(scenario, "actors") & linked_news_terms(news_items, "actor")
    )
    actor_score = min(len(actor_overlap) * 5, 15)

    geography_overlap = sorted(
        scenario_terms(scenario, "geographies") & linked_news_terms(news_items, "geography")
    )
    geography_score = min(len(geography_overlap) * 5, 10)

    news_score = min(len(news_items) * 3, 10)
    surprise_score = {"High": 5, "Medium": 3, "Low": 1}.get(
        event.get("surprise_score", ""),
        0,
    )
    repetition_level = parse_float(event.get("event_repetition_level"))
    repetition_score = 3 if repetition_level is not None and repetition_level >= 3 else 0
    total_score = (
        keyword_score
        + family_score
        + actor_score
        + geography_score
        + news_score
        + surprise_score
        + repetition_score
    )
    historical_market_reaction = market_context.get(event_key(event))

    return {
        "event_id": event["event_id"],
        "event_name": event["event_name"],
        "event_title": event["event_name"],
        "event_date": event["date"],
        "event_family": event["event_family"],
        "event_category": event["event_category"],
        "event_description": event["brief_description"],
        "similarity_score": total_score,
        "linked_news_evidence_count": len(news_items),
        "linked_news_count": len(news_items),
        "historical_market_reaction": historical_market_reaction,
        "score_components": {
            "keyword_overlap": keyword_score,
            "event_family_match": family_score,
            "actor_match": actor_score,
            "geography_match": geography_score,
            "news_evidence_count": news_score,
            "surprise_score": surprise_score,
            "repetition_level": repetition_score,
        },
        "matched_terms": overlap,
        "matched_keywords": overlap,
        "matched_actors": actor_overlap,
        "matched_geographies": geography_overlap,
        "context_note": (
            "Historical similarity result for scenario comparison and context retrieval. "
            "Historical similarity is not a forecast or investment signal."
        ),
        "cautious_interpretation": (
            "This match identifies a historically comparable coded event. Any market "
            "reaction shown is historical descriptive context only."
        ),
    }


def run_similarity(
    events: list[dict[str, str]],
    linked_news: dict[str, list[dict[str, str]]],
    market_context: dict[str, dict[str, Any]],
    car_metric: str | None,
) -> dict[str, Any]:
    scenario_results = []
    for scenario in SCENARIOS:
        scored_events = [
            score_event(
                scenario,
                event,
                linked_news.get(event_key(event), []),
                market_context,
            )
            for event in events
        ]
        top_matches = sorted(
            scored_events,
            key=lambda item: (
                item["similarity_score"],
                item["linked_news_evidence_count"],
                item["event_date"],
            ),
            reverse=True,
        )[:3]
        scenario_results.append(
            {
                "scenario_id": scenario["scenario_id"],
                "scenario_text": scenario["scenario_text"],
                "scenario_title": scenario["scenario_text"].title(),
                "scenario_event_family": scenario["event_family"],
                "top_matches": top_matches,
                "interpretation_note": (
                    "Use these matches as historical context for analyst review. "
                    "Similarity scores are transparent rule-based retrieval aids, "
                    "not future-market estimates."
                ),
                "caution_label": "Historical similarity is not a forecast or investment signal.",
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
        "historical_car_metric": car_metric,
        "scoring_method": {
            "keyword_overlap_max": 40,
            "event_family_match_max": 25,
            "actor_match_max": 15,
            "geography_match_max": 10,
            "news_evidence_count_max": 10,
            "surprise_score_max": 5,
            "repetition_level_max": 3,
            "nominal_max_similarity_score": 108,
        },
        "scenarios": scenario_results,
        "method_note": (
            "Scenario comparison uses keyword overlap, event-family match, actor match, "
            "geography match, and linked news evidence count to retrieve similar "
            "historical coded events."
        ),
        "use_limits": [
            "Historical similarity and context retrieval only.",
            "Scores are rule-based and require analyst review.",
            "Historical CAR patterns should not be treated as future-market estimates.",
            "News evidence rows may include placeholder source metadata pending verification.",
        ],
    }


def render_markdown(results: dict[str, Any]) -> str:
    lines = [
        "# Scenario Similarity Results",
        "",
        str(results["method_note"]),
        "",
        "The layer supports historical similarity analysis, context retrieval, and scenario comparison. It does not estimate future market outcomes.",
        "",
    ]

    for scenario in results["scenarios"]:
        lines.extend(
            [
                f"## {scenario['scenario_id']}: {scenario['scenario_text']}",
                "",
                f"- Scenario event family: `{scenario['scenario_event_family']}`",
                f"- Interpretation: {scenario['interpretation_note']}",
                "",
                "| Rank | Historical Event | Date | Event Family | Similarity Score | Linked News | Historical CAR Context |",
                "|---:|---|---|---|---:|---:|---|",
            ]
        )
        for index, match in enumerate(scenario["top_matches"], start=1):
            car_context = match["historical_market_reaction"]["label"] if match["historical_market_reaction"] else "N/A"
            lines.append(
                "| {rank} | {event_name} | {event_date} | {event_family} | "
                "{similarity_score} | {linked_news_evidence_count} | {car_context} |".format(
                    rank=index,
                    car_context=car_context,
                    **match,
                )
            )
        lines.append("")

    lines.extend(["## Use Limits", ""])
    lines.extend(f"- {limit}" for limit in results["use_limits"])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    events = read_csv(EVENTS_PATH, EVENT_REQUIRED_COLUMNS)
    news_rows = read_csv(NEWS_PATH, NEWS_REQUIRED_COLUMNS)
    market_rows = read_csv(MARKET_PATH, MARKET_REQUIRED_COLUMNS, optional=True)
    events_by_name, events_by_full_key, events_by_date = build_event_indexes(events)
    linked_news = link_news_to_events(
        news_rows,
        events_by_name,
        events_by_full_key,
        events_by_date,
    )
    market_context, car_metric = build_market_context(
        market_rows,
        events_by_name,
        events_by_full_key,
    )
    results = run_similarity(events, linked_news, market_context, car_metric)

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT_PATH.write_text(
        json.dumps(results, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    MD_OUTPUT_PATH.write_text(render_markdown(results), encoding="utf-8")

    print(f"Compared {len(results['scenarios'])} example scenarios.")
    print(f"Wrote {JSON_OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"Wrote {MD_OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
