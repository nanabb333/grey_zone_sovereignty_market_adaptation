# Taiwan CDS Geopolitical Risk Case Note

## Purpose

This file records research notes and source leads for Taiwan sovereign CDS spreads and geopolitical risk, especially around the Pelosi visit and August 2022 Taiwan Strait military exercises.

These sources are relevant to sovereign-risk indicators, geopolitical risk premia, Taiwan Strait escalation, and financial-market stress measurement.

## Search Terms

- Taiwan CDS spread Pelosi visit
- Taiwan sovereign CDS geopolitical risk

## Case Summary

| Topic | Project Relevance | Coding Status |
| --- | --- | --- |
| Taiwan CDS spread around Pelosi visit | Potential sovereign-risk indicator for Taiwan Strait crisis risk. | Needs market-data verification before coding. |
| Taiwan sovereign CDS geopolitical risk | Supports use of CDS spreads as a risk-premium measure. | Needs reliable CDS data source. |
| Pelosi visit and PLA drills | Provides the geopolitical shock window for testing CDS response. | Event sources available; CDS data still needed. |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| Reuters / Investing.com | 2022-08 | Geopolitical shock source | Reports missile launches and major PLA drills near Taiwan after Pelosi's visit. |
| Axios | 2022-08-04 | Geopolitical shock source | Reports live-ammunition drills, missile launches, and Taiwan MND response. |
| CNBC | 2022-08 | Geopolitical shock source | Covers Chinese live-fire drills and military response after Pelosi's visit. |
| S&P Global Market Intelligence | 2022 / current | Potential CDS or credit-risk source | Project source inventory lists S&P Global as a possible CDS / sovereign-risk indicator source. Needs direct dataset or article verification. |
| S&P Global Global Trade Monitor | 2022-09 | Geopolitical and trade-risk context | Discusses Taiwan Strait tensions after Pelosi's visit and possible trade disruption impacts. |
| Academic literature on geopolitical tensions and sovereign CDS | Current background | Methodological source | Supports concept that geopolitical risk can widen sovereign CDS spreads, but does not replace Taiwan-specific data. |
| Bloomberg / Refinitiv / Datastream / S&P Capital IQ | To collect | Market data source | Needed for Taiwan 5-year sovereign CDS levels and changes around event dates. |

## Evidence Limitation

Direct public evidence for a specific Taiwan sovereign CDS spread move around the Pelosi visit was not clearly available from the web search.

Do not code a Taiwan CDS market reaction from news coverage alone. The project needs actual CDS time-series data before making claims about spread widening or tightening.

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Event / Topic | expected_cds_reaction | military_risk | diplomatic_risk | security_relevance | Reasoning | Manual Review |
| --- | --- | --- | --- | --- | --- | --- |
| Pelosi visit | Possible CDS widening | Medium | High | High | Diplomatic crisis raised uncertainty, but actual CDS response must be verified with spread data. | Yes |
| PLA military exercises after Pelosi visit | Possible CDS widening | High | High | High | Missile launches and drills could increase perceived sovereign risk. | Yes |
| Taiwan Strait crisis | Higher CDS spread or CDS volatility | High | High | High | Strait escalation may raise default-risk premia, insurance costs, and risk-off behavior. | Yes |

## Recommended Market Data Fields

For CDS event-study analysis, collect:

| Field | Use |
| --- | --- |
| `date` | Trading date. |
| `taiwan_5y_cds` | Taiwan five-year sovereign CDS spread in basis points. |
| `taiwan_5y_cds_change` | Daily change in basis points. |
| `taiwan_5y_cds_pct_change` | Daily percentage change. |
| `regional_cds_benchmark` | Optional benchmark such as South Korea, Japan, or emerging Asia CDS index. |
| `source` | Data vendor or publication source. |

## Recommended Event Rows After Verification

These should not be copied into `data/events_v1.csv` until sources are selected and scores are finalized.

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2022-08-02,Pelosi Visit,diplomatic crisis,,,,,,,,SOURCE_URL
2022-08-04,PLA Military Exercises After Pelosi Visit,military exercise,,,,,,,,SOURCE_URL
```

## Research Notes

Key distinctions:

1. CDS spreads measure sovereign credit-risk premia, not equity-market reaction.
2. CDS reaction should be measured from actual CDS data, not inferred from military or diplomatic news.
3. A wider CDS spread usually indicates higher perceived credit or sovereign-risk premium.
4. A narrower CDS spread usually indicates lower perceived credit or sovereign-risk premium.
5. Taiwan CDS may be thinly traded, so compare results with liquidity and regional benchmark indicators if available.

Before coding:

1. Collect Taiwan 5-year sovereign CDS spreads around 2022-08-01 to 2022-08-05.
2. Calculate daily basis-point changes and event-window changes.
3. Separate event-source citations from CDS data citations.
4. Flag uncertainty for manual review if CDS data is sparse, stale, vendor-dependent, or unavailable.

