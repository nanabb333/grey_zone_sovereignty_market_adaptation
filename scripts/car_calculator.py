import pandas as pd


def calculate_car(abnormal_returns_data, event_date, window_start, window_end):
    event_date = pd.to_datetime(event_date)
    window_start = int(window_start)
    window_end = int(window_end)

    start_date = event_date + pd.Timedelta(days=window_start)
    end_date = event_date + pd.Timedelta(days=window_end)

    event_window_data = abnormal_returns_data[
        (abnormal_returns_data["date"] >= start_date)
        & (abnormal_returns_data["date"] <= end_date)
    ].copy()

    car_value = event_window_data["abnormal_return"].sum()

    return car_value, event_window_data
