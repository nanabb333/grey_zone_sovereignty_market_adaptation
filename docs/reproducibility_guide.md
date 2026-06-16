# Reproducibility Guide

## Environment Assumptions

- Python 3 is available as `python3`.
- The repository is run from its root directory.
- No API key, LLM call, or internet access is required for the static outputs.
- Scripts use Python standard-library modules only.

## Correct Script Order

Run scripts in this order:

```bash
python3 scripts/build_news_event_database.py
python3 scripts/analyze_event_family_patterns.py
python3 scripts/scenario_similarity.py
python3 scripts/validate_project_data.py
```

Or run the release check wrapper:

```bash
python3 scripts/run_all_checks.py
```

## Expected Outputs

| Script | Expected Outputs |
|---|---|
| `scripts/build_news_event_database.py` | `results/news_database_summary.json`, `results/news_database_summary.md` |
| `scripts/analyze_event_family_patterns.py` | `results/event_family_summary.csv`, `results/event_family_summary.json`, `results/event_family_summary.md` |
| `scripts/scenario_similarity.py` | `results/scenario_similarity_results.json`, `results/scenario_similarity_results.md` |
| `scripts/validate_project_data.py` | `results/data_validation_report.json`, `results/data_validation_report.md`, `results/theory_variable_coverage.json`, `results/theory_variable_coverage.md` |

## Launch Dashboard Locally

From the repository root:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open:

```text
http://127.0.0.1:8000/dashboard/
```

## Verify Results

1. Confirm each script exits successfully.
2. Confirm output files in `results/` were updated.
3. Confirm `results/data_validation_report.md` shows no errors.
4. Confirm the dashboard loads static JSON paths from `../results/`.
5. Confirm README links and screenshot references resolve.

## Known Warnings

The validation report may show `warning` because news row `N007` is intentionally retained as contextual Nauru diplomatic-recognition evidence but does not map to a coded event in `data/events_v2.csv`.

This warning is documented for analyst review. It is not a script failure and does not change the event-study methodology.

## Responsible Use

Outputs are descriptive and historical. They do not provide forecasts, trading advice, investment recommendations, or causal proof.
