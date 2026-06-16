#!/usr/bin/env python3
"""Build summary outputs for the curated news evidence database."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from statistics import mean


REQUIRED_COLUMNS = [
    "news_id",
    "date",
    "source",
    "title",
    "url",
    "related_event_id",
    "event_family",
    "actor",
    "geography",
    "summary",
    "relevance_score",
    "coding_notes",
]

REPO_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = REPO_ROOT / "data" / "news" / "news_events.csv"
RESULTS_DIR = REPO_ROOT / "results"
JSON_OUTPUT_PATH = RESULTS_DIR / "news_database_summary.json"
MD_OUTPUT_PATH = RESULTS_DIR / "news_database_summary.md"


def read_news_events(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing news database input: {path}")

    with path.open("r", newline="", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file)
        missing_columns = [
            column for column in REQUIRED_COLUMNS if column not in (reader.fieldnames or [])
        ]
        if missing_columns:
            missing = ", ".join(missing_columns)
            raise ValueError(f"Missing required column(s): {missing}")

        rows = list(reader)

    for row in rows:
        news_id = row.get("news_id", "UNKNOWN")
        try:
            score = float(row["relevance_score"])
        except ValueError as exc:
            raise ValueError(
                f"Invalid relevance_score for {news_id}: {row['relevance_score']}"
            ) from exc
        if score < 0 or score > 1:
            raise ValueError(f"relevance_score must be between 0 and 1 for {news_id}")

    return rows


def count_values(rows: list[dict[str, str]], column: str) -> dict[str, int]:
    return dict(sorted(Counter(row[column] for row in rows).items()))


def build_summary(rows: list[dict[str, str]]) -> dict[str, object]:
    relevance_scores = [float(row["relevance_score"]) for row in rows]

    return {
        "input_file": str(INPUT_PATH.relative_to(REPO_ROOT)),
        "news_item_count": len(rows),
        "count_by_event_family": count_values(rows, "event_family"),
        "count_by_actor": count_values(rows, "actor"),
        "count_by_geography": count_values(rows, "geography"),
        "average_relevance_score": round(mean(relevance_scores), 3)
        if relevance_scores
        else None,
        "method_note": (
            "Curated news-evidence starter layer for analyst review. "
            "Outputs enrich source traceability and do not replace event-study design."
        ),
        "use_limits": [
            "Curated dataset, not exhaustive.",
            "Placeholder rows require exact source verification before publication.",
            "Not investment advice, forecasting, or automated causal analysis.",
        ],
    }


def render_markdown(summary: dict[str, object]) -> str:
    def render_counts(title: str, counts: dict[str, int]) -> str:
        lines = [f"## {title}", "", "| Category | Count |", "|---|---:|"]
        lines.extend(f"| {category} | {count} |" for category, count in counts.items())
        return "\n".join(lines)

    sections = [
        "# News Evidence Database Summary",
        "",
        f"- Input file: `{summary['input_file']}`",
        f"- News items: {summary['news_item_count']}",
        f"- Average relevance score: {summary['average_relevance_score']}",
        "",
        str(summary["method_note"]),
        "",
        render_counts(
            "Count By Event Family",
            summary["count_by_event_family"],  # type: ignore[arg-type]
        ),
        "",
        render_counts("Count By Actor", summary["count_by_actor"]),  # type: ignore[arg-type]
        "",
        render_counts(
            "Count By Geography",
            summary["count_by_geography"],  # type: ignore[arg-type]
        ),
        "",
        "## Use Limits",
        "",
    ]
    sections.extend(f"- {limit}" for limit in summary["use_limits"])  # type: ignore[union-attr]
    sections.append("")
    return "\n".join(sections)


def main() -> None:
    rows = read_news_events(INPUT_PATH)
    summary = build_summary(rows)

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT_PATH.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    MD_OUTPUT_PATH.write_text(render_markdown(summary), encoding="utf-8")

    print(f"Validated {summary['news_item_count']} news evidence rows.")
    print(f"Wrote {JSON_OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"Wrote {MD_OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
