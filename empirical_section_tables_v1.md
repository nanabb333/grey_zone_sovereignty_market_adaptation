# Empirical Section Tables V1

## Purpose

These tables organize the empirical section for the dissertation. They are designed for use in the Results and Discussion chapters. The goal is not to prove investor adaptation. The goal is to evaluate whether the observed market responses are consistent with an adaptation-based interpretation while taking rival explanations seriously.

The tables use the current 18-event abnormal-return sample in `market_abnormal_returns.csv` and event metadata from `final_event_study_sample.csv`.

## Table 1. Event Classification

Expected direction is based on the event classification before observing the market reaction.

| event date | event name | event type | justification for classification | expected market direction |
| --- | --- | --- | --- | --- |
| 2022-07-19 | China Warns Against Pelosi Taiwan Visit | Geopolitical-risk event | Public PRC warning increased perceived diplomatic and cross-strait escalation risk. | Negative |
| 2022-08-02 | Pelosi Visit | Geopolitical-risk event | High-level U.S. visit directly challenged PRC red lines and raised crisis risk. | Negative |
| 2022-08-03 | China Trade Restrictions After Pelosi Visit | Geopolitical-risk event | Trade restrictions represented economic coercion after a sovereignty-related shock. | Negative |
| 2022-08-04 | PLA Military Exercises After Pelosi Visit | Geopolitical-risk event | Major military exercises signaled coercive pressure and cross-strait escalation. | Negative |
| 2022-10-07 | BIS Advanced Semiconductor Export Controls | Strategic-importance event | U.S. semiconductor controls linked Taiwan's chip ecosystem to U.S.-China technology competition. | Positive |
| 2022-12-06 | TSMC Arizona US$40B Expansion | Strategic-importance event | TSMC expansion highlighted Taiwan's centrality to strategic semiconductor supply chains. | Positive |
| 2023-04-08 | Joint Sword 2023 | Geopolitical-risk event | PLA exercises after the Tsai-McCarthy meeting increased military signaling around Taiwan. | Negative |
| 2023-08-12 | Lai U.S. Transit | Geopolitical-risk event | U.S. transit by Taiwan's vice president carried diplomatic and sovereignty-signaling risk. | Negative |
| 2023-08-19 | PLA Drills After Lai U.S. Transit | Geopolitical-risk event | PRC drills after Lai's transit represented coercive military signaling. | Negative |
| 2023-08-26 | China Sends Aircraft and Vessels After U.S. Arms Sale | Geopolitical-risk event | PRC military movement followed U.S.-Taiwan security activity. | Negative |
| 2024-04-08 | TSMC CHIPS Act Preliminary Terms | Strategic-importance event | CHIPS Act terms signaled U.S. policy support for TSMC and supply-chain restructuring. | Positive |
| 2024-05-20 | Lai Ching-te Inauguration | Geopolitical-risk event | Presidential transition carried sovereignty-signaling and PRC response risk. | Negative |
| 2024-05-23 | Joint Sword-2024A | Geopolitical-risk event | PLA exercises after Lai's inauguration directly signaled cross-strait coercion. | Negative |
| 2024-06-21 | PRC Judicial Guidelines on Taiwan Independence | Geopolitical-risk event | Legal coercion against Taiwan independence raised political and sovereignty-related risk. | Negative |
| 2024-10-14 | Joint Sword-2024B | Geopolitical-risk event | PLA exercises after political signaling represented renewed coercive military pressure. | Negative |
| 2025-01-22 | PLA Joint Combat Readiness Patrols Around Taiwan | Geopolitical-risk event | PLA patrols represented direct military pressure around Taiwan. | Negative |
| 2025-03-04 | TSMC US$165B U.S. Expansion | Strategic-importance event | Expanded TSMC U.S. investment highlighted Taiwan's strategic role in semiconductor geopolitics. | Positive |
| 2025-04-01 | Strait Thunder-2025A | Geopolitical-risk event | Large-scale PLA exercises and blockade simulations represented direct security risk. | Negative |

## Table 2. Main Results

Match is coded as `Yes` if both TWSE and TSMC CAR move in the expected direction, `No` if both contradict the expected direction, and `Mixed` if the two assets diverge.

| event name | TWSE CAR [-7,+7] | TSMC CAR [-7,+7] | matches expected direction? | short interpretation |
| --- | ---: | ---: | --- | --- |
| China Warns Against Pelosi Taiwan Visit | -0.880 | -3.254 | Yes | Early warning phase shows negative market response consistent with geopolitical-risk expectations. |
| Pelosi Visit | -4.233 | 0.234 | Mixed | Broad market reaction is negative, but TSMC is resilient, suggesting asset-specific divergence. |
| China Trade Restrictions After Pelosi Visit | -7.673 | -5.125 | Yes | Economic coercion coincides with clearly negative abnormal returns. |
| PLA Military Exercises After Pelosi Visit | -7.800 | -4.189 | Yes | Acute military escalation is consistent with the threat channel. |
| BIS Advanced Semiconductor Export Controls | -5.088 | -5.499 | No | Strategic-importance classification is contradicted; export controls may be interpreted as constraint or fragmentation. |
| TSMC Arizona US$40B Expansion | 4.998 | 1.985 | Yes | TSMC investment event is consistent with opportunity and supply-chain-support interpretation. |
| Joint Sword 2023 | -3.728 | -1.416 | Yes | Military exercise remains consistent with negative threat interpretation. |
| Lai U.S. Transit | 0.218 | 3.964 | No | Diplomatic-risk event does not produce negative abnormal returns; anticipation or market context may matter. |
| PLA Drills After Lai U.S. Transit | -3.085 | -0.898 | Yes | Military response is consistent with negative risk expectations. |
| China Sends Aircraft and Vessels After U.S. Arms Sale | -1.013 | -2.958 | Yes | Security-related PRC signaling is associated with negative abnormal returns. |
| TSMC CHIPS Act Preliminary Terms | 4.595 | 9.597 | Yes | Strongly positive results support strategic-importance and policy-support interpretation. |
| Lai Ching-te Inauguration | 0.545 | -3.320 | Mixed | TWSE and TSMC diverge, suggesting broad political risk and semiconductor expectations differ. |
| Joint Sword-2024A | -0.426 | -3.469 | Yes | Military exercise still shows negative abnormal returns, especially for TSMC. |
| PRC Judicial Guidelines on Taiwan Independence | -0.491 | 4.081 | Mixed | Legal-political risk is negative for TWSE but positive for TSMC, indicating asset-specific interpretation. |
| Joint Sword-2024B | 1.390 | 7.561 | No | Central deviant case: military-risk event generates positive abnormal returns. |
| PLA Joint Combat Readiness Patrols Around Taiwan | -0.906 | 1.736 | Mixed | Broad market response is negative but TSMC is positive, again suggesting sector-specific resilience. |
| TSMC US$165B U.S. Expansion | 7.391 | 4.935 | Yes | Strongly positive strategic-importance case consistent with opportunity interpretation. |
| Strait Thunder-2025A | -8.971 | -0.947 | Yes | Large military exercise is consistent with negative geopolitical-risk expectations. |

## Table 3. Deviant Cases

Deviant cases are events where observed market reactions contradict or complicate the pre-event classification.

| event | classification | observed pattern | why it matters theoretically |
| --- | --- | --- | --- |
| Joint Sword-2024B | Geopolitical-risk event | TWSE and TSMC CAR are both positive. | This is the most important deviant case. It challenges a simple risk model and is consistent with adaptation, anticipation, or favorable semiconductor conditions. |
| Lai U.S. Transit | Geopolitical-risk event | TWSE and TSMC CAR are both positive. | Suggests that diplomatic-risk events may be priced as manageable when anticipated or when market context is favorable. |
| BIS Advanced Semiconductor Export Controls | Strategic-importance event | TWSE and TSMC CAR are both negative. | Shows that strategic-importance events are not automatically positive; technology competition can signal restriction and fragmentation. |
| Pelosi Visit | Geopolitical-risk event | TWSE is negative but TSMC is slightly positive. | Shows that broad Taiwan market risk and TSMC-specific expectations can diverge during the same shock. |
| Lai Ching-te Inauguration | Geopolitical-risk event | TWSE is positive but TSMC is negative. | Indicates that scheduled political events may produce mixed asset-level interpretation. |
| PRC Judicial Guidelines on Taiwan Independence | Geopolitical-risk event | TWSE is negative but TSMC is positive. | Suggests that legal-political coercion may affect broad Taiwan risk more than semiconductor expectations. |
| PLA Joint Combat Readiness Patrols Around Taiwan | Geopolitical-risk event | TWSE is negative but TSMC is positive. | Raises the possibility that repeated military pressure is less damaging to TSMC than to the broader market. |

## Why the Deviant Cases Matter

The deviant cases are theoretically important because they prevent the analysis from collapsing into a simple severity model. If objective geopolitical risk were sufficient, military demonstrations and sovereignty-related shocks should be uniformly negative. They are not. If strategic importance were sufficient, semiconductor-policy events should be uniformly positive. They are not.

Joint Sword-2024B is the strongest case for the adaptation interpretation because it is a repeated military demonstration and yet produces positive abnormal returns. However, the case does not prove adaptation. It could also reflect anticipation, AI-sector strength, benchmark specification, or event-window contamination. The theoretical value of the case is that it identifies where the simple risk model fails and where rival explanations must be tested.

## Table 4. Robustness and Rival Explanations

| rival explanation | how it could challenge the adaptation argument | implication for interpretation | needed empirical check |
| --- | --- | --- | --- |
| Anticipation | Later military exercises may have been expected and priced before Day 0. | Weaker market damage may reflect low surprise rather than learning. | Code `surprise_level`; extend pre-event windows to [-14,+7] or [-21,+7]. |
| AI boom | Positive TSMC returns may reflect global AI demand rather than adaptation to Taiwan risk. | Joint Sword-2024B's positive TSMC CAR may be sector-driven. | Control for NVIDIA and AI-sector indices; compare with non-Taiwan AI-linked firms. |
| Semiconductor cycle | TSMC may outperform because of foundry-cycle strength rather than geopolitical interpretation. | Positive TSMC abnormal returns may reflect firm or sector fundamentals. | Compare TSMC with Samsung, Intel, AMD, NVIDIA, and foundry peers. |
| Benchmark specification | NASDAQ and SOX may not isolate Taiwan-specific effects. | Sign and magnitude of abnormal returns may change under different benchmarks. | Re-estimate using MSCI Asia, MSCI Emerging Markets, S&P 500, Samsung, and Korea benchmarks. |
| Event-selection bias | The sample may overrepresent major political events and crisis clusters. | Apparent adaptation may be driven by which events are included or excluded. | Re-run analysis using overlap-reduced sample and leave-one-cluster-out tests. |

## Discussion Text for Results Chapter

The empirical results show a clear average distinction between geopolitical-risk events and strategic-importance events, but the distinction is not deterministic. Risk events generally produce negative abnormal returns, which is consistent with the threat channel. Strategic-importance events generally produce positive abnormal returns, which is consistent with the opportunity channel. However, several cases deviate from these expectations. These deviations are not residual noise; they are theoretically important because they reveal where a simple geopolitical-risk model fails.

The most important deviant case is Joint Sword-2024B. It is classified as a geopolitical-risk event because it involved coercive PLA military activity around Taiwan. The expected market direction is negative. Instead, both TWSE and TSMC CAR are positive over the [-7,+7] window. This pattern is consistent with an adaptation-based interpretation: repeated military demonstrations may become less damaging as investors learn to distinguish familiar grey-zone signaling from new crisis escalation. Yet the evidence remains provisional. Joint Sword-2024B may also reflect anticipation, favorable semiconductor conditions, benchmark sensitivity, or broader AI-market strength.

The results therefore support a cautious interpretation. The evidence is consistent with adaptation, but it does not prove adaptation. The dissertation should present adaptation as the most theoretically parsimonious interpretation of the deviant risk cases, while treating anticipation, AI boom, semiconductor cycle, benchmark specification, and event-selection bias as serious rival explanations.
