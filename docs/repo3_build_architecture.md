# Repo 3 Build Architecture

## Product Context

Repo 3 is an AI-Assisted Geopolitical Risk Dashboard for a Geopolitical Risk Analyst.

The product uses Repo 2 analytics outputs to present event-study results, portfolio-level metrics, and AI-assisted interpretation in a decision-support dashboard.

This document defines the first buildable architecture for the Repo 3 MVP.

## 1. Data Sources Layer

### Purpose

Provide the structured analytics inputs that power the dashboard.

Repo 3 should use Repo 2 outputs as its source of truth rather than recalculating event-study metrics.

### Primary Data Sources

| Data Source | Role |
|---|---|
| `dashboard_data.csv` | Event-level dashboard table |
| `mechanism_summary.csv` | Mechanism-level portfolio summary |
| `executive_summary.md` | Non-technical run summary |

### Product Role

This layer connects the automated analytics engine from Repo 2 to the decision-support interface in Repo 3.

It keeps calculation and interpretation separated:

```text
Repo 2 = analytics calculation
Repo 3 = dashboard interpretation
```

## 2. Dashboard Layer

### Purpose

Transform Repo 2 outputs into business-facing metrics and dashboard-ready views.

The Dashboard Layer should organize raw output files into meaningful summaries for the analyst.

### Core Responsibilities

- summarize total events analyzed
- summarize successful and failed events
- identify strongest positive event
- identify strongest negative event
- display latest event context
- present mechanism-level summaries
- connect events to reports, figures, and event-window data

### Product Role

This layer creates the analytical backbone of the dashboard.

It allows the user to move from file-based outputs to structured decision-support views.

## 3. AI Layer

### Purpose

Generate AI-assisted interpretation from dashboard context.

The AI Layer should help the analyst explain what the Repo 2 outputs show, while avoiding prediction, trading recommendations, or unsupported claims.

### Core Responsibilities

- receive selected event context
- receive mechanism-level context
- receive executive summary context
- generate event explanation
- generate mechanism interpretation
- generate historical comparison within the current dataset
- include caveats and analyst-review language

### Product Role

This layer turns structured analytics into readable draft insight.

The AI output should be clearly labeled as draft interpretation and should remain grounded in the dashboard data.

## 4. UI Layer

### Purpose

Present metrics, event details, and AI-assisted insight in a clear analyst workflow.

The UI Layer is the user-facing surface of the Repo 3 MVP.

### MVP Sections

| Section | Role |
|---|---|
| Executive Dashboard | Shows run-level summary and key metrics |
| KPI Cards | Highlights total events, successes, failures, strongest positive event, and strongest negative event |
| Latest Event View | Displays event metadata, CAR percent, direction, and status |
| AI Insight Panel | Shows AI-assisted draft interpretation for analyst review |

### Product Role

This layer makes the analytics accessible to a non-technical or semi-technical audience.

It should support fast review, clear interpretation, and stakeholder-ready communication.

## 5. Expected User Workflow

The MVP user workflow should be simple and focused:

```text
Open Dashboard
→ View Metrics
→ Select Event
→ Receive AI Insight
```

### Step 1: Open Dashboard

The analyst opens the dashboard and immediately sees the latest Repo 2 analytics run.

Expected value:

- reduces time spent locating output files
- provides immediate project context
- confirms the dashboard is using the latest available analytics output

### Step 2: View Metrics

The analyst reviews KPI cards and executive metrics.

Expected value:

- identifies the number of processed events
- checks for failed events
- sees strongest positive and negative market reactions
- understands the overall batch result

### Step 3: Select Event

The analyst selects or reviews an event from the event-level data.

Expected value:

- connects event metadata with CAR result
- shows the mechanism and event type
- links the event to supporting reports, figures, and event-window data

### Step 4: Receive AI Insight

The analyst receives an AI-assisted interpretation based on the selected event and portfolio context.

Expected value:

- converts dashboard metrics into plain-language explanation
- supports faster stakeholder communication
- preserves analyst review and final judgment

## MVP Execution Principle

The first buildable version should stay narrow.

It should demonstrate:

```text
Repo 2 analytics outputs
→ dashboard metrics
→ selected event context
→ AI-assisted interpretation
```

The MVP should not attempt to become a full research platform, forecasting system, or trading tool.

Its purpose is to prove that structured event-study outputs can become an AI-assisted Business Analytics decision-support dashboard.
