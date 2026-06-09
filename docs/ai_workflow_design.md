# AI Workflow Design

## 1. AI Purpose

The AI component in Repo 3 acts as an interpretation and decision-support layer for the Geopolitical Risk Dashboard.

Its purpose is to help a Geopolitical Risk Analyst explain event-study outputs, compare results across geopolitical mechanisms, and prepare clear analyst-facing summaries.

The AI component should:

- summarize structured analytics outputs
- explain event-level results in plain language
- compare mechanism-level patterns
- highlight caveats and review needs
- support analyst judgment

The AI component should not:

- forecast future market movements
- make trading recommendations
- provide investment advice
- provide policy advice
- invent event classifications or unsupported conclusions

## 2. AI Inputs

The MVP AI layer should use Repo 2 dashboard-ready outputs as its source of truth.

| Input | Role |
|---|---|
| `dashboard_data.csv` | Provides event-level metadata, CAR values, CAR direction, processing status, and artifact paths |
| `mechanism_summary.csv` | Provides mechanism-level event counts and CAR summary statistics |
| `executive_summary.md` | Provides the latest non-technical batch summary for context |

These inputs allow the AI layer to remain grounded in structured analytics outputs rather than relying on open-ended generation.

## 3. AI Outputs

The MVP AI layer should produce three types of analyst-assistive outputs.

### Event Explanation

Plain-language explanation of a selected event's dashboard results.

This output should describe:

- event name and date
- mechanism and event type
- asset and benchmark
- CAR percent and direction
- whether the event was processed successfully
- where the analyst can review supporting artifacts

### Mechanism Interpretation

Plain-language interpretation of mechanism-level results.

This output should describe:

- number of events per mechanism
- average CAR by mechanism
- strongest and weakest mechanism-level outcomes
- whether the comparison is based on enough events to support confidence
- any caveats about failed events or limited sample size

### Historical Comparison

Plain-language comparison across events in the dashboard dataset.

This output should describe:

- strongest positive event
- strongest negative event
- whether similar mechanisms show similar or different results
- how the selected event compares with prior events in the same dataset
- what additional analyst review may be needed

## 4. AI Workflow

The MVP AI workflow should follow a transparent decision-support sequence:

```text
Repo 2 Outputs
→ Context Builder
→ LLM
→ AI Insight
→ Dashboard Display
```

### Repo 2 Outputs

Structured analytics files from Repo 2 provide the factual base for AI interpretation.

### Context Builder

The context builder selects the relevant event-level, mechanism-level, and summary information needed for the user question.

It should keep the AI grounded in the dashboard data and avoid unnecessary context.

### LLM

The language model converts structured analytics context into readable interpretation.

The LLM should explain what the existing results show, not create unsupported forecasts or recommendations.

### AI Insight

The AI insight is a draft explanation for analyst review.

It should be clearly labeled as AI-assisted interpretation and should include caveats when sample size, failed events, or metric limitations matter.

### Dashboard Display

The dashboard presents the AI insight beside the underlying event data, mechanism summary, figures, and reports.

This keeps the analyst in control and makes the AI output auditable.

## 5. MVP AI Features

### Feature 1: Event Explanation

Purpose:

Help the analyst quickly understand one selected event.

User value:

The analyst can select an event and receive a concise explanation of its CAR result, direction, mechanism, and supporting outputs.

Decision-support role:

This feature reduces the time needed to translate event-level CSV fields into a stakeholder-ready explanation.

### Feature 2: Mechanism Interpretation

Purpose:

Help the analyst interpret portfolio-level patterns by mechanism.

User value:

The analyst can understand whether Risk or Strategic_Importance events show stronger positive or negative abnormal CAR patterns in the current dataset.

Decision-support role:

This feature supports comparison across event categories while preserving caveats about limited sample size and failed events.

### Feature 3: Historical Comparison

Purpose:

Help the analyst compare a selected event with other events in the dashboard dataset.

User value:

The analyst can see whether an event is unusually positive, unusually negative, or broadly consistent with prior events.

Decision-support role:

This feature supports contextual interpretation without implying prediction or future market direction.

## Explainability Principles

The AI layer should be understandable, auditable, and analyst-controlled.

Core principles:

- show the data used to generate the insight
- distinguish facts from interpretation
- label AI-generated text as draft analysis
- include caveats for limited samples or failed events
- avoid forecasting and trading language
- keep the analyst responsible for final interpretation

## Portfolio Positioning

This AI workflow demonstrates how structured analytics outputs can be transformed into explainable decision-support insights.

Repo 3 should be positioned as a Business Analytics dashboard project that combines:

- event-study analytics
- product-oriented dashboard design
- AI-assisted interpretation
- explainable decision-support workflow
