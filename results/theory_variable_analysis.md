# Theory Variable Analysis

> Academic Research Notice:
> This report uses only validated V3 data from `data/events_v3.csv`. CAR summaries are descriptive and are reported only where observed CAR rows exist in `results/event_abnormal_return_summary.csv`.

## Scope

- Validated V3 events: 25
- Events with available CAR summaries: 18
- V3-only events without CAR summaries: 7

The seven V3-only events are included in event counts but excluded from CAR averages because no synthetic CAR values were created.

## Interpretation Type Counts And CAR Summaries

| Interpretation type | Event count | Share | CAR n | Avg TSMC CAR 7 | Avg TWSE CAR 7 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `Threat` | 10 | 40% | 9 | -0.820 | -2.069 |
| `Opportunity` | 6 | 24% | 3 | 2.021 | 2.324 |
| `Adaptation` | 5 | 20% | 5 | -0.480 | -1.123 |
| `Mixed` | 4 | 16% | 1 | 4.450 | -0.757 |

## Observations

- `Threat` remains the largest interpretation category. It is mostly composed of diplomatic, military, economic-coercion, political-signaling, and legal-signaling events.
- `Opportunity` becomes stronger after V3 because new industrial-policy and strategic-investment events add more non-threat cases.
- `Mixed` is more visible after V3 because export controls can raise revenue and compliance risk while also increasing the strategic value of non-China chokepoints.
- `Adaptation` remains tied to repeated military-signaling events in the current validated data.

## Limitations

- CAR coverage is incomplete for V3-only events, so CAR averages still mostly reflect the V2 analytics layer.
- The `Mixed` category has only one observed CAR row, making its average especially fragile.
- Interpretation coding is descriptive and does not establish causality.
- Event windows for newly validated V3 rows still require a separate analytics sprint.
