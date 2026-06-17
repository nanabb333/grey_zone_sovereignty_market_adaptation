from pathlib import Path

import pandas as pd


MARKET_FILE = Path("data/processed/market.csv")
V3_EVENT_FILE = Path("data/events_v3.csv")
ORIGINAL_SUMMARY_FILE = Path("results/event_abnormal_return_summary.csv")
V3_SUMMARY_FILE = Path("results/event_abnormal_return_summary_v3.csv")
V3_NEW_EVENTS_FILE = Path("results/event_abnormal_return_summary_v3_new_events.csv")
V3_INTEGRATION_EVENTS = {"E023", "E024", "E025"}
EVENT_WINDOWS = [1, 3, 7]


def load_market_data():
    market = pd.read_csv(MARKET_FILE)
    market["date"] = pd.to_datetime(market["date"])
    return market.sort_values("date").reset_index(drop=True)


def calculate_daily_abnormal_returns(market):
    market["twse_return"] = market["twse_close"].pct_change(fill_method=None) * 100
    market["tsmc_return"] = market["tsmc_close"].pct_change(fill_method=None) * 100
    market["nasdaq_return"] = market["nasdaq_close"].pct_change(fill_method=None) * 100
    market["sox_return"] = market["sox_close"].pct_change(fill_method=None) * 100
    market["twse_abnormal_return"] = market["twse_return"] - market["nasdaq_return"]
    market["tsmc_abnormal_return"] = market["tsmc_return"] - market["sox_return"]
    return market


def load_v3_events():
    events = pd.read_csv(V3_EVENT_FILE)
    events = events[events["event_id"].isin(V3_INTEGRATION_EVENTS)].copy()
    events["event_date"] = pd.to_datetime(events["event_date"])
    return events.sort_values("event_id").reset_index(drop=True)


def find_event_row(market, event_date):
    possible_rows = market.index[market["date"] >= event_date]
    if len(possible_rows) == 0:
        return None
    return possible_rows[0]


def calculate_event_summary(market, events):
    event_rows = []
    for _, event in events.iterrows():
        event_index = find_event_row(market, event["event_date"])
        if event_index is None:
            continue

        market_row = market.loc[event_index]
        result = {
            "event_id": event["event_id"],
            "coverage_group": "New_V3",
            "event_name": event["event_name"],
            "event_date": event["event_date"].strftime("%Y-%m-%d"),
            "mechanism": event["mechanism"],
            "matched_trading_date": market_row["date"].strftime("%Y-%m-%d"),
            "twse_day0_ar": market_row["twse_abnormal_return"],
            "tsmc_day0_ar": market_row["tsmc_abnormal_return"],
        }

        for window in EVENT_WINDOWS:
            window_rows = market.iloc[event_index : event_index + window + 1]
            result[f"twse_car_{window}"] = window_rows[
                "twse_abnormal_return"
            ].sum()
            result[f"tsmc_car_{window}"] = window_rows[
                "tsmc_abnormal_return"
            ].sum()

        event_rows.append(result)

    return pd.DataFrame(event_rows)


def add_original_metadata(original):
    original = original.copy()
    original.insert(0, "coverage_group", "Original_V2")
    original.insert(0, "event_id", "")
    return original


def main():
    market = calculate_daily_abnormal_returns(load_market_data())
    v3_events = load_v3_events()
    new_event_summary = calculate_event_summary(market, v3_events)

    original_summary = pd.read_csv(ORIGINAL_SUMMARY_FILE)
    original_with_metadata = add_original_metadata(original_summary)
    combined = pd.concat(
        [original_with_metadata, new_event_summary],
        ignore_index=True,
        sort=False,
    )

    V3_SUMMARY_FILE.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(V3_SUMMARY_FILE, index=False)
    new_event_summary.to_csv(V3_NEW_EVENTS_FILE, index=False)

    print(f"Saved V3 event summary to {V3_SUMMARY_FILE}")
    print(f"Saved newly integrated V3 events to {V3_NEW_EVENTS_FILE}")
    print(f"New V3 events integrated: {len(new_event_summary)}")


if __name__ == "__main__":
    main()
