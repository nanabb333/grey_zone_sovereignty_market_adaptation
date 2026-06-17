#!/usr/bin/env python3
"""Sprint 5 Scenario Comparison Engine prototype.

This deterministic layer explains why retrieved historical analogs are similar
or different. It consumes Historical Analog Engine demo output and produces
comparison matrices for dashboard and analyst review. It does not forecast,
estimate returns, or provide investment recommendations.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = REPO_ROOT / "results" / "historical_analog_engine" / "demo_results.json"
OUTPUT_DIR = REPO_ROOT / "results" / "scenario_comparison_engine"
JSON_OUTPUT_PATH = OUTPUT_DIR / "comparison_results.json"
MD_OUTPUT_PATH = OUTPUT_DIR / "comparison_results.md"

BOUNDARY_NOTE = (
    "Scenario comparison is historical decision intelligence only. It does not "
    "forecast future outcomes, estimate returns, or provide investment recommendations."
)

ALIASES = {
    "china": "prc",
    "people s republic of china": "prc",
    "prc": "prc",
    "pla": "pla",
    "people s liberation army": "pla",
    "united states": "united states",
    "u s": "united states",
    "us": "united states",
    "u s commerce department": "united states",
    "commerce department": "united states",
    "taiwan": "taiwan",
    "advanced semiconductors": "semiconductor",
    "advanced semiconductor": "semiconductor",
    "global semiconductor supply chain": "semiconductor",
    "semiconductor": "semiconductor",
    "semiconductors": "semiconductor",
    "chip": "semiconductor",
    "chips": "semiconductor",
    "taiwan strait": "taiwan strait",
}


def normalize_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value).lower()).strip()


def canonical(value: str) -> str:
    normalized = normalize_text(value)
    return ALIASES.get(normalized, normalized)


def canonical_set(values: list[str] | tuple[str, ...] | set[str]) -> set[str]:
    return {canonical(value) for value in values if canonical(value)}


def format_values(values: list[str] | tuple[str, ...] | set[str]) -> str:
    clean = [str(value) for value in values if str(value)]
    return "; ".join(clean) if clean else "N/A"


def evidence_profile(analog: dict[str, Any]) -> dict[str, Any]:
    evidence_items = analog.get("evidence_items", [])
    return {
        "linked_evidence_count": len(evidence_items),
        "source_packet_available": bool(analog.get("source_packet")),
        "event_source_available": bool(analog.get("source")),
        "evidence_sources": [item.get("source", "Unknown") for item in evidence_items],
    }


def evidence_profile_label(profile: dict[str, Any]) -> str:
    parts = [f"{profile['linked_evidence_count']} linked evidence item(s)"]
    if profile["source_packet_available"]:
        parts.append("source packet")
    if profile["event_source_available"]:
        parts.append("event source")
    return "; ".join(parts)


def compare_set_dimension(
    dimension: str,
    query_values: list[str],
    historical_values: list[str],
) -> dict[str, Any]:
    query_set = canonical_set(query_values)
    historical_set = canonical_set(historical_values)
    overlap = sorted(query_set & historical_set)
    query_only = sorted(query_set - historical_set)
    historical_only = sorted(historical_set - query_set)
    status = "match" if overlap and not query_only else "partial" if overlap else "different"
    return {
        "dimension": dimension,
        "query_value": format_values(query_values),
        "historical_value": format_values(historical_values),
        "status": status,
        "matched_values": overlap,
        "query_only": query_only,
        "historical_only": historical_only,
        "explanation": set_explanation(dimension, overlap, query_only, historical_only),
    }


def set_explanation(
    dimension: str,
    overlap: list[str],
    query_only: list[str],
    historical_only: list[str],
) -> str:
    if overlap and not query_only:
        return f"{dimension} aligns on {format_values(overlap)}."
    if overlap:
        return (
            f"{dimension} partially aligns on {format_values(overlap)}; "
            f"scenario-only values include {format_values(query_only)}."
        )
    return f"{dimension} differs; historical-only values include {format_values(historical_only)}."


def compare_scalar_dimension(
    dimension: str,
    query_value: int | float | str,
    historical_value: int | float | str,
) -> dict[str, Any]:
    try:
        delta = abs(float(query_value) - float(historical_value))
    except (TypeError, ValueError):
        delta = None
    status = "match" if delta == 0 else "partial" if delta is not None and delta <= 1 else "different"
    if delta is None:
        explanation = f"{dimension} comparison is unavailable."
    elif delta == 0:
        explanation = f"{dimension} is identical."
    else:
        explanation = f"{dimension} differs by {delta:g} point(s)."
    return {
        "dimension": dimension,
        "query_value": query_value,
        "historical_value": historical_value,
        "status": status,
        "difference": delta,
        "explanation": explanation,
    }


def compare_family(query_family: str, historical_family: str) -> dict[str, Any]:
    status = "match" if query_family == historical_family else "different"
    explanation = (
        "Event family is an exact match."
        if status == "match"
        else "Event family differs, so this analog should be interpreted as contextual rather than direct."
    )
    return {
        "dimension": "event family",
        "query_value": query_family,
        "historical_value": historical_family,
        "status": status,
        "explanation": explanation,
    }


def compare_evidence(analog: dict[str, Any]) -> dict[str, Any]:
    profile = evidence_profile(analog)
    if profile["linked_evidence_count"] and profile["event_source_available"]:
        status = "match"
        explanation = "Evidence profile is strong enough for analyst review."
    elif profile["event_source_available"]:
        status = "partial"
        explanation = "Evidence profile has an event source but limited linked evidence."
    else:
        status = "different"
        explanation = "Evidence profile is thin and requires analyst review."
    return {
        "dimension": "evidence profile",
        "query_value": "evidence-supported historical analog",
        "historical_value": evidence_profile_label(profile),
        "status": status,
        "profile": profile,
        "explanation": explanation,
    }


def comparison_matrix(question: dict[str, Any], analog: dict[str, Any]) -> list[dict[str, Any]]:
    scenario = question.get("mapped_scenario", {})
    features = analog.get("features", {})
    return [
        compare_set_dimension("actor", scenario.get("actors", []), features.get("actors", [])),
        compare_set_dimension("target", scenario.get("targets", []), features.get("targets", [])),
        compare_family(scenario.get("event_family", ""), analog.get("event_family", "")),
        compare_scalar_dimension(
            "severity",
            scenario.get("severity_score", "N/A"),
            features.get("severity_score", "N/A"),
        ),
        compare_scalar_dimension(
            "surprise",
            scenario.get("surprise_score", "N/A"),
            features.get("surprise_score", "N/A"),
        ),
        compare_evidence(analog),
    ]


def score_composition_summary(analog: dict[str, Any]) -> list[str]:
    components = analog.get("score_components", {})
    summaries = []
    for name, payload in components.items():
        points = payload.get("points", 0)
        explanation = payload.get("explanation", "No explanation available.")
        summaries.append(f"{name.replace('_', ' ').title()}: {points} point(s). {explanation}")
    return summaries


def major_matching_features(matrix: list[dict[str, Any]]) -> list[str]:
    matches = []
    for row in matrix:
        if row["status"] == "match":
            matches.append(f"{row['dimension'].title()}: {row['explanation']}")
    return matches or ["No full-dimension match; use as a contextual analog requiring review."]


def major_differences(matrix: list[dict[str, Any]]) -> list[str]:
    differences = []
    for row in matrix:
        if row["status"] in {"partial", "different"}:
            differences.append(f"{row['dimension'].title()}: {row['explanation']}")
    return differences or ["No major feature differences identified by deterministic comparison rules."]


def analog_comparison(question: dict[str, Any], analog: dict[str, Any]) -> dict[str, Any]:
    matrix = comparison_matrix(question, analog)
    return {
        "event_id": analog.get("event_id"),
        "event_name": analog.get("event_name"),
        "event_date": analog.get("event_date"),
        "event_family": analog.get("event_family"),
        "similarity_score": analog.get("similarity_score"),
        "confidence": analog.get("confidence"),
        "comparison_matrix": matrix,
        "score_composition": score_composition_summary(analog),
        "major_matching_features": major_matching_features(matrix),
        "major_differences": major_differences(matrix),
    }


def closest_vs_alternative(comparisons: list[dict[str, Any]]) -> dict[str, Any]:
    closest = comparisons[0] if comparisons else None
    alternative = comparisons[1] if len(comparisons) > 1 else None
    if not closest:
        return {
            "closest_historical_analog": None,
            "alternative_analog": None,
            "comparison_summary": "No historical analogs available for comparison.",
        }
    if not alternative:
        return {
            "closest_historical_analog": closest,
            "alternative_analog": None,
            "comparison_summary": f"{closest['event_id']} is the only available analog in this result set.",
        }

    score_gap = round(float(closest["similarity_score"]) - float(alternative["similarity_score"]), 2)
    summary = (
        f"{closest['event_id']} is the closest analog with score {closest['similarity_score']}. "
        f"{alternative['event_id']} is the alternative analog with score {alternative['similarity_score']}. "
        f"The score gap is {score_gap} point(s), so both should be reviewed when the gap is small."
    )
    return {
        "closest_historical_analog": closest,
        "alternative_analog": alternative,
        "comparison_summary": summary,
    }


def compare_question(question: dict[str, Any]) -> dict[str, Any]:
    analogs = question.get("historical_analogs", [])
    comparisons = [analog_comparison(question, analog) for analog in analogs[:3]]
    return {
        "question": question.get("question"),
        "mapped_scenario": question.get("mapped_scenario", {}),
        "analog_comparisons": comparisons,
        "closest_vs_alternative": closest_vs_alternative(comparisons),
        "analyst_notes": [
            BOUNDARY_NOTE,
            "Comparison matrices explain similarity and difference; they are not forecasts.",
            "Evidence profile describes historical source support and requires analyst review.",
        ],
    }


def run_comparison(input_path: Path = INPUT_PATH) -> dict[str, Any]:
    if not input_path.exists():
        raise FileNotFoundError(f"Missing Historical Analog Engine output: {input_path}")
    demo_results = json.loads(input_path.read_text(encoding="utf-8"))
    return {
        "prototype": "scenario_comparison_engine_sprint5",
        "input_file": str(input_path.relative_to(REPO_ROOT)),
        "boundary_note": BOUNDARY_NOTE,
        "comparisons": [compare_question(question) for question in demo_results.get("questions", [])],
    }


def render_markdown(results: dict[str, Any]) -> str:
    lines = ["# Scenario Comparison Engine Results", "", results["boundary_note"], ""]
    for comparison in results["comparisons"]:
        scenario = comparison["mapped_scenario"]
        lines.extend(
            [
                f"## {comparison['question']}",
                "",
                f"- Scenario family: `{scenario.get('event_family', 'N/A')}`",
                f"- Actors: {format_values(scenario.get('actors', []))}",
                f"- Targets: {format_values(scenario.get('targets', []))}",
                "",
            ]
        )
        cva = comparison["closest_vs_alternative"]
        lines.extend(["### Closest Match vs Alternative Match", "", cva["comparison_summary"], ""])

        for analog in comparison["analog_comparisons"]:
            lines.extend(
                [
                    f"### {analog['event_id']} - {analog['event_name']}",
                    "",
                    "| Dimension | Scenario | Historical Analog | Status | Explanation |",
                    "|---|---|---|---|---|",
                ]
            )
            for row in analog["comparison_matrix"]:
                lines.append(
                    "| {dimension} | {query_value} | {historical_value} | {status} | {explanation} |".format(
                        **row
                    )
                )
            lines.extend(["", "Major matching features:"])
            lines.extend(f"- {item}" for item in analog["major_matching_features"])
            lines.extend(["", "Major differences:"])
            lines.extend(f"- {item}" for item in analog["major_differences"])
            lines.append("")
    return "\n".join(lines)


def main() -> None:
    results = run_comparison()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    MD_OUTPUT_PATH.write_text(render_markdown(results), encoding="utf-8")
    print(f"Compared {len(results['comparisons'])} scenario question(s).")
    print(f"Wrote {JSON_OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"Wrote {MD_OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
