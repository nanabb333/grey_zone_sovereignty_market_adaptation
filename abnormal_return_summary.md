# Abnormal Return Summary

Abnormal returns are calculated as simple benchmark-adjusted percent returns: TWSE return minus NASDAQ return, and TSMC return minus SOX return.

- Input event sample: `final_event_study_sample.csv`
- Input market data: `data/market.csv`
- Events calculated: 18
- Event windows: Day 0, [-1,+1], [-3,+3], and [-7,+7] common trading days

## Top 5 Most Negative Events

Ranked by average TWSE/TSMC CAR over [-7,+7].

| event_date | event_name | mechanism | twse_car_7 | tsmc_car_7 | average_car_7 |
| --- | --- | --- | --- | --- | --- |
| 2022-08-03 | China Trade Restrictions After Pelosi Visit | Risk | -7.673 | -5.125 | -6.399 |
| 2022-08-04 | PLA Military Exercises After Pelosi Visit | Risk | -7.800 | -4.189 | -5.995 |
| 2022-10-07 | BIS Advanced Semiconductor Export Controls | Strategic_Importance | -5.088 | -5.499 | -5.294 |
| 2025-04-01 | Strait Thunder-2025A | Risk | -8.971 | -0.947 | -4.959 |
| 2023-04-08 | Joint Sword 2023 | Risk | -3.728 | -1.416 | -2.572 |

## Top 5 Most Positive Events

Ranked by average TWSE/TSMC CAR over [-7,+7].

| event_date | event_name | mechanism | twse_car_7 | tsmc_car_7 | average_car_7 |
| --- | --- | --- | --- | --- | --- |
| 2024-04-08 | TSMC CHIPS Act Preliminary Terms | Strategic_Importance | 4.595 | 9.597 | 7.096 |
| 2025-03-04 | TSMC US$165B U.S. Expansion | Strategic_Importance | 7.391 | 4.935 | 6.163 |
| 2024-10-14 | Joint Sword-2024B | Risk | 1.390 | 7.561 | 4.475 |
| 2022-12-06 | TSMC Arizona US$40B Expansion | Strategic_Importance | 4.998 | 1.985 | 3.492 |
| 2023-08-12 | Lai U.S. Transit | Risk | 0.218 | 3.964 | 2.091 |

## Average Abnormal Returns by Mechanism

| mechanism | twse_day0_ar | twse_car_1 | twse_car_3 | twse_car_7 | tsmc_day0_ar | tsmc_car_1 | tsmc_car_3 | tsmc_car_7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Risk | -0.814 | -1.078 | -0.458 | -2.647 | -1.340 | -0.391 | 1.727 | -0.571 |
| Strategic_Importance | 0.737 | 1.019 | 1.152 | 2.974 | 0.667 | 1.104 | 2.242 | 2.754 |

## Raw Return vs Abnormal Return

Averages by mechanism. Raw returns are unadjusted TWSE and TSMC returns; abnormal returns subtract NASDAQ and SOX benchmark returns.

| mechanism | twse_day0_raw | twse_day0_ar | twse_raw_car_7 | twse_car_7 | tsmc_day0_raw | tsmc_day0_ar | tsmc_raw_car_7 | tsmc_car_7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Risk | 0.076 | -0.814 | 0.541 | -2.647 | 0.189 | -1.340 | 1.716 | -0.571 |
| Strategic_Importance | -0.838 | 0.737 | -3.068 | 2.974 | -1.677 | 0.667 | -5.788 | 2.754 |
