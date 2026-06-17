# Theory Interaction Analysis

> Academic Research Notice:
> This report explores selected combinations of theory variables using descriptive counts and available CAR summaries. It does not infer causal effects or create synthetic CAR values.

## Scope

- Input dataset: `data/events_v3.csv`
- Validated events: 25
- Events with available CAR summaries: 18

## Interaction Summary

| Combination | Event count | CAR n | Avg TSMC CAR 7 | Avg TWSE CAR 7 | Event IDs |
| --- | ---: | ---: | ---: | ---: | --- |
| High Importance + High Support | 3 | 1 | 8.136 | 2.589 | E011, E023, E025 |
| High Importance + Low Support | 3 | 2 | -1.037 | 2.192 | E006, E017, E024 |
| Threat + High Support | 0 | 0 | n/a | n/a | None |
| Opportunity + High Support | 3 | 1 | 8.136 | 2.589 | E011, E023, E025 |
| Adaptation + High Support | 0 | 0 | n/a | n/a | None |

## Observations

- High support in V3 appears only in opportunity-coded events, not threat or adaptation events.
- High-importance plus high-support cases are concentrated in semiconductor industrial-policy and strategic-investment events.
- High-importance plus low-support cases include strategic investment and export-control events where the state role is present but not primarily direct subsidy.
- There are no observed `Threat + High Support` or `Adaptation + High Support` cases in V3.

## Limitations

- Interaction cells are small, and several have no CAR-observed events.
- Interaction patterns should be treated as dataset structure, not evidence of market effects.
- New V3-only rows need event-window analytics before interaction-level CAR summaries become useful.
