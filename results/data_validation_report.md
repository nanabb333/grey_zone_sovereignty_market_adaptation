# Data Validation Report

- Status: `warning`
- Events: 18
- News items: 12
- Event families: 7
- Errors: 0
- Warnings: 1

Validation checks structural data quality and linkage integrity. It does not add analytical claims or change the event-study methodology.

## Checks

- duplicate event_id
- missing event_id
- orphan news records
- invalid event family values
- missing critical fields
- duplicate news_id

## Errors

- None

## Warnings

- `orphan_news_records`: These news items do not link to an event_id in data/events_v2.csv and require analyst review before use in event-linked analysis.
  - N007: UNLINKED_NAURU_2024 - Nauru switches diplomatic recognition from Taiwan to China
