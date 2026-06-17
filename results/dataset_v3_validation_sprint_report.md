# Dataset V3 Validation Sprint Report

> Academic Research Notice:
> This sprint created the first expanded validated V3 dataset. It did not generate CAR values, synthetic observations, forecasts, or causal estimates.

## Files Created

- `data/events_v3.csv`
- `data/source_packets/2019-05-15_huawei_entity_list.md`
- `data/source_packets/2020-05-15_huawei_fdp_rule.md`
- `data/source_packets/2020-12-18_smic_entity_list.md`
- `data/source_packets/2020-05-15_tsmc_arizona_announcement.md`
- `data/source_packets/2022-08-09_chips_science_act.md`
- `data/source_packets/2022-08-02_pelosi_taiwan_visit.md`
- `data/source_packets/2022-08-04_china_live_fire_exercises_taiwan.md`
- `data/source_packets/2022-10-07_semiconductor_export_controls.md`
- `data/source_packets/2023-10-17_ai_chip_export_control_expansion.md`
- `data/source_packets/2024-05-24_china_big_fund_iii.md`
- `results/events_v3_validation_report.md`
- `results/v2_vs_v3_comparison.md`
- `results/event_family_v3_summary.md`
- `results/theory_variable_v3_summary.md`
- `results/dataset_v3_validation_sprint_report.md`

## Files Modified

- `README.md`

## Validated Event Count

| Dataset | Count |
| --- | ---: |
| V2 baseline | 18 |
| V3 validated dataset | 25 |
| Net-new validated V3 events | 7 |
| Revalidated existing V2 events with source packets | 3 |

The requested ten source-packet events produced seven net-new rows because Pelosi Taiwan Visit, China live-fire exercises around Taiwan, and October 7 semiconductor export controls were already present in V2.

## Theory Coding Coverage

| Variable | Coverage |
| --- | ---: |
| `interpretation_type` | 25 / 25 |
| `strategic_importance_level` | 13 / 25 |
| `state_support_signal` | 8 / 25 |

## Strongest Additions

- Huawei Entity List action, 2019.
- Huawei foreign-direct-product rule, 2020.
- SMIC Entity List action, 2020.
- CHIPS and Science Act signing, 2022.
- AI-chip export-control expansion, 2023.
- China Big Fund III, 2024.

## Remaining Gaps

- Recognition-diplomacy candidates are not yet integrated.
- Economic-coercion coverage remains thin.
- E020 and E022 share a date and require careful handling in future event-window analysis.
- E024 needs official-rule URL supplementation.
- E025 would be stronger with an official Chinese registration extract.
- Several new V3 rows intentionally leave event-window fields blank until a separate trading-calendar sprint.

## Exact Git Commands

```bash
git status --short
git add README.md data/events_v3.csv data/source_packets/2019-05-15_huawei_entity_list.md data/source_packets/2020-05-15_huawei_fdp_rule.md data/source_packets/2020-12-18_smic_entity_list.md data/source_packets/2020-05-15_tsmc_arizona_announcement.md data/source_packets/2022-08-09_chips_science_act.md data/source_packets/2022-08-02_pelosi_taiwan_visit.md data/source_packets/2022-08-04_china_live_fire_exercises_taiwan.md data/source_packets/2022-10-07_semiconductor_export_controls.md data/source_packets/2023-10-17_ai_chip_export_control_expansion.md data/source_packets/2024-05-24_china_big_fund_iii.md results/events_v3_validation_report.md results/v2_vs_v3_comparison.md results/event_family_v3_summary.md results/theory_variable_v3_summary.md results/dataset_v3_validation_sprint_report.md
git commit -m "Validate dataset v3 event expansion"
```
