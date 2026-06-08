# Cross-Event Findings

## Purpose

This note summarizes early patterns across four Taiwan geopolitical-risk events:

1. Pelosi Visit on 2022-08-02.
2. Joint Sword 2023 on 2023-04-08.
3. Joint Sword-2024A on 2024-05-23.
4. Joint Sword-2024B on 2024-10-14.

The comparison uses -7 to +7 trading-day windows and raw daily returns from `data/market.csv`.

## Comparison Summary

| Event | TWSE Day-0 Return | TWSE Window Return | TSMC Day-0 Return | TSMC Window Return |
| --- | ---: | ---: | ---: | ---: |
| Pelosi Visit | -1.56% | 1.74% | -2.38% | 2.59% |
| Joint Sword 2023 | 0.25% | -0.91% | -0.38% | -5.38% |
| Joint Sword-2024A | 0.26% | 3.26% | 1.27% | 3.30% |
| Joint Sword-2024B | 0.32% | 2.24% | 0.00% | 6.00% |

## Preliminary Patterns

The Pelosi Visit shows the clearest event-day disruption. Both TWSE and TSMC fell on the event day, with TSMC showing a larger negative reaction.

Joint Sword 2023 shows a weaker day-0 reaction but a worse full-window outcome, especially for TSMC. This suggests that military exercises may not always trigger an immediate one-day selloff, but they can still coincide with broader weakness across the event window.

Joint Sword-2024A shows positive day-0 and window returns for both TWSE and TSMC. This suggests that market reaction may depend on expectations, prior pricing, broader market conditions, and whether investors interpret the event as contained.

Joint Sword-2024B also shows positive window returns, especially for TSMC. This strengthens the early finding that repeated PLA exercises do not automatically produce negative raw equity returns.

## Interpretation

Across these early cases, market effects are not uniform:

1. Diplomatic crisis can produce sharp event-day disruption.
2. Military exercises can have mixed day-0 effects and sometimes positive window returns.
3. TSMC sometimes reacts more strongly than the broader TWSE index.
4. Positive window returns do not mean the geopolitical event had no risk effect; they may reflect market recovery or broader market momentum.

## Method Notes

Joint Sword 2023 occurred on 2023-04-08, which was not a trading day. The analysis uses 2023-04-10 as the event trading date.

Joint Sword-2024B occurred on 2024-10-14, which was a trading day in the cleaned market dataset.

These are raw returns only. The project does not yet include:

1. Benchmark-adjusted abnormal returns.
2. NASDAQ or global technology benchmark controls.
3. USD/TWD exchange-rate reaction.
4. Statistical significance testing.

## Future Questions

1. Do high `military_risk` events have larger window effects than high `diplomatic_risk` events?
2. Does TSMC react more strongly than TWSE during semiconductor-relevant geopolitical events?
3. Are positive post-event returns evidence of recovery, resilience, or unrelated market momentum?
4. How do results change after adding NASDAQ, NVIDIA, and USD/TWD?
