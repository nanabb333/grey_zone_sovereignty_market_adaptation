# State Support Analysis

> Academic Research Notice:
> This report provides descriptive summaries only. It does not infer causal effects or create synthetic CAR values.

## Scope

- Input dataset: `data/events_v3.csv`
- Validated events: 25
- Events with available CAR summaries: 18

## State Support Counts And CAR Summaries

| State support signal | Event count | Share | CAR n | Avg TSMC CAR 7 | Avg TWSE CAR 7 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `High` | 3 | 12% | 1 | 8.136 | 2.589 |
| `Medium` | 2 | 8% | 1 | 4.450 | -0.757 |
| `Low` | 3 | 12% | 2 | -1.037 | 2.192 |
| Blank | 17 | 68% | 14 | -0.699 | -1.731 |

## Descriptive Notes

- `High` state-support events are concentrated in strategic-investment and industrial-policy cases.
- Blank state-support values are expected for military, diplomatic, coercive, political, and legal-signaling events where direct state support is not the main mechanism.
- V3 improves state-support coverage by adding CHIPS Act and China Big Fund III, while retaining TSMC CHIPS Act preliminary terms from V2.

## Limitations

- Only one `High` state-support event currently has an observed CAR row.
- The state-support layer is intentionally conservative; blank values should not be treated as zero support.
- The available CAR summaries do not yet cover several newly validated V3 state-support events.
