import pandas as pd


# Define the input and output files.
MARKET_FILE = "data/market.csv"
OUTPUT_FILE = "output/pelosi_event_window_v2.csv"

# Define the Pelosi Visit event date.
EVENT_DATE = pd.Timestamp("2022-08-02")


def main():
    # Load the cleaned market dataset.
    market = pd.read_csv(MARKET_FILE)

    # Convert the date column to datetime for event-window filtering.
    market["date"] = pd.to_datetime(market["date"])

    # Sort market data by date before calculating returns.
    market = market.sort_values("date")

    # Calculate daily percent change for TWSE.
    market["twse_return"] = market["twse_close"].pct_change() * 100

    # Calculate daily percent change for TSMC.
    market["tsmc_return"] = market["tsmc_close"].pct_change() * 100

    # Find the row number for the Pelosi Visit event date.
    event_index = market.index[market["date"] == EVENT_DATE][0]

    # Extract a -7 to +7 trading-day window around the event row.
    event_window = market.iloc[event_index - 7:event_index + 8].copy()

    # Calculate cumulative TWSE return across the event window.
    event_window["twse_cumulative_return"] = (
        (1 + event_window["twse_return"].fillna(0) / 100).cumprod() - 1
    ) * 100

    # Calculate cumulative TSMC return across the event window.
    event_window["tsmc_cumulative_return"] = (
        (1 + event_window["tsmc_return"].fillna(0) / 100).cumprod() - 1
    ) * 100

    # Keep only the required output columns.
    event_window = event_window[
        [
            "date",
            "twse_close",
            "twse_return",
            "twse_cumulative_return",
            "tsmc_close",
            "tsmc_return",
            "tsmc_cumulative_return",
        ]
    ]

    # Format dates as YYYY-MM-DD for clean CSV output.
    event_window["date"] = event_window["date"].dt.strftime("%Y-%m-%d")

    # Save the event-window table.
    event_window.to_csv(OUTPUT_FILE, index=False)

    # Print the event-window table.
    print(event_window)


if __name__ == "__main__":
    main()
