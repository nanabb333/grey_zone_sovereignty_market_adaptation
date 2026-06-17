# Theory Expansion Readiness

> Academic Research Notice:
> This report assesses readiness for theory-variable expansion. It does not perform event-study analysis or create CAR results.

## Current Coverage

Baseline file: `data/events_v2.csv`

| Field | Current status |
| --- | --- |
| `interpretation_type` | Fully coded for 18 events. |
| `strategic_importance_level` | Sparse; concentrated in semiconductor investment and export-control events. |
| `state_support_signal` | Sparse; concentrated in strategic-investment and CHIPS-related events. |

## Projected Improvement

The 20 Include candidates would make theory coding more useful by adding repeated observations in categories that are currently underrepresented:

- Export-control escalation.
- Allied semiconductor-tool controls.
- China countermeasures.
- Critical-materials controls.
- Industrial-policy and state-support events.
- Recognition-diplomacy events.

## Readiness By Variable

| Variable | Readiness | Reason |
| --- | --- | --- |
| `interpretation_type` | High | Existing rules transfer cleanly to the candidate set. |
| `strategic_importance_level` | High | Most Include candidates have direct semiconductor, Taiwan, supply-chain, or strategic-technology relevance. |
| `state_support_signal` | Medium-High | Strong for CHIPS Act, European Chips Act, TSMC Japan, and Big Fund III; weaker for export-control and diplomatic cases. |
| `event_family` | High | Candidate families are clear, though some new categories should be standardized. |
| `surprise_score` | Medium | Requires source timing and pre-event expectation review. |

## Expected Coverage Shift

The expansion should move the project from a dataset where theory coding is dominated by military risk and a few strategic-investment events toward one with enough variation to compare policy, investment, coercion, and diplomatic mechanisms.

Expected improvements:

- More `High` strategic-importance observations.
- More `High` state-support observations.
- More `Mixed` export-control observations.
- More `Threat` observations from countermeasures and recognition losses.
- More `Opportunity` observations from industrial-policy and strategic-investment cases.

## Remaining Readiness Conditions

Before integration, the project still needs:

- Evidence packets for each Include candidate.
- Event-trading-date mapping.
- Confounding-event review.
- Consistent event-family naming.
- Coding-log updates after validation.

## Bottom Line

Theory expansion is ready at the protocol level but not yet complete at the evidence level. The next sprint should validate sources and trading dates before copying any candidates into the master event dataset.
