from pathlib import Path

import pandas as pd


MARKET_DATA_FILE = Path("data/market_data.csv")


def load_market_data(asset, benchmark):
    market_data = pd.read_csv(MARKET_DATA_FILE)

    required_columns = ["date", asset, benchmark]
    missing_columns = [
        column for column in required_columns if column not in market_data.columns
    ]

    if missing_columns:
        missing_column_list = ", ".join(missing_columns)
        raise ValueError(
            f"Missing required market data column(s): {missing_column_list}"
        )

    market_data["date"] = pd.to_datetime(market_data["date"])
    market_data = market_data.sort_values("date")

    return market_data
