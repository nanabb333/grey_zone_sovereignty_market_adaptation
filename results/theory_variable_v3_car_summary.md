# Theory Variable V3 CAR Summary

> Academic Research Notice:
> This report recomputes descriptive theory-variable summaries using the expanded V3 CAR-covered sample. It does not create synthetic values or make causal claims.

## Coverage

| Metric | Count |
| --- | ---: |
| Validated V3 events | 25 |
| CAR-covered events | 21 |
| Coverage | 84% |

## Interpretation Type

| Interpretation type | Validated events | CAR n | Avg TSMC CAR 7 | Avg TWSE CAR 7 |
| --- | ---: | ---: | ---: | ---: |
| `Adaptation` | 5 | 5 | -0.480 | -1.123 |
| `Mixed` | 4 | 2 | 5.602 | 1.547 |
| `Opportunity` | 6 | 5 | 0.879 | 0.850 |
| `Threat` | 10 | 9 | -0.820 | -2.069 |

## State Support Signal

| State support signal | Validated events | CAR n | Avg TSMC CAR 7 | Avg TWSE CAR 7 |
| --- | ---: | ---: | ---: | ---: |
| Blank | 17 | 14 | -0.699 | -1.731 |
| `High` | 3 | 3 | 2.156 | -0.044 |
| `Low` | 3 | 3 | 1.560 | 2.745 |
| `Medium` | 2 | 1 | 4.450 | -0.757 |

## Strategic Importance Level

| Strategic importance level | Validated events | CAR n | Avg TSMC CAR 7 | Avg TWSE CAR 7 |
| --- | ---: | ---: | ---: | ---: |
| Blank | 12 | 12 | -1.251 | -1.918 |
| `High` | 11 | 7 | 2.228 | 1.049 |
| `Medium` | 2 | 2 | 2.617 | -0.607 |
| `Low` | 0 | 0 | n/a | n/a |

## What Changed

- `High` state-support CAR coverage increased from one event to three events.
- `Opportunity` coverage increased because E023 and E025 now have CAR rows.
- `Mixed` coverage increased because E024 now has a CAR row.
- `High` strategic-importance coverage increased from four CAR rows to seven.

## Limitations

- The four remaining missing events are all strategically important 2019-2020 V3 events.
- The current legacy workflow computes benchmark-adjusted abnormal returns and forward CAR windows; it does not estimate a market model with a separate pre-event estimation window.
- Small cell counts mean all summaries are descriptive and fragile.
