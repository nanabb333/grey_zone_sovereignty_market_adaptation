# Theory Revision V1

## Purpose

This memo reassesses the original theoretical framework after the first event-study results. It is based on `results_section_v1.md` and `discussion_section_v1.md`.

The revision is conceptual and descriptive. It does not claim that the observed market reactions are caused by the coded events.

## Original Framework

The original framework was:

```text
Grey-Zone Sovereignty
        ↓
Risk
        ↓
Market Reaction
```

This framework treated Taiwan's contested political status mainly as a source of geopolitical risk. The expected market implication was straightforward: higher geopolitical risk should correspond to more negative market reactions.

## Empirical Problem

The preliminary findings complicate this simple framework.

Observed patterns:

1. Risk events are negative on average, but they are not uniformly negative.
2. Strategic_Importance events are positive on average, but they are not uniformly positive.
3. Some military events generate positive abnormal returns.
4. Some technology events generate negative abnormal returns.
5. TWSE and TSMC sometimes move differently, suggesting that broad-market Taiwan risk and semiconductor-specific expectations are not identical.

The strongest empirical puzzle is that high geopolitical risk does not consistently produce negative abnormal returns. Joint Sword-2024B is coded as a Risk event but appears among the most positive observations. BIS Advanced Semiconductor Export Controls is coded as Strategic_Importance but appears among the most negative observations.

## Why the Original Framework Is Too Simple

The original model assumes that geopolitical events transmit directly into markets through risk. The evidence suggests that this transmission is filtered through investor interpretation.

A Taiwan-related event can be interpreted in multiple ways:

| interpretation | meaning | possible market pattern |
| --- | --- | --- |
| Threat | The event raises perceived danger, coercion, or escalation risk. | Negative abnormal returns may appear. |
| Opportunity | The event highlights Taiwan's strategic value, policy support, or semiconductor importance. | Positive abnormal returns may appear. |
| Adaptation | The event resembles repeated prior episodes and is less surprising. | Market reaction may be muted or less negative. |
| Surprise | The event is less anticipated than expected. | Market reaction may be larger or more volatile. |

This interpretation layer helps explain why the same broad category of event can produce different market patterns.

## Revised Framework

The revised framework is:

```text
Grey-Zone Sovereignty
        ↓
Geopolitical Event
        ↓
Investor Interpretation
        ├── Threat
        ├── Opportunity
        ├── Adaptation
        └── Surprise
        ↓
Market Reaction
```

This revision changes the theory in three ways.

First, `Risk` is no longer the only pathway. Grey-zone sovereignty can generate both vulnerability and strategic value.

Second, the event itself is not enough to predict the market response. The market response depends on how investors interpret the event relative to prior expectations, repeated patterns, and the strategic role of Taiwan's semiconductor sector.

Third, market reactions may differ across assets. TWSE may reflect broad Taiwan market risk, while TSMC may reflect both Taiwan risk and semiconductor-sector expectations.

## Revised Theoretical Logic

### 1. Grey-Zone Sovereignty Creates Ambiguous Market Signals

Taiwan's sovereignty status is politically unresolved, diplomatically constrained, and militarily pressured. This creates exposure to coercive signals and cross-strait escalation.

At the same time, Taiwan's central role in semiconductors and U.S.-China technology competition gives it strategic importance. The same geopolitical environment that creates vulnerability can also increase perceived indispensability.

### 2. Geopolitical Events Are Interpreted Through Multiple Channels

Risk events can be interpreted as threat signals, but repeated risk events may also be interpreted as familiar grey-zone behavior. Strategic_Importance events can be interpreted as opportunity signals, but some technology events may also introduce uncertainty, constraints, or supply-chain disruption.

This helps explain why:

- Risk events are negative on average but not uniformly negative.
- Strategic_Importance events are positive on average but not uniformly positive.
- Military demonstrations can sometimes coincide with positive abnormal returns.
- Export controls can carry strategic significance while producing negative abnormal returns.

### 3. Adaptation Modifies the Risk Channel

The sequence from Pelosi Visit to Joint Sword-2024B suggests a possible adaptation pattern. The later repeated military demonstration does not resemble the strongly negative Pelosi crisis pattern.

This does not prove adaptation, but it suggests that repetition should be included in the theory. Investors may react differently to a novel crisis signal than to a repeated grey-zone demonstration.

### 4. Surprise Modifies the Size and Direction of Reaction

Events that are anticipated may produce smaller Day 0 reactions, while less anticipated events may produce sharper market adjustments. Surprise should therefore be separated from objective event severity.

This distinction matters because a high-risk event may produce a limited market reaction if investors expected it, while a lower-risk event may produce a larger reaction if it changes expectations.

## Revised Expectations

The revised framework implies descriptive expectations rather than causal claims.

| expectation | statement |
| --- | --- |
| E1 | Events interpreted mainly as threats should be associated with more negative abnormal returns. |
| E2 | Events interpreted mainly as strategic-importance signals should be associated with more positive abnormal returns. |
| E3 | Repeated event types should show weaker or less negative market reactions than novel shocks. |
| E4 | More surprising events should show larger market reactions than anticipated events. |
| E5 | TWSE and TSMC may respond differently because they represent different exposures to Taiwan risk and semiconductor opportunity. |

## Implications for the Project

The project should move from a single-path risk model to a conditional interpretation model.

The old question was:

> How does geopolitical risk affect Taiwan financial markets?

The revised question should ask:

> How do Taiwan-related geopolitical events affect financial markets through competing interpretations of risk, strategic importance, surprise, and adaptation?

This revised question better matches the empirical patterns. It also fits the grey-zone sovereignty concept because Taiwan's ambiguous status produces both risk and strategic value.

## Next Steps

1. Extend `event_repetition` and `surprise_level` coding to the full event sample.
2. Separate threat-oriented events from opportunity-oriented events.
3. Re-run results using the overlap-reduced event-study sample.
4. Compare TWSE and TSMC reactions separately.
5. Treat technology events as heterogeneous, distinguishing supply-chain opportunity from export-control constraint.
