# Data Flow Architecture

## Product Context

Repo 3 is an AI-Assisted Geopolitical Risk Dashboard for a Geopolitical Risk Analyst.

The dashboard uses Repo 2 analytics outputs to create a decision-support experience that combines executive metrics, event-level context, mechanism-level summaries, and AI-assisted interpretation.

This document defines how information flows through the Repo 3 MVP.

## 1. Repo 2 Outputs

Repo 2 is the analytics engine that produces the structured source files for Repo 3.

Primary Repo 2 outputs:

| Output | Role in Repo 3 |
|---|---|
| `dashboard_data.csv` | Event-level dashboard dataset |
| `mechanism_summary.csv` | Mechanism-level portfolio summary |
| `executive_summary.md` | Business-facing summary of the latest engine run |

These files are the source of truth for the dashboard.

Repo 3 should not recalculate CAR or change event-study methodology. It should consume Repo 2 outputs and transform them into dashboard and AI insight views.

## 2. Data Loader

The Data Loader is responsible for bringing Repo 2 outputs into the Repo 3 dashboard environment.

Its role is to make the source files available for dashboard display, metrics calculation, and AI context building.

Expected data objects:

- event-level dashboard data
- mechanism-level summary data
- executive summary text

The Data Loader supports the product by ensuring the dashboard starts from a consistent set of Repo 2 outputs.

## 3. Metrics Layer

The Metrics Layer turns loaded data into the key numbers shown in the Executive Dashboard and KPI Cards.

Core metrics:

- total events analyzed
- successful events
- failed events
- strongest positive event
- strongest negative event
- latest event summary
- mechanism-level mean CAR
- mechanism-level minimum and maximum CAR

This layer supports Business Analytics interpretation by converting raw output tables into decision-ready indicators.

The Metrics Layer does not change the underlying event-study results. It only summarizes and organizes them for dashboard use.

## 4. AI Context Builder

The AI Context Builder prepares selected dashboard information for AI-assisted interpretation.

Its role is to choose the relevant facts that should be passed into the LLM.

Possible context elements:

- selected event metadata
- selected event CAR percent and direction
- strongest positive event
- strongest negative event
- mechanism-level summary
- failed event count
- executive summary text
- non-investment-advice constraint

The AI Context Builder helps keep the AI insight grounded in Repo 2 outputs and prevents open-ended interpretation that is not supported by the data.

## 5. LLM Insight Generator

The LLM Insight Generator converts structured context into analyst-facing language.

Its role is to produce draft interpretation, not prediction.

Expected AI outputs:

- event explanation
- mechanism interpretation
- historical comparison within the current dataset
- caveats for analyst review

The LLM Insight Generator should avoid:

- forecasting
- trading recommendations
- investment advice
- policy advice
- unsupported causal claims

The output should be clearly labeled as AI-assisted draft interpretation.

## 6. Dashboard UI

The Dashboard UI presents the final information to the Geopolitical Risk Analyst.

The MVP UI should include:

- Executive Dashboard
- KPI Cards
- Latest Event View
- AI Insight Panel

The UI should display both structured analytics and AI-assisted interpretation so the analyst can compare the AI narrative against the underlying data.

The dashboard should support review, explanation, and communication rather than automated decision-making.

## End-to-End Workflow Diagram

```text
Repo 2 Outputs
dashboard_data.csv
mechanism_summary.csv
executive_summary.md
        ↓
Data Loader
        ↓
Metrics Layer
        ↓
Executive Dashboard + KPI Cards
        ↓
AI Context Builder
        ↓
LLM Insight Generator
        ↓
AI Insight
        ↓
Dashboard UI
        ↓
Analyst Review and Communication
```

## Information Flow Summary

The Repo 3 MVP follows a clear analytics-to-insight sequence:

```text
structured event-study outputs
→ dashboard metrics
→ selected analytical context
→ AI-assisted explanation
→ analyst-reviewed decision support
```

This flow preserves the integrity of Repo 2 calculations while making the outputs easier to understand, communicate, and use in a business analytics setting.

## Design Principle

Repo 3 should separate analytics calculation from interpretation.

Repo 2 calculates event-study outputs.

Repo 3 organizes, explains, and presents those outputs.

This separation keeps the dashboard transparent, auditable, and suitable for academic and educational analytics use.
