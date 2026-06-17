# V3 CAR Integration Findings

> Academic Research Notice:
> This memo documents actual CAR coverage expansion for validated V3 events. It does not add events, create synthetic market data, estimate missing values, or make causal claims.

## Events Integrated

Three validated V3 events gained CAR coverage:

| Event ID | Event date used | Event title | Ticker mapping | Market index mapping | Integration note |
| --- | --- | --- | --- | --- | --- |
| E023 | 2022-08-09 | CHIPS and Science Act Signed | TSMC via `tsmc_close`; TWSE via `twse_close` | TSMC benchmarked to SOX; TWSE benchmarked to NASDAQ | Existing local market data supports event date and forward CAR windows. |
| E024 | 2023-10-17 | AI Chip Export Control Expansion | TSMC via `tsmc_close`; TWSE via `twse_close` | TSMC benchmarked to SOX; TWSE benchmarked to NASDAQ | Existing local market data supports event date and forward CAR windows. |
| E025 | 2024-05-24 | China Big Fund III Established | TSMC via `tsmc_close`; TWSE via `twse_close` | TSMC benchmarked to SOX; TWSE benchmarked to NASDAQ | Integrated using the validated registration date. Public-disclosure timing around 2024-05-27 remains a sensitivity issue. |

## Methodology Used

The sprint reused the existing benchmark-adjusted abnormal-return workflow:

- TWSE abnormal return = TWSE daily return minus NASDAQ daily return.
- TSMC abnormal return = TSMC daily return minus SOX daily return.
- CAR windows are forward trading-row windows for 1, 3, and 7.
- No synthetic market data was created.
- No missing CAR values were estimated.

The current legacy workflow does not use a separate pre-event market-model estimation window. Estimation-window availability was therefore interpreted as market-data sufficiency for the existing benchmark-adjusted workflow rather than as a new model requirement.

## CAR Coverage Change

| Coverage metric | Before | After |
| --- | ---: | ---: |
| Validated V3 events | 25 | 25 |
| CAR-covered events | 18 | 21 |
| CAR coverage | 72% | 84% |
| Missing CAR events | 7 | 4 |

## What Became Analyzable

- High state-support events now have full CAR coverage in the validated V3 dataset.
- Industrial-policy events now have full CAR coverage.
- Opportunity-coded events are better represented in the CAR-covered sample.
- Mixed export-control coverage improved through E024.
- High strategic-importance coverage improved from four to seven CAR-covered events.

## Still Unavailable

Four validated V3 events remain without CAR coverage:

- E019: Huawei Added to U.S. Entity List
- E020: Huawei Foreign-Direct-Product Rule
- E021: SMIC Added to U.S. Entity List
- E022: TSMC Announces $12B Arizona Fab

These events are blocked by local market-data coverage because current processed market data starts in 2022. E020 and E022 also share the same event date, creating a confounding issue even after historical data backfill.

## Remaining Caveats

- E025 should retain a date-sensitivity note because public reporting appears later than the validated registration date.
- The new CAR rows should be interpreted as descriptive event-study outputs, not causal evidence.
- The original output file remains preserved; expanded outputs are written to V3-specific files.
