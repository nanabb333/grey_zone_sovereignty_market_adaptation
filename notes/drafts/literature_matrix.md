# Literature Matrix

## Purpose

This matrix organizes prior research relevant to the question:

How does geopolitical risk affect Taiwan financial markets?

Use this file to track theories, datasets, methods, findings, and how each source informs the project.

## Literature Matrix Template

| Source | Topic | Theory / Concept | Data | Method | Key Finding | Relevance to Project |
| --- | --- | --- | --- | --- | --- | --- |
| Author Year | Geopolitical risk and asset prices | Geopolitical risk, uncertainty, safe-haven behavior | Market returns, exchange rates, risk indexes | Event study / regression | Geopolitical shocks can increase volatility and reduce risk appetite. | Supports testing TAIEX, USD/TWD, and TSMC reactions around Taiwan-related events. |
| Author Year | Taiwan Strait tensions | Cross-strait crisis, strategic ambiguity | Taiwan Strait events, diplomatic and military activity | Case study / event coding | Taiwan Strait crises create uncertainty for investors and policymakers. | Supports coding `risk_level` for events such as Pelosi Visit or PLA exercises. |
| Author Year | Semiconductor supply chains | Strategic importance, technology competition | Semiconductor firms, trade data, investment announcements | Industry analysis / policy analysis | Taiwan's semiconductor role shapes global risk perceptions. | Supports coding `strategic_value` for TSMC, Nvidia, AI factory, and supply-chain events. |
| Author Year | Exchange-rate response to political risk | Currency pressure, capital flows | Exchange rates, political risk indicators | Time-series regression | Political uncertainty can affect exchange-rate movements. | Supports using `usd_twd_change` as a dependent variable. |
| Author Year | Event studies in financial markets | Market efficiency, abnormal returns | Stock prices and event dates | Event study | Market prices respond quickly to major news events. | Supports using before/event-day/after windows in `event_impact.py`. |

## Suggested Literature Categories

### Geopolitical Risk and Financial Markets

Focus:
How political, military, or diplomatic shocks affect asset prices, volatility, and investor behavior.

Project connection:
Provides the theoretical basis for linking `risk_level` to TAIEX, USD/TWD, and TSMC changes.

### Taiwan Strait and Strategic Ambiguity

Focus:
Taiwan's contested status, grey-zone pressure, deterrence, and U.S.-China competition.

Project connection:
Supports the conceptual framework connecting grey-zone sovereignty, strategic ambiguity, and geopolitical risk.

### Semiconductor and AI Supply Chains

Focus:
Taiwan's strategic importance in semiconductors, AI infrastructure, and global technology competition.

Project connection:
Supports the `strategic_value` variable and events such as Nvidia AI factory announcements.

### Event Study Methods

Focus:
How to measure market reactions around discrete events.

Project connection:
Supports the analysis design used in `event_analysis.py` and `event_impact.py`.

### Exchange Rates and Political Risk

Focus:
How uncertainty affects currencies, capital flows, and safe-haven behavior.

Project connection:
Supports measuring USD/TWD changes around geopolitical events.

## Source Evaluation Notes

For each source, record:

1. Whether the source is theoretical, empirical, or policy-oriented.
2. Whether the data is global, regional, Taiwan-specific, or firm-specific.
3. Whether the method is suitable for event-level analysis.
4. Whether the source helps justify `risk_level`, `strategic_value`, or market reaction variables.
5. Any limitations, such as small samples, broad indexes, or lack of Taiwan-specific data.

