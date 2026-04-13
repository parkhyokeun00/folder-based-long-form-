# Recursive Engine Protocol

Use this document when operating `F:\CODEX-PJT\long_form` as a compounding engine instead of a one-off script folder.

The model is the same one already proven in `F:\CODEX-PJT\novel`.

## Core idea

The engine repo is not where experiments go to die.
It is where stable learnings are promoted.

The actual episode experiments, drafts, and temporary overgrowth belong in sibling result workspaces.
Only generalized, reusable upgrades come back into the engine.
Result clones are disposable after extraction.
The engine must not depend on them as living references.

## Three layers

### 1. Engine

- path: `F:\CODEX-PJT\long_form`
- role: source-of-truth for reusable channel law
- contents: system docs, channel wiki, templates, tools
- edit rule: update only with promotions, not with raw experiment clutter

### 2. Results

- path: `F:\CODEX-PJT\long_form-results`
- role: one folder per experiment clone
- contents: temporary full workspaces, finished episode packets, review documents, local discoveries
- lifecycle: experiments may expire after extraction

### 3. Schema

- location: `00_system/`
- role: tells the LLM how to ingest, review, promote, lint, and protect the engine from contamination

## Default loop

1. Start from the engine repo.
2. Clone or copy the engine into a new result workspace under `long_form-results/`.
3. Produce the topic package, scripts, packaging, and local notes inside the result workspace.
4. Write a top-level recursive review document in the result workspace.
5. Extract promotion candidates from the review.
6. Run `PROMOTION_FILTER.md`.
7. Promote only accepted, generalized rules into the engine repo.
8. Log the promotion in `01_channel/indexes/log.md`.
9. Leave the result workspace as historical evidence, not as the living engine.

## Required result-side review

Every experiment folder should end with one top-level review document.

Preferred names:

- `000_CHANNEL_RECURSIVE_REVIEW.md`
- `000_RETROSPECTIVE_<slug>.md`
- `NEXT_GENERATION_REVIEW.md`

The filename may vary.
The function may not.

## Promotion targets inside the engine

Use the narrowest useful destination.

- high-level channel law: `01_channel/channel-core.md`
- hook discoveries: `01_channel/patterns/hook-patterns.md`
- pacing and retention discoveries: `01_channel/patterns/retention-patterns.md`
- title and thumbnail discoveries: `01_channel/patterns/packaging-patterns.md`
- narration discoveries: `01_channel/patterns/voice-patterns.md`
- callback and sequel discoveries: `01_channel/network/episode-network.md`
- audit or promotion pass records: `_engine_reviews/`
- navigation and chronology: `01_channel/indexes/index.md`, `01_channel/indexes/log.md`

## Hard rules

- Do not promote full scripts back into the engine.
- Do not promote topic-specific facts as if they were universal channel rules.
- Do not overwrite engine pages from inside a result clone.
- Do not promote frustration text verbatim; convert it into a reusable affirmative rule first.
- Do not let one strong experiment rewrite the engine if the lesson is still narrow or unstable.
- When a result clone is temporary, do not make engine provenance depend on that folder path staying alive.
- In that case, record a stable engine-side promotion note and use a run label instead of a hard clone path in engine logs.
- After promotion, do not keep consulting the clone as if it were part of the engine's memory.
- If a lesson matters, rewrite it into engine law here; otherwise let the clone disappear.

## Query behavior

When asked a channel question, read the engine wiki first.
Use result workspaces as supporting evidence, not as the primary law.

## Lint behavior

Periodically run an engine health check.

Look for:

- duplicated rules across pattern pages
- stale guidance superseded by better rules
- missing links between related pattern pages
- strong insights trapped in result workspaces but not yet promoted
- promoted rules that no longer match current output quality

## The intended shape

Results are many.
The engine is singular.

The results repo is where experiments happen.
The engine repo is where the channel gets smarter.
