# Discussion Section V1

## Overview

The preliminary findings complicate a simple risk-centered interpretation of Taiwan-related geopolitical events. Risk events are negative on average, but high-risk events do not consistently produce negative abnormal returns. Strategic_Importance events are positive on average, but technology-related events are also heterogeneous. The evidence therefore points toward a more conditional interpretation of Taiwan market reactions.

This section discusses theoretical implications for grey-zone sovereignty, market adaptation, and competing explanations. It does not make causal claims.

## Risk and Strategic Importance as Distinct Mechanisms

The descriptive results suggest that Taiwan-related events may enter markets through at least two different interpretive channels.

The first channel is `Risk`. Events such as military exercises, diplomatic shocks, political signaling, and economic coercion may increase perceived cross-strait uncertainty. In the current sample, Risk events have negative average abnormal returns:

| mechanism | twse_car_7 | tsmc_car_7 |
| --- | ---: | ---: |
| Risk | -2.647 | -0.571 |

The second channel is `Strategic_Importance`. Events connected to TSMC, CHIPS Act policy, and semiconductor supply-chain restructuring may highlight Taiwan's central role in global technology competition. In the current sample, Strategic_Importance events have positive average abnormal returns:

| mechanism | twse_car_7 | tsmc_car_7 |
| --- | ---: | ---: |
| Strategic_Importance | 2.974 | 2.754 |

This distinction matters because Taiwan's geopolitical position is not only a source of vulnerability. It can also signal value, indispensability, and policy support. The current data show both sides of this pattern.

## Market Adaptation

The event-repetition evidence is limited, but it raises an important question: do investors respond differently as similar Taiwan Strait events become more familiar?

The coded sequence from Pelosi Visit through Joint Sword-2024B suggests that repeated military demonstrations may not always produce the same market reaction. Pelosi Visit and Joint Sword 2023 show negative average CAR over the [-7,+7] window. Joint Sword-2024A remains slightly negative. Joint Sword-2024B is positive, especially for TSMC.

This pattern is consistent with a possible adaptation interpretation. Investors may distinguish between a novel crisis signal and a repeated grey-zone demonstration. However, the pattern should be treated cautiously. The repetition variable is currently coded for only four events, and each event occurred in a different broader market environment.

The implication is not that markets ignore geopolitical risk. Rather, the descriptive evidence suggests that the market reaction may depend on whether an event is perceived as a new shock, a repeated signal, or part of an increasingly familiar pattern of coercive behavior.

## Implications for Grey-Zone Sovereignty

The grey-zone sovereignty framework starts from the idea that Taiwan occupies an ambiguous political status: it is highly autonomous and globally important, but diplomatically constrained and militarily pressured. The event-study patterns fit this framework in a nuanced way.

On one side, grey-zone sovereignty generates risk. Military demonstrations, diplomatic shocks, and coercive actions can correspond to negative abnormal returns. The Pelosi crisis cluster and Strait Thunder-2025A illustrate this risk channel.

On the other side, grey-zone sovereignty also generates strategic importance. Taiwan's contested status and centrality to U.S.-China competition make its semiconductor sector unusually significant. TSMC-related investment and CHIPS Act events show positive average abnormal returns, suggesting that market reactions may sometimes reflect expectations of policy support, supply-chain investment, or strategic protection.

The theoretical implication is that Taiwan-related events should not be reduced to a single geopolitical-risk variable. A stronger framework should distinguish between events that primarily raise perceived danger and events that primarily highlight Taiwan's strategic indispensability.

## The Key Puzzle

The central empirical puzzle is that high geopolitical risk does not consistently correspond to negative abnormal returns.

Several patterns support this puzzle:

- Risk events are negative on average, but 4 of 14 Risk events have positive average CAR over [-7,+7].
- Joint Sword-2024B is a Risk event but appears among the most positive observations.
- Strategic_Importance events are positive on average, but BIS Advanced Semiconductor Export Controls appears among the most negative observations.
- TWSE and TSMC sometimes diverge, suggesting that broad-market Taiwan risk and semiconductor-specific expectations can move differently.

These patterns suggest that investors may not respond only to the objective severity of an event. They may also respond to perceived novelty, expected repetition, benchmark market conditions, sector-specific implications, and whether an event changes expectations about Taiwan's strategic value.

## Competing Explanations

Several competing explanations could account for the observed patterns.

One explanation is benchmark adjustment. Raw returns and abnormal returns sometimes differ sharply. For Strategic_Importance events, raw average CAR is negative while abnormal CAR is positive. This suggests that broader market conditions may mask Taiwan-specific or semiconductor-specific patterns in raw returns.

A second explanation is global technology-sector movement. TSMC abnormal returns are benchmarked against SOX, but semiconductor-market dynamics may still shape interpretation. Positive TSMC abnormal returns around CHIPS Act and U.S. expansion events may reflect sector expectations, supply-chain policy, or firm-specific news rather than Taiwan geopolitics alone.

A third explanation is event-window contamination. Some events are clustered closely together, especially during the Pelosi crisis. Overlapping windows make it difficult to isolate which event investors are responding to. The overlap-reduced sample should be used for later robustness checks.

A fourth explanation is anticipation. Some military exercises may have been expected before the event date. If investors anticipated the response, Day 0 abnormal returns may understate the full adjustment or shift it into the pre-event window.

A fifth explanation is market adaptation. Repeated grey-zone demonstrations may gradually become easier for investors to price. This could explain why later Joint Sword events do not display the same pattern as the Pelosi crisis period, although the current evidence remains preliminary.

## Theoretical Implications

The main theoretical implication is that grey-zone sovereignty may operate through a dual market logic.

The first logic is vulnerability. Taiwan's contested status exposes markets to military pressure, diplomatic shocks, and coercive economic signals. This is visible in the negative average abnormal returns for Risk events.

The second logic is indispensability. Taiwan's semiconductor and technology position can generate positive market expectations when events highlight policy support, supply-chain restructuring, or strategic investment. This is visible in the positive average abnormal returns for Strategic_Importance events.

These two logics can coexist. The same geopolitical environment that creates risk can also reinforce Taiwan's strategic value. This helps explain why a simple risk model struggles to account for the full set of preliminary results.

## Discussion Summary

The current evidence identifies patterns rather than causal effects. Risk events tend to be negative, Strategic_Importance events tend to be positive, and repeated military demonstrations may show signs of market adaptation. The most important implication is theoretical: Taiwan's grey-zone sovereignty should be modeled as producing both geopolitical risk and strategic economic value.

Future analysis should use a cleaner non-overlapping event sample, extend `event_repetition` coding to more events, and test whether surprise, repetition, and strategic-importance variables explain variation better than risk coding alone.
