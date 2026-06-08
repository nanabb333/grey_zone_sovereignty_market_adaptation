# Surprise Coding Protocol V1

## Purpose

This protocol defines a transparent coding scheme for `surprise_level` in the Taiwan geopolitical event-study dataset. The goal is to distinguish `adaptation` from `anticipation` as explanations for weakening or non-negative market reactions.

Adaptation means that repeated shocks become less damaging because investors learn how to interpret recurring grey-zone behavior. Anticipation means that the event was already expected and may have been priced before Day 0. These explanations can look similar in an event study, so surprise must be coded explicitly.

## Coding Scale

| surprise_level | label | definition |
| ---: | --- | --- |
| 0 | Fully Expected | The event was scheduled, strongly signaled, or highly predictable given recent precedent. |
| 1 | Partially Expected | The broad event type was expected, but the timing, scope, intensity, or market relevance was uncertain. |
| 2 | Highly Unexpected | The event had little public warning, limited recent precedent, or materially changed expectations. |

## Coding Criteria

Coders should consider five criteria:

1. Prior public warnings: Did officials or media signal the event before it occurred?
2. News coverage before event: Was the event discussed in advance?
3. Market expectation: Would investors plausibly have expected the event or response?
4. Recent precedent: Had similar events occurred recently?
5. Expectation change: Did the event materially change expectations about Taiwan risk or strategic importance?

## Coding Guidance

Use `0` when the event was scheduled or highly predictable. Examples include inaugurations, planned diplomatic transits, or military responses that closely follow a recent pattern.

Use `1` when investors could anticipate the general event type but not the exact timing, scope, or intensity. Examples include PRC responses to U.S.-Taiwan interaction, technology policy announcements with uncertain details, or investment announcements that were plausible but not fully specified.

Use `2` only when the event was genuinely unexpected or appears to have changed the expected risk environment. This category should be used conservatively.

## Confidence Coding

| confidence | meaning |
| --- | --- |
| High | Public information strongly supports the coding. |
| Medium | Coding is plausible but should be checked against additional news coverage. |
| Low | Coding is uncertain and requires manual review. |

## Use in the Dissertation

`surprise_level` should not be treated as proof of adaptation. Instead, it should be used as a rival-explanation control. If later military events are coded as low surprise, then weaker market reactions may reflect anticipation rather than adaptation. A stronger adaptation argument requires showing that repeated events become less damaging even after accounting for whether they were expected.
