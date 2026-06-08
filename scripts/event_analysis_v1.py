import pandas as pd


# Define input and output file paths.
EVENTS_FILE = "data/events_v1.csv"
MARKET_FILE = "data/market.csv"
OUTPUT_FILE = "output/event_summary.csv"


# Load the event dataset.
events = pd.read_csv(EVENTS_FILE)

# Load the market dataset so the validation script confirms both inputs are readable.
market = pd.read_csv(MARKET_FILE)

# Convert the event date column to datetime so date summaries are reliable.
events["date"] = pd.to_datetime(events["date"])

# Count the total number of events in the event dataset.
number_of_events = len(events)

# Count how many events belong to each event category.
event_categories_count = events["event_category"].value_counts().reset_index()
event_categories_count.columns = ["event_category", "count"]

# Identify the earliest event date in the dataset.
earliest_event_date = events["date"].min()

# Identify the latest event date in the dataset.
latest_event_date = events["date"].max()

# Print the core validation summary.
print(f"Number of events: {number_of_events}")
print("Event categories count:")
print(event_categories_count)
print(f"Earliest event date: {earliest_event_date.date()}")
print(f"Latest event date: {latest_event_date.date()}")

# Keep a reference to the market row count to show that market data loaded successfully.
print(f"Market rows loaded: {len(market)}")

# Save the category summary table for downstream review.
event_categories_count.to_csv(OUTPUT_FILE, index=False)
