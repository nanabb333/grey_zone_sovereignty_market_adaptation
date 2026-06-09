from pathlib import Path


REPORTS_DIR = Path("reports")


def generate_event_report(
    event,
    car_value,
    event_results_path,
    event_window_data_path,
    figure_path,
):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    output_file = REPORTS_DIR / f"{event['event_id']}_report.md"

    report = f"""# {event["event_name"]} Event Report

## Event Metadata

| Field | Value |
|---|---|
| Event ID | {event["event_id"]} |
| Event Name | {event["event_name"]} |
| Event Date | {event["event_date"]} |
| Mechanism | {event["mechanism"]} |
| Event Type | {event["event_type"]} |

## Asset and Benchmark

| Field | Value |
|---|---|
| Asset | {event["asset"]} |
| Benchmark | {event["benchmark"]} |

## Event Window

| Field | Value |
|---|---|
| Event Window Start | {event["event_window_start"]} |
| Event Window End | {event["event_window_end"]} |

## CAR Result

| Metric | Value |
|---|---|
| CAR Value | {car_value} |

## Output Files

| Output | Path |
|---|---|
| Event Results | {event_results_path} |
| Event Window Data | {event_window_data_path} |
| Abnormal Return Figure | {figure_path} |

## Interpretation

Interpretation will be reviewed by the analyst.
"""

    output_file.write_text(report)

    return output_file
