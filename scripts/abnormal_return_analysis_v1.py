import pandas as pd


# Define the input and output files.
MARKET_FILE = "data/market.csv"
OUTPUT_FILE = "data/market_abnormal_returns.csv"


def main():
    # Load the cleaned market dataset.
    market = pd.read_csv(MARKET_FILE)

    # Convert the date column to datetime for sorting and date summaries.
    market["date"] = pd.to_datetime(market["date"])

    # Sort observations chronologically before calculating returns.
    market = market.sort_values("date")

    # Calculate daily percent returns for Taiwan and benchmark markets.
    market["twse_return"] = market["twse_close"].pct_change(fill_method=None) * 100
    market["tsmc_return"] = market["tsmc_close"].pct_change(fill_method=None) * 100
    market["nasdaq_return"] = market["nasdaq_close"].pct_change(fill_method=None) * 100
    market["sox_return"] = market["sox_close"].pct_change(fill_method=None) * 100

    # Calculate simple benchmark-adjusted TWSE return.
    market["twse_abnormal_return"] = (
        market["twse_return"] - market["nasdaq_return"]
    )

    # Calculate simple benchmark-adjusted TSMC return.
    market["tsmc_abnormal_return"] = (
        market["tsmc_return"] - market["sox_return"]
    )

    # Format dates as YYYY-MM-DD for clean CSV output.
    market["date"] = market["date"].dt.strftime("%Y-%m-%d")

    # Save the market dataset with raw and abnormal returns.
    market.to_csv(OUTPUT_FILE, index=False)

    # Print summary statistics for abnormal returns.
    print(f"Date range: {market['date'].min()} to {market['date'].max()}")
    print("Mean abnormal return:")
    print(
        market[
            ["twse_abnormal_return", "tsmc_abnormal_return"]
        ].mean()
    )
    print("Standard deviation:")
    print(
        market[
            ["twse_abnormal_return", "tsmc_abnormal_return"]
        ].std()
    )


if __name__ == "__main__":
    main()
