def calculate_abnormal_returns(returns_data):
    returns_data = returns_data.copy()

    returns_data["abnormal_return"] = (
        returns_data["asset_return"] - returns_data["benchmark_return"]
    )

    return returns_data
