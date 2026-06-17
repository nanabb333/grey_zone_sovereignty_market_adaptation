# Sprint 5 Implementation Plan: Scenario Comparison Engine

## Sprint Goal

Create a deterministic comparison layer that explains why historical analogs are similar or different from a scenario question.

The focus is decision intelligence rather than retrieval alone.

## Deliverables

| Deliverable | Purpose |
|---|---|
| `scripts/scenario_comparison_engine.py` | Working deterministic comparison prototype |
| `results/scenario_comparison_engine/comparison_results.json` | Dashboard-ready comparison output |
| `results/scenario_comparison_engine/comparison_results.md` | Analyst-readable comparison output |
| `docs/scenario_comparison_engine_design.md` | Product and architecture design |
| `docs/similarity_explainability_framework.md` | Explanation rules and analyst interpretation |
| `docs/sprint5_implementation_plan.md` | Implementation plan and validation notes |
| Dashboard Scenario Comparison View | Productized comparison experience |

## Phase 1: Consume Historical Analog Output

Use:

```text
results/historical_analog_engine/demo_results.json
```

The comparison engine should not rerun retrieval or change similarity scores.

## Phase 2: Build Comparison Matrix

Compare each analog across:

- actor
- target
- event family
- severity
- surprise
- evidence profile

Each matrix row should include scenario value, historical value, status, and explanation.

## Phase 3: Add Explainability Layer

For every analog, generate:

- score composition notes
- major matching features
- major differences

This gives analysts a reasoned explanation of the retrieval result.

## Phase 4: Closest vs Alternative

For each scenario question, identify:

- closest historical analog
- alternative analog
- score-gap summary

The output should encourage review of alternatives when scores are close.

## Phase 5: Dashboard Integration

Add a Scenario Comparison View that displays:

- closest historical analog
- alternative analog
- similarity matrix
- match explanation
- key differences

The dashboard should load:

```text
results/scenario_comparison_engine/comparison_results.json
```

## Validation

Required checks:

```bash
python3 scripts/historical_analog_engine.py
python3 scripts/scenario_comparison_engine.py
python3 -m py_compile scripts/historical_analog_engine.py scripts/scenario_comparison_engine.py
```

Dashboard validation should confirm:

- Scenario Comparison View renders
- comparison matrix appears
- closest and alternative analogs appear
- no forecast or investment language is introduced

## Out Of Scope

- forecasting
- investment recommendations
- trading signals
- LLM APIs
- live news fetching
- changes to analytical claims
