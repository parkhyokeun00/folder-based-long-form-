# Promotion Filter

Use this before moving anything from `long_form-results` back into `long_form`.

Its job is to stop experiment noise from polluting the engine.

## Promotion rule

Promote only what is all of the following:

- reusable
- stable enough
- generalized
- beneficial to future outputs
- small enough to fit a real engine page

## Positive-only promotion

The engine should absorb value, not raw frustration.

This means:

- failure notes may stay in result reviews
- engine promotions must be rewritten as positive craft rules, gates, or warnings
- if a lesson cannot be rephrased as a useful operating rule, do not promote it

## Four gates

### 1. Reusability

Ask:

- does this help more than one topic
- does this improve process, packaging, narration, or review quality beyond a single case

If no, keep it local.

### 2. Stability

Ask:

- was this clearly useful in the experiment
- does it feel likely to remain useful across the next few runs

If uncertain, hold it as a candidate instead of promoting it.

### 3. Abstraction

Ask:

- has this been rewritten at the right level
- is it still contaminated by one topic, one title, one case, or one emotional reaction

If too specific, rewrite or discard.

### 4. Placement

Ask:

- what is the narrowest engine page that should receive this
- does an equivalent rule already exist there

If duplicated, merge instead of adding a second version.

## Verdicts

- `promote`: move into the engine now
- `hold`: useful, but not yet proven or not yet cleanly abstracted
- `discard`: interesting locally, but not engine material

## Strong promotion signals

- the same lesson appears in multiple result reviews
- the lesson fixes a recurring weakness
- the lesson changes output quality in a visible way
- the lesson can be expressed in a short rule and pointed at a clear destination page

## Weak promotion signals

- this title worked once
- this wording felt cool in one script
- the lesson is mostly emotional reaction without mechanism
- the lesson duplicates an engine rule already present

## Required metadata in a promotion pass

When promoting, record:

- source run label
- source review file
- promoted rule
- target engine page
- confidence

Store this in `01_channel/indexes/log.md` and, when needed, an engine-side audit note under `_engine_reviews/`.

If the result clone is expected to disappear, the engine-side audit note becomes the canonical provenance record.

Do not rely on the original clone staying present after promotion.
