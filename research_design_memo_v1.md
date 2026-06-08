# Research Design Memo V1

## Working Title

Grey-Zone Sovereignty and Market Adaptation: Explaining Financial Responses to Taiwan-Related Geopolitical Shocks

## Research Question

How do Taiwan-related geopolitical events affect financial markets through competing investor interpretations of threat, strategic importance, surprise, and adaptation?

The motivating puzzle is that higher geopolitical risk does not consistently produce negative abnormal returns. Pelosi Visit and Joint Sword 2023 generated negative abnormal returns, while Joint Sword-2024B and several TSMC-related strategic-importance events generated positive abnormal returns. Risk events are negative on average, but not uniformly negative. Strategic_Importance events are positive on average, but not uniformly positive.

## Dependent Variable

The dependent variable is financial-market reaction to Taiwan-related geopolitical events.

Primary measures:

- TWSE abnormal return
- TSMC abnormal return
- Day 0 abnormal return
- Cumulative abnormal returns over short event windows, especially [-7,+7]

Abnormal returns are benchmark-adjusted. TWSE returns are adjusted against NASDAQ, and TSMC returns are adjusted against SOX.

## Independent Variables

The main independent variables are event-level characteristics.

Core variables:

- `mechanism`: Risk or Strategic_Importance
- `event_category`: Military Demonstration, Diplomatic Shock, Economic Coercion, Political Signaling, Technology Competition
- `event_repetition`: degree to which similar events have occurred previously
- `surprise_level`: degree to which the event was anticipated

Risk events include military exercises, diplomatic shocks, coercive economic measures, and sovereignty-related political signaling. Strategic_Importance events include semiconductor policy, TSMC-related investment, export controls, and supply-chain restructuring.

## Mechanisms

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

Grey-zone sovereignty is defined as a persistent condition of political ambiguity that simultaneously generates recurring geopolitical risk and strategic economic importance.

Investor interpretation is the central mechanism. Risk and Strategic_Importance are not automatic determinants of market outcomes. They are sources of interpretation.

Threat: investors interpret the event as escalation, coercion, or instability.

Opportunity: investors interpret the event as evidence of Taiwan's strategic value, policy support, or semiconductor importance.

Adaptation: investors interpret repeated grey-zone events as familiar or manageable.

Surprise: investors react more strongly when events differ from expectations.

## Preliminary Empirical Patterns

Current event-level abnormal-return file:

| mechanism | n | twse_day0_ar | twse_car_7 | tsmc_day0_ar | tsmc_car_7 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Risk | 14 | -0.814 | -2.647 | -1.340 | -0.571 |
| Strategic_Importance | 4 | 0.737 | 2.974 | 0.667 | 2.754 |

Risk events are negative on average, but 4 of 14 Risk events have positive average CAR over [-7,+7]. Strategic_Importance events are positive on average, but BIS Advanced Semiconductor Export Controls is a negative exception. This supports a conditional interpretation model rather than a simple risk model.

## Alternative Explanations

Key alternatives to address:

- AI boom: positive TSMC-related returns may reflect global AI demand rather than Taiwan-specific strategic interpretation.
- Semiconductor cycle: TSMC may outperform SOX because of firm-specific cycle positioning.
- Anticipation: expected PLA responses or diplomatic events may be priced before Day 0.
- Event-window overlap: clustered events may contaminate each other's windows.
- Benchmark choice: NASDAQ and SOX may not fully isolate Taiwan-specific effects.
- Global market conditions: U.S. rates, tech-sector momentum, and macro news may drive returns.

## Identification Challenges

The main identification problem is that raw and abnormal returns cannot be interpreted as causal effects without stronger controls.

Specific challenges:

- Small-N sample, especially only 4 Strategic_Importance events.
- Manual event selection may create salience bias.
- Events cluster around crises, creating overlapping windows.
- Taiwan and U.S. trading calendars differ.
- Abnormal returns use simple benchmark subtraction rather than an estimated market model.
- `event_repetition` and `surprise_level` are not yet coded for the full sample.

The current design should therefore be presented as exploratory and descriptive.

## Theoretical Contribution

The project revises a simple geopolitical-risk model. Instead of:

```text
Grey-Zone Sovereignty -> Risk -> Market Reaction
```

it proposes:

```text
Grey-Zone Sovereignty -> Geopolitical Event -> Investor Interpretation -> Market Reaction
```

The theoretical contribution is to show that Taiwan's grey-zone sovereignty generates both vulnerability and strategic value. Financial-market reactions depend on whether investors interpret events as threats, opportunities, repeated grey-zone behavior, or surprises.

## Expected Contribution to IR and IPE

For IR, the project connects sovereignty ambiguity, recognition constraints, strategic ambiguity, and coercive grey-zone activity to observable market behavior.

For IPE, it links geopolitical shocks to financial-market pricing, semiconductor supply chains, economic statecraft, and strategic investment.

The expected contribution is a framework for studying how markets interpret geopolitical shocks in cases where security risk and strategic economic value coexist.
