# Repo 3 MVP Product Specification

## 1. Product Name

AI-Assisted Geopolitical Risk Dashboard

## 2. Target User

Geopolitical Risk Analyst

The target user monitors geopolitical events, evaluates their market relevance, and communicates risk insights to decision-makers in research, finance, policy, or business strategy settings.

## 3. Problem Statement

Geopolitical risk analysis often requires analysts to connect event narratives, market data, classification logic, and financial outcomes across multiple tools.

Repo 2 already automates the event-study workflow and produces structured outputs, but those outputs still require interpretation, comparison, and presentation before they can support decision-making.

The AI-Assisted Geopolitical Risk Dashboard should transform Repo 2 analytics outputs into a decision-support interface that helps analysts quickly understand:

- which events generated the strongest market reactions
- which mechanisms are associated with positive or negative abnormal returns
- which events require further review
- how event-level results compare across a portfolio of geopolitical shocks
- what summary insight can be communicated to non-technical stakeholders

The dashboard is not intended to replace analyst judgment. It is intended to make event-study outputs easier to explore, explain, and operationalize.

## 4. Data Sources

The MVP should use dashboard-ready outputs from Repo 2.

Primary inputs:

| Data Source | Purpose |
|---|---|
| `results/dashboard_data.csv` | Event-level dashboard dataset with CAR value, CAR percent, direction, status, and output paths |
| `results/mechanism_summary.csv` | Portfolio-level summary by geopolitical mechanism |
| `results/executive_summary.md` | Non-technical summary of the latest engine run |

Supporting artifacts:

| Artifact | Purpose |
|---|---|
| `reports/{event_id}_report.md` | Event-level analyst report |
| `figures/{event_id}_abnormal_returns.png` | Event-level abnormal return visualization |
| `results/event_windows/{event_id}_event_window_data.csv` | Daily event-window return and abnormal-return data |

## 5. MVP Features

The MVP should focus on turning existing Repo 2 outputs into clear, usable decision-support views.

Recommended MVP features:

| Feature | User Value |
|---|---|
| Event Overview Table | Lets analysts scan all processed events, CAR percent, direction, mechanism, and status |
| Mechanism Summary View | Helps compare market reactions across Risk and Strategic_Importance mechanisms |
| Event Detail View | Shows one event's metadata, CAR result, abnormal return figure, and report link |
| Strongest Positive / Negative Event Highlight | Surfaces the most important event-level outcomes quickly |
| Failed Event Review Panel | Shows events that failed processing and why |
| Executive Summary Panel | Presents business-facing summary language for quick review |
| AI-Assisted Insight Draft | Provides a clearly labeled draft interpretation that the analyst can accept, revise, or reject |

The AI-assisted feature should be advisory and transparent. It should summarize existing outputs rather than invent new classifications or claims.

## 6. Success Metric

The MVP is successful if a geopolitical risk analyst can use the dashboard to move from Repo 2 outputs to a stakeholder-ready risk summary in less time than reviewing CSVs, figures, and Markdown reports manually.

Primary success metric:

```text
Analyst can identify the strongest positive event, strongest negative event, mechanism-level pattern, and any failed events within 2 minutes.
```

Secondary success indicators:

- the dashboard clearly distinguishes successful and failed events
- every event links back to its report, figure, and event-window data
- mechanism-level summaries are easy to compare
- AI-assisted text is clearly labeled as draft interpretation
- the dashboard supports analyst review rather than replacing it

## Product Positioning

Repo 3 should be presented as a Business Analytics and AI-assisted decision-support product.

Repo 1 created the research foundation.

Repo 2 automated the event-study analytics workflow.

Repo 3 turns those analytics outputs into an interactive dashboard for analyst interpretation, communication, and decision support.
