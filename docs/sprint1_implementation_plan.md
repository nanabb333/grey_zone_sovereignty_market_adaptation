# Sprint 1 Implementation Plan: Historical Analog Engine

## Sprint Goal

Build the product architecture for a Historical Analog Engine that retrieves validated historical geopolitical analogs, explains similarity, and assembles supporting evidence for analyst review.

Sprint 1 should produce a scalable design foundation. It should not implement forecasting, return prediction, or investment recommendations.

## Deliverables

| Deliverable | Purpose |
|---|---|
| `docs/architecture.md` | System architecture and product boundary |
| `docs/scenario_taxonomy.md` | Normalized scenario-family taxonomy |
| `docs/event_feature_schema.md` | Minimum feature schema for retrieval |
| `docs/historical_analog_engine_design.md` | Retrieval, scoring, and output design |
| `docs/sprint1_implementation_plan.md` | Phased implementation roadmap |

## Phase 1: Align Inputs

Objective: define how existing repository assets feed the analog engine.

Tasks:

- Treat `data/events_v3.csv` as the preferred validated event source.
- Preserve `event_id` as the stable join key.
- Map existing event labels to the Sprint 1 scenario taxonomy.
- Identify required fields missing from current records, especially `actor`, `target`, and numeric `severity_score`.
- Use `data/news/news_events.csv` as the evidence-link source.
- Use CAR outputs only as descriptive historical context.

Acceptance criteria:

- every indexed event has a stable ID
- every indexed event maps to one primary taxonomy family
- missing feature fields are flagged rather than silently inferred

## Phase 2: Define Feature Extraction

Objective: create a repeatable feature layer without changing original event records.

Tasks:

- Convert `surprise_score` values from `Low`, `Medium`, and `High` into numeric scores.
- Define deterministic severity scoring rules.
- Normalize actor names and aliases.
- Normalize targets across actors, sectors, technologies, and geographies.
- Preserve original source fields for audit.
- Store derived features as a separate table or object.

Acceptance criteria:

- feature derivation is reproducible
- original event records remain unchanged
- every derived score has a documented rule

## Phase 3: Build Retrieval Design

Objective: define a deterministic retrieval architecture.

Tasks:

- Build a candidate index from validated events.
- Compute a decomposable similarity score.
- Return top ranked analogs.
- Include score components in output.
- Apply low-score and low-evidence flags.

Acceptance criteria:

- same input scenario returns the same ranking across runs
- every analog includes a score breakdown
- analyst can see why each analog was retrieved

## Phase 4: Assemble Evidence

Objective: link analogs to source support and historical context.

Tasks:

- Attach linked news evidence by `related_event_id`.
- Attach source packet paths when available.
- Attach event source URL from the validated event record.
- Attach descriptive historical CAR fields when available.
- Label all CAR fields as historical context only.

Acceptance criteria:

- every analog has an evidence section
- missing evidence is visible to the analyst
- output language avoids predictive or investment framing

## Phase 5: Define Analyst Output

Objective: standardize the final analyst-facing brief.

Required sections:

- Historical Analogs
- Similarity Explanation
- Evidence Base
- Observed Historical Pathways
- Analyst Notes

Acceptance criteria:

- output can be rendered as Markdown
- output can be represented as JSON later
- caveats are included by default
- no future market or investment recommendation language is generated

## Future Implementation Sequence

Recommended build order after Sprint 1 design approval:

1. Create taxonomy mapping table.
2. Create derived event feature table.
3. Add validation checks for required feature fields.
4. Implement deterministic similarity scoring.
5. Generate Markdown analog briefs.
6. Generate JSON analog result files.
7. Add dashboard view for scenario analogs.
8. Add analyst feedback fields for retrieval quality.

## Data Quality Risks

| Risk | Mitigation |
|---|---|
| Existing event families do not map cleanly to the new taxonomy | Keep original labels and add normalized taxonomy separately |
| Actor and target fields are incomplete | Derive conservatively and flag missing fields |
| News evidence contains placeholder rows | Label evidence quality and require verification before publication |
| CAR context may be overinterpreted | Include explicit historical-context-only language |
| Similarity score may look more precise than it is | Report components and confidence bands, not only total score |

## Product Scalability Roadmap

### Sprint 2 Candidate Work

- Feature extraction prototype
- Taxonomy mapping file
- Similarity score implementation
- Markdown brief generator
- Retrieval validation report

### Sprint 3 Candidate Work

- Dashboard integration
- Analyst feedback capture
- Evidence quality scoring
- More detailed pathway tagging
- JSON API contract

### Later Work

- Actor ontology
- Technology and sector graph
- Multilingual source evidence
- Human-in-the-loop taxonomy review
- LLM-assisted summarization constrained to retrieved evidence

Forecasting, trading signals, portfolio allocation, and investment recommendations should remain out of scope unless a separate governance process defines a compliant product boundary.
