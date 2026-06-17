# Similarity Explainability Framework

## Purpose

The similarity explainability framework makes historical analog retrieval auditable. It translates deterministic scores into analyst-readable explanations of matches and differences.

## Explainability Layers

### 1. Score Composition

Each analog retains the original similarity score components:

- event-family match
- actor overlap
- target overlap
- severity proximity
- surprise proximity
- temporal-context fit
- evidence coverage

The Scenario Comparison Engine reports these components as score composition notes.

### 2. Major Matching Features

The engine identifies dimensions with full alignment.

Examples:

- event family is an exact match
- severity is identical
- surprise score is identical
- actor or target overlap is complete after alias normalization
- evidence profile is strong enough for analyst review

### 3. Major Differences

The engine identifies dimensions with partial or different status.

Examples:

- actor overlap is partial
- target overlap is partial
- event family differs
- severity differs by one or more points
- evidence profile has limited linked evidence

### 4. Closest vs Alternative Explanation

The engine compares the top two analogs and reports the score gap. This helps analysts judge whether the closest match is clearly dominant or whether the alternative should be reviewed alongside it.

## Matrix Status Rules

| Status | Meaning |
|---|---|
| `match` | The feature aligns under deterministic rules |
| `partial` | The feature has overlap but also important differences |
| `different` | The feature does not align or evidence is thin |

## Analyst Interpretation

The output should be read as:

```text
This is why the system retrieved this historical analog.
```

It should not be read as:

```text
This is what will happen next.
```

## Safe-Use Boundary

Similarity explanations are retrieval explanations only. They do not establish causality, forecast returns, or support investment recommendations.
