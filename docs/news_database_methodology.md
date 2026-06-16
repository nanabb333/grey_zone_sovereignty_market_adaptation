# News Evidence Database Methodology

## Purpose

The news evidence database adds a structured evidence layer to the Taiwan geopolitical risk dashboard project. The original repository focuses on event-study outputs, deterministic summaries, and analyst-facing dashboard presentation. This layer does not change those research claims, event windows, abnormal-return calculations, or interpretation rules.

Instead, `data/news/news_events.csv` provides a starter table for curated source evidence that can be linked to existing geopolitical event coding. The goal is to make future analyst review, source tracing, and dashboard drilldowns easier without treating news items as market forecasts or automated causal evidence.

## Selection Logic

News items are selected when they plausibly document one of the project's existing geopolitical themes:

- Taiwan grey-zone or military activity
- diplomatic shocks and cross-strait political signaling
- semiconductor supply-chain and strategic-importance risk
- policy responses by governments or firms
- related regional or international tensions

The starter rows are placeholder-safe examples. They use cautious summaries and source home pages or institution pages where exact article URLs have not yet been verified. Before formal use, each row should be reviewed by an analyst, matched to an exact article or official document, and checked for timestamp, headline, author or institution, and archival stability.

## Connection To Existing Event Coding

The `related_event_id` field links each news item to an existing dashboard event ID, event name, or candidate event from the repository's event datasets. For example, rows can connect to dashboard events such as `E001`, `E002`, and `E003`, or to dated candidate events that were excluded from the current event-study sample.

The `event_family` field keeps the news evidence analytically aligned with the existing coding structure. It groups source material into categories such as `Military Demonstration`, `Diplomatic Shock`, `Policy Response`, `Technology Competition`, and `Semiconductor Supply Chain`.

This linkage supports richer qualitative traceability, but it does not create new event-study windows by itself. Adding a source item is not equivalent to adding an event to the empirical sample.

## Analytical Use

The database can support future modules such as:

- dashboard drilldowns that show source evidence next to event-study outputs
- analyst-reviewed event coding audits
- evidence inventories for mechanism-level interpretation
- transparent documentation of why an event was grouped into a particular family

These uses enrich the evidence base around the existing design. They do not replace the event-study methodology, market-data processing, abnormal-return calculations, or deterministic dashboard outputs already in the project.

## Limitations

This dataset is curated and intentionally limited. It is not exhaustive, real-time, or a comprehensive news archive. The placeholder rows are examples for structure and workflow development, not final citations.

Analyst review is required before using any row in a paper, presentation, or public dashboard. Exact URLs, publication dates, source names, article titles, and summaries should be verified against the original source.

The database is for academic, educational, and evidence-enrichment purposes only. It does not provide investment advice, trading recommendations, market forecasts, policy advice, or unsupported causal claims.
