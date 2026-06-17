# CAR Expansion Plan

> Academic Research Notice:
> This plan identifies requirements for extending CAR coverage to validated V3 events. It does not calculate CAR values.

## Current State

- Validated V3 events: 25
- Existing CAR-covered events: 18
- Validated events still needing CAR coverage: 7

The current local market data in `data/processed/market.csv` starts in 2022. This supports the 2022-2024 missing events but does not support the 2019-2020 missing events without historical backfill.

## Missing Event Readiness

| Event ID | Event date | Event title | Ticker availability | Market data requirements | Expected estimation window requirements | Potential data issues |
| --- | --- | --- | --- | --- | --- | --- |
| E019 | 2019-05-15 | Huawei Added to U.S. Entity List | TSMC 2330.TW and TWSE are conceptually available, but not in current local 2022-forward files. | Backfill TSMC and TWSE daily prices to cover 2018-2019; optional NVDA, SOX, and NASDAQ for technology exposure. | Need enough pre-event trading days for the chosen estimation window plus event window. | Current processed market data does not cover 2019; announcement date and Federal Register effective date differ. |
| E020 | 2020-05-15 | Huawei Foreign-Direct-Product Rule | TSMC 2330.TW and TWSE are conceptually available, but not in current local 2022-forward files. | Backfill TSMC and TWSE daily prices to cover 2019-2020; optional NVDA, SOX, and NASDAQ. | Need pre-event estimation window ending before 2020-05-15. | Same event date as E022 creates confounding risk; COVID-period market volatility may complicate interpretation. |
| E021 | 2020-12-18 | SMIC Added to U.S. Entity List | TSMC 2330.TW and TWSE are conceptually available, but not in current local 2022-forward files. | Backfill TSMC and TWSE daily prices to cover 2020; optional SOX and NASDAQ. | Need pre-event estimation window before 2020-12-18. | Current processed market data does not cover 2020; U.S.-China technology-policy sequence may create overlapping expectations. |
| E022 | 2020-05-15 | TSMC Announces $12B Arizona Fab | TSMC 2330.TW and TWSE are conceptually available, but not in current local 2022-forward files. | Backfill TSMC and TWSE daily prices to cover 2019-2020; optional U.S. technology indexes. | Need pre-event estimation window ending before 2020-05-15. | Same event date as E020 creates attribution risk; strategic-investment and export-control shocks overlap. |
| E023 | 2022-08-09 | CHIPS and Science Act Signed | TSMC 2330.TW and TWSE are present in current local files. | Existing local 2022-forward market data appears sufficient for TSMC/TWSE; optional NVDA/SOX/NASDAQ are also present. | Need confirm sufficient pre-event observations before 2022-08-09. | Event was anticipated through legislative process, so surprise coding and event timing should be handled conservatively. |
| E024 | 2023-10-17 | AI Chip Export Control Expansion | TSMC 2330.TW, TWSE, NVDA, SOX, and NASDAQ are present in current local files. | Existing local 2022-forward market data appears sufficient. | Need estimation window ending before 2023-10-17 and normal event-window construction. | Strong U.S. AI-chip exposure suggests optional NVDA/SOX analysis may be more informative than TSMC-only analysis. |
| E025 | 2024-05-24 | China Big Fund III Established | TSMC 2330.TW and TWSE are present in current local files. | Existing local 2022-forward market data appears sufficient for Taiwan market coverage; optional SOX/NASDAQ available. | Need estimation window ending before 2024-05-24. | Public reporting occurred around 2024-05-27 after the reported registration date; event-date versus disclosure-date handling must be documented. |

## Priority Order

1. E024: high analytical value and current market data likely sufficient.
2. E023: high state-support relevance and current market data likely sufficient.
3. E025: high industrial-policy relevance, but event-date/disclosure-date review is needed.
4. E019-E022: high analytical value, but require historical market-data backfill and stronger confounding review.

## Validation Requirements

Before CAR expansion, each event needs:

- confirmed event trading date
- event window start and end
- estimation window definition
- benchmark choice
- ticker/index availability check
- duplicate and confounding review
- generated event-window file
- updated CAR summary row
