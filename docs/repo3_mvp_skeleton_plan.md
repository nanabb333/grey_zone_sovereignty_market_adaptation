# Repo 3 MVP Skeleton Implementation Plan

## Purpose

This document defines the first runnable dashboard skeleton for Repo 3.

The skeleton demonstrates how Repo 2 outputs can be displayed in a single-page dashboard before AI integration is added.

## MVP Scope

The first runnable version includes:

- Executive Dashboard
- KPI Cards
- Latest Event View
- Executive Summary display
- AI Insight Panel placeholder

The MVP does not include:

- AI integration
- forecasting
- trading recommendations
- complex filtering
- multi-page navigation
- new event-study calculations

## File Structure

```text
dashboard/
  index.html
  styles.css
  app.js
```

## Data Inputs

The skeleton reads existing Repo 2 outputs:

```text
results/dashboard_data.csv
results/executive_summary.md
```

## Dashboard Sections

| Section | Purpose |
|---|---|
| Header | Identifies the product and academic-use context |
| KPI Cards | Shows total events, successful events, failed events, strongest positive event, and strongest negative event |
| Latest Event View | Displays the most recent event by event date |
| Executive Summary | Renders the Repo 2 executive summary |
| AI Insight Panel | Reserves space for future analyst-reviewed AI interpretation |

## Run Plan

Run the dashboard from the repository root with a local static server.

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/dashboard/
```

## Success Criteria

The MVP skeleton is successful if:

- the dashboard loads in a browser
- KPI cards are populated from `results/dashboard_data.csv`
- the latest event view displays event metadata and CAR direction
- `results/executive_summary.md` is visible in the dashboard
- the AI Insight Panel clearly states that AI integration is not enabled yet

## Product Positioning

This skeleton establishes Repo 3 as a Business Analytics dashboard layer.

It proves the first connection between:

```text
Repo 2 analytics outputs
→ Repo 3 dashboard display
→ future AI-assisted interpretation
```
