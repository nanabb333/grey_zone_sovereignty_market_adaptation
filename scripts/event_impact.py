from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"


def main():
    events = pd.read_csv(DATA_DIR / "events.csv", parse_dates=["date"])
    market = pd.read_csv(DATA_DIR / "market.csv", parse_dates=["date"])

    market_by_date = market.set_index("date")
    market_variables = ["taiex", "usd_twd", "tsmc"]
    rows = []

    for _, event in events.iterrows():
        event_date = event["date"]
        before_date = event_date - pd.Timedelta(days=1)
        after_date = event_date + pd.Timedelta(days=1)

        row = {
            "event_name": event["event_name"],
            "event_type": event["event_type"],
            "risk_level": event["risk_level"],
            "strategic_value": event["strategic_value"],
        }

        for variable in market_variables:
            series = market_by_date[variable]
            before = series.get(before_date, pd.NA)
            event_day = series.get(event_date, pd.NA)
            after = series.get(after_date, pd.NA)

            if pd.notna(before) and pd.notna(after):
                percentage_change = ((after - before) / before) * 100
            else:
                percentage_change = pd.NA

            row[f"{variable}_before"] = before
            row[f"{variable}_event_day"] = event_day
            row[f"{variable}_after"] = after
            row[f"{variable}_change"] = percentage_change

        rows.append(row)

    impact = pd.DataFrame(rows)

    OUTPUT_DIR.mkdir(exist_ok=True)
    impact.to_csv(OUTPUT_DIR / "event_impact.csv", index=False)

    print(impact)


if __name__ == "__main__":
    main()
