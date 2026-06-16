# Scenario Similarity Results

Scenario comparison uses keyword overlap, event-family match, actor match, geography match, and linked news evidence count to retrieve similar historical coded events.

The layer supports historical similarity analysis, context retrieval, and scenario comparison. It does not estimate future market outcomes.

## S001: large-scale military exercises near Taiwan

- Scenario event family: `Military_Exercise`
- Interpretation: Use these matches as historical context for analyst review. Similarity scores are transparent rule-based retrieval aids, not future-outcome estimates.

| Rank | Historical Event | Date | Event Family | Similarity Score | Linked News |
|---:|---|---|---|---:|---:|
| 1 | Joint Sword 2023 | 2023-04-08 | Military_Exercise | 70 | 1 |
| 2 | Joint Sword-2024B | 2024-10-14 | Military_Exercise | 62 | 1 |
| 3 | Joint Sword-2024A | 2024-05-23 | Military_Exercise | 62 | 1 |

## S002: new semiconductor export control restrictions

- Scenario event family: `Export_Control`
- Interpretation: Use these matches as historical context for analyst review. Similarity scores are transparent rule-based retrieval aids, not future-outcome estimates.

| Rank | Historical Event | Date | Event Family | Similarity Score | Linked News |
|---:|---|---|---|---:|---:|
| 1 | BIS Advanced Semiconductor Export Controls | 2022-10-07 | Export_Control | 75 | 1 |
| 2 | TSMC US$165B U.S. Expansion | 2025-03-04 | Strategic_Investment | 21 | 1 |
| 3 | TSMC CHIPS Act Preliminary Terms | 2024-04-08 | Strategic_Investment | 21 | 1 |

## S003: high-level diplomatic visit involving Taiwan

- Scenario event family: `Diplomatic_Shock`
- Interpretation: Use these matches as historical context for analyst review. Similarity scores are transparent rule-based retrieval aids, not future-outcome estimates.

| Rank | Historical Event | Date | Event Family | Similarity Score | Linked News |
|---:|---|---|---|---:|---:|
| 1 | Pelosi Visit | 2022-08-02 | Diplomatic_Shock | 75 | 2 |
| 2 | China Warns Against Pelosi Taiwan Visit | 2022-07-19 | Diplomatic_Shock | 49 | 0 |
| 3 | Lai U.S. Transit | 2023-08-12 | Diplomatic_Shock | 41 | 0 |

## Use Limits

- Historical similarity and context retrieval only.
- Scores are rule-based and require analyst review.
- Historical CAR patterns should not be treated as future-outcome estimates.
- News evidence rows may include placeholder source metadata pending verification.
