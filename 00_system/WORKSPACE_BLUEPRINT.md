# Workspace Blueprint

This document explains the exact shape of the current workspace so it can be rebuilt without guessing.

## Current tree

```text
README.md
_engine_reviews/
00_system/
  BENCHMARK_TRANSLATION.md
  MASTER_AGENT.md
  NEW_CHANNEL_BOOTSTRAP.md
  PROMOTION_FILTER.md
  RECURSIVE_ENGINE_PROTOCOL.md
  RESULTS_REPOSITORY_CONTRACT.md
  SCHEMA.md
  VOICE_CONTRACT.md
  WORKSPACE_BLUEPRINT.md
  templates/
    episode/
      episode-packet.md
    review/
      recursive-channel-review.md
01_channel/
  channel-core.md
  indexes/
    index.md
    log.md
  network/
    episode-network.md
  patterns/
    hook-patterns.md
    packaging-patterns.md
    retention-patterns.md
    voice-patterns.md
02_sources/
  raw/
  parsed/
  canon-integrated/
  deprecated/
03_topics/
images/
tools/
  bootstrap_episode.py

Sibling repository:
F:\CODEX-PJT\long_form-results/
  README.md
  _templates/
    000_CHANNEL_RECURSIVE_REVIEW.md
```

## Purpose of each layer

- `_engine_reviews/`: engine-side audits and promotion passes
- `00_system/`: stable operating law
- `01_channel/`: live channel source-of-truth plus promoted wiki pages
- `02_sources/`: research intake and trust separation
- `03_topics/`: one episode candidate per folder
- `images/`: prompt and image asset workspace
- `tools/`: small repeatable utilities
- `long_form-results/`: result clones and per-run recursive reviews

## Reconstruction order

1. create the root folders
2. create the engine review folder
3. create the system documents
4. create `01_channel/channel-core.md`
5. create channel wiki index and pattern pages
6. create the `02_sources/` intake partitions
7. create `03_topics/`
8. create the sibling results repository and review template
9. add the episode bootstrap tool

## Structure philosophy

This is not a dumping folder for random scripts.
It is a recursive operating system for a Korean long-form channel.

The stable rules live in `00_system/`.
The live brand and promoted knowledge state live in `01_channel/`.
Engine audits live in `_engine_reviews/`.
Local episode work lives in `03_topics/` or a result clone.
Disposable experiments live in `long_form-results/`.
