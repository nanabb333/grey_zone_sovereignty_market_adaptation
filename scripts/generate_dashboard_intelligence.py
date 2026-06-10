import csv
import json
from pathlib import Path


DASHBOARD_DATA_FILE = Path("results/dashboard_data.csv")
MECHANISM_SUMMARY_FILE = Path("results/mechanism_summary.csv")
EVENT_INSIGHTS_FILE = Path("results/event_insights.json")
LLM_CONTEXT_FILE = Path("results/llm_context.json")
HISTORICAL_COMPARISON_FILE = Path("results/historical_comparison.json")
EXECUTIVE_BRIEF_FILE = Path("results/executive_brief.json")


def read_csv_rows(path):
    with path.open(newline="") as file:
        return list(csv.DictReader(file))


def read_json(path):
    return json.loads(path.read_text())


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2))


def parse_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def format_percent(value):
    if value is None:
        return "N/A"
    return f"{value * 100:.2f}%"


def mechanism_lookup(mechanism_rows):
    return {
        row["mechanism"]: {
            "event_count": int(row["event_count"]),
            "mean_car_value": parse_float(row["mean_car_value"]),
            "min_car_value": parse_float(row["min_car_value"]),
            "max_car_value": parse_float(row["max_car_value"]),
            "successful_event_count": int(row["successful_event_count"]),
            "failed_event_count": int(row["failed_event_count"]),
        }
        for row in mechanism_rows
    }


def successful_events(events):
    return [
        event
        for event in events
        if event["status"] == "success" and parse_float(event["car_value"]) is not None
    ]


def strongest_positive(events):
    positive_events = [
        event for event in successful_events(events) if parse_float(event["car_value"]) > 0
    ]
    if not positive_events:
        return None
    return max(positive_events, key=lambda event: parse_float(event["car_value"]))


def strongest_negative(events):
    negative_events = [
        event for event in successful_events(events) if parse_float(event["car_value"]) < 0
    ]
    if not negative_events:
        return None
    return min(negative_events, key=lambda event: parse_float(event["car_value"]))


def event_summary(event):
    if event is None:
        return None
    car_value = parse_float(event["car_value"])
    return {
        "event_id": event["event_id"],
        "event_name": event["event_name"],
        "event_date": event["event_date"],
        "mechanism": event["mechanism"],
        "car_value": car_value,
        "car_percent": format_percent(car_value),
        "car_direction": event["car_direction"],
    }


def compare_event_to_mechanism(event, mechanisms):
    car_value = parse_float(event["car_value"])
    mechanism = event["mechanism"]
    mechanism_average = mechanisms.get(mechanism, {}).get("mean_car_value")

    comparison = {
        "event_id": event["event_id"],
        "event_name": event["event_name"],
        "event_date": event["event_date"],
        "mechanism": mechanism,
        "event_car_value": car_value,
        "event_car_percent": format_percent(car_value),
        "mechanism_average_car": mechanism_average,
        "mechanism_average_percent": format_percent(mechanism_average),
        "relative_strength": "N/A",
        "magnitude_ratio": None,
        "comparison_rule": "abs(event_car_value) compared with abs(mechanism_average_car)",
        "interpretation": "Comparison unavailable because required CAR values are missing.",
    }

    if car_value is None or mechanism_average is None:
        return comparison

    event_strength = abs(car_value)
    average_strength = abs(mechanism_average)

    if average_strength == 0:
        comparison["relative_strength"] = "N/A"
        comparison["interpretation"] = (
            "Comparison unavailable because the mechanism average magnitude is zero."
        )
        return comparison

    comparison["magnitude_ratio"] = event_strength / average_strength

    if event_strength > average_strength:
        comparison["relative_strength"] = "stronger_than_mechanism_average"
        comparison["interpretation"] = (
            f"{event['event_name']} had a larger abnormal-CAR magnitude than "
            f"the current {mechanism} mechanism average."
        )
    elif event_strength < average_strength:
        comparison["relative_strength"] = "weaker_than_mechanism_average"
        comparison["interpretation"] = (
            f"{event['event_name']} had a smaller abnormal-CAR magnitude than "
            f"the current {mechanism} mechanism average."
        )
    else:
        comparison["relative_strength"] = "equal_to_mechanism_average"
        comparison["interpretation"] = (
            f"{event['event_name']} matched the current {mechanism} mechanism "
            "average abnormal-CAR magnitude."
        )

    return comparison


def build_historical_comparison(events, mechanism_rows):
    mechanisms = mechanism_lookup(mechanism_rows)
    comparisons = [
        compare_event_to_mechanism(event, mechanisms)
        for event in sorted(successful_events(events), key=lambda row: row["event_id"])
    ]
    return {
        "method": "deterministic_historical_comparison",
        "comparison_basis": "event abnormal CAR magnitude versus mechanism mean abnormal CAR magnitude",
        "comparison_count": len(comparisons),
        "comparisons": comparisons,
        "use_note": "Educational and research use only. Not investment advice.",
    }


def build_llm_context(events, mechanism_rows, insights, historical_comparison):
    mechanisms = mechanism_lookup(mechanism_rows)
    return {
        "purpose": "Structured context for future analyst-reviewed LLM integration.",
        "use_constraints": [
            "Educational and research use only",
            "Do not forecast",
            "Do not provide trading recommendations",
            "Do not provide investment advice",
            "Use only the provided structured context",
        ],
        "source_files": [
            str(DASHBOARD_DATA_FILE),
            str(MECHANISM_SUMMARY_FILE),
            str(EVENT_INSIGHTS_FILE),
        ],
        "run_summary": {
            "event_count": len(events),
            "successful_event_count": len(successful_events(events)),
            "failed_event_count": len(events) - len(successful_events(events)),
            "strongest_positive_event": event_summary(strongest_positive(events)),
            "strongest_negative_event": event_summary(strongest_negative(events)),
        },
        "events": events,
        "mechanisms": mechanisms,
        "rule_based_insights": insights["insights"],
        "historical_comparisons": historical_comparison["comparisons"],
    }


def build_executive_brief(events, mechanism_rows, insights, historical_comparison):
    positive_event = event_summary(strongest_positive(events))
    negative_event = event_summary(strongest_negative(events))
    mechanisms = mechanism_lookup(mechanism_rows)

    mechanism_summaries = []
    for mechanism, values in mechanisms.items():
        mechanism_summaries.append(
            {
                "mechanism": mechanism,
                "summary": (
                    f"{mechanism} includes {values['event_count']} event(s), "
                    f"with mean abnormal CAR of {format_percent(values['mean_car_value'])}."
                ),
                "mean_car_value": values["mean_car_value"],
                "mean_car_percent": format_percent(values["mean_car_value"]),
            }
        )

    highlights = []
    if positive_event:
        highlights.append(
            f"Strongest positive event: {positive_event['event_name']} "
            f"({positive_event['car_percent']})."
        )
    if negative_event:
        highlights.append(
            f"Strongest negative event: {negative_event['event_name']} "
            f"({negative_event['car_percent']})."
        )
    highlights.append(f"Rule-based insights generated: {len(insights['insights'])}.")
    highlights.append(
        "Historical comparisons use event abnormal CAR magnitude versus mechanism average magnitude."
    )

    return {
        "title": "Taiwan Geopolitical Risk Dashboard Executive Brief",
        "method": "deterministic_rule_based_template",
        "overview": (
            f"The dashboard summarizes {len(events)} Taiwan-related event(s), "
            f"including {len(successful_events(events))} successful event-study result(s)."
        ),
        "highlights": highlights,
        "mechanism_summaries": mechanism_summaries,
        "comparison_summary": {
            "comparison_count": historical_comparison["comparison_count"],
            "stronger_than_average_count": sum(
                1
                for comparison in historical_comparison["comparisons"]
                if comparison["relative_strength"] == "stronger_than_mechanism_average"
            ),
            "weaker_than_average_count": sum(
                1
                for comparison in historical_comparison["comparisons"]
                if comparison["relative_strength"] == "weaker_than_mechanism_average"
            ),
        },
        "analyst_note": (
            "This brief is generated with deterministic templates from dashboard outputs. "
            "It is intended for educational and research use only."
        ),
        "restriction_note": (
            "This brief does not provide forecasts, trading recommendations, investment "
            "advice, policy advice, or official conclusions."
        ),
    }


def main():
    events = read_csv_rows(DASHBOARD_DATA_FILE)
    mechanism_rows = read_csv_rows(MECHANISM_SUMMARY_FILE)
    insights = read_json(EVENT_INSIGHTS_FILE)

    historical_comparison = build_historical_comparison(events, mechanism_rows)
    llm_context = build_llm_context(events, mechanism_rows, insights, historical_comparison)
    executive_brief = build_executive_brief(
        events,
        mechanism_rows,
        insights,
        historical_comparison,
    )

    write_json(HISTORICAL_COMPARISON_FILE, historical_comparison)
    write_json(LLM_CONTEXT_FILE, llm_context)
    write_json(EXECUTIVE_BRIEF_FILE, executive_brief)

    print(f"historical comparison saved to {HISTORICAL_COMPARISON_FILE}")
    print(f"llm context saved to {LLM_CONTEXT_FILE}")
    print(f"executive brief saved to {EXECUTIVE_BRIEF_FILE}")


if __name__ == "__main__":
    main()
