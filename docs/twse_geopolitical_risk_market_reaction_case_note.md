# TWSE Geopolitical Risk Market Reaction Case Note

## Purpose

This file records research notes and source leads for Taiwan stock-market reactions to geopolitical risk, especially the Pelosi visit and PLA military exercises in August 2022.

These sources are relevant to TAIEX/TWSE market reaction, military risk, diplomatic risk, and Taiwan Strait geopolitical-risk coding.

## Search Terms

- Taiwan stock market reaction Pelosi visit
- Taiwan stock market military exercises
- TWSE geopolitical risk

## Case Summary

| Topic | Project Relevance | Coding Status |
| --- | --- | --- |
| Taiwan stock market reaction to Pelosi visit | Supports the market-reaction dependent variable around diplomatic crisis events. | Needs source verification before coding. |
| Taiwan stock market reaction to PLA military exercises | Links military escalation to market volatility and sector reactions. | Needs source verification before coding. |
| TWSE geopolitical risk framing | Supports broader use of geopolitical risk as an explanatory variable for Taiwan equity-market movement. | Needs source verification before coding. |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| Taipei Times | 2022-08-03 | Taiwan market reaction source | Reports TAIEX decline ahead of the rumored Pelosi visit and notes pressure on transportation-related shares. |
| Reuters / Investing.com | 2022-08 | Military escalation source | Reports China fired missiles and conducted major drills near Taiwan after Pelosi's visit. |
| Axios | 2022-08-04 | Military escalation source | Reports live-ammunition drills and Taiwan MND response after Pelosi's visit. |
| CNBC | 2022-08 | Diplomatic and military response source | Covers China's pressure and military exercises around Pelosi's visit. |
| Taiwan News | 2022-08-03 | Regional market reaction source | Covers Asian markets and notes Taiwan's TAIEX movement around Pelosi-related risk. |
| Global Taiwan Institute | 2022-09 | Analytical source | Provides analysis of Chinese military activity near Taiwan in early August 2022. |
| Taiwan Stock Exchange material | Current / background | Market-institution source | Useful for broader TWSE framing of international geopolitical risk and stock-market volatility. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Event / Topic | market_reaction | military_risk | diplomatic_risk | security_relevance | Reasoning | Manual Review |
| --- | --- | --- | --- | --- | --- | --- |
| Pelosi visit market reaction | Negative / volatile | Medium | High | High | TAIEX reportedly fell ahead of the visit amid U.S.-China tension and uncertainty. | Yes |
| PLA military exercises after Pelosi visit | Negative / volatile | High | High | High | Military drills and missile activity increased Taiwan Strait risk after the visit. | Yes |
| TWSE geopolitical risk | Contextual | Varies | Varies | High | TWSE/Taiwan equity movements can be used as dependent variables in response to geopolitical-risk events. | Yes |

## Recommended Event Rows After Verification

These should not be copied into `data/events_v1.csv` until sources are selected and scores are finalized.

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2022-08-02,Pelosi Visit,diplomatic crisis,,,,,,,,SOURCE_URL
2022-08-04,PLA Military Exercises After Pelosi Visit,military exercise,,,,,,,,SOURCE_URL
```

## Market Data Notes

For event-study analysis, the market dataset should ideally include:

| Field | Use |
| --- | --- |
| `date` | Trading date. |
| `taiex` | Taiwan equity-market benchmark. |
| `twse_return` | Daily return for the TWSE/TAIEX. |
| `tsmc` | Semiconductor-sector bellwether. |
| `usd_twd` | Exchange-rate pressure indicator. |
| `volume` | Optional liquidity / stress indicator. |
| `source` | Market data source. |

## Research Notes

Key distinctions:

1. The Pelosi visit date and the PLA military-exercise date may need to be coded separately.
2. Market reaction should be measured using actual market data, not only news descriptions.
3. News sources can justify event selection, but market data should come from TWSE, Yahoo Finance, Refinitiv, Bloomberg, or another consistent data source.
4. If the project uses TAIEX, make clear whether it means index level, daily return, abnormal return, or volatility.
5. If a date falls on a non-trading day, use the next available trading day and flag the adjustment.

Before coding:

1. Verify exact TAIEX levels and returns around 2022-08-01 to 2022-08-05.
2. Separate event-source citations from market-data citations.
3. Attach reasoning for `military_risk`, `diplomatic_risk`, and `security_relevance`.
4. Flag uncertainty for manual review if market reaction is mixed or quickly reverses.

