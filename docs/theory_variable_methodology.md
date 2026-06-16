# Theory Variable Methodology

## Purpose

The theory variable layer operationalizes core dissertation concepts in `data/events_v2.csv` without changing the event-study methodology, historical CAR results, or existing research claims.

The added fields are optional interpretive coding variables:

- `interpretation_type`
- `state_support_signal`
- `strategic_importance_level`

Blank values are allowed and indicate that the existing documentation does not provide sufficient support for conservative coding.

## Theoretical Origins

The coding draws from the project's existing theory documents, especially:

- `notes/theory_notes.md`
- `notes/event_coding_notes.md`
- `docs/adaptation_vs_anticipation.md`
- `docs/adaptation_vs_anticipation_dissertation_section.md`
- `docs/research_design_revision_v2.md`

These documents describe Taiwan-related market interpretation through threat, opportunity, adaptation, strategic importance, surprise, and repeated-event familiarity.

## Coding Logic

### interpretation_type

Allowed values:

- `Threat`
- `Opportunity`
- `Adaptation`
- `Mixed`

`Threat` is used when existing coding frames the event as military pressure, diplomatic escalation, coercion, legal-political pressure, or direct Taiwan Strait instability.

`Opportunity` is used when the event highlights Taiwan's semiconductor centrality, strategic investment value, allied industrial policy, or supply-chain importance.

`Adaptation` is used conservatively for repeated military or grey-zone events where the existing repetition coding and adaptation documentation support interpretation as recurring, increasingly familiar pressure.

`Mixed` is used when an event plausibly contains both strategic-importance and restrictive/threat-like elements, such as export controls.

### state_support_signal

Allowed values:

- `High`
- `Medium`
- `Low`

This field codes whether the event contains a visible state-policy support or state-policy intervention signal. It is coded only where the event description or supporting documentation provides a clear basis.

`High` is reserved for explicit state support, such as CHIPS Act preliminary terms.

`Medium` is used for state policy actions that reinforce strategic positioning but are not direct firm support.

`Low` is used for strategic investment events where the event indicates strategic value but the row does not itself document direct state support.

### strategic_importance_level

Allowed values:

- `High`
- `Medium`
- `Low`

This field codes whether an event directly reinforces Taiwan's strategic economic, semiconductor, or technology-policy importance. It is coded conservatively and left blank for events that are primarily risk or coercion events without clear strategic-importance framing.

## Limitations

The variables are structured interpretive fields. They do not identify causal mechanisms, predict market reactions, or change historical CAR outputs.

The coding is based on existing project documentation and event descriptions. It should be reviewed by an analyst before formal use in dissertation tables, public dashboards, or publication-ready datasets.

## Analyst Review Requirement

Future reviewers should check:

- whether each coded row has sufficient documentary support
- whether blank rows should remain blank
- whether `Adaptation` coding is too broad or too narrow
- whether state-support signals should be separated from broader state-policy actions
- whether strategic-importance coding should remain limited to `Strategic_Importance` mechanism events
