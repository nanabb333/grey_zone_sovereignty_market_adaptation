# Historical Analog Engine Demo Briefs

Historical analog retrieval only. This output does not forecast future outcomes, estimate future returns, or provide investment recommendations.

---

# Analyst Brief: Renewed Joint Sword-Style Military Exercise

## Question

What happens if China launches another Joint Sword exercise?

Mapped scenario family: `Military Exercise`

Mapping rationale: The question references Joint Sword and launch of another exercise, which maps to the Military Exercise family.

## Historical Analogs

| Rank | Event ID | Historical Event | Date | Family | Score | Confidence |
|---:|---|---|---|---|---:|---|
| 1 | E013 | Joint Sword-2024A | 2024-05-23 | Military Exercise | 97.00 | Strong analog |
| 2 | E007 | Joint Sword 2023 | 2023-04-08 | Military Exercise | 97.00 | Strong analog |
| 3 | E004 | PLA Military Exercises After Pelosi Visit | 2022-08-04 | Military Exercise | 93.50 | Strong analog |
| 4 | E009 | PLA Drills After Lai U.S. Transit | 2023-08-19 | Military Exercise | 93.00 | Strong analog |
| 5 | E015 | Joint Sword-2024B | 2024-10-14 | Military Exercise | 89.50 | Strong analog |

## Similarity Explanation

### 1. E013 - Joint Sword-2024A

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Military Exercise | Military Exercise | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | PRC; PLA; China | pla; prc; taiwan | 20.00 | Alias-aware actor overlap. |
| Target Overlap | Taiwan; Taiwan Strait | taiwan; taiwan strait | 15.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 4 | 4 | 10.00 | Distance between deterministic severity scores. |
| Surprise Proximity | 3 | 3 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | joint sword; military; exercise; drill; taiwan | Joint Sword-2024A | 5.00 | Named Joint Sword pattern match. |
| Evidence Coverage | linked evidence and source packet coverage | 1 linked news item(s) | 7.00 | Linked news evidence available. |

### 2. E007 - Joint Sword 2023

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Military Exercise | Military Exercise | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | PRC; PLA; China | pla; prc; taiwan | 20.00 | Alias-aware actor overlap. |
| Target Overlap | Taiwan; Taiwan Strait | taiwan; taiwan strait | 15.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 4 | 4 | 10.00 | Distance between deterministic severity scores. |
| Surprise Proximity | 3 | 3 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | joint sword; military; exercise; drill; taiwan | Joint Sword 2023 | 5.00 | Named Joint Sword pattern match. |
| Evidence Coverage | linked evidence and source packet coverage | 1 linked news item(s) | 7.00 | Linked news evidence available. |

### 3. E004 - PLA Military Exercises After Pelosi Visit

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Military Exercise | Military Exercise | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | PRC; PLA; China | pla; prc; taiwan | 20.00 | Alias-aware actor overlap. |
| Target Overlap | Taiwan; Taiwan Strait | prc; taiwan; taiwan strait | 15.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 4 | 5 | 7.50 | Distance between deterministic severity scores. |
| Surprise Proximity | 3 | 3 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | joint sword; military; exercise; drill; taiwan | PLA Military Exercises After Pelosi Visit | 1.00 | General historical context. |
| Evidence Coverage | linked evidence and source packet coverage | 1 linked news item(s) | 10.00 | Source packet and linked news evidence available. |

### 4. E009 - PLA Drills After Lai U.S. Transit

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Military Exercise | Military Exercise | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | PRC; PLA; China | pla; prc; taiwan; united states | 20.00 | Alias-aware actor overlap. |
| Target Overlap | Taiwan; Taiwan Strait | prc; taiwan; taiwan strait | 15.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 4 | 4 | 10.00 | Distance between deterministic severity scores. |
| Surprise Proximity | 3 | 3 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | joint sword; military; exercise; drill; taiwan | PLA Drills After Lai U.S. Transit | 1.00 | General historical context. |
| Evidence Coverage | linked evidence and source packet coverage | 1 linked news item(s) | 7.00 | Linked news evidence available. |

### 5. E015 - Joint Sword-2024B

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Military Exercise | Military Exercise | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | PRC; PLA; China | pla; prc; taiwan | 20.00 | Alias-aware actor overlap. |
| Target Overlap | Taiwan; Taiwan Strait | taiwan; taiwan strait | 15.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 4 | 3 | 7.50 | Distance between deterministic severity scores. |
| Surprise Proximity | 3 | 1 | 5.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | joint sword; military; exercise; drill; taiwan | Joint Sword-2024B | 5.00 | Named Joint Sword pattern match. |
| Evidence Coverage | linked evidence and source packet coverage | 1 linked news item(s) | 7.00 | Linked news evidence available. |

## Evidence Base

### E013 - Joint Sword-2024A

- Event source: https://www.mnd.gov.tw/en/Publication/83035
- Surprise rationale: A PRC military response after Lai's inauguration was widely plausible, but the exercise timing and operational details still introduced information.
- Historical CAR context: tsmc_car_7=-0.4712, tsmc_car_3=-1.4771, twse_car_7=-0.9806, twse_car_3=-0.6509. Historical context only.
- N009: Reuters placeholder - China conducts Joint Sword-2024A exercises around Taiwan (https://www.reuters.com/)

### E007 - Joint Sword 2023

- Event source: https://chinapower.csis.org/tracking-chinas-april-2023-military-exercises-around-taiwan/
- Surprise rationale: A PRC response to the Tsai-McCarthy meeting was plausible, but the timing and scale of Joint Sword 2023 remained uncertain before the exercises.
- Historical CAR context: tsmc_car_7=-1.0286, tsmc_car_3=-1.9749, twse_car_7=-1.2837, twse_car_3=-1.1468. Historical context only.
- N005: Reuters placeholder - PLA launches Joint Sword exercises near Taiwan (https://www.reuters.com/)

### E004 - PLA Military Exercises After Pelosi Visit

- Event source: https://www.investing.com/news/stock-market-news/suspected-drones-over-taiwan-cyber-attacks-after-pelosi-visit-2862740
- Source packet: `data/source_packets/2022-08-04_china_live_fire_exercises_taiwan.md`
- Surprise rationale: A military response was expected after the visit, but the scale and operational intensity of the exercises still introduced new information.
- Historical CAR context: tsmc_car_7=3.3773, tsmc_car_3=8.0097, twse_car_7=0.6505, twse_car_3=3.2349. Historical context only.
- N002: Associated Press placeholder - China begins military drills around Taiwan after high-profile visit (https://apnews.com/)

### E009 - PLA Drills After Lai U.S. Transit

- Event source: https://www.aljazeera.com/news/2023/8/19/china-launches-military-drills-in-stern-warning-to-taiwan-after-us-visit
- Surprise rationale: A military response to Lai's U.S. transit was foreseeable, but the specific timing and operational form still mattered for market interpretation.
- Historical CAR context: tsmc_car_7=-2.2359, tsmc_car_3=3.9235, twse_car_7=-3.3276, twse_car_3=1.0242. Historical context only.
- N006: Taiwan MND placeholder - Taiwan reports PLA aircraft and vessels after Lai U.S. transit (https://www.mnd.gov.tw/)

### E015 - Joint Sword-2024B

- Event source: https://chinapower.csis.org/china-taiwan-joint-sword-2024b-coast-guard/
- Surprise rationale: The event fit an increasingly recognizable Joint Sword pattern, making the category relatively expected even if details remained uncertain.
- Historical CAR context: tsmc_car_7=5.3488, tsmc_car_3=1.4217, twse_car_7=2.2491, twse_car_3=0.5034. Historical context only.
- N011: Reuters placeholder - China announces Joint Sword-2024B drills after Taiwan National Day speech (https://www.reuters.com/)

## Observed Historical Pathways

### E013 - Joint Sword-2024A
- Later same-family records in the dataset include Joint Sword-2024B (2024-10-14), PLA Joint Combat Readiness Patrols Around Taiwan (2025-01-22), Strait Thunder-2025A (2025-04-01).
- Near-term subsequent coded events include China Big Fund III Established (2024-05-24), PRC Judicial Guidelines on Taiwan Independence (2024-06-21).
- The event is coded with repetition level 3, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

### E007 - Joint Sword 2023
- Later same-family records in the dataset include PLA Drills After Lai U.S. Transit (2023-08-19), China Sends Aircraft and Vessels After U.S. Arms Sale (2023-08-26), Joint Sword-2024A (2024-05-23).
- Near-term subsequent coded events include Lai U.S. Transit (2023-08-12), PLA Drills After Lai U.S. Transit (2023-08-19).
- The event is coded with repetition level 2, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

### E004 - PLA Military Exercises After Pelosi Visit
- Later same-family records in the dataset include Joint Sword 2023 (2023-04-08), PLA Drills After Lai U.S. Transit (2023-08-19), China Sends Aircraft and Vessels After U.S. Arms Sale (2023-08-26).
- Near-term subsequent coded events include CHIPS and Science Act Signed (2022-08-09), BIS Advanced Semiconductor Export Controls (2022-10-07).
- The event is coded with repetition level 1, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

### E009 - PLA Drills After Lai U.S. Transit
- Later same-family records in the dataset include China Sends Aircraft and Vessels After U.S. Arms Sale (2023-08-26), Joint Sword-2024A (2024-05-23), Joint Sword-2024B (2024-10-14).
- Near-term subsequent coded events include China Sends Aircraft and Vessels After U.S. Arms Sale (2023-08-26), AI Chip Export Control Expansion (2023-10-17).
- The event is coded with repetition level 2, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

### E015 - Joint Sword-2024B
- Later same-family records in the dataset include PLA Joint Combat Readiness Patrols Around Taiwan (2025-01-22), Strait Thunder-2025A (2025-04-01).
- The event is coded with repetition level 4, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

## Analyst Notes

- Historical analog retrieval only. This output does not forecast future outcomes, estimate future returns, or provide investment recommendations.
- Similarity scores are deterministic retrieval aids and require analyst review.
- Evidence rows may contain placeholder source metadata that should be verified before publication.
- Historical CAR fields, when shown, describe prior coded events and are not estimates for the question scenario.

---

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

---

# Analyst Brief: Major Taiwan Election or Leadership Transition

## Question

What happens after a major Taiwan election?

Mapped scenario family: `Election`

Mapping rationale: The question references a major Taiwan election, which maps to the Election family and related political-signaling records.

## Historical Analogs

| Rank | Event ID | Historical Event | Date | Family | Score | Confidence |
|---:|---|---|---|---|---:|---|
| 1 | E012 | Lai Ching-te Inauguration | 2024-05-20 | Election | 81.50 | Strong analog |
| 2 | E014 | PRC Judicial Guidelines on Taiwan Independence | 2024-06-21 | Diplomatic Shock | 74.00 | Useful analog |
| 3 | E002 | Pelosi Visit | 2022-08-02 | Diplomatic Shock | 72.00 | Useful analog |
| 4 | E001 | China Warns Against Pelosi Taiwan Visit | 2022-07-19 | Diplomatic Shock | 72.00 | Useful analog |
| 5 | E008 | Lai U.S. Transit | 2023-08-12 | Diplomatic Shock | 69.50 | Useful analog |

## Similarity Explanation

### 1. E012 - Lai Ching-te Inauguration

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Election | Election | 30.00 | Exact taxonomy-family match. |
| Actor Overlap | Taiwan | prc; taiwan | 20.00 | Alias-aware actor overlap. |
| Target Overlap | Taiwan; Taiwan Strait; PRC | taiwan | 5.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 3 | 2 | 7.50 | Distance between deterministic severity scores. |
| Surprise Proximity | 1 | 1 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | election; inauguration; taiwan; president; leadership | Lai Ching-te Inauguration | 4.00 | Election-adjacent political sequence. |
| Evidence Coverage | linked evidence and source packet coverage | 0 linked news item(s) | 5.00 | Event source URL available. |

### 2. E014 - PRC Judicial Guidelines on Taiwan Independence

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Election | Diplomatic Shock | 18.00 | Related taxonomy family under Sprint 2 mapping rules. |
| Actor Overlap | Taiwan | prc; taiwan | 20.00 | Alias-aware actor overlap. |
| Target Overlap | Taiwan; Taiwan Strait; PRC | prc; taiwan | 10.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 3 | 3 | 10.00 | Distance between deterministic severity scores. |
| Surprise Proximity | 1 | 3 | 5.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | election; inauguration; taiwan; president; leadership | PRC Judicial Guidelines on Taiwan Independence | 4.00 | Election-adjacent political sequence. |
| Evidence Coverage | linked evidence and source packet coverage | 1 linked news item(s) | 7.00 | Linked news evidence available. |

### 3. E002 - Pelosi Visit

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Election | Diplomatic Shock | 18.00 | Related taxonomy family under Sprint 2 mapping rules. |
| Actor Overlap | Taiwan | prc; taiwan; united states | 20.00 | Alias-aware actor overlap. |
| Target Overlap | Taiwan; Taiwan Strait; PRC | taiwan; taiwan strait | 10.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 3 | 3 | 10.00 | Distance between deterministic severity scores. |
| Surprise Proximity | 1 | 5 | 0.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | election; inauguration; taiwan; president; leadership | Pelosi Visit | 4.00 | Election-adjacent political sequence. |
| Evidence Coverage | linked evidence and source packet coverage | 1 linked news item(s) | 10.00 | Source packet and linked news evidence available. |

### 4. E001 - China Warns Against Pelosi Taiwan Visit

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Election | Diplomatic Shock | 18.00 | Related taxonomy family under Sprint 2 mapping rules. |
| Actor Overlap | Taiwan | prc; taiwan | 20.00 | Alias-aware actor overlap. |
| Target Overlap | Taiwan; Taiwan Strait; PRC | prc; taiwan | 10.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 3 | 3 | 10.00 | Distance between deterministic severity scores. |
| Surprise Proximity | 1 | 3 | 5.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | election; inauguration; taiwan; president; leadership | China Warns Against Pelosi Taiwan Visit | 4.00 | Election-adjacent political sequence. |
| Evidence Coverage | linked evidence and source packet coverage | 0 linked news item(s) | 5.00 | Event source URL available. |

### 5. E008 - Lai U.S. Transit

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | Election | Diplomatic Shock | 18.00 | Related taxonomy family under Sprint 2 mapping rules. |
| Actor Overlap | Taiwan | prc; taiwan; united states | 20.00 | Alias-aware actor overlap. |
| Target Overlap | Taiwan; Taiwan Strait; PRC | taiwan | 5.00 | Alias-aware target, geography, and sector overlap. |
| Severity Proximity | 3 | 2 | 7.50 | Distance between deterministic severity scores. |
| Surprise Proximity | 1 | 1 | 10.00 | Distance between deterministic surprise scores. |
| Temporal Context Fit | election; inauguration; taiwan; president; leadership | Lai U.S. Transit | 4.00 | Election-adjacent political sequence. |
| Evidence Coverage | linked evidence and source packet coverage | 0 linked news item(s) | 5.00 | Event source URL available. |

## Evidence Base

### E012 - Lai Ching-te Inauguration

- Event source: https://chinapower.csis.org/china-respond-inauguration-taiwan-william-lai-joint-sword-2024a-military-exercise/
- Surprise rationale: The inauguration date was scheduled and highly visible, so the event itself was expected even if PRC reactions remained uncertain.
- Historical CAR context: tsmc_car_7=0.0312, tsmc_car_3=1.8693, twse_car_7=-0.2749, twse_car_3=1.3367. Historical context only.
- Linked news evidence: none in current evidence database.

### E014 - PRC Judicial Guidelines on Taiwan Independence

- Event source: https://english.scio.gov.cn/pressroom/2024-06/21/content_117267501.htm
- Surprise rationale: PRC legal pressure on Taiwan independence was consistent with prior signaling, but the formal judicial guidelines introduced specific legal-political content.
- Historical CAR context: tsmc_car_7=-1.0081, tsmc_car_3=0.6854, twse_car_7=-3.9926, twse_car_3=-2.2721. Historical context only.
- N010: Xinhua or legal-policy placeholder - PRC issues judicial guidelines related to Taiwan independence cases (https://www.gov.cn/)

### E002 - Pelosi Visit

- Event source: https://www.cnbc.com/2022/08/02/china-ratchets-up-military-and-economic-pressure-on-taiwan-as-pelosi-begins-her-visit-.html
- Source packet: `data/source_packets/2022-08-02_pelosi_taiwan_visit.md`
- Surprise rationale: The visit was discussed in advance, but uncertainty remained over whether it would occur and how Beijing would respond.
- Historical CAR context: tsmc_car_7=1.8572, tsmc_car_3=-0.0834, twse_car_7=-1.8636, twse_car_3=-1.9399. Historical context only.
- N001: Reuters placeholder - Pelosi arrives in Taiwan amid heightened cross-strait warnings (https://www.reuters.com/)

### E001 - China Warns Against Pelosi Taiwan Visit

- Event source: https://www.axios.com/2022/07/19/china-pelosi-taiwan-visit
- Surprise rationale: The possibility of a Pelosi visit was already public, but the warning clarified escalation risk and official PRC signaling before the visit.
- Historical CAR context: tsmc_car_7=-8.6019, tsmc_car_3=-4.5601, twse_car_7=-5.8369, twse_car_3=-2.6162. Historical context only.
- Linked news evidence: none in current evidence database.

### E008 - Lai U.S. Transit

- Event source: https://www.aljazeera.com/news/2023/8/19/china-launches-military-drills-in-stern-warning-to-taiwan-after-us-visit
- Surprise rationale: The transit was scheduled and publicly visible before the event, making the occurrence relatively expected even if follow-on reactions remained uncertain.
- Historical CAR context: tsmc_car_7=-1.4803, tsmc_car_3=1.516, twse_car_7=-0.7369, twse_car_3=1.9057. Historical context only.
- Linked news evidence: none in current evidence database.

## Observed Historical Pathways

### E012 - Lai Ching-te Inauguration
- Near-term subsequent coded events include Joint Sword-2024A (2024-05-23), China Big Fund III Established (2024-05-24).
- The event is coded with repetition level 1, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

### E014 - PRC Judicial Guidelines on Taiwan Independence
- Near-term subsequent coded events include Joint Sword-2024B (2024-10-14).
- The event is coded with repetition level 1, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

### E002 - Pelosi Visit
- Later same-family records in the dataset include Lai U.S. Transit (2023-08-12), PRC Judicial Guidelines on Taiwan Independence (2024-06-21).
- Near-term subsequent coded events include China Trade Restrictions After Pelosi Visit (2022-08-03), PLA Military Exercises After Pelosi Visit (2022-08-04).
- The event is coded with repetition level 1, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

### E001 - China Warns Against Pelosi Taiwan Visit
- Later same-family records in the dataset include Pelosi Visit (2022-08-02), Lai U.S. Transit (2023-08-12), PRC Judicial Guidelines on Taiwan Independence (2024-06-21).
- Near-term subsequent coded events include Pelosi Visit (2022-08-02), China Trade Restrictions After Pelosi Visit (2022-08-03).
- The event is coded with repetition level 1, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

### E008 - Lai U.S. Transit
- Later same-family records in the dataset include PRC Judicial Guidelines on Taiwan Independence (2024-06-21).
- Near-term subsequent coded events include PLA Drills After Lai U.S. Transit (2023-08-19), China Sends Aircraft and Vessels After U.S. Arms Sale (2023-08-26).
- The event is coded with repetition level 2, which indicates whether the pattern was novel or recurring in the historical sample.
- Historical CAR context is available as descriptive event-study evidence only.

## Analyst Notes

- Historical analog retrieval only. This output does not forecast future outcomes, estimate future returns, or provide investment recommendations.
- Similarity scores are deterministic retrieval aids and require analyst review.
- Evidence rows may contain placeholder source metadata that should be verified before publication.
- Historical CAR fields, when shown, describe prior coded events and are not estimates for the question scenario.
