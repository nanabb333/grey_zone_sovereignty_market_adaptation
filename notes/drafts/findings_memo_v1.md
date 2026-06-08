# Findings Memo V1

## Purpose

This memo summarizes preliminary empirical patterns from `market_abnormal_returns.csv` and `final_event_study_sample.csv`.

The analysis is descriptive. It identifies patterns in abnormal returns but does not make causal claims.

## Data Used

| input file | role |
| --- | --- |
| `final_event_study_sample.csv` | Event sample and mechanism classification |
| `market_abnormal_returns.csv` | Day 0 abnormal returns and cumulative abnormal returns |

The current abnormal-return file contains 18 events:

| mechanism | events |
| --- | ---: |
| Risk | 14 |
| Strategic_Importance | 4 |

Abnormal returns are benchmark-adjusted returns from the current project output:

| market variable | benchmark |
| --- | --- |
| TWSE abnormal return | TWSE return adjusted by NASDAQ return |
| TSMC abnormal return | TSMC return adjusted by SOX return |

## Descriptive Statistics

| metric | mean | median | std_dev | min | max |
| --- | ---: | ---: | ---: | ---: | ---: |
| twse_day0_ar | -0.469 | -0.510 | 1.441 | -3.282 | 2.435 |
| twse_car_1 | -0.612 | -0.642 | 2.374 | -4.706 | 2.630 |
| twse_car_3 | -0.101 | 0.000 | 2.331 | -4.317 | 3.095 |
| twse_car_7 | -1.398 | -0.893 | 4.461 | -8.971 | 7.391 |
| tsmc_day0_ar | -0.894 | -0.966 | 2.358 | -5.520 | 3.455 |
| tsmc_car_1 | -0.059 | -0.269 | 4.070 | -6.308 | 8.059 |
| tsmc_car_3 | 1.842 | 1.753 | 3.318 | -3.251 | 6.728 |
| tsmc_car_7 | 0.168 | -0.923 | 4.424 | -5.499 | 9.597 |
| avg_car_7 | -0.615 | -1.966 | 4.055 | -6.399 | 7.096 |

Preliminary pattern:

The full sample is slightly negative on average over the [-7,+7] window, but the range is wide. The average TWSE CAR is more negative than the average TSMC CAR, suggesting that the broader Taiwan equity market and TSMC do not always move in the same way after these events.

## Most Negative Events

Ranked by the average of TWSE CAR [-7,+7] and TSMC CAR [-7,+7].

| event_date | event_name | mechanism | twse_car_7 | tsmc_car_7 | avg_car_7 |
| --- | --- | --- | ---: | ---: | ---: |
| 2022-08-03 | China Trade Restrictions After Pelosi Visit | Risk | -7.673 | -5.125 | -6.399 |
| 2022-08-04 | PLA Military Exercises After Pelosi Visit | Risk | -7.800 | -4.189 | -5.995 |
| 2022-10-07 | BIS Advanced Semiconductor Export Controls | Strategic_Importance | -5.088 | -5.499 | -5.294 |
| 2025-04-01 | Strait Thunder-2025A | Risk | -8.971 | -0.947 | -4.959 |
| 2023-04-08 | Joint Sword 2023 | Risk | -3.728 | -1.416 | -2.572 |

Preliminary interpretation:

The most negative events are mostly Risk events, especially the Pelosi-related escalation sequence and later military exercises. However, the BIS Advanced Semiconductor Export Controls event is also highly negative, even though it is coded as Strategic_Importance. This suggests that strategic-importance events can still generate negative market reactions when they involve restrictive technology controls or uncertainty around semiconductor supply chains.

## Most Positive Events

Ranked by the average of TWSE CAR [-7,+7] and TSMC CAR [-7,+7].

| event_date | event_name | mechanism | twse_car_7 | tsmc_car_7 | avg_car_7 |
| --- | --- | --- | ---: | ---: | ---: |
| 2024-04-08 | TSMC CHIPS Act Preliminary Terms | Strategic_Importance | 4.595 | 9.597 | 7.096 |
| 2025-03-04 | TSMC US$165B U.S. Expansion | Strategic_Importance | 7.391 | 4.935 | 6.163 |
| 2024-10-14 | Joint Sword-2024B | Risk | 1.390 | 7.561 | 4.475 |
| 2022-12-06 | TSMC Arizona US$40B Expansion | Strategic_Importance | 4.998 | 1.985 | 3.492 |
| 2023-08-12 | Lai U.S. Transit | Risk | 0.218 | 3.964 | 2.091 |

Preliminary interpretation:

The strongest positive events are mainly Strategic_Importance events connected to TSMC, CHIPS Act support, and semiconductor supply-chain restructuring. The presence of Joint Sword-2024B among the most positive events is an important puzzle: a high-profile military demonstration did not correspond to negative abnormal returns in this window.

## Average Abnormal Returns by Mechanism

| mechanism | n | twse_day0_ar_mean | twse_car_7_mean | tsmc_day0_ar_mean | tsmc_car_7_mean | avg_car_7_mean |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Risk | 14 | -0.814 | -2.647 | -1.340 | -0.571 | -1.609 |
| Strategic_Importance | 4 | 0.737 | 2.974 | 0.667 | 2.754 | 2.864 |

Preliminary interpretation:

Risk events are negative on average across both Day 0 and the [-7,+7] window. Strategic_Importance events are positive on average. This pattern is consistent with the idea that Taiwan-related events can transmit through different channels: some events raise perceived geopolitical risk, while others highlight Taiwan's strategic value in semiconductor and technology supply chains.

The sample is small, especially for Strategic_Importance events, so these averages should be treated as descriptive rather than conclusive.

## Sign Patterns

| mechanism | n | negative_avg_car_7 | positive_avg_car_7 | negative_twse_day0 | positive_twse_day0 | negative_tsmc_day0 | positive_tsmc_day0 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Risk | 14 | 10 | 4 | 11 | 3 | 11 | 3 |
| Strategic_Importance | 4 | 1 | 3 | 1 | 3 | 1 | 3 |

Preliminary interpretation:

Most Risk events have negative average CAR over the [-7,+7] window, but 4 of 14 Risk events have positive average CAR. Most Strategic_Importance events have positive average CAR, but the BIS export-control event is negative. The sign pattern therefore does not support a simple one-direction model.

## Market Adaptation Analysis

The `event_repetition` variable is currently available only for four core events in `data/events_v2.csv`. This section uses only those coded observations.

| event_name | event_date | event_repetition | surprise_level | twse_day0_ar | twse_car_7 | tsmc_day0_ar | tsmc_car_7 | avg_car_7 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Pelosi Visit | 2022-08-02 | 1 | 2 | -1.401 | -4.233 | -2.261 | 0.234 | -1.999 |
| Joint Sword 2023 | 2023-04-08 | 2 | 1 | 0.443 | -3.728 | -1.986 | -1.416 | -2.572 |
| Joint Sword-2024A | 2024-05-23 | 3 | 1 | 0.648 | -0.426 | 1.289 | -3.469 | -1.947 |
| Joint Sword-2024B | 2024-10-14 | 4 | 1 | -0.549 | 1.390 | -1.804 | 7.561 | 4.475 |

Preliminary pattern:

The four-event comparison is broadly consistent with a market-adaptation pattern, but the evidence is not yet strong enough for a causal claim. As `event_repetition` rises from 1 to 4, the average [-7,+7] abnormal return moves from negative to positive by Joint Sword-2024B. The transition is not perfectly monotonic: Joint Sword 2023 is more negative than Pelosi Visit on average, and Joint Sword-2024A remains slightly negative.

This suggests a possible adaptation pattern, but it should be tested with more coded events and a cleaner non-overlapping sample.

## Key Puzzle

Question:

Does high geopolitical risk consistently produce negative abnormal returns?

Preliminary answer:

No, not consistently in the current descriptive data.

Supporting patterns:

- Risk events are negative on average.
- The most negative events are mostly Risk events.
- Several Risk events have positive abnormal returns, especially Joint Sword-2024B.
- Strategic_Importance events are positive on average, but BIS Advanced Semiconductor Export Controls is negative.
- TSMC and TWSE sometimes diverge, suggesting that Taiwan market reactions may differ between broad-market risk and semiconductor-specific expectations.

Interpretation:

The data do not support a simple pattern in which every high-risk Taiwan geopolitical event produces negative abnormal returns. A more plausible descriptive pattern is conditional: reactions appear to vary by mechanism, repetition, surprise, and whether the event is interpreted as damaging risk or as evidence of Taiwan's strategic importance.

## Preliminary Takeaways

1. Risk events show negative average abnormal returns, but the effect is not uniform.
2. Strategic_Importance events show positive average abnormal returns, except when the event involves restrictive technology controls.
3. The strongest positive events are connected to TSMC and semiconductor supply-chain restructuring.
4. The strongest negative events are connected to acute crisis escalation or coercive pressure.
5. The repetition comparison suggests possible market adaptation, but the current coding covers only four events.
6. These findings should be interpreted as patterns for further testing, not causal estimates.

## Next Empirical Steps

- Apply `event_repetition` coding to the full event sample.
- Re-run abnormal returns using the overlap-reduced `final_event_study_sample_v2.csv`.
- Compare raw returns and abnormal returns event by event.
- Separate military-risk events from economic-coercion and political-signaling events.
- Test whether surprise, repetition, and semiconductor relevance explain variation better than risk coding alone.
