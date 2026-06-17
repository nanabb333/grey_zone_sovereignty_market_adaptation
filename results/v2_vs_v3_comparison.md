# V2 Versus V3 Dataset Comparison

> Academic Research Notice:
> This comparison reports descriptive dataset coverage only. It does not report CAR values, forecasts, or causal claims.

## Event Count

| Dataset | Event count | Notes |
| --- | ---: | --- |
| V2, `data/events_v2.csv` | 18 | Existing validated baseline. |
| V3, `data/events_v3.csv` | 25 | V2 plus seven net-new validated events and three revalidated V2 source packets. |

## Family Coverage

| Event family | V2 count | V3 count | Change |
| --- | ---: | ---: | ---: |
| `Military_Exercise` | 8 | 8 | 0 |
| `Diplomatic_Shock` | 3 | 3 | 0 |
| `Strategic_Investment` | 3 | 4 | +1 |
| `Economic_Coercion` | 1 | 1 | 0 |
| `Export_Control` | 1 | 5 | +4 |
| `Political_Signaling` | 1 | 1 | 0 |
| `Legal_Judicial_Signaling` | 1 | 1 | 0 |
| `Industrial_Policy` | 0 | 2 | +2 |
| Total | 18 | 25 | +7 |

## Theory-Variable Coverage

| Variable | V2 coverage | V3 coverage | Change |
| --- | ---: | ---: | ---: |
| `interpretation_type` | 18 / 18 | 25 / 25 | Full coverage retained. |
| `strategic_importance_level` | 4 / 18 | 13 / 25 | Strong expansion through export-control and industrial-policy events. |
| `state_support_signal` | 4 / 18 | 8 / 25 | Expanded through CHIPS Act, TSMC Arizona, AI-chip controls, and Big Fund III. |

## Diplomatic Competition Coverage

Diplomatic-shock coverage remains unchanged at three rows. The V3 validation sprint did not yet integrate recognition-diplomacy candidates such as Honduras or Nauru. This remains a gap for future expansion.

## Export-Control Coverage

Export-control coverage improves from one event to five events:

- E005: BIS Advanced Semiconductor Export Controls
- E019: Huawei Added to U.S. Entity List
- E020: Huawei Foreign-Direct-Product Rule
- E021: SMIC Added to U.S. Entity List
- E024: AI Chip Export Control Expansion

This is the strongest V3 upgrade.

## Industrial-Policy Coverage

Industrial-policy coverage improves from zero events to two events:

- E023: CHIPS and Science Act Signed
- E025: China Big Fund III Established

This creates a clearer state-support comparison layer.

## Strategic-Investment Coverage

Strategic-investment coverage improves from three events to four events through:

- E022: TSMC Announces $12B Arizona Fab

This event is analytically important but has a same-day confounding warning because E020 occurred on the same date.

## Bottom Line

V3 substantially improves export-control and industrial-policy coverage while preserving the existing military-heavy Taiwan security baseline. The main remaining gaps are recognition diplomacy, economic coercion, and legal or judicial signaling.
