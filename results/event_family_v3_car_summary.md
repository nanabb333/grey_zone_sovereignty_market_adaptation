# Event Family V3 CAR Summary

> Academic Research Notice:
> This report summarizes descriptive CAR coverage by event family using `data/events_v3.csv` and `results/event_abnormal_return_summary_v3.csv`. It does not make causal claims or forecast market reactions.

## Coverage

| Metric | Count |
| --- | ---: |
| Validated V3 events | 25 |
| CAR-covered events after V3 integration | 21 |
| Remaining events without CAR coverage | 4 |
| CAR coverage | 84% |

## Event-Family Summary

| Event family | Validated events | CAR n | Avg TSMC CAR 7 | Avg TWSE CAR 7 |
| --- | ---: | ---: | ---: | ---: |
| `Diplomatic_Shock` | 3 | 3 | -2.742 | -2.812 |
| `Economic_Coercion` | 1 | 1 | 1.709 | -1.954 |
| `Export_Control` | 5 | 2 | 5.602 | 1.547 |
| `Industrial_Policy` | 2 | 2 | -0.834 | -1.361 |
| `Legal_Judicial_Signaling` | 1 | 1 | -1.008 | -3.993 |
| `Military_Exercise` | 8 | 8 | -0.286 | -1.197 |
| `Political_Signaling` | 1 | 1 | 0.031 | -0.275 |
| `Strategic_Investment` | 4 | 3 | 2.021 | 2.324 |

## Observations

- Industrial policy now has CAR coverage for both validated V3 industrial-policy events.
- Export-control coverage improved from one CAR-covered event to two, but three earlier 2019-2020 export-control events remain unavailable because local market data starts in 2022.
- Military-exercise coverage was already complete and remains the largest fully covered family.

## Limitations

- CAR n is still small for export controls and industrial policy.
- The 2019-2020 export-control sequence remains missing from the CAR-covered sample.
- E025 uses the validated registration date; public-disclosure timing remains an interpretation caveat.
