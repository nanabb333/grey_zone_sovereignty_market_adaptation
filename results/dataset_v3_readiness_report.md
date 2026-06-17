# Dataset V3 Readiness Report

> Academic Research Notice:
> This report assesses readiness for a future dataset expansion. It does not insert candidate events into the validated event dataset and does not report new event-study results.

## Current Dataset Size

The conservative validated baseline is `data/events_v2.csv`, which contains 18 events. This file is also the baseline used by the existing V2 summary and theory-variable coverage documents.

The repository also contains `data/events/events_v3.csv`, which contains 25 rows. Because the current sprint is a review-pipeline sprint, this report treats `data/events_v2.csv` as the validated baseline and does not modify either dataset file.

## Candidate Review Outcome

| Inclusion status | Count |
| --- | ---: |
| Include | 20 |
| Review Further | 3 |
| Exclude | 7 |
| Total reviewed | 30 |

## Projected Dataset Size

| Scenario | Event count |
| --- | ---: |
| Current validated baseline | 18 |
| Baseline plus Include candidates | 38 |
| Baseline plus Include and Review Further candidates | 41 |

The most defensible near-term projection is 38 events, pending source collection, trading-date mapping, and final coding.

## Projected Category Distribution

Projected distribution uses the 18-event V2 baseline plus the 20 Include candidates.

| Category | Current V2 count | New Include candidates | Projected V3 count |
| --- | ---: | ---: | ---: |
| Military exercise and military demonstration | 8 | 0 | 8 |
| Export controls and technology restrictions | 1 | 11 | 12 |
| Strategic investment, state support, and industrial policy | 3 | 4 | 7 |
| Diplomatic, political, legal, and recognition signaling | 5 | 4 | 9 |
| Economic coercion and supply-chain countermeasures | 1 | 1 | 2 |
| Total | 18 | 20 | 38 |

## Theory-Variable Coverage Estimate

The expansion would substantially improve coverage of the project's strategic-importance and state-support mechanisms.

| Theory variable | Current coverage | Projected effect |
| --- | --- | --- |
| `strategic_importance_level` | 4 coded events in V2 | Likely expands through export-control, chip-tool, state-support, and strategic-investment candidates. |
| `state_support_signal` | 4 coded events in V2 | Likely expands through CHIPS Act, European Chips Act, TSMC Japan, and China Big Fund III. |
| `interpretation_type` | 18 coded events in V2 | Would need full recoding for all new candidates; expected mix of Threat, Mixed, Opportunity, and Adaptation. |
| `event_family` | Military-heavy in V2 | Becomes more balanced through export-control, recognition-diplomacy, industrial-policy, and critical-materials families. |
| `event_repetition_level` | Strong coverage for repeated military events | Would add repeated export-control and industrial-policy sequences. |

## Strongest New Additions

The strongest candidates are events with clean dates, clear actors, and obvious investor-interpretation channels:

- CAND-V3-002: 2023-10-17 U.S. AI-chip export-control tightening.
- CAND-V3-003: 2024-12-02 U.S. semiconductor-control expansion.
- CAND-V3-004: 2019-05-15 Huawei Entity List action.
- CAND-V3-006: 2020-12-18 SMIC Entity List action.
- CAND-V3-007: 2023-01-27 U.S.-Japan-Netherlands chip-tool control alignment.
- CAND-V3-011: 2023-05-21 China Micron restriction.
- CAND-V3-012: 2023-07-03 China gallium and germanium export controls.
- CAND-V3-015: 2024-12-03 China strategic-materials export restrictions against the United States.
- CAND-V3-016: 2022-08-09 U.S. CHIPS and Science Act signing.
- CAND-V3-022: 2024-05-24 China Big Fund III.

## Remaining Gaps

- Source package still needed: each Include candidate needs official-source and contemporaneous-news evidence before validation.
- Trading-calendar alignment still needed: weekend and after-hours events require event-trading-date mapping.
- Confounding review still needed: May 15, 2020 is especially sensitive because Huawei FDPR and TSMC Arizona occurred on the same date.
- Military event expansion is limited: the shortlist adds little new validated military coverage because major military events are already present in V2.
- 2018 coverage remains thin: the expansion improves 2019-2025 coverage but still lacks strong 2018 events after duplicate and relevance screening.
- Diplomatic-recognition events need careful interpretation: recognition switches may be politically important but may have weaker immediate market effects than semiconductor controls or military exercises.

## Readiness Assessment

Dataset V3 is ready for a validation sprint, not for automatic integration. The candidate pipeline now separates event discovery from event insertion, identifies the 20 strongest additions, preserves three cases for further review, and excludes seven duplicates already represented in V2.
