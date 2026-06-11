#!/usr/bin/env python3
"""Validate the structure of the latex-forge Claude skill.

Checks that SKILL.md exists, has well-formed frontmatter (name matching the
skill folder, non-empty description within Claude's length limit), and that
every local file referenced from SKILL.md actually exists.
"""

import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent / "latex-forge"
MAX_DESCRIPTION_LENGTH = 1024

errors = []

skill_md = SKILL_DIR / "SKILL.md"
if not skill_md.is_file():
    errors.append(f"missing {skill_md}")
else:
    text = skill_md.read_text(encoding="utf-8")

    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md: missing YAML frontmatter block")
    else:
        frontmatter = match.group(1)

        name_match = re.search(r"^name:\s*(\S+)\s*$", frontmatter, re.MULTILINE)
        if not name_match:
            errors.append("SKILL.md: frontmatter has no 'name' field")
        elif name_match.group(1) != SKILL_DIR.name:
            errors.append(
                f"SKILL.md: name '{name_match.group(1)}' does not match "
                f"folder name '{SKILL_DIR.name}'"
            )

        desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
        if not desc_match or not desc_match.group(1).strip():
            errors.append("SKILL.md: frontmatter has no 'description' field")
        elif len(desc_match.group(1)) > MAX_DESCRIPTION_LENGTH:
            errors.append(
                f"SKILL.md: description is {len(desc_match.group(1))} chars, "
                f"limit is {MAX_DESCRIPTION_LENGTH}"
            )

    for link in re.findall(r"\]\((?!https?://|#)([^)]+)\)", text):
        target = SKILL_DIR / link.split("#", 1)[0]
        if not target.exists():
            errors.append(f"SKILL.md: broken local link '{link}'")

references = SKILL_DIR / "references"
if not references.is_dir() or not any(references.glob("*.md")):
    errors.append("references/ is missing or contains no markdown files")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)

print("Skill structure is valid.")
