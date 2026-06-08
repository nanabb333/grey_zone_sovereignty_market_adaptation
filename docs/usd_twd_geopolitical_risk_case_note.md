# USD/TWD Geopolitical Risk Case Note

## Purpose

This file records research notes and source leads for USD/TWD reactions to Taiwan Strait geopolitical risk.

These sources are relevant to exchange-rate reaction, Taiwan dollar risk, safe-haven flows, and Taiwan Strait crisis coding.

## Search Terms

- USD TWD reaction Taiwan Strait crisis
- Taiwan dollar geopolitical risk

## Case Summary

| Topic | Project Relevance | Coding Status |
| --- | --- | --- |
| USD/TWD reaction to Taiwan Strait crisis | Supports using exchange-rate movement as a dependent variable. | Needs market-data verification before coding. |
| Taiwan dollar geopolitical risk | Links cross-strait risk to currency pressure and safe-haven dynamics. | Needs market-data verification before coding. |
| Pelosi visit and PLA drills | Provides a geopolitical shock window for testing USD/TWD reaction. | Event sources available; currency data still needed. |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| Reuters / Investing.com | 2022-08 | Geopolitical shock source | Reports China fired missiles and conducted major drills near Taiwan after Pelosi's visit. |
| Axios | 2022-08-04 | Geopolitical shock source | Reports live-ammunition drills, missile launches, and Taiwan MND response. |
| Reuters / Investing.com | 2022-08 | Continued escalation source | Reports China announced additional drills around Taiwan after Pelosi's visit. |
| Reuters / Business Recorder | 2022-08-03 | Regional FX tension source | Reports yuan weakness as Pelosi visit heightened Taiwan Strait tensions. |
| UBS | 2025 | Taiwan dollar market structure source | Discusses USD/TWD dynamics, carry trades, hedging, and central bank behavior. Useful background, not a Pelosi-specific source. |
| TWSE / market data provider | To collect | Market data source | Needed for actual USD/TWD levels, returns, and volatility around event dates. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Event / Topic | expected_usd_twd_reaction | military_risk | diplomatic_risk | security_relevance | Reasoning | Manual Review |
| --- | --- | --- | --- | --- | --- | --- |
| Pelosi visit | Possible USD/TWD increase | Medium | High | High | Diplomatic crisis increased uncertainty, but actual FX response must be verified with data. | Yes |
| PLA military exercises after Pelosi visit | Possible USD/TWD increase | High | High | High | Missile launches and drills may create Taiwan dollar depreciation pressure or higher FX volatility. | Yes |
| Taiwan Strait crisis | Higher USD/TWD volatility | High | High | High | Strait risk may trigger risk-off behavior, safe-haven U.S. dollar demand, or central bank smoothing. | Yes |

## Recommended Market Data Fields

For USD/TWD event-study analysis, collect:

| Field | Use |
| --- | --- |
| `date` | Trading date. |
| `usd_twd` | Spot exchange rate level. |
| `usd_twd_return` | Daily percentage change. |
| `usd_twd_volatility` | Rolling or implied volatility if available. |
| `central_bank_intervention_note` | Optional qualitative note if CBC activity is reported. |
| `source` | Market data provider or official source. |

## Recommended Event Rows After Verification

These should not be copied into `data/events_v1.csv` until sources are selected and scores are finalized.

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2022-08-02,Pelosi Visit,diplomatic crisis,,,,,,,,SOURCE_URL
2022-08-04,PLA Military Exercises After Pelosi Visit,military exercise,,,,,,,,SOURCE_URL
```

## Research Notes

Key distinctions:

1. Geopolitical-event sources can justify the event window, but they do not provide the actual USD/TWD reaction.
2. USD/TWD reaction should be measured from exchange-rate data, not inferred from news tone.
3. A higher USD/TWD usually means Taiwan dollar depreciation against the U.S. dollar.
4. A lower USD/TWD usually means Taiwan dollar appreciation against the U.S. dollar.
5. Taiwan's central bank may smooth currency movements, so small spot moves may still coexist with higher implied volatility or hedging demand.

Before coding:

1. Collect USD/TWD levels around 2022-08-01 to 2022-08-05.
2. Calculate daily percentage changes and before/event-day/after changes.
3. Separate FX market-data sources from geopolitical event sources.
4. Flag uncertainty for manual review if USD/TWD moves are driven by broad U.S. dollar trends rather than Taiwan-specific risk.

