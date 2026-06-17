# Events V3 Validation Report

> Academic Research Notice:
> This validation report checks dataset structure, source-packet coverage, duplicate handling, and theory-variable values. It does not report CAR values, forecasts, or causal estimates.

## Input

- Dataset: `data/events_v3.csv`
- Source packets: `data/source_packets/`
- Baseline preserved: `data/events_v2.csv`

## Dataset Size

| Status | Count |
| --- | ---: |
| `V2_validated` | 15 |
| `V2_revalidated` | 3 |
| `V3_validated` | 7 |
| Total validated V3 rows | 25 |

Three required events were already present in V2 and were revalidated through source packets rather than duplicated:

- E002: Pelosi Visit
- E004: PLA Military Exercises After Pelosi Visit
- E005: BIS Advanced Semiconductor Export Controls

## Validation Checks

| Check | Result | Notes |
| --- | --- | --- |
| Event IDs present | Pass | All rows have `event_id`. |
| Event ID format | Pass | All IDs follow `E###`. |
| Duplicate event IDs | Pass | No duplicate IDs detected. |
| Required theory fields present | Pass | `interpretation_type`, `strategic_importance_level`, and `state_support_signal` are present. |
| Theory value domain | Pass | Populated values use allowed labels only. |
| Event-family values | Pass | All rows use controlled family labels. |
| Duplicate event detection | Pass | No exact duplicate event-name and event-date pairs detected. |
| Source-packet links | Pass | All rows with `source_packet` point to existing packet files. |

## Allowed Values Checked

### `interpretation_type`

Allowed:

- `Threat`
- `Opportunity`
- `Adaptation`
- `Mixed`
- blank

### `strategic_importance_level`

Allowed:

- `High`
- `Medium`
- `Low`
- blank

### `state_support_signal`

Allowed:

- `High`
- `Medium`
- `Low`
- blank

## Family Categories Present

| Event family | Count |
| --- | ---: |
| `Military_Exercise` | 8 |
| `Export_Control` | 5 |
| `Strategic_Investment` | 4 |
| `Diplomatic_Shock` | 3 |
| `Industrial_Policy` | 2 |
| `Economic_Coercion` | 1 |
| `Political_Signaling` | 1 |
| `Legal_Judicial_Signaling` | 1 |

## Duplicate And Confounding Notes

- No exact duplicate rows were added for Pelosi, the August 2022 PLA exercises, or the October 7 export controls.
- E020 and E022 share the date 2020-05-15. This is not a duplicate because the events are substantively different, but it is a confounding warning for any future event-window analysis.
- Several new V3 rows have blank event-window fields. This is intentional until trading-calendar and event-window construction is performed in a separate analytics sprint.

## Source Quality Warnings

- E024, AI Chip Export Control Expansion, has strong contemporaneous reporting but should be supplemented with the exact official BIS or Federal Register rule URL before formal publication.
- E025, China Big Fund III, has reputable reporting and a clear reported registration date, but an official Chinese registration extract should be retained if available.
- E022, TSMC Arizona Announcement, has high-quality company evidence but same-day confounding with E020.

## Validation Conclusion

`data/events_v3.csv` passes structural validation for a 25-event validated research dataset. It preserves V2, adds seven net-new validated V3 events, and revalidates three existing V2 events with source packets.
