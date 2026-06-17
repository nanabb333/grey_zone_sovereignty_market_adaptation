# Analyst Brief: New Semiconductor Export Controls

## Question

What happens if new semiconductor export controls are announced?

Mapped scenario family: `Export Control`

Mapping rationale: The question references semiconductor export controls, which maps to the Export Control family.

## Historical Analogs

| Rank | Event ID | Historical Event | Date | Family | Score | Confidence |
|---:|---|---|---|---|---:|---|
| 1 | E005 | BIS Advanced Semiconductor Export Controls | 2022-10-07 | Export Control | 93.50 | Strong analog |
| 2 | E024 | AI Chip Export Control Expansion | 2023-10-17 | Export Control | 91.50 | Strong analog |
| 3 | E021 | SMIC Added to U.S. Entity List | 2020-12-18 | Export Control | 91.50 | Strong analog |
| 4 | E020 | Huawei Foreign-Direct-Product Rule | 2020-05-15 | Export Control | 82.00 | Strong analog |
| 5 | E019 | Huawei Added to U.S. Entity List | 2019-05-15 | Export Control | 82.00 | Strong analog |

## Similarity Explanation

### 1. E005 - BIS Advanced Semiconductor Export Controls

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Export Control | Export Control | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | United States; U.S. Commerce Department | prc; united states | 20.00 | Alias-aware actor overlap. |
| Target Overlap | China; Advanced semiconductors; Global semiconductor supply chain | prc; semiconductor; united states | 15.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 4 | 5 | 7.50 | Distance between deterministic severity scores. |
| Surprise Proximity | 3 | 3 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | export; control; semiconductor; chip; entity; china | BIS Advanced Semiconductor Export Controls | 1.00 | General historical context. |
| Evidence Coverage | linked evidence and source packet coverage | 1 linked news item(s) | 10.00 | Source packet and linked news evidence available. |

### 2. E024 - AI Chip Export Control Expansion

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Export Control | Export Control | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | United States; U.S. Commerce Department | prc; united states | 20.00 | Alias-aware actor overlap. |
| Target Overlap | China; Advanced semiconductors; Global semiconductor supply chain | prc; semiconductor | 15.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 4 | 5 | 7.50 | Distance between deterministic severity scores. |
| Surprise Proximity | 3 | 3 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | export; control; semiconductor; chip; entity; china | AI Chip Export Control Expansion | 3.00 | Repeated historical pattern. |
| Evidence Coverage | linked evidence and source packet coverage | 0 linked news item(s) | 6.00 | Source packet and event source available. |

### 3. E021 - SMIC Added to U.S. Entity List

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Export Control | Export Control | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | United States; U.S. Commerce Department | prc; united states | 20.00 | Alias-aware actor overlap. |
| Target Overlap | China; Advanced semiconductors; Global semiconductor supply chain | prc; semiconductor; smic | 15.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 4 | 5 | 7.50 | Distance between deterministic severity scores. |
| Surprise Proximity | 3 | 3 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | export; control; semiconductor; chip; entity; china | SMIC Added to U.S. Entity List | 3.00 | Repeated historical pattern. |
| Evidence Coverage | linked evidence and source packet coverage | 0 linked news item(s) | 6.00 | Source packet and event source available. |

### 4. E020 - Huawei Foreign-Direct-Product Rule

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Export Control | Export Control | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | United States; U.S. Commerce Department | united states | 20.00 | Alias-aware actor overlap. |
| Target Overlap | China; Advanced semiconductors; Global semiconductor supply chain | huawei; semiconductor | 7.50 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 4 | 5 | 7.50 | Distance between deterministic severity scores. |
| Surprise Proximity | 3 | 3 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | export; control; semiconductor; chip; entity; china | Huawei Foreign-Direct-Product Rule | 1.00 | General historical context. |
| Evidence Coverage | linked evidence and source packet coverage | 0 linked news item(s) | 6.00 | Source packet and event source available. |

### 5. E019 - Huawei Added to U.S. Entity List

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Export Control | Export Control | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | United States; U.S. Commerce Department | united states | 20.00 | Alias-aware actor overlap. |
| Target Overlap | China; Advanced semiconductors; Global semiconductor supply chain | huawei; semiconductor | 7.50 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 4 | 5 | 7.50 | Distance between deterministic severity scores. |
| Surprise Proximity | 3 | 3 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | export; control; semiconductor; chip; entity; china | Huawei Added to U.S. Entity List | 1.00 | General historical context. |
| Evidence Coverage | linked evidence and source packet coverage | 0 linked news item(s) | 6.00 | Source packet and event source available. |

## Evidence Base

### E005 - BIS Advanced Semiconductor Export Controls

- Event source: https://www.bis.gov/press-release/commerce-implements-new-export-controls-advanced-computing-semiconductor-manufacturing-items-peoples
- Source packet: `data/source_packets/2022-10-07_semiconductor_export_controls.md`
- Surprise rationale: U.S.-China technology controls were foreseeable, but the scope of the advanced-computing and semiconductor restrictions contained important new policy detail.
- Historical CAR context: tsmc_car_7=4.4497, tsmc_car_3=3.08, twse_car_7=-0.7568, twse_car_3=2.3331. Historical context only.
- N003: U.S. BIS placeholder - United States announces advanced semiconductor export-control measures (https://www.bis.doc.gov/)

### E024 - AI Chip Export Control Expansion

- Event source: https://www.axios.com/2023/10/17/biden-export-restrictions-ai-chips-china
- Source packet: `data/source_packets/2023-10-17_ai_chip_export_control_expansion.md`
- Surprise rationale: The 2023 update was a follow-on to the 2022 controls, but the detailed tightening and loophole closure provided new policy information.
- Historical CAR context: tsmc_car_7=6.7548, tsmc_car_3=7.4752, twse_car_7=3.8509, twse_car_3=3.0999. Historical context only.
- Linked news evidence: none in current evidence database.

### E021 - SMIC Added to U.S. Entity List

- Event source: https://2017-2021.commerce.gov/news/press-releases/2020/12/commerce-department-adds-dozens-chinese-companies-entity-list.html
- Source packet: `data/source_packets/2020-12-18_smic_entity_list.md`
- Surprise rationale: The action was a clear semiconductor technology-control event, though investors had already seen a series of U.S.-China technology restrictions.
- Linked news evidence: none in current evidence database.

### E020 - Huawei Foreign-Direct-Product Rule

- Event source: https://www.bis.doc.gov/index.php/documents/about-bis/newsroom/press-releases/2569-commerce-addresses-huawei-s-efforts-to-undermine-entity-list-restricts-products-designed-and-produced-with-u-s-technologies/file
- Source packet: `data/source_packets/2020-05-15_huawei_fdp_rule.md`
- Surprise rationale: The rule materially extended U.S. export-control reach; same-day TSMC Arizona announcement creates confounding risk for event-window interpretation.
- Linked news evidence: none in current evidence database.

### E019 - Huawei Added to U.S. Entity List

- Event source: https://www.federalregister.gov/documents/2019/05/21/2019-10616/addition-of-entities-to-the-entity-list
- Source packet: `data/source_packets/2019-05-15_huawei_entity_list.md`
- Surprise rationale: The Entity List action was a major policy escalation; the Federal Register effective date was 2019-05-16, but the public announcement date is coded as 2019-05-15.
- Linked news evidence: none in current evidence database.

## Observed Historical Pathways

### E005 - BIS Advanced Semiconductor Export Controls
- Later same-family records in the dataset include AI Chip Export Control Expansion (2023-10-17).
- Near-term subsequent coded events include TSMC Arizona US$40B Expansion (2022-12-06).
- The event is coded with repetition level 1, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

### E024 - AI Chip Export Control Expansion
- The event is coded with repetition level 4, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

### E021 - SMIC Added to U.S. Entity List
- Later same-family records in the dataset include BIS Advanced Semiconductor Export Controls (2022-10-07), AI Chip Export Control Expansion (2023-10-17).
- The event is coded with repetition level 3, which indicates whether the pattern was novel or recurring in the historical sample.

### E020 - Huawei Foreign-Direct-Product Rule
- Later same-family records in the dataset include SMIC Added to U.S. Entity List (2020-12-18), BIS Advanced Semiconductor Export Controls (2022-10-07), AI Chip Export Control Expansion (2023-10-17).
- Near-term subsequent coded events include SMIC Added to U.S. Entity List (2020-12-18).
- The event is coded with repetition level 2, which indicates whether the pattern was novel or recurring in the historical sample.

### E019 - Huawei Added to U.S. Entity List
- Later same-family records in the dataset include Huawei Foreign-Direct-Product Rule (2020-05-15), SMIC Added to U.S. Entity List (2020-12-18), BIS Advanced Semiconductor Export Controls (2022-10-07).
- The event is coded with repetition level 1, which indicates whether the pattern was novel or recurring in the historical sample.

## Analyst Notes

- Historical analog retrieval only. This output does not forecast future outcomes, estimate future returns, or provide investment recommendations.
- Similarity scores are deterministic retrieval aids and require analyst review.
- Evidence rows may contain placeholder source metadata that should be verified before publication.
- Historical CAR fields, when shown, describe prior coded events and are not estimates for the question scenario.
