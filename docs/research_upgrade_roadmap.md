# Research Upgrade Roadmap

> Academic Research Notice:
> This roadmap describes staged dataset expansion. It does not validate new events, generate synthetic observations, or report new CAR results.

## Stage 1: 18 To 38 Events

### Objectives

- Integrate the 20 Include candidates after source validation.
- Preserve `data/events_v2.csv` as the validated baseline.
- Add official-source and contemporaneous-news evidence packets.
- Map event dates to trading dates.
- Extend theory coding for `interpretation_type`, `strategic_importance_level`, and `state_support_signal`.

### Risks

- Some events may have ambiguous announcement, publication, effective, or disclosure dates.
- Same-day confounding may affect May 15, 2020 and other high-news periods.
- Recognition-diplomacy events may have weaker immediate market effects.
- Export-control events may produce mixed interpretations depending on investor asset universe.

### Expected Analytical Gains

- Export-control events become a real family rather than one observation.
- State-support and industrial-policy mechanisms become testable at a descriptive level.
- China countermeasures and critical-materials controls enter the dataset.
- Diplomatic-recognition competition becomes visible in the empirical design.

## Stage 2: 38 To 60 Events

### Objectives

- Add approximately 22 additional validated events after targeted discovery.
- Prioritize underrepresented families:
  - legal and judicial signaling
  - economic coercion
  - diplomatic recognition and international-space events
  - additional allied subsidy decisions
  - supply-chain security restrictions
- Add more 2018-2021 events to reduce time-period clustering.

### Risks

- More events may be cumulative policies rather than clean event-date shocks.
- Expanding too quickly can dilute event quality.
- Event windows may overlap more often.
- Evidence standards may become uneven across jurisdictions and languages.

### Expected Analytical Gains

- Better balance across military, diplomatic, export-control, industrial-policy, and coercion families.
- More credible event-family comparisons.
- Better ability to distinguish first-of-kind events from repeated-event adaptation.
- Stronger basis for surprise and anticipation coding.

## Stage 3: 60 To 100+ Events

### Objectives

- Build a broad geopolitical competition event database with more than 100 validated observations.
- Add structured evidence metadata for every event.
- Introduce systematic search protocols by actor, country, policy domain, and event family.
- Prepare for larger-sample statistical summaries while preserving interpretive caution.

### Risks

- Larger samples may include lower-salience events unless thresholds are enforced.
- Cross-country comparability becomes harder.
- Coding drift becomes a serious threat unless audit procedures are standardized.
- More event overlap can weaken clean event-study interpretation.

### Expected Analytical Gains

- Stronger descriptive power across geopolitical competition mechanisms.
- More robust repeated-event analysis.
- Better separation of threat, opportunity, mixed, and adaptation interpretations.
- Ability to study escalation sequences, policy reciprocity, and cross-domain spillovers.

## Governance Principle

Each stage should produce a separate candidate file, audit document, and validation log before any event is promoted to the master dataset. The project should never treat candidate discovery as equivalent to validated event inclusion.
