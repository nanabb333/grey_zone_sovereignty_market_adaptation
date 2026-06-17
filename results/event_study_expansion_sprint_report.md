# Event Study Expansion Sprint Report

> Academic Research Notice:
> This sprint audited empirical coverage and prepared CAR expansion inputs. It did not calculate CAR values or add new events.

## Coverage

| Metric | Count |
| --- | ---: |
| Validated V3 events | 25 |
| Events with CAR coverage | 18 |
| Events missing CAR coverage | 7 |
| Coverage percentage | 72% |

## Missing Events

- E019: Huawei Added to U.S. Entity List
- E020: Huawei Foreign-Direct-Product Rule
- E021: SMIC Added to U.S. Entity List
- E022: TSMC Announces $12B Arizona Fab
- E023: CHIPS and Science Act Signed
- E024: AI Chip Export Control Expansion
- E025: China Big Fund III Established

## Expansion Difficulty

| Difficulty | Events | Reason |
| --- | --- | --- |
| Lower | E023, E024 | Current local 2022-forward market data appears sufficient; mapping and pipeline execution remain. |
| Medium | E025 | Market data appears sufficient, but event date versus public disclosure date needs review. |
| Higher | E019, E020, E021, E022 | Current local market data starts in 2022, so 2019-2020 events require historical backfill. |

## Highest-Priority Events

1. E024: AI Chip Export Control Expansion.
2. E023: CHIPS and Science Act Signed.
3. E025: China Big Fund III Established.
4. E019-E022 after historical market data is backfilled.

## Files Created

- `results/event_study_coverage_audit.md`
- `docs/car_expansion_plan.md`
- `data/car_expansion_candidates.csv`
- `docs/event_study_pipeline_gap_analysis.md`
- `docs/event_study_expansion_impact.md`
- `results/event_study_expansion_sprint_report.md`

## Files Modified

- `README.md`

## Exact Git Commands

```bash
git status --short
git add README.md results/event_study_coverage_audit.md docs/car_expansion_plan.md data/car_expansion_candidates.csv docs/event_study_pipeline_gap_analysis.md docs/event_study_expansion_impact.md results/event_study_expansion_sprint_report.md
git commit -m "Audit v3 event study coverage expansion"
```
