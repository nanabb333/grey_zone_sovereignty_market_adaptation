# MVP Build Plan

## 1. MVP Goal

The Repo 3 MVP should demonstrate how Repo 2 analytics outputs can be transformed into an AI-assisted geopolitical risk dashboard.

The smallest buildable product should combine:

```text
Repo 2 Analytics
+
Repo 3 AI Interpretation
```

The MVP should help a Geopolitical Risk Analyst quickly understand the latest event-study results, review key market-impact metrics, and generate a clearly labeled AI-assisted interpretation draft.

The MVP is not intended to be a full dashboard platform. It is a focused decision-support prototype.

## 2. In Scope Features

### Executive Dashboard

Purpose:

Provide a single-screen overview of the latest Repo 2 analytics run.

Expected user value:

The analyst can understand the current batch result without opening individual CSV files, Markdown reports, or figures manually.

### KPI Cards

Purpose:

Summarize the most important run-level and event-level metrics.

In-scope KPI cards:

- total events analyzed
- successful events
- failed events
- strongest positive event
- strongest negative event

Expected user value:

The analyst can identify the most important results in seconds.

### Latest Event View

Purpose:

Show a concise view of one recent or selected event from the Repo 2 dashboard data.

Displayed information should include:

- event name
- event date
- mechanism
- event type
- asset
- benchmark
- CAR percent
- CAR direction
- processing status

Expected user value:

The analyst can move from run-level summary to event-level context without navigating through multiple files.

### AI Insight Panel

Purpose:

Generate a clearly labeled draft interpretation based on Repo 2 outputs.

The AI Insight Panel should support:

- event explanation
- mechanism interpretation
- historical comparison within the current dataset
- caveats and analyst review reminders

Expected user value:

The analyst can convert structured analytics outputs into business-facing language more efficiently while retaining final judgment.

## 3. Out of Scope Features

The MVP should intentionally exclude features that would expand the product beyond the first buildable version.

Out of scope:

- forecasting
- predictions
- trading recommendations
- investment advice
- policy recommendations
- complex filtering
- multi-page navigation
- automated event discovery
- automated classification
- user accounts
- database storage
- live market data feeds
- model evaluation dashboards
- advanced statistical testing

These exclusions keep the MVP focused on demonstrating the core value proposition:

```text
structured event-study outputs
→ dashboard summary
→ AI-assisted interpretation
```

## 4. Success Criteria

The MVP is successful if a Geopolitical Risk Analyst can use the dashboard to understand and explain the latest Repo 2 results faster than reviewing the output files manually.

Primary success criteria:

- The analyst can see total, successful, and failed event counts.
- The analyst can identify the strongest positive event.
- The analyst can identify the strongest negative event.
- The analyst can review one event's key metadata and CAR direction.
- The analyst can read an AI-assisted interpretation draft.
- The AI output is clearly labeled as draft interpretation.
- The dashboard includes a clear non-investment-advice notice.

Business Analytics success metric:

```text
The analyst can move from Repo 2 output files to a stakeholder-ready summary in under 2 minutes.
```

Portfolio success metric:

```text
The project clearly demonstrates workflow automation, dashboard product thinking, event-study analytics, and AI-assisted interpretation.
```

## 5. Future Expansion Opportunities

After the MVP is complete, Repo 3 can expand into a richer analytics product.

Potential future features:

- multi-page dashboard navigation
- event filtering by mechanism, date, asset, or status
- event detail pages
- mechanism comparison visuals
- embedded abnormal-return figures
- linked event reports
- raw CAR and abnormal CAR comparison
- analyst notes field
- exportable executive briefing
- AI-generated caveat checklist
- AI-assisted report drafting
- automated data refresh from Repo 2 outputs
- dashboard deployment

Future AI enhancements should remain explainable and analyst-controlled.

The product should continue to avoid forecasting, trading recommendations, and unsupported claims.

## MVP Positioning

The Repo 3 MVP should be presented as a Business Analytics decision-support prototype.

Its value is not that it predicts future events.

Its value is that it turns structured event-study outputs into a clear, reviewable, and business-facing analytics experience.
