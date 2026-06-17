# Product Case Study: Geopolitical Scenario Intelligence Engine

## Problem

Geopolitical risk analysis often lives across research notes, event lists, news links, market reaction files, and dashboard summaries. That makes it hard for an analyst or reviewer to quickly answer a practical question such as: "Which historical cases look similar to this scenario, and what evidence supports the comparison?"

The project addresses this by turning a Taiwan geopolitical event-study repository into a portfolio-ready intelligence product.

## Product Concept

The Geopolitical Scenario Intelligence Engine is an evidence-based historical analog and scenario reasoning system.

It lets an analyst start from a question, map that question to a scenario family, retrieve comparable historical events, inspect similarity logic, and read an analyst-style brief. The product is designed for review and explanation, not prediction.

Example questions:

- What happens if China launches another Joint Sword exercise?
- What happens if new semiconductor export controls are announced?
- What happens after a major Taiwan election?

## Data Foundation

The engine builds on existing repository assets:

- validated geopolitical event dataset
- expanded V3 event dataset and source packets
- CAR-covered historical event analysis
- curated news evidence database
- event-family analytics
- scenario similarity outputs
- historical analog demo outputs

The data model keeps event IDs stable so events, evidence, CAR context, and analyst briefs can be traced back to source records.

## Analytics Workflow

The workflow follows a Research → Analytics → Product sequence:

1. Research layer: validate events, event families, dates, mechanisms, and source packets.
2. Evidence layer: link news evidence and coding notes to event IDs.
3. Analytics layer: summarize event families and historical CAR context.
4. Scenario layer: map questions to scenario families and retrieve historical analogs.
5. Product layer: render analyst-ready cards and briefs in the dashboard.

CAR context remains historical and descriptive. It is not used to forecast returns.

## Deterministic Reasoning Design

The Historical Analog Engine uses deterministic rules instead of LLM APIs.

The similarity score is decomposed into:

- event-family match
- actor overlap
- target overlap
- severity proximity
- surprise proximity
- temporal-context fit
- evidence coverage

Each retrieved analog includes a score breakdown so the analyst can review why it appeared. This makes the system auditable and suitable for a portfolio demo.

## Dashboard Experience

The dashboard includes a Scenario Intelligence Demo section. For each demo question, it displays:

- scenario classification
- top historical analogs
- similarity scores
- brief similarity explanation
- evidence base
- observed historical pathways
- analyst notes

The dashboard reads deterministic outputs from `results/historical_analog_engine/demo_results.json`. If the JSON cannot be loaded, the dashboard shows fallback instructions rather than failing silently.

## Portfolio Value

This project demonstrates:

- research-to-product translation
- data modeling across events, evidence, analytics, and dashboard outputs
- deterministic reasoning design
- analyst-facing product communication
- responsible boundaries around geopolitical and market-sensitive analysis
- static dashboard delivery without API keys or live services

It gives a reviewer a concrete product demo while preserving the discipline of the original event-study design.

## Limitations And Safe Boundaries

This is a historical analog retrieval and analyst briefing system.

It does not provide:

- return forecasts
- investment advice
- trading recommendations
- live news monitoring
- LLM-generated analysis
- automated causal claims

Similarity scores are retrieval aids, not probabilities or severity measures. News evidence rows may include placeholder-safe source metadata that should be verified before formal publication.
