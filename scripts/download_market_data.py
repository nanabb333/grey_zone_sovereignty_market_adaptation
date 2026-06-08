from pathlib import Path

import pandas as pd
import yfinance as yf


# Define the download range. yfinance treats the end date as exclusive,
# so use 2025-06-01 to include observations through 2025-05-31.
START_DATE = "2022-01-01"
END_DATE = "2025-06-01"

# Define the tickers and output files.
DOWNLOADS = [
    ("^TWII", Path("data/raw/twse_twii_yahoo.csv")),
    ("2330.TW", Path("data/raw/tsmc_2330tw_yahoo.csv")),
    ("^IXIC", Path("data/raw/nasdaq_ixic_yahoo.csv")),
    ("NVDA", Path("data/raw/nvidia_nvda_yahoo.csv")),
    ("^SOX", Path("data/raw/sox_yahoo.csv")),
]


def download_ticker(ticker, output_file):
    try:
        # Download daily market data from Yahoo Finance.
        data = yf.download(
            ticker,
            start=START_DATE,
            end=END_DATE,
            auto_adjust=False,
            progress=False,
        )

        # Stop early if Yahoo Finance returns no rows for the ticker.
        if data.empty:
            print(f"ERROR: No data returned for {ticker}")
            return

        # Convert the date index into a regular Date column.
        data = data.reset_index()

        # If yfinance returns multi-level columns, flatten them.
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [
                column[0] if column[0] else column[1]
                for column in data.columns
            ]

        # Save the raw downloaded data.
        data.to_csv(output_file, index=False)

        # Print basic validation information.
        first_date = data["Date"].min()
        last_date = data["Date"].max()
        row_count = len(data)

        print(f"{ticker}")
        print(f"first date: {first_date.date()}")
        print(f"last date: {last_date.date()}")
        print(f"row count: {row_count}")
        print()
    except Exception as error:
        # Print a simple error message and continue with the next ticker.
        print(f"ERROR: Could not download {ticker}")
        print(f"Reason: {error}")
        print()


def main():
    # Create the raw data directory before saving downloads.
    Path("data/raw").mkdir(parents=True, exist_ok=True)

    # Download each requested ticker and save it to the target raw file.
    for ticker, output_file in DOWNLOADS:
        download_ticker(ticker, output_file)


if __name__ == "__main__":
    main()
