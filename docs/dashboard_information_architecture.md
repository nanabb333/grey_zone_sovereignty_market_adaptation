# Dashboard Information Architecture

## Product Context

Repo 3 is an AI-Assisted Geopolitical Risk Dashboard designed for a Geopolitical Risk Analyst.

The dashboard transforms Repo 2 event-study outputs into decision-support views for reviewing geopolitical events, comparing market reactions, and preparing analyst-facing insights.

The MVP should prioritize clarity, comparison, and analyst workflow support.

## Dashboard Structure

The MVP dashboard is organized into four pages:

1. Executive Overview
2. Event Explorer
3. Mechanism Analysis
4. AI Insight Panel

## Page 1: Executive Overview

### Purpose

Provide a high-level summary of the latest event-study run for quick stakeholder review.

This page should help the analyst understand the overall batch result without opening individual CSV files, charts, or reports.

### Key Metrics

- Total events analyzed
- Successful events
- Failed events
- Strongest positive event
- Strongest negative event
- Average CAR by mechanism
- Count of positive, negative, and neutral events

### User Questions Answered

- What happened in the latest analytics run?
- How many events were successfully processed?
- Which event had the strongest positive market reaction?
- Which event had the strongest negative market reaction?
- Are there any failed events that need review?
- What is the overall portfolio-level signal?

## Page 2: Event Explorer

### Purpose

Allow the analyst to review individual events and compare event-level outputs.

This page should function as the main analytical workspace for scanning, filtering, and selecting events.

### Key Metrics

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
- Processing status
- Report path
- Figure path
- Event-window data path

### User Questions Answered

- Which events are included in the current dataset?
- Which events produced positive or negative abnormal CAR?
- Which mechanism is assigned to each event?
- What asset and benchmark were used?
- Which events require analyst review?
- Where can I find the event report, figure, or event-window data?

## Page 3: Mechanism Analysis

### Purpose

Help the analyst compare results across geopolitical mechanisms.

This page should support portfolio-level interpretation by grouping event outcomes by mechanism rather than treating each event in isolation.

### Key Metrics

- Mechanism
- Event count
- Successful event count
- Failed event count
- Mean CAR value
- Minimum CAR value
- Maximum CAR value
- Distribution of CAR direction by mechanism

### User Questions Answered

- Which mechanisms are represented in the dataset?
- Which mechanism has the strongest average market reaction?
- Are Risk events behaving differently from Strategic_Importance events?
- Are negative abnormal returns concentrated in one mechanism?
- Are there enough events in each mechanism to support comparison?
- Which mechanisms need more event coverage in future data collection?

## Page 4: AI Insight Panel

### Purpose

Provide analyst-assistive interpretation based on the structured dashboard outputs.

This page should help the analyst draft concise, reviewable insights for business-facing communication.

The AI feature should support analyst judgment rather than replace it.

### Key Metrics

- Latest executive summary
- Selected event metadata
- Selected event CAR percent
- Selected event CAR direction
- Mechanism-level summary
- Processing status
- Analyst review status

### User Questions Answered

- What is the plain-language interpretation of the current results?
- How should I summarize the strongest positive or negative event?
- What mechanism-level pattern is most important?
- Which caveats should be included?
- What should be reviewed before sharing the insight?
- Does the AI-generated draft stay grounded in the actual dashboard data?

## MVP Design Principle

The dashboard should move the analyst through a clear decision-support flow:

```text
Understand the run
↓
Explore individual events
↓
Compare mechanisms
↓
Draft analyst-reviewed insight
```

The MVP should avoid unnecessary complexity and focus on making Repo 2 outputs easier to understand, communicate, and validate.
