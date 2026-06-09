# Dashboard Wireframe Specification

## Product Context

Repo 3 is an AI-Assisted Geopolitical Risk Dashboard for a Geopolitical Risk Analyst.

The dashboard turns Repo 2 analytics outputs into a structured decision-support interface for reviewing market reactions to Taiwan-related geopolitical events.

This wireframe specification defines the MVP dashboard layout from a Business Analytics and product design perspective.

## 1. Header Section

### Purpose

Establish the dashboard context and give the analyst immediate orientation.

The header should make clear what the dashboard analyzes, what dataset is currently loaded, and what type of output the user is reviewing.

### Displayed Information

- Product name
- Current run or dataset label
- Date of latest analytics run
- Source engine reference
- Academic and educational use notice
- Not investment advice notice

### User Value

The analyst can quickly understand the scope and purpose of the dashboard before interpreting any results.

This reduces ambiguity and reinforces that the dashboard is an analytics decision-support tool, not a forecasting or trading product.

## 2. KPI Cards Section

### Purpose

Provide a concise executive overview of the current analytics run.

The KPI cards should summarize the batch result before the analyst moves into detailed exploration.

### Displayed Information

- Total events analyzed
- Successful events
- Failed events
- Strongest positive event
- Strongest negative event
- Average CAR across successful events
- Count of positive, negative, and neutral CAR outcomes

### User Value

The analyst can identify the most important portfolio-level facts at a glance.

This section supports quick stakeholder briefings and helps the analyst decide where to focus deeper review.

## 3. Market Impact Visualization Section

### Purpose

Visualize event-level market reactions so the analyst can compare abnormal CAR outcomes across events.

This section should turn the event-level results into an intuitive visual comparison.

### Displayed Information

- Event names
- CAR percent by event
- CAR direction
- Mechanism grouping or color coding
- Processing status indicator
- Highlight for strongest positive and strongest negative event

### User Value

The analyst can quickly see which geopolitical events were associated with positive or negative benchmark-adjusted abnormal returns.

The visualization helps make event-study outputs easier to explain to non-technical stakeholders.

## 4. Mechanism Analysis Section

### Purpose

Support portfolio-level interpretation by grouping outcomes by geopolitical mechanism.

This section should help the analyst understand whether different mechanisms show different market-impact patterns.

### Displayed Information

- Mechanism name
- Event count
- Successful event count
- Failed event count
- Mean CAR value
- Minimum CAR value
- Maximum CAR value
- Direction distribution by mechanism

### User Value

The analyst can compare Risk events with Strategic_Importance events and assess whether one mechanism appears associated with stronger positive or negative abnormal CAR in the current dataset.

This section supports higher-level analytical reasoning beyond individual event review.

## 5. Event Explorer Section

### Purpose

Provide the main workspace for reviewing event-level details.

The Event Explorer should allow the analyst to scan events, compare metadata, and access supporting artifacts.

### Displayed Information

- Event ID
- Event name
- Event date
- Mechanism
- Event type
- Asset
- Benchmark
- CAR value
- CAR percent
- CAR direction
- Status
- Report link
- Figure link
- Event-window data link

### User Value

The analyst can move from a high-level dashboard view into specific event evidence.

This section supports validation, comparison, and detailed review without requiring the user to manually open multiple output folders.

## 6. AI Insight Panel Section

### Purpose

Provide AI-assisted interpretation grounded in the dashboard data.

The panel should help the analyst draft explanations while keeping the underlying evidence visible and reviewable.

### Displayed Information

- Selected event summary
- Event explanation
- Mechanism interpretation
- Historical comparison
- Caveats and analyst review notes
- Clear label that the text is AI-assisted draft interpretation
- Reminder that outputs are not investment advice

### User Value

The analyst can move faster from structured outputs to stakeholder-ready language.

The AI panel supports explanation and communication while preserving analyst control over final interpretation.

## 7. User Journey

### Purpose

Define the intended flow through the dashboard.

The MVP should guide the analyst from quick understanding to deeper review and then to communication-ready insight.

### Displayed Information

The user journey should follow this sequence:

```text
Open dashboard
↓
Review run-level KPIs
↓
Identify strongest positive and negative events
↓
Compare events in the market impact visualization
↓
Review mechanism-level patterns
↓
Inspect individual events in the Event Explorer
↓
Use the AI Insight Panel to draft interpretation
↓
Analyst reviews, edits, and decides what to communicate
```

### User Value

The analyst has a clear workflow for turning event-study outputs into decision-support insights.

The dashboard reduces the gap between analytics production and business-facing communication.

## MVP Wireframe Principle

The dashboard should prioritize:

- clarity over complexity
- comparison over decoration
- analyst review over automation
- explainability over prediction
- decision support over recommendation

The MVP should make Repo 2 outputs easier to understand, validate, and communicate without changing the underlying analytics methodology.
