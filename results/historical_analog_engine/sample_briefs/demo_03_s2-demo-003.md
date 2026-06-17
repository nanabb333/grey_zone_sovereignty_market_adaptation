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
