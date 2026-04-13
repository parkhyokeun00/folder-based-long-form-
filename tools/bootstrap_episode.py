from __future__ import annotations

import argparse
import re
from pathlib import Path


FILE_TEMPLATES = {
    "00_topic-angle.md": """# Topic Angle

## Topic

- topic: {topic}

## Core question

- what makes this topic click-worthy now:

## Viewer state

- what viewers think before clicking:
- what they should feel by the end:

## Emotional angle

- fear / fascination / frustration / relief:

## Rejection check

- why this topic might still be too dry:
""",
    "01_thumbnail-hook.md": """# Thumbnail And Hook

## Late-stage packaging

- fill this after the draft has a stable spine

## Thumbnail text candidates

- option-1:
- option-2:
- option-3:

## First image promise

- what weird, concrete thing the viewer sees first:

## Opening anomaly

- the strange case, line, or contradiction that starts the video:

## Opening promise

- what the finished script can genuinely promise:
""",
    "02_evidence-map.md": """# Evidence Map

## Reference set actually used

- research note:
- source-1:
- source-2:
- source-3:

## Anchor case

- strongest case:

## Supporting proof

- proof-1:
- proof-2:
- proof-3:

## Source ladder

- tier-1:
- tier-2:
- tier-3:

## Adopted claims safe to narrate

- claim-1:

## Rejected or downgraded claims

- claim-1:

## Chronology, scope, and mechanism checks

- chronology risk:
- scope risk:
- mechanism risk:

## Exact facts that must stay exact

- fact-1:

## Weak or risky claims to avoid

- risk-1:

## Plain-language conversion options

- abstract term:
- everyday explanation:
""",
    "03_outline.md": """# Outline

## Opening

- anomaly or case:
- real question:

## Anchor case

- what carries the piece emotionally or conceptually:

## Middle turn 1

- what the viewer learns first:

## Middle turn 2

- what complicates or reverses the first understanding:

## Modern re-entry

- what returns the topic to now:

## Ending

- changed way of seeing the topic:
- sequel or callback opening:
""",
    "04_segment-map.md": """# Segment Map

## Segment 1

- goal:
- tension question:
- proof used:
- transition:

## Segment 2

- goal:
- tension question:
- proof used:
- transition:

## Segment 3

- goal:
- tension question:
- proof used:
- transition:

## Segment 4

- goal:
- tension question:
- proof used:
- payoff:
""",
    "05_script-draft.md": """# Script Draft

## Opening slot

- branded opener:

## Draft

Write the spoken draft here.
Keep it conversational.
Let the draft discover its structure before you compress anything.
""",
    "06_final-script.md": """# Final Script

Write narration only.
Remove planning notes before publication.
""",
    "07_publish-card.md": """# Publish Card

## Packaging

- final thumbnail direction:
- final title direction:

## Network

- backward callback:
- forward seed:

## Risk

- where retention may sag:

## Postmortem

- what worked:
- what should become a channel rule:
""",
}


def sanitize_slug(raw: str) -> str:
    value = raw.strip().lower()
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"[^\w\-가-힣]", "", value)
    value = value.strip("-")
    if not value:
        raise ValueError("Could not derive a folder name. Pass --slug with a safe value.")
    if value in {".", ".."} or ".." in value or "/" in value or "\\" in value:
        raise ValueError("Unsafe slug.")
    return value


def render_files(topic_dir: Path, topic: str) -> list[tuple[Path, str]]:
    return [(topic_dir / name, template.format(topic=topic)) for name, template in FILE_TEMPLATES.items()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new long-form episode packet.")
    parser.add_argument("topic", help="Human-readable topic name")
    parser.add_argument("--slug", help="Folder name override")
    parser.add_argument(
        "--topics-dir",
        type=Path,
        help="Override the topics directory. Defaults to <workspace>/03_topics.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing files")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    workspace_root = Path(__file__).resolve().parents[1]
    topics_dir = (args.topics_dir or (workspace_root / "03_topics")).resolve()
    slug = args.slug or sanitize_slug(args.topic)
    topic_dir = (topics_dir / slug).resolve()

    if topic_dir.parent != topics_dir:
        raise ValueError("Refusing to write outside the topics directory.")

    files = render_files(topic_dir, args.topic)

    print(f"Workspace root: {workspace_root}")
    print(f"Topic directory: {topic_dir}")
    for path, _ in files:
        print(f"- {path}")

    if args.dry_run:
        return 0

    topic_dir.mkdir(parents=True, exist_ok=True)
    for path, content in files:
        if path.exists() and not args.force:
            raise FileExistsError(f"{path} already exists. Use --force to overwrite.")
        path.write_text(content, encoding="utf-8")

    print("Episode packet created.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
