# Event Study V3 Completion Sprint Report

> Academic Research Notice:
> This sprint increased actual CAR coverage for validated V3 events using existing market data. It did not add events, create synthetic market data, estimate unavailable values, or add dashboard features.

## Coverage Change

| Metric | Before | After |
| --- | ---: | ---: |
| Validated V3 events | 25 | 25 |
| CAR-covered events | 18 | 21 |
| Missing CAR events | 7 | 4 |
| CAR coverage | 72% | 84% |

## Events Integrated

- E023: CHIPS and Science Act Signed
- E024: AI Chip Export Control Expansion
- E025: China Big Fund III Established

## Outputs Created

- `scripts/calculate_abnormal_returns_v3.py`
- `results/event_abnormal_return_summary_v3.csv`
- `results/event_abnormal_return_summary_v3_new_events.csv`
- `results/event_family_v3_car_summary.md`
- `results/theory_variable_v3_car_summary.md`
- `docs/v3_car_integration_findings.md`
- `results/event_study_v3_completion_report.md`

## Outputs Modified

- `data/car_expansion_candidates.csv`

## Events Still Missing

- E019: Huawei Added to U.S. Entity List
- E020: Huawei Foreign-Direct-Product Rule
- E021: SMIC Added to U.S. Entity List
- E022: TSMC Announces $12B Arizona Fab

## Remaining Blockers

- Current local processed market data starts in 2022, so 2019-2020 events require historical market-data backfill.
- E020 and E022 share 2020-05-15, creating confounding risk.
- E025 was integrated using the validated registration date, but public-disclosure timing remains a sensitivity issue.
- The current legacy CAR workflow is benchmark-adjusted and does not use a separate market-model estimation window.

## Exact Git Commands

```bash
git status --short
git add scripts/calculate_abnormal_returns_v3.py results/event_abnormal_return_summary_v3.csv results/event_abnormal_return_summary_v3_new_events.csv results/event_family_v3_car_summary.md results/theory_variable_v3_car_summary.md docs/v3_car_integration_findings.md results/event_study_v3_completion_report.md data/car_expansion_candidates.csv
git commit -m "Expand v3 event study CAR coverage"
```
