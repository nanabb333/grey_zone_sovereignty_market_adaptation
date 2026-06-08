from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"


def main():
    events = pd.read_csv(DATA_DIR / "events.csv")
    market = pd.read_csv(DATA_DIR / "market.csv")

    summary = events.merge(market, on="date", how="left")
    summary = summary[
        [
            "date",
            "event_name",
            "event_type",
            "risk_level",
            "strategic_value",
            "taiex",
            "usd_twd",
            "tsmc",
        ]
    ]

    OUTPUT_DIR.mkdir(exist_ok=True)
    summary.to_csv(OUTPUT_DIR / "event_summary.csv", index=False)

    print(summary)


if __name__ == "__main__":
    main()
