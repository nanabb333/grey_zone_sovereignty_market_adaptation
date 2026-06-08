# Chapter 5: Results

## 5.1 Overview of Market Responses

This chapter presents the empirical results from the Taiwan event-study analysis. Its purpose is descriptive: to report observed patterns in abnormal returns around Taiwan-related geopolitical-risk and strategic-importance events. Causal interpretation is reserved for Chapter 6.

The analysis uses benchmark-adjusted abnormal returns for two financial-market indicators: the TWSE, representing the broader Taiwan equity market, and TSMC, representing Taiwan's strategic semiconductor exposure. TWSE abnormal returns are calculated relative to NASDAQ returns, while TSMC abnormal returns are calculated relative to the Philadelphia Semiconductor Index. The main outcome is cumulative abnormal return over the [-7,+7] event window, although Day 0 and shorter windows are also reported in the underlying results.

The abnormal-return file contains eighteen events. Fourteen are coded as geopolitical-risk events and four are coded as strategic-importance events. This imbalance should be noted from the outset: risk events are more frequent in the sample, while strategic-importance events are fewer and therefore more sensitive to individual cases.

The first descriptive pattern is clear: risk events are negative on average, while strategic-importance events are positive on average. For risk events, the average TWSE CAR over the [-7,+7] window is -2.647, while the average TSMC CAR is -0.571. For strategic-importance events, the average TWSE CAR is 2.974, while the average TSMC CAR is 2.754. Day 0 abnormal returns show the same broad contrast. Risk events have negative average Day 0 abnormal returns for both TWSE and TSMC, while strategic-importance events have positive average Day 0 abnormal returns.

| mechanism | n | TWSE Day 0 AR | TWSE CAR [-7,+7] | TSMC Day 0 AR | TSMC CAR [-7,+7] |
| --- | ---: | ---: | ---: | ---: | ---: |
| Risk | 14 | -0.814 | -2.647 | -1.340 | -0.571 |
| Strategic_Importance | 4 | 0.737 | 2.974 | 0.667 | 2.754 |

The second descriptive pattern is that benchmark adjustment changes the appearance of the results. For risk events, raw average returns are slightly positive, but abnormal returns are negative. This suggests that once broader market movements are considered, Taiwan-related underperformance becomes more visible. For strategic-importance events, raw average returns are negative, but abnormal returns are positive. This indicates that some events may look weak in raw price terms while still outperforming broader benchmarks. The contrast between raw and abnormal returns is important because it shows why benchmark adjustment is necessary for interpretation.

| mechanism | TWSE Day 0 raw | TWSE Day 0 AR | TWSE raw CAR [-7,+7] | TWSE CAR [-7,+7] | TSMC Day 0 raw | TSMC Day 0 AR | TSMC raw CAR [-7,+7] | TSMC CAR [-7,+7] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Risk | 0.076 | -0.814 | 0.541 | -2.647 | 0.189 | -1.340 | 1.716 | -0.571 |
| Strategic_Importance | -0.838 | 0.737 | -3.068 | 2.974 | -1.677 | 0.667 | -5.788 | 2.754 |

Figure 5.1 would visualise the average CAR [-7,+7] by event type, comparing geopolitical-risk events with strategic-importance events for both TWSE and TSMC. The purpose of the figure would be to show the main descriptive contrast in the results: risk events are negative on average, while strategic-importance events are positive on average.

**Figure 5.1: Average CAR [-7,+7] by Event Type**

The third descriptive pattern is variation. The average results conceal considerable dispersion across events. Across the full sample, the average TWSE CAR [-7,+7] is negative, while the average TSMC CAR is close to zero. The range is wide: TWSE CAR varies from -8.971 to 7.391, while TSMC CAR varies from -5.499 to 9.597. This spread is central to the dissertation's puzzle. The results do not show a simple pattern in which all geopolitical-risk events produce negative abnormal returns or all strategic-importance events produce positive abnormal returns. Instead, the results show group-level tendencies combined with important exceptions.

## 5.2 Responses to Geopolitical-Risk Events

Geopolitical-risk events show negative average abnormal returns. This is the strongest descriptive finding in the chapter. Risk events have an average TWSE CAR [-7,+7] of -2.647 and an average TSMC CAR [-7,+7] of -0.571. The broader Taiwan market response is more negative than the TSMC response, suggesting that country-level risk may be more visible in the TWSE than in TSMC. This pattern is consistent with the expectation that events involving coercion, escalation, diplomatic tension, or sovereignty-related pressure tend to increase uncertainty for Taiwan markets.

The sign pattern reinforces this point. Ten of fourteen risk events have negative average CAR over the [-7,+7] window, while four have positive average CAR. On Day 0, eleven of fourteen risk events are negative for TWSE and eleven of fourteen are negative for TSMC. This indicates that negative market responses are common among risk events, especially on the event day. However, the presence of positive risk-event observations also shows that the pattern is not uniform.

| mechanism | n | negative average CAR [-7,+7] | positive average CAR [-7,+7] | negative TWSE Day 0 | positive TWSE Day 0 | negative TSMC Day 0 | positive TSMC Day 0 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Risk | 14 | 10 | 4 | 11 | 3 | 11 | 3 |
| Strategic_Importance | 4 | 1 | 3 | 1 | 3 | 1 | 3 |

The most negative observations are concentrated among risk events. Four of the five most negative events in the sample are coded as risk events. These include China Trade Restrictions After Pelosi Visit, PLA Military Exercises After Pelosi Visit, Strait Thunder-2025A, and Joint Sword 2023. The China Trade Restrictions event records a TWSE CAR of -7.673 and a TSMC CAR of -5.125, producing an average CAR of -6.399. The PLA Military Exercises After Pelosi Visit event records a TWSE CAR of -7.800 and a TSMC CAR of -4.189, with an average CAR of -5.995. Strait Thunder-2025A records the most negative TWSE CAR in the sample, at -8.971, although its TSMC CAR is less negative at -0.947.

Figure 5.2 would display event-level average CAR [-7,+7] for all events, ordered from most negative to most positive. This figure would make visible the wide dispersion hidden by group averages and would highlight the main deviant observations, including Joint Sword-2024B and BIS Advanced Semiconductor Export Controls.

**Figure 5.2: Event-level Average CAR [-7,+7]**

| event date | event name | mechanism | TWSE CAR [-7,+7] | TSMC CAR [-7,+7] | average CAR [-7,+7] |
| --- | --- | --- | ---: | ---: | ---: |
| 2022-08-03 | China Trade Restrictions After Pelosi Visit | Risk | -7.673 | -5.125 | -6.399 |
| 2022-08-04 | PLA Military Exercises After Pelosi Visit | Risk | -7.800 | -4.189 | -5.995 |
| 2022-10-07 | BIS Advanced Semiconductor Export Controls | Strategic_Importance | -5.088 | -5.499 | -5.294 |
| 2025-04-01 | Strait Thunder-2025A | Risk | -8.971 | -0.947 | -4.959 |
| 2023-04-08 | Joint Sword 2023 | Risk | -3.728 | -1.416 | -2.572 |

The Pelosi-related crisis period is especially important descriptively. The China Trade Restrictions event and the PLA Military Exercises event both appear among the most negative observations. Pelosi Visit itself is also negative for TWSE over the [-7,+7] window, with a TWSE CAR of -4.233, although TSMC CAR is slightly positive at 0.234. This suggests that the broader Taiwan market registered a negative abnormal response during the Pelosi crisis period, while TSMC's response was less uniformly negative.

Military demonstrations also vary. Joint Sword 2023 is negative for both TWSE and TSMC over the [-7,+7] window. Joint Sword-2024A is negative for both indicators as well, although the TWSE decline is small at -0.426 while TSMC falls by -3.469. By contrast, Joint Sword-2024B is positive over the same window for both TWSE and TSMC. This variation within the military-demonstration category is one of the most important descriptive findings. It shows that event category alone does not fully determine market direction.

The results for political-signalling and diplomatic-risk events are also mixed. Lai U.S. Transit is coded as a risk event but produces positive CAR over the [-7,+7] window for both TWSE and TSMC. PRC Judicial Guidelines on Taiwan Independence produces a slightly negative TWSE CAR but a positive TSMC CAR. These observations do not overturn the average negative pattern among risk events, but they show that the market response to geopolitical risk is heterogeneous.

## 5.3 Responses to Strategic-Importance Events

Strategic-importance events are positive on average. The four events in this category have an average TWSE CAR [-7,+7] of 2.974 and an average TSMC CAR of 2.754. Day 0 abnormal returns are also positive on average. This pattern is consistent with the expectation that events highlighting Taiwan's role in semiconductor geopolitics, supply-chain restructuring, and technology competition may generate positive market responses when investors interpret them as signals of policy support, strategic value, or future investment.

Three of the five most positive events in the sample are strategic-importance events. TSMC CHIPS Act Preliminary Terms is the most positive observation overall, with a TWSE CAR of 4.595 and a TSMC CAR of 9.597. TSMC US$165B U.S. Expansion is the second most positive event, with a TWSE CAR of 7.391 and a TSMC CAR of 4.935. TSMC Arizona US$40B Expansion is also positive, with a TWSE CAR of 4.998 and a TSMC CAR of 1.985. These results suggest that TSMC-related strategic investment and U.S. industrial-policy support are associated with positive abnormal returns in the current sample.

| event date | event name | mechanism | TWSE CAR [-7,+7] | TSMC CAR [-7,+7] | average CAR [-7,+7] |
| --- | --- | --- | ---: | ---: | ---: |
| 2024-04-08 | TSMC CHIPS Act Preliminary Terms | Strategic_Importance | 4.595 | 9.597 | 7.096 |
| 2025-03-04 | TSMC US$165B U.S. Expansion | Strategic_Importance | 7.391 | 4.935 | 6.163 |
| 2024-10-14 | Joint Sword-2024B | Risk | 1.390 | 7.561 | 4.475 |
| 2022-12-06 | TSMC Arizona US$40B Expansion | Strategic_Importance | 4.998 | 1.985 | 3.492 |
| 2023-08-12 | Lai U.S. Transit | Risk | 0.218 | 3.964 | 2.091 |

The strongest strategic-importance event is the TSMC CHIPS Act Preliminary Terms announcement. It produces positive abnormal returns for both TWSE and TSMC, with the TSMC response particularly large. This suggests that markets responded favourably to an event associated with industrial-policy support and supply-chain restructuring. The TSMC US$165B U.S. Expansion event also produces positive abnormal returns for both indicators. The positive TWSE response indicates that strategic-importance events may affect the broader Taiwan market as well as TSMC.

However, the category is not uniformly positive. BIS Advanced Semiconductor Export Controls is a strategic-importance event but appears among the five most negative observations. It records a TWSE CAR of -5.088 and a TSMC CAR of -5.499. This is a crucial descriptive result because it prevents an overly simple interpretation of strategic importance. Events connected to semiconductor geopolitics can be positive when they signal support, investment, or protection. They can be negative when they signal restriction, fragmentation, compliance costs, or uncertainty in technology supply chains.

The strategic-importance results therefore support a conditional descriptive pattern. The category is positive on average, but not because strategic importance automatically produces positive returns. Rather, the positive average is driven by TSMC-related investment and policy-support events, while the BIS export-control event shows that technology competition can also be market-negative. This distinction matters for the dissertation's theoretical framework because it supports the claim that strategic importance is a source of interpretation rather than a deterministic market signal.

## 5.4 Deviant Cases

The results include several deviant cases, meaning observations where market reactions contradict the broad expectation associated with the event classification. These cases are important because they reveal the limits of a simple risk-versus-opportunity classification. They do not invalidate the classification scheme, but they show that market responses vary within each category.

The key deviant case is Joint Sword-2024B. It is classified as a risk event because it was a military demonstration around Taiwan. Under a simple geopolitical-risk expectation, such an event would be expected to produce negative abnormal returns. Instead, Joint Sword-2024B records a positive TWSE CAR of 1.390 and a strongly positive TSMC CAR of 7.561 over the [-7,+7] window. Its average CAR of 4.475 places it among the five most positive observations in the sample. This makes it the most important case for the dissertation's central puzzle: a high-profile military event did not correspond to negative abnormal returns in the observed window.

The deviance of Joint Sword-2024B is especially clear when compared with earlier military-demonstration events. Joint Sword 2023 records negative CAR for both TWSE and TSMC. Joint Sword-2024A records a slightly negative TWSE CAR and a more negative TSMC CAR. The PLA Military Exercises After Pelosi Visit event is strongly negative for both indicators. Joint Sword-2024B therefore differs from several earlier military-risk events. The chapter does not explain this difference causally; it simply notes that the observation is inconsistent with a uniform risk-response model.

The second major deviant case is BIS Advanced Semiconductor Export Controls. It is classified as a strategic-importance event because it belongs to semiconductor geopolitics and U.S.-China technology competition. A broad strategic-importance expectation might suggest positive returns if investors interpreted the event as highlighting the value of advanced semiconductor capabilities. Instead, the event produces negative abnormal returns for both TWSE and TSMC. This indicates that strategic-importance events can also be associated with negative market responses, especially when the event involves restrictions rather than investment or support.

Lai U.S. Transit is another deviant case, though less central than Joint Sword-2024B. It is classified as a risk event but produces positive CAR for both TWSE and TSMC. PRC Judicial Guidelines on Taiwan Independence also shows divergence across indicators: TWSE is slightly negative while TSMC is positive. These cases show that not all risk events are priced in the same way and that TSMC may respond differently from the broader Taiwan market.

The deviant cases are useful because they sharpen rather than weaken the empirical contribution. If all risk events were negative and all strategic-importance events were positive, the results would support a simple classification model. Instead, the data show average tendencies with important exceptions. The exceptions are precisely what motivate the theoretical framework developed in Chapters 2 and 3. At this stage, however, the chapter confines itself to description. The implications of these deviant cases for adaptation, anticipation, and rival explanations are developed in Chapter 6.

## 5.5 Preliminary Evidence Consistent with Adaptation

The results contain limited preliminary evidence compatible with an adaptation-based interpretation. This evidence should be treated cautiously. Adaptation is not directly observed in the data. The analysis observes abnormal returns around repeated events and asks whether the pattern is consistent with the possibility that investors interpret later shocks as more familiar or less novel. It does not prove that investors learned, adapted, or consciously reclassified Taiwan-related risk.

The clearest descriptive comparison involves four core events for which repetition and surprise coding are currently available: Pelosi Visit, Joint Sword 2023, Joint Sword-2024A, and Joint Sword-2024B. These events form a sequence of Taiwan-related crisis or military-demonstration episodes. In this sequence, event repetition rises from 1 for Pelosi Visit to 4 for Joint Sword-2024B. The average CAR over the [-7,+7] window is negative for the first three events and positive for Joint Sword-2024B.

Figure 5.3 would plot this repetition sequence, showing event repetition on the horizontal axis and average CAR [-7,+7] on the vertical axis. Its purpose would be illustrative rather than confirmatory: the figure would show the movement from negative average CAR in the earlier observations to positive average CAR for Joint Sword-2024B, while also making clear that the sequence contains only four coded cases.

**Figure 5.3: Repetition Sequence from Pelosi Visit to Joint Sword-2024B**

| event name | event date | event repetition | surprise level | TWSE Day 0 AR | TWSE CAR [-7,+7] | TSMC Day 0 AR | TSMC CAR [-7,+7] | average CAR [-7,+7] |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Pelosi Visit | 2022-08-02 | 1 | 2 | -1.401 | -4.233 | -2.261 | 0.234 | -1.999 |
| Joint Sword 2023 | 2023-04-08 | 2 | 1 | 0.443 | -3.728 | -1.986 | -1.416 | -2.572 |
| Joint Sword-2024A | 2024-05-23 | 3 | 1 | 0.648 | -0.426 | 1.289 | -3.469 | -1.947 |
| Joint Sword-2024B | 2024-10-14 | 4 | 1 | -0.549 | 1.390 | -1.804 | 7.561 | 4.475 |

This sequence is consistent with, but does not prove, an adaptation interpretation. Pelosi Visit and Joint Sword 2023 are negative on average. Joint Sword-2024A remains negative on average but less strongly so. Joint Sword-2024B becomes positive on average. The sequence should be interpreted as an illustrative pattern rather than a statistically robust trend. It suggests that later repeated military demonstrations may have produced less negative market responses than earlier crisis events, but the sequence is not perfectly monotonic. Joint Sword 2023 is more negative than Pelosi Visit on average, and Joint Sword-2024A still shows a negative TSMC response. The number of coded observations is also very small.

The surprise coding further complicates interpretation. Pelosi Visit has a higher surprise level than the later Joint Sword events. This is consistent with the idea that novelty matters: the Pelosi episode may have carried more information because it was more surprising, while later Joint Sword events may have been more anticipated. Yet this creates a rival interpretation. A weaker reaction to later events may reflect anticipation rather than adaptation. If investors expected a PRC military response before Day 0, the event-window return may understate the full market adjustment.

For this reason, the evidence should be described as consistent with adaptation rather than as evidence of adaptation itself. The data show that later repeated events do not always produce the same negative response as earlier events. They also show that Joint Sword-2024B is a positive deviant case within the risk category. These patterns are compatible with the adaptation-based framework, but they also fit other possible explanations, including anticipation, AI-sector momentum, semiconductor-cycle effects, benchmark specification, and event-selection choices. Chapter 6 evaluates these rival explanations more directly.

## 5.6 Summary of Findings

The chapter reports six main empirical findings. First, geopolitical-risk events are negative on average. This is visible in both Day 0 abnormal returns and cumulative abnormal returns over the [-7,+7] window. The broader Taiwan market, represented by TWSE, shows a stronger negative average response than TSMC.

Second, strategic-importance events are positive on average. TSMC CHIPS Act Preliminary Terms, TSMC US$165B U.S. Expansion, and TSMC Arizona US$40B Expansion all produce positive abnormal returns over the [-7,+7] window. These events are connected to semiconductor policy, supply-chain restructuring, and strategic investment.

Third, the results show substantial variation across events. Most risk events are negative, but four of fourteen risk events have positive average CAR over the [-7,+7] window. Most strategic-importance events are positive, but BIS Advanced Semiconductor Export Controls is negative. The results therefore do not support a uniform one-direction model.

Fourth, Joint Sword-2024B is the key deviant case. It is classified as a geopolitical-risk event because it is a military demonstration, yet it produces positive abnormal returns over the [-7,+7] window, especially for TSMC. This result is central to the dissertation's empirical puzzle.

Fifth, TWSE and TSMC do not always move together. Some events are negative for the broader Taiwan market but less negative or positive for TSMC. This divergence suggests that broad-market Taiwan risk and semiconductor-specific expectations may differ.

Sixth, the repetition sequence from Pelosi Visit to Joint Sword-2024B provides preliminary evidence compatible with an adaptation-based interpretation. The evidence is limited and should not be treated as proof. It shows that later repeated military events are not uniformly more damaging and that the most recent Joint Sword event in the sequence is positive over the main event window.

Overall, the results are consistent with the theoretical framework developed in Chapters 2 and 3, but they do not prove it. The empirical pattern is best described as conditional. Risk events tend to be negative, strategic-importance events tend to be positive, and substantial variation remains within both categories. The descriptive evidence suggests that a simple geopolitical-risk model may be insufficient to explain all observed market reactions. Chapter 6 therefore turns from description to interpretation, assessing whether these patterns are better explained by adaptation or by alternative explanations such as anticipation effects, AI-sector optimism, semiconductor-cycle dynamics, benchmark specification, and event-selection choices.
