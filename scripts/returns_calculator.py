def calculate_returns(market_data, asset, benchmark):
    market_data = market_data.copy()

    market_data["asset_return"] = market_data[asset].pct_change(fill_method=None)
    market_data["benchmark_return"] = market_data[benchmark].pct_change(fill_method=None)

    market_data = market_data.dropna(subset=["asset_return", "benchmark_return"])

    return market_data
