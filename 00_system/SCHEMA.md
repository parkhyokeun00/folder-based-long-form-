# Schema

This workspace uses a topic-folder model and a layered long-form channel operating system.

The purpose is to keep episodes compelling, consistent, and reusable across time.

It now also operates as a recursive engine:

- the engine repo stores reusable law
- a sibling results repo stores per-run experiments
- promotions move value from experiments back into the engine

## Core model

- One topic folder equals one episode candidate.
- One episode is built from segments, not from a flat essay.
- The thumbnail and hook are locked before the full narration is accepted.
- Reusable knowledge lives at the channel layer so later episodes can call back to earlier ones.
- Research does not become script truth until it is selected, framed, and simplified for viewers.

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

- `raw/`: captured but untouched material
- `parsed/`: normalized notes with claims separated from noise
- `canon-integrated/`: claims actively used by the channel system
- `deprecated/`: rejected, outdated, or misleading material

Research only becomes episode truth after it is selected into `02_evidence-map.md`.

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

- `00_topic-angle.md`: why this topic matters now, for whom, and through what emotional angle
- `01_thumbnail-hook.md`: click promise, first-image promise, and first-30-seconds proof
- `02_evidence-map.md`: cases, facts, quotes, uncertainty notes, and interested-party claim markers
- `03_outline.md`: chapter flow
- `04_segment-map.md`: segment-by-segment pressure, question, and payoff
- `05_script-draft.md`: full narration with room for revision
- `06_final-script.md`: final spoken script only
- `07_publish-card.md`: callback plan, packaging notes, and postmortem

## Operating cadence

### Research-close

- capture sources in `02_sources/`
- normalize reusable material
- separate adopted claims from interesting noise

### Angle-close

- complete `00_topic-angle.md`
- reject the topic if the promise is generic, purely academic, or emotionally thin
- complete `01_thumbnail-hook.md`
- do not continue if the opening image is weak

### Build-close

- complete `02_evidence-map.md`
- complete `03_outline.md`
- complete `04_segment-map.md`
- confirm each middle segment either escalates, reframes, or reveals
- if the topic is cultural, behavioral, or historical, map origin -> spread -> modern form instead of stopping at background explanation
- if the topic is economy, industry, state, supply-chain, or policy driven, make sure the evidence map covers actors, mechanism, response, human cost, interested-party claims, and an unresolved choice

### Script-close

- draft `05_script-draft.md`
- compress into `06_final-script.md`
- remove planning labels and evidence tables from the final file
- make sure the host voice is audible, not only the research summary
- when the topic supports it, front-load a dense example cluster before the first long explanation block
- for structure-heavy topics, trim repetition only after coverage is complete
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
2. channel rules in `01_channel/channel-core.md`
3. `02_evidence-map.md`
4. `03_outline.md` and `04_segment-map.md`
5. `05_script-draft.md`
6. `06_final-script.md`
7. packaging guesses in `07_publish-card.md`

## Hard gates

- Do not write the full draft before the thumbnail and hook are locked.
- Do not keep abstract terms that have not been translated into viewer language.
- Do not finalize an episode that lacks a backward callback or forward seed when a connection is available.
- Do not let the script sound like notes being read aloud.
- Do not stop a culture script at origin alone; bring it back to how the pattern lives now.
- Do not quote interested-party framing as if it were neutral fact.
- Do not compress a structure-heavy topic before its core layers are present.
- Do not end on mood alone when the topic demands a judgment or a concrete question.
- Do not promote raw experiment clutter into the engine.
- Do not promote topic-specific success as universal law without abstraction.
