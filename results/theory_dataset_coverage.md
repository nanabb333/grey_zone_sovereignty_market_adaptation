# Theory Dataset Coverage

> Academic Research Notice:
> This report summarizes coding coverage in `data/events_v3.csv`. It does not report new event-study calculations.

## Dataset

- Input file: `data/events_v3.csv`
- Validated events: 25

## Coverage Percentages

| Theory variable | Coded events | Missing events | Coverage |
| --- | ---: | ---: | ---: |
| `interpretation_type` | 25 | 0 | 100% |
| `strategic_importance_level` | 13 | 12 | 52% |
| `state_support_signal` | 8 | 17 | 32% |

## Value Distribution

### `interpretation_type`

| Value | Count | Share |
| --- | ---: | ---: |
| `Threat` | 10 | 40% |
| `Opportunity` | 6 | 24% |
| `Adaptation` | 5 | 20% |
| `Mixed` | 4 | 16% |

### `strategic_importance_level`

| Value | Count | Share |
| --- | ---: | ---: |
| `High` | 11 | 44% |
| `Medium` | 2 | 8% |
| `Low` | 0 | 0% |
| Missing | 12 | 48% |

### `state_support_signal`

| Value | Count | Share |
| --- | ---: | ---: |
| `High` | 3 | 12% |
| `Medium` | 2 | 8% |
| `Low` | 3 | 12% |
| Missing | 17 | 68% |

## Missing Theory Values

Missing values are concentrated in variables where conservative coding requires direct evidence:

- `strategic_importance_level` is missing mainly for events where the Taiwan security or coercion channel is present but direct semiconductor or strategic-technology relevance is less explicit.
- `state_support_signal` is missing mainly for military, diplomatic, legal, and coercive events where public subsidy or state-backed investment is not the primary mechanism.

## Strongest Theory Dimensions

- `interpretation_type` is the strongest dimension because all events are coded.
- `strategic_importance_level` is substantially stronger after V3 because new export-control and industrial-policy rows support High coding.

## Weakest Theory Dimensions

- `state_support_signal` remains the weakest dimension by coverage percentage.
- Recognition-diplomacy theory coverage remains absent from validated V3 because those candidate events were not integrated in this sprint.

## Use Limit

Coverage percentages describe coding availability, not explanatory power or causal strength.
