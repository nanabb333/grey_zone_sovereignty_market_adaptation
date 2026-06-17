# Theory Coding Expansion Plan

> Academic Research Notice:
> This plan defines coding logic for future Dataset V3 integration. It does not assign CAR results or alter the validated event dataset.

## Baseline

The current validated baseline is `data/events_v2.csv`, with 18 events. Existing theory fields are:

- `interpretation_type`
- `state_support_signal`
- `strategic_importance_level`

Current coverage is complete for `interpretation_type`, but sparse for `state_support_signal` and `strategic_importance_level`. The V3 candidate set should expand those sparse fields, especially for semiconductor policy, export controls, strategic investments, and state support.

## Coding Decision Rules

### `interpretation_type`

| Code | Use when |
| --- | --- |
| `Threat` | The event primarily raises geopolitical, regulatory, military, supply-chain, or revenue-risk concerns. |
| `Opportunity` | The event primarily increases expected support, capacity, resilience, or strategic value for exposed firms or regions. |
| `Mixed` | The event plausibly creates both costs and benefits, such as controls that restrict China revenue while improving strategic value for non-China capacity. |
| `Adaptation` | The event belongs to a repeated pattern where investor interpretation may reflect normalization or learned response rather than a fresh shock. |

### `strategic_importance_level`

| Code | Use when |
| --- | --- |
| `High` | The event directly concerns semiconductor capacity, export controls, Taiwan security, strategic materials, state-backed chip investment, or major supply-chain resilience. |
| `Medium` | The event is geopolitically relevant but has a less direct link to semiconductor or Taiwan asset valuation. |
| `Low` | The event is relevant to background competition but weakly tied to investable market mechanisms. |
| Blank | Evidence is insufficient for conservative coding. |

### `state_support_signal`

| Code | Use when |
| --- | --- |
| `High` | The event creates or announces major public subsidies, public financing, state-backed funds, or explicit industrial-policy support. |
| `Medium` | The event implies meaningful public support, procurement preference, or regulatory backing but lacks clear direct funding scale. |
| `Low` | The event has some state-support context but the main mechanism is not public funding or industrial support. |
| Blank | The event is a risk, coercion, military, or diplomatic event without clear state-support content. |

## Expected Coding For Include Candidates

| Candidate ID | Expected `interpretation_type` | Expected `strategic_importance_level` | Expected `state_support_signal` | Coding rationale |
| --- | --- | --- | --- | --- |
| CAND-V3-002 | Mixed | High | Low | Restricts China access but may increase strategic value of allied supply chains. |
| CAND-V3-003 | Mixed | High | Low | Escalates technology controls; risk to China revenue but support for allied chokepoint value. |
| CAND-V3-004 | Threat | High | Blank | Raises decoupling and supplier-revenue risk. |
| CAND-V3-005 | Mixed | High | Blank | Threat to Huawei/China exposure but reinforces foundry chokepoint importance. |
| CAND-V3-006 | Mixed | High | Blank | Restricts SMIC but supports strategic value of non-China capacity. |
| CAND-V3-007 | Mixed | High | Low | Allied control coordination raises policy risk and chokepoint importance. |
| CAND-V3-008 | Mixed | High | Low | Controls affect ASML/China revenue but strengthen allied technology leverage. |
| CAND-V3-010 | Mixed | High | Low | Taiwan policy alignment increases strategic-security relevance. |
| CAND-V3-011 | Threat | High | Blank | China retaliation increases firm-specific and policy-risk concerns. |
| CAND-V3-012 | Threat | High | Blank | Critical-materials controls raise input and supply-security risk. |
| CAND-V3-013 | Threat | Medium | Blank | Strategic-materials risk extends beyond semiconductors into broader technology supply chains. |
| CAND-V3-015 | Threat | High | Blank | Direct material-export retaliation against the United States. |
| CAND-V3-016 | Opportunity | High | High | Major U.S. semiconductor subsidy and capacity-support package. |
| CAND-V3-019 | Opportunity | High | High | EU industrial-policy framework supports regional semiconductor capacity. |
| CAND-V3-020 | Opportunity | High | High | Taiwan-linked Japan fab opening with state-support context. |
| CAND-V3-022 | Opportunity | High | High | Large China state-backed semiconductor investment fund. |
| CAND-V3-025 | Threat | Medium | Blank | Election outcome may raise cross-strait risk expectations despite being scheduled. |
| CAND-V3-028 | Threat | Medium | Blank | Recognition loss signals diplomatic pressure on Taiwan. |
| CAND-V3-029 | Threat | Medium | Blank | Recognition loss signals diplomatic pressure on Taiwan. |
| CAND-V3-030 | Opportunity | Medium | Low | U.S. law supports Taiwan's diplomatic space, but direct state funding signal is limited. |

## Examples

### Export-Control Escalation

An export-control event should usually be coded `Mixed` when it both increases technology-policy risk and reinforces the strategic value of non-China supply chains. The `strategic_importance_level` should be `High` when controls directly affect advanced chips, semiconductor equipment, foundry access, or AI accelerators.

### State-Support Event

An industrial-policy event should be coded `Opportunity` when public support plausibly improves capacity, resilience, or firm economics. `state_support_signal` should be `High` when the policy includes major subsidies, grants, tax credits, loans, or state-backed investment funds.

### Diplomatic-Recognition Event

A recognition switch away from Taiwan should usually be coded `Threat` because it signals pressure on Taiwan's international space. `strategic_importance_level` should normally be `Medium` unless the recognition event coincides with a direct security or semiconductor policy action.

## Unresolved Cases

- CAND-V3-009: needs event-date resolution before coding.
- CAND-V3-014: likely `Threat` or `Mixed`, but coding depends on whether the event is treated as a formal substitution policy or later public reporting.
- CAND-V3-017: likely `Opportunity`, `High` strategic importance, and `Medium` or `High` state-support signal, but same-day confounding must be resolved before integration.
- Some export-control events may require `Threat` rather than `Mixed` if the target asset universe is China-revenue-heavy rather than Taiwan or allied supply-chain-oriented.

## Implementation Standard

Theory coding should be applied only after the event passes source validation and trading-date mapping. The coding log should record the specific evidence basis for each field so later readers can distinguish observed event facts from interpretive classification.
