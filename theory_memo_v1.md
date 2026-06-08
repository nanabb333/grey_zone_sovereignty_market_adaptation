# Theory Memo V1

## Purpose

This memo identifies the minimum theory needed to explain the current findings. It is based on `01_introduction_v2.md`, `research_design_memo_v1.md`, `02_literature_architecture_v1.md`, `results_section_v1.md`, and `discussion_section_v1.md`.

The goal is parsimony. The theory should not maximize mechanisms. It should identify the simplest mechanism that explains the central puzzle:

Why do some Taiwan-related geopolitical shocks fail to generate persistent market damage despite elevated objective risk?

## Main Conclusion

The primary mechanism should be `Adaptation`.

The current evidence does not support a simple theory:

```text
Grey-Zone Sovereignty
        ↓
Risk
        ↓
Market Reaction
```

Risk matters, but risk alone does not explain the variation. A more parsimonious theory is:

```text
Grey-Zone Sovereignty
        ↓
Repeated Geopolitical Shocks
        ↓
Investor Adaptation
        ↓
Market Reaction
```

This model keeps the theory focused. Grey-zone sovereignty produces repeated shocks. Repetition changes investor interpretation. As investors become more familiar with recurring grey-zone behavior, some shocks become less damaging than a simple risk model would predict.

## Which Mechanism Has the Strongest Empirical Support?

The answer depends on the level of analysis.

At the broad descriptive level, `Threat` has the strongest support. Risk events are negative on average:

| mechanism | n | twse_car_7 | tsmc_car_7 |
| --- | ---: | ---: | ---: |
| Risk | 14 | -2.647 | -0.571 |
| Strategic_Importance | 4 | 2.974 | 2.754 |

Risk events also account for most of the most negative observations. This supports the basic claim that threat matters.

However, `Threat` does not explain the central puzzle. If threat were sufficient, high-risk military events should consistently produce negative abnormal returns. They do not. Joint Sword-2024B is a Risk event but appears among the most positive observations.

For explaining the puzzle, `Adaptation` has the strongest theoretical leverage. The limited repetition evidence shows a movement from the negative Pelosi and Joint Sword 2023 responses toward a positive Joint Sword-2024B response:

| event | event_repetition | avg_car_7 |
| --- | ---: | ---: |
| Pelosi Visit | 1 | -1.999 |
| Joint Sword 2023 | 2 | -2.572 |
| Joint Sword-2024A | 3 | -1.947 |
| Joint Sword-2024B | 4 | 4.475 |

The pattern is not fully monotonic, and the sample is small. Still, adaptation best explains why repeated military demonstrations may become less damaging over time.

## Primary Mechanism

`Adaptation` should be treated as the primary mechanism.

Reason:

The project's core puzzle is not whether risk ever damages markets. It does. The puzzle is why some high-risk events do not produce persistent market damage. Adaptation directly addresses that puzzle by linking repeated grey-zone shocks to changing investor interpretation.

Primary mechanism:

```text
Repeated shocks reduce novelty.
Reduced novelty weakens threat interpretation.
Weaker threat interpretation produces less negative market reaction.
```

This mechanism fits the revised concept of grey-zone sovereignty. Grey-zone sovereignty is not a one-time crisis condition. It is a persistent political ambiguity that generates recurring shocks. Because the shocks recur, investors may learn to distinguish between familiar signaling and events that materially change the risk environment.

## Secondary Mechanisms

### Threat

`Threat` should be treated as the baseline mechanism.

Risk events are negative on average. This means the theory should not abandon geopolitical risk. Threat explains why Pelosi Visit, Joint Sword 2023, trade restrictions, and Strait Thunder-2025A are negative.

But threat is not sufficient because several Risk events are not negative.

### Opportunity

`Opportunity` should be treated as a secondary mechanism for technology and semiconductor events.

Strategic_Importance events are positive on average, especially TSMC CHIPS Act Preliminary Terms and TSMC U.S. expansion. These events suggest that some Taiwan-related shocks highlight policy support, supply-chain value, or semiconductor centrality.

But opportunity is not sufficient because BIS Advanced Semiconductor Export Controls is a Strategic_Importance event and is negative. Strategic importance can create opportunity, but it can also signal constraint or fragmentation.

### Surprise

`Surprise` should be treated as a conditioning mechanism.

Surprise likely affects the size of market reactions, but current evidence does not directly measure surprise across the full sample. It should be included in future coding, but not treated as the central theory yet.

## Which Model Does the Current Evidence Support?

The evidence supports the second model more strongly:

```text
Grey-Zone Sovereignty
        ↓
Repeated Shocks
        ↓
Investor Adaptation
        ↓
Market Reaction
```

The simple risk model explains the average direction of Risk events but fails to explain the exceptions. The adaptation model explains why repeated military demonstrations can become less damaging even when objective risk remains high.

The simplest version of the theory is therefore not:

```text
More risk -> more negative returns
```

It is:

```text
Repeated grey-zone shocks become less novel,
and less novel shocks generate weaker negative market reactions.
```

## Simplest Theory That Explains the Findings

The minimum theory is:

Taiwan's grey-zone sovereignty produces recurring geopolitical shocks. Early or novel shocks are more likely to be interpreted as threats and produce negative abnormal returns. Repeated shocks become more familiar, allowing investors to adapt. As adaptation increases, some high-risk events generate weaker negative reactions or even positive abnormal returns, especially when they do not change expected fundamentals.

This theory explains:

1. Why Risk events are negative on average.
2. Why some Risk events are not negative.
3. Why Joint Sword-2024B can be positive despite being a military event.
4. Why the project needs repetition and interpretation, not only objective risk.

It does not fully explain Strategic_Importance events. For those, opportunity remains a secondary mechanism. But the central puzzle is about high-risk events that fail to damage markets, so adaptation should carry the theoretical core.

## Theory Choice

Primary theory:

```text
Grey-Zone Sovereignty -> Repeated Shocks -> Investor Adaptation -> Market Reaction
```

Secondary extensions:

```text
Threat explains negative first-order risk responses.
Opportunity explains positive strategic-importance responses.
Surprise conditions the size of the reaction.
```

This is the most parsimonious theory currently supported by the evidence.
