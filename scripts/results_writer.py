from pathlib import Path

import pandas as pd


RESULTS_FILE = Path("results/event_results.csv")
EVENT_WINDOWS_DIR = Path("results/event_windows")
RUN_SUMMARY_FILE = Path("results/run_summary.md")
MECHANISM_SUMMARY_FILE = Path("results/mechanism_summary.csv")


RESULT_COLUMNS = [
    "event_id",
    "event_name",
    "event_date",
    "mechanism",
    "event_type",
    "asset",
    "benchmark",
    "event_window_start",
    "event_window_end",
    "trading_days_in_window",
    "car_value",
    "status",
    "error_message",
]


def initialize_event_results():
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    if RESULTS_FILE.exists():
        RESULTS_FILE.unlink()


def append_event_result(result_row):
    event_results = pd.DataFrame([result_row], columns=RESULT_COLUMNS)
    event_results.to_csv(
        RESULTS_FILE,
        mode="a",
        header=not RESULTS_FILE.exists(),
        index=False,
    )


def save_event_results(event, car_value, event_window_data):
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    EVENT_WINDOWS_DIR.mkdir(parents=True, exist_ok=True)

    append_event_result(
        {
            "event_id": event["event_id"],
            "event_name": event["event_name"],
            "event_date": event["event_date"],
            "mechanism": event["mechanism"],
            "event_type": event["event_type"],
            "asset": event["asset"],
            "benchmark": event["benchmark"],
            "event_window_start": event["event_window_start"],
            "event_window_end": event["event_window_end"],
            "trading_days_in_window": len(event_window_data),
            "car_value": car_value,
            "status": "success",
            "error_message": "",
        }
    )

    event_window_output = event_window_data[
        ["date", "asset_return", "benchmark_return", "abnormal_return"]
    ].copy()
    event_window_data_file = (
        EVENT_WINDOWS_DIR / f"{event['event_id']}_event_window_data.csv"
    )
    event_window_output.to_csv(event_window_data_file, index=False)

    return RESULTS_FILE, event_window_data_file


def save_failed_event_result(event, error_message):
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)

    append_event_result(
        {
            "event_id": event["event_id"],
            "event_name": event["event_name"],
            "event_date": event["event_date"],
            "mechanism": event["mechanism"],
            "event_type": event["event_type"],
            "asset": event["asset"],
            "benchmark": event["benchmark"],
            "event_window_start": event["event_window_start"],
            "event_window_end": event["event_window_end"],
            "trading_days_in_window": "",
            "car_value": "",
            "status": "failed",
            "error_message": error_message,
        }
    )

    return RESULTS_FILE


def write_run_summary():
    event_results = pd.read_csv(RESULTS_FILE)

    total_events = len(event_results)
    successful_events = (event_results["status"] == "success").sum()
    failed_events = (event_results["status"] == "failed").sum()

    status_rows = event_results[
        [
            "event_id",
            "event_name",
            "mechanism",
            "status",
            "car_value",
            "error_message",
        ]
    ].fillna("")

    status_table_lines = [
        "| event_id | event_name | mechanism | status | car_value | error_message |",
        "|---|---|---|---|---:|---|",
    ]
    for _, row in status_rows.iterrows():
        status_table_lines.append(
            "| "
            + " | ".join(
                [
                    str(row["event_id"]),
                    str(row["event_name"]),
                    str(row["mechanism"]),
                    str(row["status"]),
                    str(row["car_value"]),
                    str(row["error_message"]),
                ]
            )
            + " |"
        )
    status_table = "\n".join(status_table_lines)

    summary = f"""# Taiwan Geopolitical Risk Event Study Engine - Run Summary

## Run-Level Counts

| Metric | Count |
|---|---:|
| Total events | {total_events} |
| Successful events | {successful_events} |
| Failed events | {failed_events} |

## Event Status

{status_table}

## Output Locations

- results/event_results.csv
- results/mechanism_summary.csv
- results/event_windows/
- reports/
- figures/

## Notes

- `status=success` means the event was processed successfully.
- `status=failed` means the event failed but the batch continued.
- `car_value` is benchmark-adjusted abnormal CAR based on the current engine definition.
"""

    RUN_SUMMARY_FILE.parent.mkdir(parents=True, exist_ok=True)
    RUN_SUMMARY_FILE.write_text(summary)

    return RUN_SUMMARY_FILE


def write_mechanism_summary():
    event_results = pd.read_csv(RESULTS_FILE)
    successful_events = event_results[event_results["status"] == "success"].copy()
    successful_events["car_value"] = pd.to_numeric(
        successful_events["car_value"],
        errors="coerce",
    )

    summary_rows = []
    for mechanism, mechanism_rows in event_results.groupby("mechanism", sort=True):
        successful_mechanism_rows = successful_events[
            successful_events["mechanism"] == mechanism
        ]
        failed_event_count = (mechanism_rows["status"] == "failed").sum()

        summary_rows.append(
            {
                "mechanism": mechanism,
                "event_count": len(mechanism_rows),
                "mean_car_value": successful_mechanism_rows["car_value"].mean(),
                "min_car_value": successful_mechanism_rows["car_value"].min(),
                "max_car_value": successful_mechanism_rows["car_value"].max(),
                "successful_event_count": len(successful_mechanism_rows),
                "failed_event_count": failed_event_count,
            }
        )

    mechanism_summary = pd.DataFrame(
        summary_rows,
        columns=[
            "mechanism",
            "event_count",
            "mean_car_value",
            "min_car_value",
            "max_car_value",
            "successful_event_count",
            "failed_event_count",
        ],
    )
    mechanism_summary.to_csv(MECHANISM_SUMMARY_FILE, index=False)

    return MECHANISM_SUMMARY_FILE
