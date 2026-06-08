# Limitations V1

## Purpose

This memo lists the main limitations of the current Taiwan event-study design. It is written from the standpoint of a skeptical reviewer.

The goal is to identify weaknesses that must be addressed before stronger claims can be made.

## 1. Small-N Design

The current abnormal-return analysis contains 18 events. Only 4 are coded as `Strategic_Importance`.

This creates several problems:

- Means are sensitive to individual events.
- Outliers can dominate mechanism-level averages.
- Category comparisons are imbalanced.
- Statistical inference is not meaningful at this stage.
- Adaptation cannot be tested robustly with only four coded repetition observations.

The current results should therefore be described as exploratory and descriptive.

## 2. Event Selection

The event sample is manually constructed. This is appropriate for an early-stage project, but it creates selection concerns.

Potential weaknesses:

| limitation | implication |
| --- | --- |
| Manual inclusion | The sample may reflect researcher judgment rather than a systematic event universe. |
| Salience bias | Highly publicized events may be overrepresented. |
| Ex post knowledge | Event inclusion may be influenced by later awareness of importance. |
| Uneven coverage | Military and diplomatic events are more numerous than technology events. |
| Exclusion sensitivity | Results may change after overlap reduction or alternative event filtering. |

The project needs a clearer rule for the event universe: what counts as a Taiwan geopolitical event, what does not, and how borderline cases are handled.

## 3. Event-Window Contamination

The current study uses [-7,+7] trading-day windows. Several events occur close together, especially during crisis periods.

Examples:

- Pelosi warning, visit, trade restrictions, and military exercises occur within a short period.
- Tsai-McCarthy Meeting and Joint Sword 2023 are closely linked.
- Lai inauguration and Joint Sword-2024A are closely linked.
- Lai National Day Speech and Joint Sword-2024B are closely linked.

This makes it difficult to assign abnormal returns to a single event. A return inside the event window may reflect multiple signals, policy responses, or market updates.

The overlap-reduced sample is a useful improvement, but results should be compared across both the full and reduced samples.

## 4. Anticipation and Information Leakage

Many events were not complete surprises. Investors may have adjusted before the event date.

This is especially important for:

- high-profile diplomatic visits;
- inaugurations;
- scheduled speeches;
- anticipated PLA responses;
- expected U.S. technology-policy announcements.

If repricing occurs before Day 0, event-day returns may understate the market reaction. If the event is anticipated and unfolds as expected, the post-event reaction may look muted or even positive.

The current design does not directly measure anticipation.

## 5. Benchmark Choice

The study currently uses simple benchmark-adjusted returns:

| market | benchmark |
| --- | --- |
| TWSE | NASDAQ |
| TSMC | SOX |

This is useful as a first adjustment, but it is not a full abnormal-return model.

Limitations:

- NASDAQ may be too technology-heavy to represent broad global market conditions.
- SOX may be too close to the same semiconductor forces driving TSMC.
- The method subtracts benchmark returns rather than estimating normal sensitivity.
- Calendar mismatches between Taiwan and U.S. markets can create missing or shifted observations.
- Currency effects are not included.
- Regional Asian market conditions are not included.

Future versions should compare results using multiple benchmarks, such as MSCI Taiwan, MSCI Asia, S&P 500, NASDAQ, SOX, and possibly USD/TWD.

## 6. AI Boom Confounding

The sample period overlaps with a major AI-related equity-market boom. This is a serious confounder for TSMC and semiconductor-related events.

TSMC-related positive abnormal returns may reflect:

- AI-chip demand;
- NVIDIA supply-chain expectations;
- advanced-node scarcity;
- data-center investment;
- global semiconductor momentum;
- U.S. industrial-policy enthusiasm.

These forces may be related to Taiwan's strategic importance, but they are not identical to it.

Without stronger controls, it is difficult to separate Taiwan-specific strategic interpretation from global AI-sector momentum.

## 7. Semiconductor Cycle Confounding

Semiconductor returns are shaped by industry cycles. TSMC may move differently from SOX because of firm-specific cycle positioning.

Relevant cycle factors include:

- inventory correction;
- foundry utilization;
- capital expenditure;
- customer demand;
- smartphone and PC cycles;
- AI-server demand;
- advanced-node pricing power.

These factors could explain some TSMC abnormal returns without requiring a geopolitical interpretation.

## 8. Measurement of Mechanisms

The current mechanism categories are useful but still broad.

`Risk` includes:

- military demonstrations;
- diplomatic shocks;
- economic coercion;
- political signaling.

`Strategic_Importance` includes:

- technology competition;
- supply-chain restructuring;
- CHIPS Act and TSMC investment events.

These categories may hide important differences. A military demonstration, diplomatic visit, export-control event, and TSMC investment announcement may operate through different channels.

Future coding should distinguish:

- military threat;
- diplomatic shock;
- economic coercion;
- export-control constraint;
- supply-chain support;
- AI opportunity;
- semiconductor-cycle exposure.

## 9. Limited Adaptation Coding

The market-adaptation argument currently relies on `event_repetition`, but this variable is coded for only four events in `data/events_v2.csv`.

This is not enough to test adaptation. The current evidence can only suggest a possible pattern.

A stronger adaptation test would require:

- repetition coding for the full sample;
- explicit crisis-cluster identifiers;
- separation of anticipated and unexpected events;
- comparison of early vs later events within the same event family;
- robustness checks using shorter and longer event windows.

## 10. No Causal Identification

The current project identifies patterns, not causal effects.

The event-study design does not fully rule out:

- simultaneous macroeconomic news;
- global equity-market movement;
- semiconductor-sector shocks;
- AI-related repricing;
- foreign-exchange effects;
- firm-specific TSMC news;
- overlapping Taiwan political events.

The language of the paper should therefore avoid claims that an event caused a particular market movement unless stronger identification is added.

## Highest-Priority Fixes

1. Re-run abnormal returns using the overlap-reduced sample.
2. Add multiple benchmarks and compare sensitivity.
3. Code `event_repetition` and `surprise_level` for the full sample.
4. Separate AI/semiconductor-cycle variables from Taiwan geopolitical variables.
5. Add robustness checks for [-1,+1], [-3,+3], and [-7,+7] windows.
6. Document the event-selection rule more systematically.

## Bottom Line

The current evidence is promising but fragile. The most important limitations are small sample size, event-window overlap, AI and semiconductor-cycle confounding, benchmark choice, and incomplete measurement of anticipation and adaptation.

At this stage, the project should present its findings as exploratory patterns and theoretical motivation, not as evidence of a settled causal relationship.
