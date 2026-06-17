# Dataset V3 Expansion Sprint Report

> Academic Research Notice:
> This sprint expanded the review and planning layer only. It did not insert candidate events into the validated dataset and did not generate CAR results.

## Files Created

- `data/event_candidates_v3.csv`
- `docs/event_dataset_v3_expansion.md`
- `docs/event_inclusion_protocol.md`
- `results/dataset_v3_readiness_report.md`
- `docs/event_v3_integration_audit.md`
- `docs/theory_coding_expansion_plan.md`
- `results/theory_expansion_readiness.md`
- `results/event_family_expansion_projection.md`
- `docs/research_upgrade_roadmap.md`
- `docs/future_analysis_opportunities.md`
- `docs/portfolio_impact_assessment.md`
- `results/dataset_v3_expansion_sprint_report.md`

## Files Modified

No existing validated dataset files were modified.

## Projected Dataset Size

| Dataset state | Event count |
| --- | ---: |
| Current validated baseline, `data/events_v2.csv` | 18 |
| Projected V3 after 20 Include candidates | 38 |
| Upper-bound pool if 3 Review Further candidates pass | 41 |

## Projected Theory Coverage

The projected V3 dataset should materially improve coverage of:

- `strategic_importance_level`, especially through export controls, chip-tool controls, critical-materials controls, and semiconductor investment events.
- `state_support_signal`, especially through U.S. CHIPS Act, European Chips Act, TSMC Japan, and China Big Fund III events.
- `interpretation_type`, by adding more `Mixed`, `Opportunity`, and `Threat` variation outside military-signaling events.

## Strongest Analytical Improvements

- Export controls become a real event family rather than a single case.
- Industrial policy becomes observable as a distinct mechanism.
- China countermeasures and critical-materials leverage enter the dataset.
- Recognition diplomacy becomes a dedicated Taiwan competition channel.
- The project becomes less dependent on Taiwan military events for empirical variation.

## Remaining Weaknesses

- Candidate events still require source packets and official-date verification.
- Trading-date mapping remains incomplete.
- Some candidate dates may refer to announcement, publication, implementation, or disclosure rather than a single clean market event.
- Diplomatic-recognition events may have weaker immediate market-response channels.
- Military-signaling coverage remains broad but not expanded by this candidate batch.

## Exact Git Commands

```bash
git status --short
git add data/event_candidates_v3.csv docs/event_dataset_v3_expansion.md docs/event_inclusion_protocol.md docs/event_v3_integration_audit.md docs/theory_coding_expansion_plan.md docs/research_upgrade_roadmap.md docs/future_analysis_opportunities.md docs/portfolio_impact_assessment.md results/dataset_v3_readiness_report.md results/theory_expansion_readiness.md results/event_family_expansion_projection.md results/dataset_v3_expansion_sprint_report.md
git commit -m "Add dataset v3 expansion sprint documentation"
```
