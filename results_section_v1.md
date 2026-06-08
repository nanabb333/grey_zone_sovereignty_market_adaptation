# Results Section V1

## Overview

This section reports preliminary descriptive patterns from the Taiwan event-study dataset. The analysis uses `market_abnormal_returns.csv`, `final_event_study_sample.csv`, `findings_memo_v1.md`, and `abnormal_return_summary.md`.

The current event-level abnormal-return file contains 18 events. Of these, 14 are coded as `Risk` events and 4 are coded as `Strategic_Importance` events. Abnormal returns are benchmark-adjusted returns, with TWSE compared against NASDAQ and TSMC compared against SOX.

The results should be interpreted as descriptive patterns. They do not establish causal effects.

## Risk vs Strategic Importance

The clearest descriptive pattern is the contrast between events coded as `Risk` and those coded as `Strategic_Importance`.

| mechanism | n | twse_day0_ar | twse_car_7 | tsmc_day0_ar | tsmc_car_7 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Risk | 14 | -0.814 | -2.647 | -1.340 | -0.571 |
| Strategic_Importance | 4 | 0.737 | 2.974 | 0.667 | 2.754 |

Risk events are negative on average for both Day 0 abnormal returns and the [-7,+7] cumulative abnormal return window. Strategic_Importance events are positive on average across the same measures.

The raw-return comparison also points in the same direction after benchmark adjustment.

| mechanism | twse_day0_raw | twse_day0_ar | twse_raw_car_7 | twse_car_7 | tsmc_day0_raw | tsmc_day0_ar | tsmc_raw_car_7 | tsmc_car_7 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Risk | 0.076 | -0.814 | 0.541 | -2.647 | 0.189 | -1.340 | 1.716 | -0.571 |
| Strategic_Importance | -0.838 | 0.737 | -3.068 | 2.974 | -1.677 | 0.667 | -5.788 | 2.754 |

For Risk events, raw average returns are slightly positive, while abnormal returns are negative. This suggests that once broader market benchmarks are considered, Taiwan-specific or Taiwan-related underperformance is more visible. For Strategic_Importance events, raw average returns are negative, while abnormal returns are positive. This indicates that some technology or supply-chain events may look weak in raw price terms but stronger after accounting for broader market movements.

## Most Negative Events

The most negative events are ranked by the average of TWSE CAR [-7,+7] and TSMC CAR [-7,+7].

| event_date | event_name | mechanism | twse_car_7 | tsmc_car_7 | average_car_7 |
| --- | --- | --- | ---: | ---: | ---: |
| 2022-08-03 | China Trade Restrictions After Pelosi Visit | Risk | -7.673 | -5.125 | -6.399 |
| 2022-08-04 | PLA Military Exercises After Pelosi Visit | Risk | -7.800 | -4.189 | -5.995 |
| 2022-10-07 | BIS Advanced Semiconductor Export Controls | Strategic_Importance | -5.088 | -5.499 | -5.294 |
| 2025-04-01 | Strait Thunder-2025A | Risk | -8.971 | -0.947 | -4.959 |
| 2023-04-08 | Joint Sword 2023 | Risk | -3.728 | -1.416 | -2.572 |

Four of the five most negative events are Risk events. These include trade restrictions, military exercises after the Pelosi visit, Joint Sword 2023, and Strait Thunder-2025A. The one Strategic_Importance event in this group is the BIS Advanced Semiconductor Export Controls event. This is an important exception because it suggests that technology-related events are not uniformly positive; export controls may carry strategic-importance content while also creating uncertainty for semiconductor markets.

## Most Positive Events

The most positive events are also ranked by the average of TWSE CAR [-7,+7] and TSMC CAR [-7,+7].

| event_date | event_name | mechanism | twse_car_7 | tsmc_car_7 | average_car_7 |
| --- | --- | --- | ---: | ---: | ---: |
| 2024-04-08 | TSMC CHIPS Act Preliminary Terms | Strategic_Importance | 4.595 | 9.597 | 7.096 |
| 2025-03-04 | TSMC US$165B U.S. Expansion | Strategic_Importance | 7.391 | 4.935 | 6.163 |
| 2024-10-14 | Joint Sword-2024B | Risk | 1.390 | 7.561 | 4.475 |
| 2022-12-06 | TSMC Arizona US$40B Expansion | Strategic_Importance | 4.998 | 1.985 | 3.492 |
| 2023-08-12 | Lai U.S. Transit | Risk | 0.218 | 3.964 | 2.091 |

Three of the five most positive events are Strategic_Importance events. These are all connected to TSMC, CHIPS Act support, or supply-chain restructuring. This pattern is consistent with the idea that some Taiwan-related events may highlight economic and technological importance rather than only geopolitical vulnerability.

At the same time, two Risk events appear among the most positive observations. Joint Sword-2024B is especially important because it is a military demonstration but shows positive average abnormal returns over the [-7,+7] window.

## Sign Patterns

| mechanism | n | negative_avg_car_7 | positive_avg_car_7 | negative_twse_day0 | positive_twse_day0 | negative_tsmc_day0 | positive_tsmc_day0 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Risk | 14 | 10 | 4 | 11 | 3 | 11 | 3 |
| Strategic_Importance | 4 | 1 | 3 | 1 | 3 | 1 | 3 |

Most Risk events have negative average CAR over the [-7,+7] window, but not all do. Most Strategic_Importance events have positive average CAR over the same window, but not all do. The sign pattern therefore does not support a simple one-direction interpretation in which Taiwan-related geopolitical risk always corresponds to negative abnormal returns.

## Market Adaptation

The current `event_repetition` variable is available only for four core events in `data/events_v2.csv`. These observations provide an initial way to examine market adaptation.

| event_name | event_date | event_repetition | surprise_level | twse_day0_ar | twse_car_7 | tsmc_day0_ar | tsmc_car_7 | avg_car_7 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Pelosi Visit | 2022-08-02 | 1 | 2 | -1.401 | -4.233 | -2.261 | 0.234 | -1.999 |
| Joint Sword 2023 | 2023-04-08 | 2 | 1 | 0.443 | -3.728 | -1.986 | -1.416 | -2.572 |
| Joint Sword-2024A | 2024-05-23 | 3 | 1 | 0.648 | -0.426 | 1.289 | -3.469 | -1.947 |
| Joint Sword-2024B | 2024-10-14 | 4 | 1 | -0.549 | 1.390 | -1.804 | 7.561 | 4.475 |

The four-event sequence suggests a possible adaptation pattern. The average CAR remains negative for the first three observations but becomes positive for Joint Sword-2024B. The pattern is not monotonic, and the number of coded observations is small. Still, the later Joint Sword event does not resemble the strongly negative response seen in the earlier Pelosi crisis window.

## Results Summary

The descriptive results point to four main patterns.

First, Risk events are negative on average, but their market response is heterogeneous. Second, Strategic_Importance events are positive on average, but the BIS export-control event is a notable negative exception. Third, TSMC and TWSE do not always move together, suggesting that semiconductor-specific expectations may differ from broader Taiwan equity-market reactions. Fourth, the limited event-repetition evidence is consistent with possible market adaptation, but additional coding and testing are needed.

These patterns motivate a discussion of grey-zone sovereignty as a dual mechanism: it can generate geopolitical risk while also reinforcing Taiwan's strategic economic importance.
