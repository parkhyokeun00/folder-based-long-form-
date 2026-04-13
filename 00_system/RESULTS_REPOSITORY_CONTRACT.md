# Results Repository Contract

This file defines how `F:\CODEX-PJT\long_form-results` should behave.

## Purpose

The results repository is not the engine.
It is the experiment graveyard, evidence locker, and review archive.

Each folder represents a full run or a significant experiment.
These folders are disposable by design.

## Folder rule

One experiment folder should contain:

- a cloned or copied working snapshot of the engine
- the topic work produced in that run
- one top-level review document
- any local notes needed to explain what changed and why

## Required top-level artifacts

Every experiment folder should end with:

- `README.md`
- one recursive review document

Recommended review names:

- `000_CHANNEL_RECURSIVE_REVIEW.md`
- `000_RETROSPECTIVE_<slug>.md`
- `NEXT_GENERATION_REVIEW.md`

## What belongs here

- episode drafts
- topic-specific packaging experiments
- local benchmarks
- failed branches
- honest notes about what was weak or awkward
- promotion candidates waiting to be filtered

## What does not belong here

- the living engine law
- generalized rules without provenance
- edits intended to replace the engine without a promotion pass

## Lifecycle

1. create experiment folder
2. do the work there
3. write the review
4. promote accepted learnings into the engine
5. archive the experiment folder as historical evidence

The experiment may stop evolving.
Its review remains valuable.
If the folder later disappears, the engine should still be complete without it.

## Promotion boundary

Do not treat a result folder as the new source-of-truth just because its output was strong.

Only promoted rules become engine law.
Everything else stays a local experiment.
Never treat an old clone as part of the engine's active memory.
