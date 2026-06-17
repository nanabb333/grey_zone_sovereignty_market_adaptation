# Historical Analog Retrieval Workflow

## Workflow Summary

The Sprint 2 retrieval workflow converts an analyst question into a ranked historical analog brief.

```text
Question
  -> Scenario Mapping
  -> Feature Normalization
  -> Candidate Scoring
  -> Top Analog Selection
  -> Evidence Assembly
  -> Pathway Extraction
  -> Analyst Brief
```

## Step 1: Question Mapping

The engine uses explicit keyword rules to map a question into a scenario family.

Example:

```text
"Joint Sword exercise" -> Military Exercise
```

The mapped scenario also receives deterministic actors, targets, severity score, and surprise score. These fields are visible in the output as the mapping rationale.

## Step 2: Feature Normalization

Historical events are normalized from `data/events_v3.csv`.

Normalization includes:

- taxonomy family mapping
- actor inference from linked news and event text
- target inference from geography, sector, and event text
- numeric surprise scoring
- deterministic severity scoring
- evidence coverage scoring

Original event fields are preserved and shown in the evidence section.

## Step 3: Candidate Scoring

Each historical event receives a deterministic score from 0 to 100.

The score uses:

- event-family match
- actor overlap
- target overlap
- severity proximity
- surprise proximity
- temporal-context fit
- evidence coverage

The scoring system is retrieval logic only. It is not a probability, prediction, or market estimate.

## Step 4: Analog Selection

The prototype keeps events with a score of at least 40 and returns the top five by:

1. total similarity score
2. event-family score
3. evidence coverage
4. event date

Each result receives a confidence label:

| Score Range | Label |
|---|---|
| 80-100 | Strong analog |
| 60-79 | Useful analog |
| 40-59 | Weak analog requiring analyst review |
| Below 40 | Do not show by default |

## Step 5: Evidence Assembly

For each analog, the prototype attaches:

- event source URL
- source packet path when available
- surprise rationale
- linked news evidence
- historical CAR context when available

Historical CAR context is explicitly labeled as descriptive context only.

## Step 6: Pathway Extraction

The pathway extractor reports observed patterns from the validated historical sample:

- later same-family records
- near-term subsequent coded events
- repetition-level coding
- whether historical CAR context exists

The extractor does not infer future pathways.

## Step 7: Analyst Brief Generation

The final brief follows the required section order:

1. Question
2. Historical Analogs
3. Similarity Explanation
4. Evidence Base
5. Observed Historical Pathways
6. Analyst Notes

The brief is intentionally transparent and reviewable. It prioritizes analyst experience over model complexity.
