# Alternative Explanations

## Purpose

This memo evaluates alternative explanations for the preliminary event-study patterns. It is based on `results_section_v1.md`, `discussion_section_v1.md`, and `theory_revision_v1.md`.

The posture here is skeptical. The goal is not to defend the revised theory, but to identify other mechanisms that could explain the observed abnormal-return patterns.

## Summary of the Empirical Pattern

The current results show:

- Risk events are negative on average, but not uniformly negative.
- Strategic_Importance events are positive on average, but not uniformly positive.
- Some military events show positive abnormal returns.
- Some technology events show negative abnormal returns.
- TWSE and TSMC sometimes diverge.

These patterns may be consistent with a grey-zone sovereignty interpretation, but they may also reflect broader market forces, sector cycles, anticipation, sample design, or benchmark limitations.

## 1. AI Boom

The positive abnormal returns around TSMC-related events may reflect the global AI boom rather than Taiwan-specific strategic importance.

During the period covered by the study, investor enthusiasm around AI chips, data centers, advanced semiconductors, and NVIDIA-linked supply chains became a major market force. TSMC sits at the center of this global AI hardware ecosystem. Positive abnormal returns around TSMC expansion or CHIPS Act events may therefore reflect AI-demand expectations rather than a market interpretation of Taiwan's geopolitical importance.

This is especially relevant for:

| event | concern |
| --- | --- |
| TSMC CHIPS Act Preliminary Terms | May reflect AI-chip demand and U.S. industrial policy optimism. |
| TSMC US$165B U.S. Expansion | May reflect global AI supply-chain expectations rather than Taiwan-specific geopolitics. |
| TSMC Arizona US$40B Expansion | May reflect long-run semiconductor capacity expectations. |

Skeptical interpretation:

The positive Strategic_Importance pattern may be partly or mostly an AI-sector valuation effect. Without explicit controls for AI-related market movement, the project may overstate the geopolitical interpretation of these positive returns.

## 2. Semiconductor Cycle

The semiconductor industry is cyclical. Returns around Taiwan-related technology events may reflect where the industry was in its demand, inventory, and capital-expenditure cycle.

Semiconductor stocks can move because of:

- inventory corrections;
- foundry utilization expectations;
- memory and logic demand cycles;
- capital-expenditure guidance;
- customer demand from AI, smartphones, cloud, and automotive sectors;
- global rate and liquidity conditions.

This matters because TSMC abnormal returns are benchmarked against SOX, but SOX may not fully capture TSMC-specific positioning within the cycle. TSMC may outperform or underperform SOX because of firm-specific expectations rather than Taiwan geopolitics.

Skeptical interpretation:

The difference between TSMC and SOX may not be a clean Taiwan-specific abnormal return. It may reflect TSMC's position within the semiconductor cycle, especially if TSMC was expected to benefit more than other semiconductor firms from AI demand or advanced-node scarcity.

## 3. Anticipation

Several geopolitical events were likely anticipated before the event date. If investors adjusted expectations before Day 0, the event-study design may misplace the market reaction.

Examples:

| event | anticipation concern |
| --- | --- |
| Pelosi Visit | The visit was discussed before the event date, so some repricing may have occurred before arrival. |
| Joint Sword 2023 | The PLA response followed the Tsai-McCarthy meeting and may have been expected. |
| Joint Sword-2024A | A PRC response after Lai's inauguration may have been anticipated. |
| Joint Sword-2024B | A response after sovereignty-related political signaling may have been anticipated. |

Anticipation creates two problems.

First, Day 0 abnormal returns may understate the total event effect. Second, positive or muted returns after the event may not mean the event was interpreted positively; it may mean the negative information had already been priced in.

Skeptical interpretation:

The apparent market adaptation pattern may partly reflect anticipation. Later Joint Sword events may look less negative because investors expected them before the event window or because the event did not exceed prior expectations.

## 4. Event Selection

The sample is constructed from manually selected events. This creates possible selection bias.

Potential issues:

| issue | concern |
| --- | --- |
| Salience bias | Highly visible events are more likely to be included than less visible but market-relevant events. |
| Ex post selection | Events may be selected partly because they are known to matter historically. |
| Uneven category coverage | Risk events outnumber Strategic_Importance events. |
| Cluster dependence | Multiple events come from the same crisis period, especially the Pelosi cluster. |
| Documentation availability | Events with stronger English-language documentation may be overrepresented. |

The current abnormal-return file uses 18 events, but the overlap-reduced sample contains fewer independent events. This matters because the strongest negative and positive observations may be sensitive to whether clustered events are included.

Skeptical interpretation:

The Risk vs Strategic_Importance contrast may be partly a sample-construction artifact. If the event list changes, especially if overlapping events are reduced or if more technology events are added, the mechanism averages may change.

## 5. Benchmark Choice

The abnormal-return design uses:

| Taiwan variable | benchmark |
| --- | --- |
| TWSE | NASDAQ |
| TSMC | SOX |

These are reasonable first-pass benchmarks, but they may not fully isolate Taiwan-specific effects.

Concerns:

- NASDAQ is U.S.-technology heavy, not a global equity-market benchmark.
- SOX is semiconductor-sector specific, but it may still be strongly affected by the same AI and chip-cycle forces that affect TSMC.
- Currency movements, Taiwan domestic macro conditions, and Asia-Pacific market movements are not directly controlled.
- Benchmark trading calendars differ from Taiwan's market calendar.
- A simple return subtraction does not estimate normal market sensitivity using a market model.

Skeptical interpretation:

The abnormal returns may still contain unmodeled global, regional, sectoral, and currency effects. The benchmark adjustment improves on raw returns, but it should not be treated as a full identification strategy.

## 6. Small-N Limitations

The sample is small, especially for Strategic_Importance events.

Current mechanism counts:

| mechanism | n |
| --- | ---: |
| Risk | 14 |
| Strategic_Importance | 4 |

The Strategic_Importance average is therefore highly sensitive to individual observations. For example, one negative technology event, BIS Advanced Semiconductor Export Controls, materially changes the interpretation. Similarly, positive results for CHIPS Act and TSMC expansion events may dominate the category average.

Small-N also limits the ability to evaluate:

- adaptation;
- surprise;
- category-specific effects;
- TWSE vs TSMC differences;
- event-window sensitivity;
- outlier influence.

Skeptical interpretation:

The results are useful for generating hypotheses, but the sample is not large enough to support stable estimates or strong theoretical adjudication.

## Most Important Alternative Explanation

The strongest skeptical alternative is that the observed positive Strategic_Importance pattern may be driven by the AI boom and semiconductor cycle rather than by investor interpretation of Taiwan's geopolitical importance.

The strongest skeptical challenge to the Risk pattern is anticipation and event clustering. If later military events were expected, or if multiple crisis events overlap, the observed abnormal returns may not map cleanly onto individual geopolitical shocks.

## Reviewer Takeaway

The current theory is plausible but underidentified. The observed patterns could reflect grey-zone sovereignty, but they could also reflect AI-sector momentum, semiconductor-cycle variation, event anticipation, sample construction, and benchmark design.

The next version of the project should treat these explanations as live alternatives rather than background caveats.
