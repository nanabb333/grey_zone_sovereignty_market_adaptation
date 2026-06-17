# Event Study Coverage Audit

> Academic Research Notice:
> This audit compares validated V3 events against existing CAR outputs. It does not calculate new CAR values or create synthetic observations.

## Inputs

- Validated event dataset: `data/events_v3.csv`
- Existing CAR summary: `results/event_abnormal_return_summary.csv`

## Coverage Summary

| Metric | Count |
| --- | ---: |
| Validated V3 events | 25 |
| Events with CAR coverage | 18 |
| Events without CAR coverage | 7 |
| Coverage percentage | 72% |
| Missing percentage | 28% |

Coverage was assessed by matching event title and event date between `data/events_v3.csv` and `results/event_abnormal_return_summary.csv`.

## Events With CAR Coverage

| Event ID | Event date | Event title |
| --- | --- | --- |
| E001 | 2022-07-19 | China Warns Against Pelosi Taiwan Visit |
| E002 | 2022-08-02 | Pelosi Visit |
| E003 | 2022-08-03 | China Trade Restrictions After Pelosi Visit |
| E004 | 2022-08-04 | PLA Military Exercises After Pelosi Visit |
| E005 | 2022-10-07 | BIS Advanced Semiconductor Export Controls |
| E006 | 2022-12-06 | TSMC Arizona US$40B Expansion |
| E007 | 2023-04-08 | Joint Sword 2023 |
| E008 | 2023-08-12 | Lai U.S. Transit |
| E009 | 2023-08-19 | PLA Drills After Lai U.S. Transit |
| E010 | 2023-08-26 | China Sends Aircraft and Vessels After U.S. Arms Sale |
| E011 | 2024-04-08 | TSMC CHIPS Act Preliminary Terms |
| E012 | 2024-05-20 | Lai Ching-te Inauguration |
| E013 | 2024-05-23 | Joint Sword-2024A |
| E014 | 2024-06-21 | PRC Judicial Guidelines on Taiwan Independence |
| E015 | 2024-10-14 | Joint Sword-2024B |
| E016 | 2025-01-22 | PLA Joint Combat Readiness Patrols Around Taiwan |
| E017 | 2025-03-04 | TSMC US$165B U.S. Expansion |
| E018 | 2025-04-01 | Strait Thunder-2025A |

## Events Without CAR Coverage

| Event ID | Event date | Event title | Event family |
| --- | --- | --- | --- |
| E019 | 2019-05-15 | Huawei Added to U.S. Entity List | `Export_Control` |
| E020 | 2020-05-15 | Huawei Foreign-Direct-Product Rule | `Export_Control` |
| E021 | 2020-12-18 | SMIC Added to U.S. Entity List | `Export_Control` |
| E022 | 2020-05-15 | TSMC Announces $12B Arizona Fab | `Strategic_Investment` |
| E023 | 2022-08-09 | CHIPS and Science Act Signed | `Industrial_Policy` |
| E024 | 2023-10-17 | AI Chip Export Control Expansion | `Export_Control` |
| E025 | 2024-05-24 | China Big Fund III Established | `Industrial_Policy` |

## Interpretation

The empirical event-study layer still reflects the original 18-event V2 coverage. The validated V3 dataset has expanded to 25 events, but seven validated events have not yet been processed through the CAR pipeline.

The missing events are analytically important because they are concentrated in export controls, industrial policy, and strategic investment. This means current CAR outputs underrepresent the main domains added by V3.
