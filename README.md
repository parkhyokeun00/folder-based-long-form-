# Long Form Knowledge OS

This workspace refactors the novel-oriented system in `F:\CODEX-PJT\novel` into a Korean YouTube long-form operating system.

The goal is not to write "more scripts."
The goal is to build a repeatable channel engine that:

- sounds narrated, not lectured
- turns research into curiosity-first episodes
- preserves reusable knowledge and callbacks across episodes
- improves through postmortems instead of intuition alone
- compounds through recursive promotion the way `novel` already does

## Root structure

- `00_system/`: rules, contracts, benchmark translation, and templates
- `_engine_reviews/`: engine-side promotion passes, lint notes, and recursive audits
- `01_channel/`: live channel source-of-truth and promoted channel wiki
- `02_sources/`: raw, parsed, adopted, and deprecated research
- `03_topics/`: one folder per episode candidate
- `tools/`: small utilities such as episode bootstrapping

Sibling repository:

- `F:\CODEX-PJT\long_form-results`: cloned experiment workspaces and result-side recursive reviews

## Operating model

1. Treat `long_form` as the engine repo and `long_form-results` as the experiment repo.
2. Lock the channel promise and voice in `01_channel/channel-core.md`.
3. Capture and normalize research in `02_sources/`.
4. Create one topic folder in `03_topics/` or inside a result clone.
5. Build the case field before deciding packaging.
6. Draft long enough to discover the real spine, then cut repetition.
7. Write a recursive review at the end of the run.
8. Promote only generalized, reusable rules back into the engine.

## Important rule

This system uses the benchmark channel as a structural reference, not as a surface-copy target.
We translate the benchmark's strengths into repeatable rules rather than cloning its exact wording.

It also follows the recursive engine model already proven in `novel`:

- experiments are disposable
- reviews are valuable
- promotions make the engine smarter
- clones are not long-term references
- only extracted engine law survives

## First read

- `00_system/OPERATING_RULES_REBOOT.md`
- `00_system/BENCHMARK_TRANSLATION.md`
- `00_system/RECURSIVE_ENGINE_PROTOCOL.md`
- `00_system/VOICE_CONTRACT.md`
- `00_system/NEW_CHANNEL_BOOTSTRAP.md`

## First command

```bash
python tools/bootstrap_episode.py "<topic>" --dry-run
```
