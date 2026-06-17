#!/usr/bin/env python3
"""Sprint 2 Historical Analog Engine prototype.

This script maps analyst questions to structured scenarios, retrieves comparable
historical events with deterministic scoring, extracts observed historical
pathways, and renders analyst briefs. It is not a forecasting or investment
recommendation system.
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
EVENTS_PATH = REPO_ROOT / "data" / "events_v3.csv"
NEWS_PATH = REPO_ROOT / "data" / "news" / "news_events.csv"
MARKET_PATH = REPO_ROOT / "results" / "event_abnormal_return_summary_v3.csv"
RESULTS_DIR = REPO_ROOT / "results" / "historical_analog_engine"
BRIEFS_DIR = RESULTS_DIR / "sample_briefs"
JSON_OUTPUT_PATH = RESULTS_DIR / "demo_results.json"
MD_OUTPUT_PATH = RESULTS_DIR / "demo_analyst_briefs.md"

EVENT_REQUIRED_COLUMNS = [
    "event_id",
    "event_date",
    "event_name",
    "event_category",
    "brief_description",
    "surprise_score",
    "surprise_rationale",
    "event_family",
    "event_repetition_level",
    "interpretation_type",
    "source",
]
NEWS_REQUIRED_COLUMNS = [
    "news_id",
    "source",
    "title",
    "url",
    "related_event_id",
    "actor",
    "geography",
    "summary",
    "coding_notes",
]
MARKET_REQUIRED_COLUMNS = ["event_name", "event_date"]
PREFERRED_CAR_COLUMNS = ["tsmc_car_7", "tsmc_car_3", "twse_car_7", "twse_car_3"]

BOUNDARY_NOTE = (
    "Historical analog retrieval only. This output does not forecast future outcomes, "
    "estimate future returns, or provide investment recommendations."
)


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    question: str
    title: str
    event_family: str
    actors: tuple[str, ...]
    targets: tuple[str, ...]
    severity_score: int
    surprise_score: int
    query_terms: tuple[str, ...]
    mapping_reason: str


DEMO_QUESTIONS = [
    "What happens if China launches another Joint Sword exercise?",
    "What happens if new semiconductor export controls are announced?",
    "What happens after a major Taiwan election?",
]

QUESTION_PATTERNS: list[dict[str, Any]] = [
    {
        "scenario_id": "S2-DEMO-001",
        "keywords": ["joint sword", "military exercise", "drill", "exercises", "blockade"],
        "title": "Renewed Joint Sword-Style Military Exercise",
        "event_family": "Military Exercise",
        "actors": ("PRC", "PLA", "China"),
        "targets": ("Taiwan", "Taiwan Strait"),
        "severity_score": 4,
        "surprise_score": 3,
        "query_terms": ("joint sword", "military", "exercise", "drill", "taiwan"),
        "mapping_reason": (
            "The question references Joint Sword and launch of another exercise, "
            "which maps to the Military Exercise family."
        ),
    },
    {
        "scenario_id": "S2-DEMO-002",
        "keywords": ["export control", "export controls", "semiconductor", "chip controls", "entity list"],
        "title": "New Semiconductor Export Controls",
        "event_family": "Export Control",
        "actors": ("United States", "U.S. Commerce Department"),
        "targets": ("China", "Advanced semiconductors", "Global semiconductor supply chain"),
        "severity_score": 4,
        "surprise_score": 3,
        "query_terms": ("export", "control", "semiconductor", "chip", "entity", "china"),
        "mapping_reason": (
            "The question references semiconductor export controls, which maps to "
            "the Export Control family."
        ),
    },
    {
        "scenario_id": "S2-DEMO-003",
        "keywords": ["election", "inauguration", "vote", "presidential"],
        "title": "Major Taiwan Election or Leadership Transition",
        "event_family": "Election",
        "actors": ("Taiwan",),
        "targets": ("Taiwan", "Taiwan Strait", "PRC"),
        "severity_score": 3,
        "surprise_score": 1,
        "query_terms": ("election", "inauguration", "taiwan", "president", "leadership"),
        "mapping_reason": (
            "The question references a major Taiwan election, which maps to the "
            "Election family and related political-signaling records."
        ),
    },
]

FAMILY_ALIASES = {
    "Military_Exercise": "Military Exercise",
    "Military Demonstration": "Military Exercise",
    "Diplomatic_Shock": "Diplomatic Shock",
    "Diplomatic Shock": "Diplomatic Shock",
    "Political_Signaling": "Election",
    "Political Signaling": "Election",
    "Export_Control": "Export Control",
    "Export Control": "Export Control",
    "Industrial_Policy": "Strategic Investment",
    "Strategic_Investment": "Strategic Investment",
    "Semiconductor Supply Chain": "Strategic Investment",
    "Economic_Coercion": "Sanction",
    "Economic Coercion": "Sanction",
    "Legal_Judicial_Signaling": "Diplomatic Shock",
    "Technology Competition": "Technology Restriction",
}

RELATED_FAMILIES = {
    ("Export Control", "Technology Restriction"),
    ("Export Control", "Sanction"),
    ("Diplomatic Shock", "Election"),
    ("Military Exercise", "Diplomatic Shock"),
    ("Strategic Investment", "Technology Restriction"),
}

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
    "tsmc": "tsmc",
    "advanced semiconductors": "semiconductor",
    "advanced semiconductor": "semiconductor",
    "semiconductor": "semiconductor",
    "semiconductors": "semiconductor",
    "chip": "semiconductor",
    "chips": "semiconductor",
    "global semiconductor supply chain": "semiconductor",
    "taiwan strait": "taiwan strait",
}


def read_csv(path: Path, required_columns: list[str], optional: bool = False) -> list[dict[str, str]]:
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


def normalize_family(value: str) -> str:
    value = value.strip()
    return FAMILY_ALIASES.get(value, FAMILY_ALIASES.get(value.replace(" ", "_"), value.replace("_", " ")))


def canonical(value: str) -> str:
    normalized = normalize_text(value)
    return ALIASES.get(normalized, normalized)


def split_terms(value: str) -> set[str]:
    return {canonical(item) for item in re.split(r";|,|/|\band\b", value) if canonical(item)}


def parse_float(value: str | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def bounded(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def confidence_label(score: float) -> str:
    if score >= 80:
        return "Strong analog"
    if score >= 60:
        return "Useful analog"
    if score >= 40:
        return "Weak analog requiring analyst review"
    return "Do not show by default"


def map_question(question: str) -> Scenario:
    normalized = normalize_text(question)
    best_pattern = None
    best_hits = -1
    for pattern in QUESTION_PATTERNS:
        hits = sum(1 for keyword in pattern["keywords"] if normalize_text(keyword) in normalized)
        if hits > best_hits:
            best_pattern = pattern
            best_hits = hits
    if best_pattern is None or best_hits <= 0:
        best_pattern = QUESTION_PATTERNS[0]

    return Scenario(
        scenario_id=best_pattern["scenario_id"],
        question=question,
        title=best_pattern["title"],
        event_family=best_pattern["event_family"],
        actors=best_pattern["actors"],
        targets=best_pattern["targets"],
        severity_score=best_pattern["severity_score"],
        surprise_score=best_pattern["surprise_score"],
        query_terms=best_pattern["query_terms"],
        mapping_reason=best_pattern["mapping_reason"],
    )


def build_news_index(news_rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    linked: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in news_rows:
        related_event_id = row.get("related_event_id", "").strip()
        if related_event_id and not related_event_id.startswith("UNLINKED"):
            linked[related_event_id].append(row)
    return dict(linked)


def build_market_context(market_rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, Any]]:
    if not market_rows:
        return {}
    fieldnames = set(market_rows[0].keys())
    car_columns = [column for column in PREFERRED_CAR_COLUMNS if column in fieldnames]
    context: dict[tuple[str, str], dict[str, Any]] = {}
    for row in market_rows:
        metrics = {}
        for column in car_columns:
            value = parse_float(row.get(column))
            if value is not None:
                metrics[column] = round(value, 4)
        if metrics:
            key = (normalize_text(row.get("event_name", "")), row.get("event_date", ""))
            context[key] = {
                "matched_trading_date": row.get("matched_trading_date", ""),
                "metrics": metrics,
                "note": "Historical descriptive CAR context only; not a forecast.",
            }
    return context


def event_market_context(event: dict[str, str], market_context: dict[tuple[str, str], dict[str, Any]]) -> dict[str, Any] | None:
    key = (normalize_text(event.get("event_name", "")), event.get("event_date", event.get("date", "")))
    return market_context.get(key)


def infer_event_actors(event: dict[str, str], news_items: list[dict[str, str]]) -> set[str]:
    actors: set[str] = set()
    for item in news_items:
        actors.update(split_terms(item.get("actor", "")))
    text = normalize_text(" ".join([event.get("event_name", ""), event.get("brief_description", ""), event.get("source", "")]))
    if any(term in text for term in ["china", "prc"]):
        actors.add("prc")
    if "pla" in text:
        actors.add("pla")
    if any(term in text for term in ["u s", "united states", "commerce", "bis", "biden"]):
        actors.add("united states")
    if "taiwan" in text:
        actors.add("taiwan")
    if "tsmc" in text:
        actors.add("tsmc")
    return actors


def infer_event_targets(event: dict[str, str], news_items: list[dict[str, str]]) -> set[str]:
    targets: set[str] = set()
    for item in news_items:
        targets.update(split_terms(item.get("geography", "")))
    text = normalize_text(" ".join([event.get("event_name", ""), event.get("brief_description", ""), event.get("event_category", "")]))
    if "taiwan strait" in text:
        targets.add("taiwan strait")
    if "taiwan" in text:
        targets.add("taiwan")
    if any(term in text for term in ["semiconductor", "chip", "chips", "foundry", "huawei", "smic"]):
        targets.add("semiconductor")
    if "china" in text:
        targets.add("prc")
    if "huawei" in text:
        targets.add("huawei")
    if "smic" in text:
        targets.add("smic")
    return targets


def surprise_numeric(value: str) -> int:
    return {"Low": 1, "Medium": 3, "High": 5}.get(value.strip(), 3)


def derive_severity(event: dict[str, str], family: str) -> int:
    base = {
        "Military Exercise": 4,
        "Export Control": 4,
        "Technology Restriction": 4,
        "Sanction": 3,
        "Election": 3,
        "Diplomatic Shock": 3,
        "Strategic Investment": 3,
    }.get(family, 3)
    text = normalize_text(" ".join([event.get("event_name", ""), event.get("brief_description", "")]))
    if any(term in text for term in ["blockade", "missile", "live fire", "major", "advanced", "expanded", "broadened"]):
        base += 1
    if event.get("strategic_importance_level", "") == "High":
        base += 1
    if event.get("surprise_score", "") == "Low":
        base -= 1
    return int(bounded(base, 1, 5))


def related_family_score(query_family: str, event_family: str) -> tuple[float, str]:
    if query_family == event_family:
        return 30.0, "Exact taxonomy-family match."
    if (query_family, event_family) in RELATED_FAMILIES or (event_family, query_family) in RELATED_FAMILIES:
        return 18.0, "Related taxonomy family under Sprint 2 mapping rules."
    return 0.0, "No direct taxonomy-family match."


def overlap_score(query_values: tuple[str, ...], event_values: set[str], weight: float) -> tuple[float, list[str]]:
    query_set = {canonical(value) for value in query_values}
    overlap = sorted(query_set & event_values)
    if not query_set:
        return 0.0, []
    return round(weight * (len(overlap) / len(query_set)), 2), overlap


def temporal_context_score(scenario: Scenario, event: dict[str, str]) -> tuple[float, str]:
    event_name = normalize_text(event.get("event_name", ""))
    query_terms = {normalize_text(term) for term in scenario.query_terms}
    if "joint sword" in query_terms and "joint sword" in event_name:
        return 5.0, "Named Joint Sword pattern match."
    if scenario.event_family == "Election" and normalize_family(event.get("event_family", "")) in {"Election", "Diplomatic Shock"}:
        return 4.0, "Election-adjacent political sequence."
    repetition = parse_float(event.get("event_repetition_level"))
    if repetition is not None and repetition >= 3:
        return 3.0, "Repeated historical pattern."
    return 1.0, "General historical context."


def evidence_score(event: dict[str, str], news_items: list[dict[str, str]]) -> tuple[float, str]:
    has_packet = bool(event.get("source_packet", "").strip())
    has_news = bool(news_items)
    has_source = bool(event.get("source", "").strip())
    if has_packet and has_news:
        return 10.0, "Source packet and linked news evidence available."
    if has_news:
        return 7.0, "Linked news evidence available."
    if has_packet and has_source:
        return 6.0, "Source packet and event source available."
    if has_source:
        return 5.0, "Event source URL available."
    return 2.0, "Minimal event metadata available."


def score_event(
    scenario: Scenario,
    event: dict[str, str],
    news_items: list[dict[str, str]],
    market_context: dict[tuple[str, str], dict[str, Any]],
) -> dict[str, Any]:
    event_family = normalize_family(event.get("event_family", ""))
    family_points, family_explanation = related_family_score(scenario.event_family, event_family)

    event_actors = infer_event_actors(event, news_items)
    actor_points, actor_overlap = overlap_score(scenario.actors, event_actors, 20.0)

    event_targets = infer_event_targets(event, news_items)
    target_points, target_overlap = overlap_score(scenario.targets, event_targets, 15.0)

    event_severity = derive_severity(event, event_family)
    severity_points = round(10.0 * (1 - abs(scenario.severity_score - event_severity) / 4), 2)
    severity_points = bounded(severity_points, 0.0, 10.0)

    event_surprise = surprise_numeric(event.get("surprise_score", ""))
    surprise_points = round(10.0 * (1 - abs(scenario.surprise_score - event_surprise) / 4), 2)
    surprise_points = bounded(surprise_points, 0.0, 10.0)

    temporal_points, temporal_explanation = temporal_context_score(scenario, event)
    evidence_points, evidence_explanation = evidence_score(event, news_items)

    total = round(
        family_points
        + actor_points
        + target_points
        + severity_points
        + surprise_points
        + temporal_points
        + evidence_points,
        2,
    )

    return {
        "event_id": event["event_id"],
        "event_name": event["event_name"],
        "event_date": event.get("event_date") or event.get("date"),
        "event_family": event_family,
        "original_event_family": event.get("event_family", ""),
        "event_category": event.get("event_category", ""),
        "brief_description": event.get("brief_description", ""),
        "source": event.get("source", ""),
        "source_packet": event.get("source_packet", ""),
        "surprise_rationale": event.get("surprise_rationale", ""),
        "interpretation_type": event.get("interpretation_type", ""),
        "event_repetition_level": event.get("event_repetition_level", ""),
        "similarity_score": total,
        "confidence": confidence_label(total),
        "features": {
            "actors": sorted(event_actors),
            "targets": sorted(event_targets),
            "severity_score": event_severity,
            "surprise_score": event_surprise,
        },
        "score_components": {
            "event_family_match": {
                "points": family_points,
                "query_value": scenario.event_family,
                "historical_value": event_family,
                "explanation": family_explanation,
            },
            "actor_overlap": {
                "points": actor_points,
                "query_value": list(scenario.actors),
                "historical_value": sorted(event_actors),
                "matched_values": actor_overlap,
                "explanation": "Alias-aware actor overlap.",
            },
            "target_overlap": {
                "points": target_points,
                "query_value": list(scenario.targets),
                "historical_value": sorted(event_targets),
                "matched_values": target_overlap,
                "explanation": "Alias-aware target, geography, and sector overlap.",
            },
            "severity_proximity": {
                "points": severity_points,
                "query_value": scenario.severity_score,
                "historical_value": event_severity,
                "explanation": "Distance between deterministic severity scores.",
            },
            "surprise_proximity": {
                "points": surprise_points,
                "query_value": scenario.surprise_score,
                "historical_value": event_surprise,
                "explanation": "Distance between deterministic surprise scores.",
            },
            "temporal_context_fit": {
                "points": temporal_points,
                "query_value": list(scenario.query_terms),
                "historical_value": event.get("event_name", ""),
                "explanation": temporal_explanation,
            },
            "evidence_coverage": {
                "points": evidence_points,
                "query_value": "linked evidence and source packet coverage",
                "historical_value": f"{len(news_items)} linked news item(s)",
                "explanation": evidence_explanation,
            },
        },
        "evidence_items": [
            {
                "news_id": item.get("news_id", ""),
                "source": item.get("source", ""),
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "summary": item.get("summary", ""),
                "coding_notes": item.get("coding_notes", ""),
            }
            for item in news_items
        ],
        "historical_market_context": event_market_context(event, market_context),
    }


def retrieve_analogs(
    scenario: Scenario,
    events: list[dict[str, str]],
    news_index: dict[str, list[dict[str, str]]],
    market_context: dict[tuple[str, str], dict[str, Any]],
    top_k: int = 5,
) -> list[dict[str, Any]]:
    scored = [
        score_event(scenario, event, news_index.get(event["event_id"], []), market_context)
        for event in events
    ]
    filtered = [item for item in scored if item["similarity_score"] >= 40]
    return sorted(
        filtered,
        key=lambda item: (
            item["similarity_score"],
            item["score_components"]["event_family_match"]["points"],
            item["score_components"]["evidence_coverage"]["points"],
            item["event_date"],
        ),
        reverse=True,
    )[:top_k]


def extract_pathways(analog: dict[str, Any], events: list[dict[str, str]]) -> list[str]:
    event_date = analog["event_date"]
    event_id = analog["event_id"]
    same_family_later = [
        event
        for event in events
        if event.get("event_id") != event_id
        and normalize_family(event.get("event_family", "")) == analog["event_family"]
        and event.get("event_date", "") > event_date
    ]
    same_family_later = sorted(same_family_later, key=lambda item: item.get("event_date", ""))[:3]

    near_term = [
        event
        for event in events
        if event.get("event_id") != event_id
        and event.get("event_date", "") > event_date
        and event.get("event_date", "")[:4] == event_date[:4]
    ]
    near_term = sorted(near_term, key=lambda item: item.get("event_date", ""))[:2]

    pathways = []
    if same_family_later:
        names = ", ".join(f"{item['event_name']} ({item['event_date']})" for item in same_family_later)
        pathways.append(f"Later same-family records in the dataset include {names}.")
    if near_term:
        names = ", ".join(f"{item['event_name']} ({item['event_date']})" for item in near_term)
        pathways.append(f"Near-term subsequent coded events include {names}.")
    if analog.get("event_repetition_level"):
        pathways.append(
            f"The event is coded with repetition level {analog['event_repetition_level']}, "
            "which indicates whether the pattern was novel or recurring in the historical sample."
        )
    if analog.get("historical_market_context"):
        pathways.append("Historical CAR context is available as descriptive event-study evidence only.")
    if not pathways:
        pathways.append("No clear subsequent pathway is coded in the current validated event sample.")
    return pathways


def brief_for_question(
    scenario: Scenario,
    analogs: list[dict[str, Any]],
    events: list[dict[str, str]],
) -> dict[str, Any]:
    return {
        "question": scenario.question,
        "mapped_scenario": {
            "scenario_id": scenario.scenario_id,
            "title": scenario.title,
            "event_family": scenario.event_family,
            "actors": list(scenario.actors),
            "targets": list(scenario.targets),
            "severity_score": scenario.severity_score,
            "surprise_score": scenario.surprise_score,
            "mapping_reason": scenario.mapping_reason,
        },
        "historical_analogs": [
            {
                **analog,
                "observed_historical_pathways": extract_pathways(analog, events),
            }
            for analog in analogs
        ],
        "analyst_notes": [
            BOUNDARY_NOTE,
            "Similarity scores are deterministic retrieval aids and require analyst review.",
            "Evidence rows may contain placeholder source metadata that should be verified before publication.",
            "Historical CAR fields, when shown, describe prior coded events and are not estimates for the question scenario.",
        ],
    }


def render_brief(brief: dict[str, Any]) -> str:
    scenario = brief["mapped_scenario"]
    lines = [
        f"# Analyst Brief: {scenario['title']}",
        "",
        "## Question",
        "",
        brief["question"],
        "",
        f"Mapped scenario family: `{scenario['event_family']}`",
        "",
        f"Mapping rationale: {scenario['mapping_reason']}",
        "",
        "## Historical Analogs",
        "",
        "| Rank | Event ID | Historical Event | Date | Family | Score | Confidence |",
        "|---:|---|---|---|---|---:|---|",
    ]
    for index, analog in enumerate(brief["historical_analogs"], start=1):
        lines.append(
            f"| {index} | {analog['event_id']} | {analog['event_name']} | "
            f"{analog['event_date']} | {analog['event_family']} | "
            f"{analog['similarity_score']:.2f} | {analog['confidence']} |"
        )

    lines.extend(["", "## Similarity Explanation", ""])
    for index, analog in enumerate(brief["historical_analogs"], start=1):
        lines.extend(
            [
                f"### {index}. {analog['event_id']} - {analog['event_name']}",
                "",
                "| Component | Query Value | Historical Value | Points | Explanation |",
                "|---|---|---|---:|---|",
            ]
        )
        for component, payload in analog["score_components"].items():
            query_value = payload["query_value"]
            historical_value = payload["historical_value"]
            if isinstance(query_value, list):
                query_value = "; ".join(str(item) for item in query_value)
            if isinstance(historical_value, list):
                historical_value = "; ".join(str(item) for item in historical_value)
            lines.append(
                f"| {component.replace('_', ' ').title()} | {query_value} | "
                f"{historical_value} | {payload['points']:.2f} | {payload['explanation']} |"
            )
        lines.append("")

    lines.extend(["## Evidence Base", ""])
    for analog in brief["historical_analogs"]:
        lines.append(f"### {analog['event_id']} - {analog['event_name']}")
        lines.append("")
        lines.append(f"- Event source: {analog['source'] or 'Not available'}")
        if analog.get("source_packet"):
            lines.append(f"- Source packet: `{analog['source_packet']}`")
        if analog.get("surprise_rationale"):
            lines.append(f"- Surprise rationale: {analog['surprise_rationale']}")
        if analog.get("historical_market_context"):
            metrics = ", ".join(
                f"{key}={value}" for key, value in analog["historical_market_context"]["metrics"].items()
            )
            lines.append(f"- Historical CAR context: {metrics}. Historical context only.")
        if analog["evidence_items"]:
            for item in analog["evidence_items"]:
                lines.append(
                    f"- {item['news_id']}: {item['source']} - {item['title']} ({item['url']})"
                )
        else:
            lines.append("- Linked news evidence: none in current evidence database.")
        lines.append("")

    lines.extend(["## Observed Historical Pathways", ""])
    for analog in brief["historical_analogs"]:
        lines.append(f"### {analog['event_id']} - {analog['event_name']}")
        for pathway in analog["observed_historical_pathways"]:
            lines.append(f"- {pathway}")
        lines.append("")

    lines.extend(["## Analyst Notes", ""])
    for note in brief["analyst_notes"]:
        lines.append(f"- {note}")
    lines.append("")
    return "\n".join(lines)


def run_demo(questions: list[str]) -> dict[str, Any]:
    events = read_csv(EVENTS_PATH, EVENT_REQUIRED_COLUMNS)
    news_rows = read_csv(NEWS_PATH, NEWS_REQUIRED_COLUMNS)
    market_rows = read_csv(MARKET_PATH, MARKET_REQUIRED_COLUMNS, optional=True)
    news_index = build_news_index(news_rows)
    market_context = build_market_context(market_rows)

    briefs = []
    for question in questions:
        scenario = map_question(question)
        analogs = retrieve_analogs(scenario, events, news_index, market_context)
        briefs.append(brief_for_question(scenario, analogs, events))

    return {
        "prototype": "historical_analog_engine_sprint2",
        "boundary_note": BOUNDARY_NOTE,
        "input_files": {
            "events": str(EVENTS_PATH.relative_to(REPO_ROOT)),
            "news": str(NEWS_PATH.relative_to(REPO_ROOT)),
            "market_context": str(MARKET_PATH.relative_to(REPO_ROOT)) if MARKET_PATH.exists() else None,
        },
        "questions": briefs,
    }


def main() -> None:
    results = run_demo(DEMO_QUESTIONS)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    brief_sections = ["# Historical Analog Engine Demo Briefs\n\n" + BOUNDARY_NOTE + "\n"]
    for index, brief in enumerate(results["questions"], start=1):
        rendered = render_brief(brief)
        brief_path = BRIEFS_DIR / f"demo_{index:02d}_{brief['mapped_scenario']['scenario_id'].lower()}.md"
        brief_path.write_text(rendered, encoding="utf-8")
        brief_sections.append(rendered)
    MD_OUTPUT_PATH.write_text("\n---\n\n".join(brief_sections), encoding="utf-8")

    print(f"Processed {len(results['questions'])} demo questions.")
    print(f"Wrote {JSON_OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"Wrote {MD_OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"Wrote sample briefs under {BRIEFS_DIR.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
