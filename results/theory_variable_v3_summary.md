# Theory Variable V3 Summary

> Academic Research Notice:
> This report summarizes theory-variable coverage in `data/events_v3.csv`. It does not report CAR values, forecasts, or causal claims.

## Dataset

- Input file: `data/events_v3.csv`
- Event count: 25

## `interpretation_type`

Coverage: 25 / 25 events coded.

| Value | Count |
| --- | ---: |
| `Threat` | 10 |
| `Opportunity` | 6 |
| `Adaptation` | 5 |
| `Mixed` | 4 |

## `strategic_importance_level`

Coverage: 13 / 25 events coded.

| Value | Count |
| --- | ---: |
| `High` | 11 |
| `Medium` | 2 |
| Blank | 12 |

## `state_support_signal`

Coverage: 8 / 25 events coded.

| Value | Count |
| --- | ---: |
| `High` | 3 |
| `Medium` | 2 |
| `Low` | 3 |
| Blank | 17 |

## Descriptive Interpretation

V3 improves theory-variable coverage most clearly for strategic importance. New export-control, industrial-policy, and strategic-investment rows create more observations where strategic semiconductor relevance can be coded with confidence.

State-support coverage improves but remains selective. This is appropriate because military, diplomatic, coercive, and legal-signaling events generally should not receive a state-support code unless the evidence directly supports one.

## Uncertain Cases

- E020 and E022 share 2020-05-15, creating confounding risk for later market-window interpretation.
- E024 should receive official-rule URL supplementation before publication.
- E025 should receive official Chinese registration evidence if available.

## Use Limit

Theory coding is interpretive and descriptive. These counts do not establish causal effects.
