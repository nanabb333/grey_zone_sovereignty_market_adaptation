# Strategic Importance Analysis

> Academic Research Notice:
> This report provides descriptive summaries only. It does not infer causal effects or create synthetic CAR values.

## Scope

- Input dataset: `data/events_v3.csv`
- Validated events: 25
- Events with available CAR summaries: 18

## Strategic Importance Counts And CAR Summaries

| Strategic importance level | Event count | Share | CAR n | Avg TSMC CAR 7 | Avg TWSE CAR 7 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `High` | 11 | 44% | 4 | 2.628 | 1.554 |
| `Medium` | 2 | 8% | 2 | 2.617 | -0.607 |
| `Low` | 0 | 0% | 0 | n/a | n/a |
| Blank | 12 | 48% | 12 | -1.251 | -1.918 |

## Descriptive Notes

- V3 makes `High` strategic importance a major theory dimension rather than a sparse annotation.
- `High` strategic-importance events are mostly export controls, semiconductor investment, and industrial-policy events.
- `Medium` strategic-importance cases in V3 are tied to Taiwan security shocks where the market channel is important but less directly semiconductor-policy focused.
- No validated V3 event is currently coded `Low`, reflecting conservative coding rather than evidence that low-importance events do not exist.

## Limitations

- More than half of the `High` strategic-importance rows are V3-only and do not yet have CAR summaries.
- Blank values should be interpreted as insufficient direct evidence for conservative coding, not as low strategic importance.
- The apparent positive CAR averages for coded strategic-importance cases are descriptive only and based on a small CAR-observed subset.
