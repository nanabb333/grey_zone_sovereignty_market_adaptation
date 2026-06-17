# Event Study Pipeline Gap Analysis

> Academic Research Notice:
> This document identifies gaps between validated event coverage and CAR coverage. It does not compute CAR values.

## Current State

The current event-study output file, `results/event_abnormal_return_summary.csv`, covers 18 events. These correspond to the original V2 empirical coverage.

## Target State

The validated V3 dataset, `data/events_v3.csv`, contains 25 events. The target state is 25 validated events with CAR outputs, subject to data availability and event-window validation.

## Coverage Gap

| Item | Count |
| --- | ---: |
| Current CAR-covered events | 18 |
| Target validated V3 events | 25 |
| Missing CAR events | 7 |

## Missing Inputs

The seven missing events need:

- event trading date confirmation
- event-window start and end dates
- estimation-window definition
- benchmark mapping
- event-window output file path
- updated CAR summary row

## Missing Market Data

The current local processed market data starts in 2022. This creates two readiness groups:

- 2019-2020 events: require historical market-data backfill before CAR calculation.
- 2022-2024 events: likely processable with current local market data after mapping and validation.

## Missing Mappings

The V3 dataset contains event metadata, but the missing events need explicit empirical mappings:

- event ID to event-study run configuration
- event date to first valid trading date
- ticker to market index
- event family to output grouping
- event title to CAR summary row

## Validation Requirements

Before the CAR summary is expanded, the pipeline should verify:

- no duplicate event IDs
- no duplicate event-date/event-title pairs
- market data covers the full estimation window
- market data covers the event window
- event trading date is valid
- benchmark index is available
- output row includes only observed calculations
- no CAR values are fabricated for missing data

## Key Technical Gap

The validated event dataset has moved ahead of the empirical event-study outputs. The next technical step is not more event discovery; it is extending the event-study runner so V3 event rows can be processed consistently and safely.
