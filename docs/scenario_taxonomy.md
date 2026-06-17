# Scenario Taxonomy

## Purpose

The scenario taxonomy standardizes how the Historical Analog Engine classifies query scenarios and historical events. It is designed for retrieval and explanation, not for prediction.

The taxonomy should be stable enough for product use while flexible enough to map existing repository labels into a smaller analyst-facing set of scenario families.

## Taxonomy Families

### Military Exercise

Military Exercise events involve visible military activity, exercises, patrols, blockade simulations, missile activity, or coercive military signaling near a relevant geography.

Common signals:

- named military exercises
- live-fire drills
- naval or air patrols
- missile launches
- blockade or quarantine simulations
- military activity linked to a political trigger

Existing label mappings:

| Existing label | Taxonomy family |
|---|---|
| `Military_Exercise` | Military Exercise |
| `Military Demonstration` | Military Exercise |
| grey-zone patrol activity | Military Exercise |

### Diplomatic Shock

Diplomatic Shock events involve high-salience diplomatic contact, official visits, warnings, recognition disputes, or state-to-state signaling that changes perceived geopolitical tension.

Common signals:

- high-level official visit
- diplomatic warning
- recognition or sovereignty statement
- official meeting involving Taiwan or cross-strait relations
- rapid escalation in diplomatic language

Existing label mappings:

| Existing label | Taxonomy family |
|---|---|
| `Diplomatic_Shock` | Diplomatic Shock |
| `Political_Signaling` | Diplomatic Shock when primarily diplomatic |

### Export Control

Export Control events involve formal restrictions on technology, goods, equipment, software, or services crossing jurisdictions.

Common signals:

- export administration rule
- licensing requirement
- controlled product category
- advanced semiconductor or equipment restriction
- foreign direct product rule

Existing label mappings:

| Existing label | Taxonomy family |
|---|---|
| `Export_Control` | Export Control |
| `Technology Competition` | Export Control when the event is a trade-control action |

### Sanction

Sanction events involve punitive legal, financial, commercial, or entity-based restrictions imposed on a target actor.

Common signals:

- entity-list addition when framed as punitive restriction
- financial sanctions
- trade blacklist
- asset freeze
- sectoral sanction
- import ban or coercive trade measure

Existing label mappings:

| Existing label | Taxonomy family |
|---|---|
| `Economic_Coercion` | Sanction when coercive or punitive |
| entity-list action | Sanction when target-specific and punitive |

### Election

Election events involve scheduled or unscheduled electoral outcomes, leadership transitions, inaugurations, or campaign events that materially change geopolitical interpretation.

Common signals:

- presidential election
- legislative election
- inauguration
- leadership transition
- party platform shift with geopolitical relevance

Existing label mappings:

| Existing label | Taxonomy family |
|---|---|
| `Political_Signaling` | Election when tied to electoral process |
| election event records | Election |

### Strategic Investment

Strategic Investment events involve state-supported or strategically framed capital allocation, industrial policy, fab construction, supply-chain diversification, or public-private investment.

Common signals:

- CHIPS Act or industrial-policy funding
- semiconductor fab investment
- strategic capacity expansion
- national resilience investment
- public subsidy or preliminary terms

Existing label mappings:

| Existing label | Taxonomy family |
|---|---|
| `Strategic_Investment` | Strategic Investment |
| `Semiconductor Supply Chain` | Strategic Investment when investment-led |

### Technology Restriction

Technology Restriction events involve constraints on access to technologies, platforms, equipment, chips, software, data flows, or technical collaboration. This category is broader than Export Control and may include domestic restrictions or technology-access limits that are not primarily export rules.

Common signals:

- access restriction
- technology ban
- chip, equipment, software, or platform restriction
- national-security technology rule
- controls on technical collaboration

Existing label mappings:

| Existing label | Taxonomy family |
|---|---|
| `Technology Competition` | Technology Restriction when access-limiting |
| `Export_Control` | Export Control if trade-rule specific; Technology Restriction if broader |

## Classification Rules

Use the following hierarchy when a scenario could fit multiple families:

1. If the event is a formal export rule, classify as Export Control.
2. If the event is a punitive restriction on a named actor or sector, classify as Sanction.
3. If the event is broader technology-access limitation, classify as Technology Restriction.
4. If the event is physical military activity, classify as Military Exercise.
5. If the event is high-level political or diplomatic signaling, classify as Diplomatic Shock.
6. If the event is directly tied to an electoral outcome or leadership transition, classify as Election.
7. If the event is capital allocation or industrial-policy support, classify as Strategic Investment.

## Multi-Label Handling

Historical events may carry secondary labels. For Sprint 1:

- assign one primary taxonomy family for retrieval
- allow optional secondary tags for explanation
- never duplicate the same event across families in the same query result
- report ambiguity in Analyst Notes when classification is mixed

## Taxonomy Governance

The taxonomy should be reviewed when:

- a new event does not fit any existing family
- two families become indistinguishable in retrieval results
- analyst review repeatedly overrides the primary family
- new source evidence changes the interpretation of a historical event

Taxonomy changes should preserve existing event IDs and maintain a versioned mapping table.
