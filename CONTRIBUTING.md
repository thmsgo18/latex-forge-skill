# Contributing to LaTeX Forge Skill

Thank you for your interest in contributing! Issues and pull requests are welcome.

## Repository layout

- `SKILL.md`: the skill itself. Claude reads the frontmatter
  `description` to decide when to load the skill, then follows the body as
  its playbook.
- `references/`: deeper reference material loaded on demand
  (CLI command reference, template catalog).
- `scripts/validate_skill.py`: structural checks run by CI.

## Testing your changes

Symlink (or copy) this repo into your personal skills folder and use it in a
real [Claude Code](https://docs.claude.com/en/docs/claude-code) session:

```bash
ln -s "$(pwd)" ~/.claude/skills/latex-forge
```

Then ask Claude for a LaTeX document (a report, a CV, a thesis chapter...)
and check that it picks the right template, fills in the metadata, builds,
and exports as described in `SKILL.md`.

Before opening a pull request, run the validator:

```bash
python3 scripts/validate_skill.py
```

## Guidelines

- Keep `SKILL.md` short and action-oriented: it is loaded into Claude's
  context whenever the skill triggers, so every paragraph must earn its
  place. Long-form details belong in `references/`.
- The frontmatter `description` is what makes Claude select the skill.
  If you change it, make sure it still mentions the document types and
  the latex-forge commands it covers.
- When the CLI gains or changes a command, update
  `references/commands.md` accordingly, and the template
  catalog in `references/templates.md` when the
  [gallery](https://github.com/thmsgo18/latex-forge-gallery) evolves.
- Update `CHANGELOG.md` with your changes under the `[Unreleased]` section.
