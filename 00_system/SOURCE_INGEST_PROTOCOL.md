# Source Ingest Protocol

`02_sources/` is not a dumping ground.
It is the ratification layer between browsing and spoken script truth.

## Purpose

Separate:

- raw material that has not been processed
- research notes that test contested claims and preserve exclusions
- parsed notes that normalize reusable cases or extracts
- canon-integrated notes that are stable enough to reuse across episodes
- deprecated material that should remain searchable but not live

## Recommended source areas

- `02_sources/raw/`: untouched intake
- `02_sources/research/`: research notes for disputed, historical, scientific, policy, or viral claims
- `02_sources/parsed/`: normalized cases, summaries, or extracted proof
- `02_sources/canon-integrated/`: claims solid enough to reuse as channel memory
- `02_sources/deprecated/`: superseded, rejected, weak, or misleading material

## Required metadata for a research or parsed note

Every durable note should record:

- `source-id`
- `type`
- `status`
- `origin`
- `date`
- `trust-level`
- `linked-topics`
- `adopted-claims`
- `rejected-claims`
- `notes`

## Trust ladder

Use an explicit source ladder before turning confidence into narration.

- tier-1: primary documents, peer-reviewed papers, public institutions, official data, direct records
- tier-2: high-quality reference works, respected syntheses, strong explainers grounded in citations
- tier-3: secondary commentary, fact-checks, magazine summaries, useful but non-authoritative explainers

One tier-1 contradiction should outweigh several tier-3 repeats.

## Claim ladder

Do not store all claims as one blob.
Classify them.

- verified fact
- supported interpretation
- working hypothesis
- rejected or downgraded claim

## Ingest flow

1. Capture the material into `raw/` or directly into `research/` when the topic is contested.
2. If the topic is disputed, historical, scientific, or viral, open or update a research note in `research/`.
3. Summarize reusable cases or extracts into `parsed/`.
4. Record the trust ladder and claim ladder.
5. Move only stable, reusable claims into `canon-integrated/` when they deserve to become channel memory.
6. Move broken, weak, or outdated material into `deprecated/`.

## Script-safety rule

No source becomes script truth just because it was read.

A claim becomes script-safe only when all are true:

- the source is logged in `02_sources/`
- the authority tier is named
- the claim status is named
- the claim is selected into `02_evidence-map.md` or ratified into `canon-integrated/`
- obvious competing explanations or scope limits are recorded when relevant

## Myth-check rule

For viral-history, internet myth, science-explainer, and debate-heavy topics, every research note should explicitly test:

- scope: local case, regional pattern, or system-wide claim
- chronology: whether the timeline actually supports the claimed chain
- mechanism: what would have to happen for the claim to work
- representative evidence: whether the strongest example is typical or merely vivid
- what the popular one-line story leaves out

If one link in the clean chain fails, narrate the complexity instead of repeating the meme.

## Main-agent ratification rule

Parallel research helpers may widen the search.
They do not replace final ratification.

The master agent should independently verify the high-impact lines that enter the script spine.

## Provenance rule

When a research note materially changes an episode:

- record the note or source set in `02_evidence-map.md`
- keep adopted and rejected claims visible
- preserve enough context that the argument still makes sense if the chat history disappears
