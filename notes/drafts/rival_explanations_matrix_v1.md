# Rival Explanations Matrix V1

## Purpose

This memo acts as a skeptical review of the adaptation theory. It assumes the adaptation theory may be wrong and identifies alternative explanations for the current findings.

Current adaptation claim:

```text
Grey-Zone Sovereignty
        ↓
Repeated Shocks
        ↓
Investor Adaptation
        ↓
Market Reaction
```

The key empirical pattern is that Risk events are negative on average, but not uniformly negative. Joint Sword-2024B is a Risk event but appears among the most positive observations. The adaptation theory interprets this as evidence that repeated grey-zone shocks may become less damaging as investors learn the pattern. The rival explanations below challenge that interpretation.

## Rival Explanation 1: AI Boom

### Question

Did improving semiconductor and AI market conditions create the appearance of adaptation?

### Evidence For

The sample period overlaps with a major AI-driven equity boom. TSMC is deeply connected to AI chips, advanced-node manufacturing, and NVIDIA-linked supply chains. Positive abnormal returns around TSMC-related events may therefore reflect AI-market enthusiasm rather than adaptation to geopolitical risk.

Joint Sword-2024B appears positive especially because TSMC CAR [-7,+7] is strongly positive. This could reflect sector momentum or AI-related investor expectations rather than a learned response to repeated military exercises.

Strategic_Importance events are positive on average, especially TSMC CHIPS Act Preliminary Terms and TSMC U.S. expansion. These events may be capturing AI infrastructure expectations more than Taiwan-specific investor interpretation.

### Evidence Against

The analysis adjusts TSMC returns against SOX, which should partially account for semiconductor-sector movement. If TSMC still outperforms SOX around certain events, there may be a Taiwan-specific or firm-specific component.

Not all technology-related events are positive. BIS Advanced Semiconductor Export Controls is negative despite being part of semiconductor geopolitics. This weakens a simple "AI boom explains everything" account.

### What Additional Evidence Is Needed?

- Add NVIDIA returns and AI-sector indices as explicit controls.
- Compare TSMC with Samsung, SK Hynix, and other major semiconductor firms.
- Test whether positive TSMC abnormal returns cluster around AI news rather than Taiwan events.
- Separate AI-demand events from geopolitical or policy events.

## Rival Explanation 2: Semiconductor Cycle

### Question

Did sector-wide semiconductor strength explain positive TSMC abnormal returns?

### Evidence For

Semiconductor returns are cyclical. TSMC may outperform because of foundry utilization, advanced-node demand, inventory recovery, smartphone cycles, cloud demand, or capital-expenditure expectations.

The positive Strategic_Importance pattern may reflect where the semiconductor cycle was during CHIPS Act and TSMC expansion events. If TSMC was entering a stronger earnings or demand cycle, positive abnormal returns may not reflect geopolitical interpretation.

TSMC and TWSE sometimes diverge. This divergence may reflect TSMC-specific cycle dynamics rather than a theory of grey-zone sovereignty.

### Evidence Against

The use of SOX as a benchmark partially controls for sector-wide semiconductor movement. Positive TSMC abnormal returns after adjustment suggest that TSMC may have moved differently from the broader semiconductor sector.

Some Risk events also show positive returns, which a pure semiconductor-cycle explanation may not fully explain for TWSE.

### Needed Tests

- Compare TSMC abnormal returns against Samsung, Intel, AMD, NVIDIA, and a global foundry peer group.
- Add TSMC earnings dates, revenue announcements, and guidance changes as controls.
- Include semiconductor-cycle indicators such as SOX trend, foundry utilization proxies, and memory/logic cycle indicators.
- Re-run event windows excluding dates near TSMC earnings or major semiconductor news.

## Rival Explanation 3: Event Anticipation

### Question

Were later military exercises expected and therefore priced before Day 0?

### Evidence For

Many Taiwan-related events were predictable. The Pelosi Visit was discussed in advance. Joint Sword 2023 followed the Tsai-McCarthy meeting. Joint Sword-2024A followed Lai's inauguration. Joint Sword-2024B followed sovereignty-related political signaling.

If investors expected a PRC military response, the market adjustment may have occurred before the event date. A muted or positive Day 0 or event-window reaction does not necessarily mean adaptation; it may mean the event contained little new information.

This explanation is especially relevant to later military exercises. Their positive or less negative returns may reflect low surprise rather than learning.

### Evidence Against

The current event-window design includes pre-event days, especially [-7,+7], which should capture some anticipatory repricing. However, if anticipation occurs earlier than seven trading days before the event, the window may still miss it.

The event_repetition pattern from Pelosi to Joint Sword-2024B is consistent with adaptation, but anticipation and adaptation are difficult to separate because repeated events are also more predictable.

### Needed Tests

- Code `surprise_level` for the full sample.
- Extend pre-event windows to [-14,+7] and [-21,+7].
- Track news mentions and prediction signals before event dates.
- Compare scheduled events with unscheduled shocks.
- Separate "anticipated response" events from genuinely unexpected events.

## Rival Explanation 4: Event Selection Bias

### Question

Does the sample overrepresent major political events?

### Evidence For

The sample is manually constructed and may overrepresent highly visible diplomatic and military events. Major political events are easier to identify and source than lower-salience market-relevant events.

The current abnormal-return file contains 18 events, with Risk events outnumbering Strategic_Importance events. Strategic_Importance has only 4 observations, so category averages are fragile.

Several events belong to crisis clusters, especially the Pelosi period. Clustered events may overweight a few episodes and make repeated-shock patterns appear stronger than they are.

### Evidence Against

The project has already created overlap reports and an overlap-reduced sample, which shows awareness of contamination risk. The main event families are substantively important and not arbitrary.

The included events map onto clear inclusion criteria: Taiwan Strait military activity, diplomatic shocks, economic coercion, semiconductor geopolitics, and U.S.-Taiwan/China-Taiwan relations.

### Needed Tests

- Define a systematic event universe before estimating effects.
- Use transparent inclusion/exclusion rules for all events.
- Re-run results with the overlap-reduced sample only.
- Conduct leave-one-cluster-out tests, especially excluding the Pelosi cluster.
- Add lower-salience events to test whether patterns hold outside headline crises.

## Rival Explanation 5: Benchmark Specification

### Question

Would different benchmarks change the findings?

Examples:

- TWSE vs MSCI Asia
- TWSE vs MSCI Emerging Markets
- TSMC vs Samsung
- TSMC vs global foundry peers
- Taiwan vs Korea

### Evidence For

The current abnormal returns are calculated using simple benchmark subtraction: TWSE minus NASDAQ and TSMC minus SOX. These benchmarks are reasonable first-pass choices, but they may not isolate Taiwan-specific effects.

NASDAQ is technology-heavy and U.S.-specific. SOX may be affected by the same semiconductor and AI forces that affect TSMC. Taiwan and U.S. trading calendars also differ. Different benchmarks could change the sign or magnitude of abnormal returns.

The raw vs abnormal comparison already shows that benchmark choice matters. For Strategic_Importance events, raw average CAR is negative while abnormal CAR is positive. This means the findings are sensitive to adjustment method.

### Evidence Against

Benchmark adjustment is still better than raw returns, and the TWSE/NASDAQ and TSMC/SOX pairings are conceptually defensible as first-pass controls.

The Risk vs Strategic_Importance contrast appears meaningful after adjustment, and the major puzzle cases remain visible in the current specification.

### Needed Tests

- Recalculate abnormal returns using MSCI Asia, MSCI Emerging Markets, S&P 500, and regional Asia benchmarks.
- Compare Taiwan to Korea as a regional technology-market counterfactual.
- Compare TSMC to Samsung and global semiconductor peers.
- Estimate market-model abnormal returns rather than simple subtraction.
- Report whether the adaptation pattern survives across benchmark specifications.

## Research Design Roadmap

### Ranking of Rival Explanations

| rank | explanation | plausibility | reason |
| ---: | --- | --- | --- |
| 1 | Event Anticipation | Most plausible | Repeated military exercises are likely anticipated, and anticipation is hard to separate from adaptation. |
| 2 | Benchmark Specification | Most plausible | Raw and abnormal results differ substantially, so benchmark choice may affect conclusions. |
| 3 | AI Boom | Moderately plausible | Positive TSMC returns may reflect AI-sector momentum, especially in later events. |
| 4 | Semiconductor Cycle | Moderately plausible | Sector-cycle dynamics may explain TSMC-specific strength, but SOX adjustment partially addresses this. |
| 5 | Event Selection Bias | Moderately plausible | Manual event selection and clustering matter, but the event universe is substantively grounded. |

### Needed Research Design Improvements

Priority tests:

1. Re-run all results on the overlap-reduced sample.
2. Add full-sample `event_repetition` and `surprise_level` coding.
3. Run alternative benchmark specifications.
4. Compare TSMC with Samsung, NVIDIA, and global semiconductor peers.
5. Extend pre-event windows to test anticipation.
6. Conduct cluster-robust or leave-cluster-out robustness checks.

### Confidence in Adaptation Theory

Confidence level: `Moderate`

Justification:

The adaptation theory is plausible and directly addresses the central puzzle. It explains why repeated military demonstrations may become less damaging over time and why the simple risk model fails. The sequence from Pelosi Visit to Joint Sword-2024B is consistent with adaptation.

However, confidence should not be high. Event anticipation is a serious rival explanation because repeated events are also more predictable. Benchmark specification may affect abnormal-return signs. AI boom and semiconductor-cycle dynamics may explain positive TSMC returns. The current evidence also relies on a small number of coded repetition observations.

The appropriate position is therefore moderate confidence: adaptation is the best current theoretical explanation, but it remains underidentified until anticipation, benchmark sensitivity, AI-sector conditions, semiconductor-cycle effects, and event selection are tested more systematically.
