# Scenario Similarity Results

Scenario comparison uses keyword overlap, event-family match, actor match, geography match, and linked news evidence count to retrieve similar historical coded events.

The layer supports historical similarity analysis, context retrieval, and scenario comparison. It does not estimate future market outcomes.

## S001: large-scale military exercises near Taiwan

- Scenario event family: `Military_Exercise`
- Interpretation: Use these matches as historical context for analyst review. Similarity scores are transparent rule-based retrieval aids, not future-market estimates.

| Rank | Historical Event | Date | Event Family | Similarity Score | Linked News | Historical CAR Context |
|---:|---|---|---|---:|---:|---|
| 1 | Joint Sword 2023 | 2023-04-08 | Military_Exercise | 73 | 1 | tsmc_car_7=-1.0286 (historical descriptive market reaction) |
| 2 | Joint Sword-2024A | 2024-05-23 | Military_Exercise | 68 | 1 | tsmc_car_7=-0.4712 (historical descriptive market reaction) |
| 3 | Joint Sword-2024B | 2024-10-14 | Military_Exercise | 66 | 1 | tsmc_car_7=5.3488 (historical descriptive market reaction) |

## S002: new semiconductor export control restrictions

- Scenario event family: `Export_Control`
- Interpretation: Use these matches as historical context for analyst review. Similarity scores are transparent rule-based retrieval aids, not future-market estimates.

| Rank | Historical Event | Date | Event Family | Similarity Score | Linked News | Historical CAR Context |
|---:|---|---|---|---:|---:|---|
| 1 | BIS Advanced Semiconductor Export Controls | 2022-10-07 | Export_Control | 78 | 1 | tsmc_car_7=4.4497 (historical descriptive market reaction) |
| 2 | TSMC US$165B U.S. Expansion | 2025-03-04 | Strategic_Investment | 27 | 1 | tsmc_car_7=-3.0385 (historical descriptive market reaction) |
| 3 | TSMC CHIPS Act Preliminary Terms | 2024-04-08 | Strategic_Investment | 24 | 1 | tsmc_car_7=8.136 (historical descriptive market reaction) |

## S003: high-level diplomatic visit involving Taiwan

- Scenario event family: `Diplomatic_Shock`
- Interpretation: Use these matches as historical context for analyst review. Similarity scores are transparent rule-based retrieval aids, not future-market estimates.

| Rank | Historical Event | Date | Event Family | Similarity Score | Linked News | Historical CAR Context |
|---:|---|---|---|---:|---:|---|
| 1 | Pelosi Visit | 2022-08-02 | Diplomatic_Shock | 80 | 2 | tsmc_car_7=1.8572 (historical descriptive market reaction) |
| 2 | China Warns Against Pelosi Taiwan Visit | 2022-07-19 | Diplomatic_Shock | 52 | 0 | tsmc_car_7=-8.6019 (historical descriptive market reaction) |
| 3 | Lai U.S. Transit | 2023-08-12 | Diplomatic_Shock | 42 | 0 | tsmc_car_7=-1.4803 (historical descriptive market reaction) |

## S004: grey-zone naval and air pressure around Taiwan

- Scenario event family: `Military_Exercise`
- Interpretation: Use these matches as historical context for analyst review. Similarity scores are transparent rule-based retrieval aids, not future-market estimates.

| Rank | Historical Event | Date | Event Family | Similarity Score | Linked News | Historical CAR Context |
|---:|---|---|---|---:|---:|---|
| 1 | PLA Drills After Lai U.S. Transit | 2023-08-19 | Military_Exercise | 54 | 1 | tsmc_car_7=-2.2359 (historical descriptive market reaction) |
| 2 | PLA Joint Combat Readiness Patrols Around Taiwan | 2025-01-22 | Military_Exercise | 53 | 0 | tsmc_car_7=-0.3487 (historical descriptive market reaction) |
| 3 | Joint Sword-2024A | 2024-05-23 | Military_Exercise | 52 | 1 | tsmc_car_7=-0.4712 (historical descriptive market reaction) |

## S005: strategic chip investment or state support announcement

- Scenario event family: `Strategic_Investment`
- Interpretation: Use these matches as historical context for analyst review. Similarity scores are transparent rule-based retrieval aids, not future-market estimates.

| Rank | Historical Event | Date | Event Family | Similarity Score | Linked News | Historical CAR Context |
|---:|---|---|---|---:|---:|---|
| 1 | TSMC CHIPS Act Preliminary Terms | 2024-04-08 | Strategic_Investment | 83 | 1 | tsmc_car_7=8.136 (historical descriptive market reaction) |
| 2 | TSMC Arizona US$40B Expansion | 2022-12-06 | Strategic_Investment | 75 | 1 | tsmc_car_7=0.9649 (historical descriptive market reaction) |
| 3 | TSMC US$165B U.S. Expansion | 2025-03-04 | Strategic_Investment | 70 | 1 | tsmc_car_7=-3.0385 (historical descriptive market reaction) |

## S006: supply-chain disruption risk linked to cross-strait tensions

- Scenario event family: `Economic_Coercion`
- Interpretation: Use these matches as historical context for analyst review. Similarity scores are transparent rule-based retrieval aids, not future-market estimates.

| Rank | Historical Event | Date | Event Family | Similarity Score | Linked News | Historical CAR Context |
|---:|---|---|---|---:|---:|---|
| 1 | TSMC US$165B U.S. Expansion | 2025-03-04 | Strategic_Investment | 30 | 1 | tsmc_car_7=-3.0385 (historical descriptive market reaction) |
| 2 | China Trade Restrictions After Pelosi Visit | 2022-08-03 | Economic_Coercion | 28 | 0 | tsmc_car_7=1.7094 (historical descriptive market reaction) |
| 3 | TSMC CHIPS Act Preliminary Terms | 2024-04-08 | Strategic_Investment | 27 | 1 | tsmc_car_7=8.136 (historical descriptive market reaction) |

## Use Limits

- Historical similarity and context retrieval only.
- Scores are rule-based and require analyst review.
- Historical CAR patterns should not be treated as future-market estimates.
- News evidence rows may include placeholder source metadata pending verification.
