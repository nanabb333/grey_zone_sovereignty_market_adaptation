#!/usr/bin/env python3
"""Validate core data integrity for the intelligence prototype."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
EVENTS_PATH = REPO_ROOT / "data" / "events_v2.csv"
NEWS_PATH = REPO_ROOT / "data" / "news" / "news_events.csv"
RESULTS_DIR = REPO_ROOT / "results"
JSON_OUTPUT_PATH = RESULTS_DIR / "data_validation_report.json"
MD_OUTPUT_PATH = RESULTS_DIR / "data_validation_report.md"

EVENT_CRITICAL_FIELDS = [
    "event_id",
    "date",
    "event_name",
    "event_category",
    "mechanism",
    "event_family",
]
NEWS_CRITICAL_FIELDS = [
    "news_id",
    "date",
    "source",
    "title",
    "related_event_id",
    "event_family",
    "summary",
    "relevance_score",
]
EVENT_FAMILY_ALLOWED = {
    "Diplomatic_Shock",
    "Economic_Coercion",
    "Export_Control",
    "Legal_Judicial_Signaling",
    "Military_Exercise",
    "Political_Signaling",
    "Strategic_Investment",
}
NEWS_FAMILY_ALLOWED = {
    "Diplomatic Shock",
    "Diplomatic Tension",
    "Military Demonstration",
    "Policy Response",
    "Semiconductor Supply Chain",
    "Technology Competition",
}
EVENT_ID_PATTERN = re.compile(r"^E\d{3}$")


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing required data file: {path}")
    with path.open("r", newline="", encoding="utf-8") as input_file:
        return list(csv.DictReader(input_file))


def blank(value: str | None) -> bool:
    return value is None or value.strip() == ""


def duplicate_values(values: list[str]) -> list[str]:
    return sorted(value for value, count in Counter(values).items() if count > 1)


def validate_rows_have_fields(
    rows: list[dict[str, str]],
    fields: list[str],
    id_field: str,
) -> list[dict[str, str]]:
    issues = []
    for index, row in enumerate(rows, start=1):
        missing = [field for field in fields if blank(row.get(field))]
        if missing:
            issues.append(
                {
                    "row": str(index),
                    "record_id": row.get(id_field, ""),
                    "missing_fields": ", ".join(missing),
                }
            )
    return issues


def validate_project_data() -> dict[str, Any]:
    events = read_csv(EVENTS_PATH)
    news_rows = read_csv(NEWS_PATH)
    event_ids = [row.get("event_id", "").strip() for row in events]
    news_ids = [row.get("news_id", "").strip() for row in news_rows]
    event_id_set = set(event_ids)

    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []

    missing_event_id_rows = [
        {"row": index, "event_name": row.get("event_name", "")}
        for index, row in enumerate(events, start=1)
        if blank(row.get("event_id"))
    ]
    if missing_event_id_rows:
        errors.append({"check": "missing_event_id", "records": missing_event_id_rows})

    duplicate_event_ids = duplicate_values([event_id for event_id in event_ids if event_id])
    if duplicate_event_ids:
        errors.append({"check": "duplicate_event_id", "event_ids": duplicate_event_ids})

    invalid_event_ids = [
        event_id for event_id in event_ids if event_id and not EVENT_ID_PATTERN.match(event_id)
    ]
    if invalid_event_ids:
        errors.append({"check": "invalid_event_id_format", "event_ids": invalid_event_ids})

    missing_event_fields = validate_rows_have_fields(
        events,
        EVENT_CRITICAL_FIELDS,
        "event_id",
    )
    if missing_event_fields:
        errors.append({"check": "missing_event_critical_fields", "records": missing_event_fields})

    duplicate_news_ids = duplicate_values([news_id for news_id in news_ids if news_id])
    if duplicate_news_ids:
        errors.append({"check": "duplicate_news_id", "news_ids": duplicate_news_ids})

    missing_news_fields = validate_rows_have_fields(
        news_rows,
        NEWS_CRITICAL_FIELDS,
        "news_id",
    )
    if missing_news_fields:
        errors.append({"check": "missing_news_critical_fields", "records": missing_news_fields})

    invalid_event_families = sorted(
        {
            row.get("event_family", "")
            for row in events
            if row.get("event_family", "") not in EVENT_FAMILY_ALLOWED
        }
    )
    if invalid_event_families:
        errors.append(
            {"check": "invalid_event_family_values", "values": invalid_event_families}
        )

    invalid_news_families = sorted(
        {
            row.get("event_family", "")
            for row in news_rows
            if row.get("event_family", "") not in NEWS_FAMILY_ALLOWED
        }
    )
    if invalid_news_families:
        errors.append({"check": "invalid_news_family_values", "values": invalid_news_families})

    orphan_news_records = [
        {
            "news_id": row.get("news_id", ""),
            "related_event_id": row.get("related_event_id", ""),
            "title": row.get("title", ""),
        }
        for row in news_rows
        if row.get("related_event_id", "").strip() not in event_id_set
    ]
    if orphan_news_records:
        warnings.append(
            {
                "check": "orphan_news_records",
                "records": orphan_news_records,
                "note": (
                    "These news items do not link to an event_id in data/events_v2.csv "
                    "and require analyst review before use in event-linked analysis."
                ),
            }
        )

    status = "pass"
    if errors:
        status = "fail"
    elif warnings:
        status = "warning"

    return {
        "status": status,
        "input_files": {
            "events": str(EVENTS_PATH.relative_to(REPO_ROOT)),
            "news": str(NEWS_PATH.relative_to(REPO_ROOT)),
        },
        "summary": {
            "event_count": len(events),
            "news_item_count": len(news_rows),
            "event_family_count": len({row.get("event_family", "") for row in events}),
            "error_count": len(errors),
            "warning_count": len(warnings),
        },
        "checks": [
            "duplicate event_id",
            "missing event_id",
            "orphan news records",
            "invalid event family values",
            "missing critical fields",
            "duplicate news_id",
        ],
        "errors": errors,
        "warnings": warnings,
        "method_note": (
            "Validation checks structural data quality and linkage integrity. It does "
            "not add analytical claims or change the event-study methodology."
        ),
    }


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# Data Validation Report",
        "",
        f"- Status: `{report['status']}`",
        f"- Events: {summary['event_count']}",
        f"- News items: {summary['news_item_count']}",
        f"- Event families: {summary['event_family_count']}",
        f"- Errors: {summary['error_count']}",
        f"- Warnings: {summary['warning_count']}",
        "",
        str(report["method_note"]),
        "",
        "## Checks",
        "",
    ]
    lines.extend(f"- {check}" for check in report["checks"])

    lines.extend(["", "## Errors", ""])
    if report["errors"]:
        lines.extend(f"- `{error['check']}`: {error}" for error in report["errors"])
    else:
        lines.append("- None")

    lines.extend(["", "## Warnings", ""])
    if report["warnings"]:
        for warning in report["warnings"]:
            lines.append(f"- `{warning['check']}`: {warning.get('note', '')}")
            for record in warning.get("records", []):
                lines.append(
                    f"  - {record.get('news_id', '')}: {record.get('related_event_id', '')} - {record.get('title', '')}"
                )
    else:
        lines.append("- None")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    report = validate_project_data()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT_PATH.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    MD_OUTPUT_PATH.write_text(render_markdown(report), encoding="utf-8")

    print(f"Validation status: {report['status']}")
    print(f"Wrote {JSON_OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"Wrote {MD_OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
