import pandas as pd


# Define the input and output files.
MARKET_FILE = "data/market.csv"
OUTPUT_FILE = "output/joint_sword_2024b_window.csv"

# Define the Joint Sword-2024B event date.
EVENT_DATE = pd.Timestamp("2024-10-14")


def main():
    # Load the cleaned market dataset.
    market = pd.read_csv(MARKET_FILE)

    # Convert the date column to datetime for event-window selection.
    market["date"] = pd.to_datetime(market["date"])

    # Sort market data by date before calculating returns.
    market = market.sort_values("date").reset_index(drop=True)

    # Calculate daily percent change for TWSE.
    market["twse_return"] = market["twse_close"].pct_change() * 100

    # Calculate daily percent change for TSMC.
    market["tsmc_return"] = market["tsmc_close"].pct_change() * 100

    # Use the event date if it is a trading day; otherwise use the next trading day.
    event_rows = market.index[market["date"] >= EVENT_DATE]
    event_index = event_rows[0]
    event_trading_date = market.loc[event_index, "date"]

    # Extract a -7 to +7 trading-day window around the event trading date.
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
    print()

    # Print summary statistics for the event window.
    print(f"Event date: {EVENT_DATE.date()}")
    print(f"Event trading date used: {event_trading_date.date()}")
    print(f"Window start: {event_window['date'].iloc[0]}")
    print(f"Window end: {event_window['date'].iloc[-1]}")
    print(f"Row count: {len(event_window)}")
    print(f"TWSE event-day return: {market.loc[event_index, 'twse_return']:.2f}%")
    print(f"TSMC event-day return: {market.loc[event_index, 'tsmc_return']:.2f}%")
    print(
        "TWSE cumulative return at end of window: "
        f"{event_window['twse_cumulative_return'].iloc[-1]:.2f}%"
    )
    print(
        "TSMC cumulative return at end of window: "
        f"{event_window['tsmc_cumulative_return'].iloc[-1]:.2f}%"
    )


if __name__ == "__main__":
    main()
