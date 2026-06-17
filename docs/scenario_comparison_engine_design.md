# Scenario Comparison Engine Design

## Purpose

The Scenario Comparison Engine explains why a historical analog is similar to, or different from, a mapped scenario question. It extends historical analog retrieval into decision intelligence by showing feature-level comparison rather than only ranked matches.

This engine does not forecast future outcomes, estimate returns, or provide investment recommendations.

## Product Role

The Historical Analog Engine answers:

```text
Which historical events are most similar?
```

The Scenario Comparison Engine answers:

```text
Why are they similar, where do they differ, and which alternative analog should be reviewed?
```

## Inputs

Primary input:

```text
results/historical_analog_engine/demo_results.json
```

The input already contains:

- mapped scenario classification
- retrieved analogs
- deterministic similarity score components
- inferred actors and targets
- severity and surprise scores
- evidence items
- observed historical pathways

## Outputs

Primary outputs:

```text
results/scenario_comparison_engine/comparison_results.json
results/scenario_comparison_engine/comparison_results.md
```

The JSON output is designed for dashboard rendering. The Markdown output is designed for analyst review.

## Comparison Matrix

Each analog is compared across six dimensions:

| Dimension | Purpose |
|---|---|
| Actor | Compares scenario actors with historical event actors |
| Target | Compares scenario targets with historical targets, geography, or sector |
| Event family | Identifies exact or different scenario-family classification |
| Severity | Compares deterministic severity score |
| Surprise | Compares deterministic surprise score |
| Evidence profile | Summarizes source support and linked evidence |

Each row receives a status:

- `match`
- `partial`
- `different`

## Closest vs Alternative Match

For each question, the engine identifies:

- closest historical analog
- alternative analog
- score gap
- comparison summary

This helps analysts avoid over-focusing on only the top ranked match when the alternative is close.

## Dashboard Integration

The dashboard reads:

```text
results/scenario_comparison_engine/comparison_results.json
```

The Scenario Comparison View displays:

- closest historical analog
- alternative analog
- similarity matrix
- match explanation
- key differences

## Boundary

The comparison engine is a deterministic explanation layer. It supports analyst review and decision intelligence. It does not produce forecasts, investment advice, trading recommendations, or causal claims.
