# New Channel Bootstrap

Use this when starting the system from a cold state or when the old pipeline has clearly failed.

Its job is to stop random rebuilding and force a sharper restart.

## Restart assumptions

- the old output pipeline did not create enough watchability
- correctness alone is not enough
- the new system must optimize for curiosity, narration, and reuse
- the channel must learn from each run the way the novel engine already does

## First build order

1. Read `00_system/BENCHMARK_TRANSLATION.md`.
2. Read `00_system/VOICE_CONTRACT.md`.
3. Read `00_system/RECURSIVE_ENGINE_PROTOCOL.md`.
4. Fill the empty sections in `01_channel/channel-core.md`.
5. Define your opener slot, closer slot, and three topic lanes.
6. Define why a viewer clicks and why a viewer leaves.
7. Run `python tools/bootstrap_episode.py "<topic>"`.
8. Fill the topic packet in order.
9. When the run is over, write a recursive review and promote only accepted rules back into the engine.

## Hard gate

Do not write `06_final-script.md` until all are true:

- `00_topic-angle.md` has a real emotional angle
- `01_thumbnail-hook.md` contains a clear click promise
- `02_evidence-map.md` separates strong proof from weak proof
- `03_outline.md` has at least one turn, not just accumulation
- `04_segment-map.md` shows how the middle avoids flatness

## Topic selection rule

Pick topics that satisfy at least three:

- a viewer thinks they already understand it
- the reality is stranger than the viewer expects
- the topic can be explained with one vivid case
- the topic has a modern emotional bridge
- the topic connects to an earlier or future episode

## Recursive improvement rule

After each finished episode:

- record what made the packaging strong or weak
- record where the viewer would likely leave
- record which analogy or opening device felt alive
- promote only repeatable lessons into the engine
- use the narrowest destination page possible
- convert negative notes into affirmative operating rules before promotion

## Stop line

If you have:

- a stable opener
- a stable closer
- three clear topic lanes
- one filled topic packet
- one feedback loop format

then stop redesigning the system and start shipping episodes through it.
