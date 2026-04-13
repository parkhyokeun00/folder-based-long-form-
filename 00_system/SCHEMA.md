# Schema

This workspace uses a topic-folder model and a layered long-form channel operating system.

The purpose is not to produce scripts quickly.
The purpose is to produce episodes that are researched enough to earn their structure.

It now also operates as a recursive engine:

- the engine repo stores reusable law
- a sibling results repo stores per-run experiments
- promotions move value from experiments back into the engine

When this file conflicts with older workflow assumptions, follow:

- `00_system/OPERATING_RULES_REBOOT.md`

## Core model

- One topic folder equals one episode candidate.
- One episode is built from cases, pressure, and interpretation, not from packaging alone.
- Packaging is late-stage and provisional until the script spine is stable.
- Reusable knowledge lives at the channel layer so later episodes can call back to earlier ones.
- Research does not become script truth until it is selected, framed, and tested against competing explanations.
- Research notes are first-class artifacts, not optional scratch.

## Channel contract

Live channel truth is stored in:

- `01_channel/channel-core.md`
- `01_channel/patterns/`
- `01_channel/network/`
- `01_channel/indexes/`

That file should hold:

- channel promise
- viewer model
- opener and closer formulas
- topic lanes
- callback rules
- retention hypotheses
- feedback loop notes

The channel wiki should then distribute reusable learnings into:

- hook patterns
- retention patterns
- packaging patterns
- voice patterns
- episode network
- index and log

## Source contract

`02_sources/` separates intake stages:

- `raw/`: captured material and first-pass notes
- `research/`: ratified research notes for contested or source-sensitive topics
- `parsed/`: case roles, tensions, and open questions
- `canon-integrated/`: claims solid enough to build with
- `deprecated/`: rejected, outdated, or misleading material

Research only becomes episode truth after it is selected into `02_evidence-map.md`.
Research notes should preserve adopted claims, rejected claims, scope limits, chronology risks, mechanism gaps, and source ladder.

## Topic folder contract

Every episode candidate folder in `03_topics/` should contain:

- `00_topic-angle.md`
- `01_thumbnail-hook.md`
- `02_evidence-map.md`
- `03_outline.md`
- `04_segment-map.md`
- `05_script-draft.md`
- `06_final-script.md`
- `07_publish-card.md`

## Recursive engine contract

The living engine is `F:\CODEX-PJT\long_form`.

Experiments should live in the sibling repository:

- `F:\CODEX-PJT\long_form-results`

Use:

- `00_system/RECURSIVE_ENGINE_PROTOCOL.md`
- `00_system/PROMOTION_FILTER.md`
- `00_system/RESULTS_REPOSITORY_CONTRACT.md`

to decide what may return from a result workspace to the engine.

## File roles

- `00_topic-angle.md`: real question, stakes, and why the topic matters
- `01_thumbnail-hook.md`: late-stage packaging memo; provisional thumbnail/title ideas after the draft earns them
- `02_evidence-map.md`: cases, facts, uncertainty notes, what each case proves, the reference set actually used, and any rejected but tempting claims
- `03_outline.md`: chapter flow after the case field is known
- `04_segment-map.md`: segment-by-segment role, proof, and tension
- `05_script-draft.md`: exploratory full narration with room to discover structure
- `06_final-script.md`: final spoken script only
- `07_publish-card.md`: packaging summary, sequel notes, and postmortem

## Operating cadence

### Research-close

- gather more than one explanatory source
- create or update a research note in `02_sources/research/` when the topic rests on disputed, historical, scientific, or viral claims
- collect concrete cases before abstract framing
- rank the source set by authority
- separate verified fact, supported interpretation, working hypothesis, and rejected claim
- test chronology, scope, and mechanism before using a clean causal chain
- distinguish primary fact, secondary interpretation, and your own hypothesis
- note what each case uniquely contributes

### Build-close

- complete `00_topic-angle.md`
- complete `02_evidence-map.md`
- do not freeze packaging yet
- confirm the governing claim is narrower than the total material
- confirm no two major cases are doing the same argumentative job
- confirm the evidence map records the reference set actually used and any rejected-but-tempting claims
- if the topic is economy, industry, state, supply-chain, or policy driven, make sure the evidence map covers actors, mechanism, response, human cost, interested-party claims, and an unresolved choice

### Draft-close

- complete `03_outline.md`
- complete `04_segment-map.md`
- write `05_script-draft.md`
- allow the draft to become longer if the material is still thinly covered
- cut repeated conclusions only after the real structure is visible
- if the topic is cultural, behavioral, or historical, bring the topic from lived use or present anomaly into origin, then back into modern meaning

### Final-close

- write `06_final-script.md`
- remove planning labels and evidence tables from the final file
- make sure the final script is not simply a compressed copy of the draft
- make sure the ending happens once
- only then write `01_thumbnail-hook.md` and `07_publish-card.md`
- do not let interested-party framing read like neutral fact in the narration
- when the topic makes a real tradeoff visible, the ending should name a concrete question, tradeoff, or writer judgment

### Publish-close

- record callbacks, sequel angles, and postmortem notes in `07_publish-card.md`
- update `01_channel/channel-core.md` when a lesson becomes reusable
- if the lesson is narrower than channel law, update the correct pattern page instead
- append a promotion or experiment entry to `01_channel/indexes/log.md`

### Promotion-close

- read the result-side recursive review
- extract candidate promotions
- run the promotion filter
- promote only accepted, generalized rules
- record provenance and confidence in the log

### Lint-close

- check for duplicated or stale rules across pattern pages
- check for strong learnings trapped in result workspaces but not promoted
- check for orphan pages missing from `01_channel/indexes/index.md`

## Authority model

When files disagree, use this order:

1. verified research in `02_sources/canon-integrated/`
2. ratified research notes in `02_sources/research/`
3. operating law in `00_system/`
4. `02_evidence-map.md`
5. `03_outline.md` and `04_segment-map.md`
6. `05_script-draft.md`
7. `06_final-script.md`
8. packaging notes in `01_thumbnail-hook.md` and `07_publish-card.md`

## Hard gates

- Do not lock title or thumbnail before the cases are real.
- Do not build from one explainer article alone.
- Do not use multiple cases that only restate the same conclusion.
- Do not keep abstract terms that have not been translated into viewer language.
- Do not finalize an episode that lacks a backward callback or forward seed when a connection is available.
- Do not let the script sound like notes being read aloud.
- Do not narrate a disputed or viral claim before a research note separates confirmed fact, supported interpretation, and rejected myth.
- Do not use a neat causal chain when chronology, scope, or mechanism are still untested.
- Do not stop a culture script at origin alone; bring it back to how the pattern lives now.
- Do not quote interested-party framing as if it were neutral fact.
- Do not compress because the material is under-researched.
- Do not end on mood alone when the topic demands a judgment or a concrete question.
- Do not end three times.
- Do not let an abstract phrase cover missing evidence.
- Do not promote raw experiment clutter into the engine.
- Do not promote topic-specific success as universal law without abstraction.
