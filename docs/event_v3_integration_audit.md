# Event V3 Integration Audit

> Academic Research Notice:
> This audit reviews candidate events for possible Dataset V3 integration. It does not validate, calculate returns for, or insert any event into the master event dataset.

## Scope

Inputs reviewed:

- `data/event_candidates_v3.csv`
- `docs/event_dataset_v3_expansion.md`
- `docs/event_inclusion_protocol.md`

This audit covers candidates marked `Include` or `Review Further`. Candidates marked `Exclude` are omitted from event-level review because they duplicate events already represented in `data/events_v2.csv`.

## Integration Audit Table

| Candidate ID | Status | Inclusion rationale | Expected theoretical relevance | Expected event family | Evidence quality assessment |
| --- | --- | --- | --- | --- | --- |
| CAND-V3-002 | Include | Distinct follow-on tightening of U.S. AI-chip controls after the 2022 BIS action. | Strategic competition; export-control escalation; strategic-importance signal. | `Export_Control` | High: official U.S. rulemaking should be available; needs final-rule date and market-timing check. |
| CAND-V3-003 | Include | Major late-period U.S. semiconductor-control expansion targeting advanced-chip capacity. | Strategic competition; technology containment; supply-chain security. | `Export_Control` | High: official BIS documentation should support date and scope; source packet still needed. |
| CAND-V3-004 | Include | Early anchor event in U.S.-China technology decoupling. | Strategic competition; threat to China-facing technology revenue; substitution pressure. | `Export_Control` | High: official Entity List action and contemporaneous reporting should be available. |
| CAND-V3-005 | Include | Directly affects foreign foundries using U.S. technology, including Taiwan-linked manufacturing exposure. | Strategic importance of foundry chokepoints; extraterritorial control risk. | `Export_Control` | Medium-High: official evidence likely strong; same-day TSMC Arizona announcement requires confounding review. |
| CAND-V3-006 | Include | Restricts China's leading foundry and strengthens the semiconductor-capability constraint narrative. | Strategic competition; China self-sufficiency pressure; equipment bottlenecks. | `Export_Control` | High: official Entity List action should be traceable. |
| CAND-V3-007 | Include | Converts U.S. restrictions into a more credible allied control regime. | Coalition-based technology containment; strategic importance of semiconductor tools. | `Export_Control` | Medium-High: strong news evidence likely; needs precise announcement timing and official corroboration. |
| CAND-V3-008 | Include | Netherlands licensing rules directly affect ASML and advanced semiconductor equipment access. | Allied export controls; lithography chokepoints; China fab-capex constraints. | `Export_Control` | High: government rule and contemporaneous reporting should support inclusion. |
| CAND-V3-010 | Include | Taiwan-specific export-control alignment against Huawei and SMIC. | Taiwan's technology-security role; cross-strait semiconductor restriction channel. | `Export_Control` | Medium: strong if official Taiwan publication is collected; needs date and market-timing verification. |
| CAND-V3-011 | Include | Chinese restriction on Micron gives the dataset a clear retaliation/countermeasure case. | Economic coercion; supply-chain security; U.S.-China retaliation. | `Economic_Coercion` | High: official CAC decision and market reporting should be available. |
| CAND-V3-012 | Include | Critical-materials licensing event with direct semiconductor and defense relevance. | Supply-chain leverage; strategic materials; retaliatory policy channel. | `Critical_Materials_Control` | High: official China Ministry of Commerce notice and broad reporting should be available. |
| CAND-V3-013 | Include | Extends the materials-control mechanism into battery and strategic technology inputs. | Supply-chain security; strategic-materials leverage beyond semiconductors. | `Critical_Materials_Control` | High: official notice and contemporaneous market reporting should be available. |
| CAND-V3-015 | Include | Direct China retaliation after U.S. semiconductor controls, focused on strategic materials. | Escalatory retaliation; supply-chain security; defense and semiconductor input risk. | `Critical_Materials_Control` | High: official notice and contemporaneous reporting should be available. |
| CAND-V3-016 | Include | U.S. CHIPS Act signing is a central semiconductor state-support event. | State support; industrial policy; strategic importance of domestic fab capacity. | `Industrial_Policy` | High: statute signing date and official White House/Congress evidence should be available. |
| CAND-V3-019 | Include | European Chips Act adds allied industrial-policy coverage beyond the United States. | State support; subsidy competition; supply-chain regionalization. | `Industrial_Policy` | High: EU official publication provides a clear source date. |
| CAND-V3-020 | Include | TSMC Kumamoto opening captures Taiwan-linked capacity diversification with Japanese support. | Strategic investment; state support; supply-chain resilience. | `Strategic_Investment` | High: company, government, and contemporaneous reporting should be available. |
| CAND-V3-022 | Include | China's Big Fund III is a large state-backed semiconductor-capacity signal. | State support; import substitution; strategic industrial policy. | `Industrial_Policy` | High: registration and reporting evidence should support inclusion. |
| CAND-V3-025 | Include | Taiwan's presidential election outcome is a major cross-strait political signal. | Political risk; cross-strait expectations; continuity of Taiwan policy. | `Political_Signaling` | High for historical date; weekend trading-date mapping required. |
| CAND-V3-028 | Include | Nauru's recognition switch adds a direct diplomatic-isolation event. | Diplomatic competition; Taiwan international-space pressure. | `Recognition_Diplomacy` | High: official and contemporaneous reporting likely available. |
| CAND-V3-029 | Include | Honduras recognition switch adds another concrete Taiwan diplomatic-loss event. | Diplomatic competition; China influence; Taiwan international-space pressure. | `Recognition_Diplomacy` | High: official and contemporaneous reporting likely available; weekend trading-date mapping required. |
| CAND-V3-030 | Include | U.S. TAIPEI Act is a policy response to diplomatic-recognition pressure on Taiwan. | Diplomatic support; U.S.-Taiwan political backing; recognition competition. | `Recognition_Diplomacy` | High: statutory evidence available; market relevance may be weaker than semiconductor controls. |
| CAND-V3-009 | Review Further | Relevant ASML control case, but event date may refer to rule effectiveness, license revocation, or disclosure. | Allied export-control escalation; semiconductor-equipment chokepoint. | `Export_Control` | Medium-Low until date reconciliation is complete. |
| CAND-V3-014 | Review Further | Relevant China substitution case, but market-relevant disclosure date is uncertain. | Technology self-sufficiency; China countermeasure; supplier displacement. | `Supply_Chain_Security` | Medium-Low until official policy date and public-disclosure date are reconciled. |
| CAND-V3-017 | Review Further | Strategically important TSMC U.S. capacity announcement, but same-day Huawei FDPR creates event-window confounding. | Strategic investment; supply-chain resilience; Taiwan capacity diversification. | `Strategic_Investment` | Medium: event is real and relevant, but causal interpretation is hard unless isolated carefully. |

## Strongest Additions

The strongest additions are the candidates with clean dates, official-source availability, and direct investor interpretation channels:

- CAND-V3-002: U.S. 2023 AI-chip export-control tightening.
- CAND-V3-003: U.S. 2024 semiconductor-control expansion.
- CAND-V3-004: Huawei Entity List action.
- CAND-V3-006: SMIC Entity List action.
- CAND-V3-011: China restriction on Micron.
- CAND-V3-012: China gallium and germanium controls.
- CAND-V3-015: China strategic-materials restrictions against the United States.
- CAND-V3-016: U.S. CHIPS and Science Act signing.
- CAND-V3-020: TSMC Kumamoto opening.
- CAND-V3-022: China Big Fund III.

## Weakest Additions

Weakest does not mean irrelevant. It means weaker for event-study integration without additional evidence work.

- CAND-V3-009: date ambiguity around ASML shipment restrictions.
- CAND-V3-014: market-relevant disclosure date may differ from the underlying policy action.
- CAND-V3-017: same-day confounding with Huawei FDPR makes event-window interpretation difficult.
- CAND-V3-030: high political relevance but potentially weaker immediate market effect than semiconductor controls or military events.

## Remaining Ambiguities

- Some candidates require exact market-timing classification: before market open, during trading, after market close, weekend, or holiday.
- Some export-control cases may have multiple relevant dates: announcement, rule publication, effective date, license decision, or company disclosure.
- Diplomatic-recognition events are substantively important but may need careful explanation if short-window market reactions are weak.
- The expansion improves policy and technology coverage more than military coverage because major military events are already present in V2.
