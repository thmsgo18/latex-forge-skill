# Changelog

All notable changes to the LaTeX Forge skill will be documented in this file.

## [Unreleased]

### Changed

- The CLI is installed through latex-forge's one-line installer (uv, with
  its own Python) instead of pipx, so it works on machines without Python.
- LaTeX setup follows the CLI's new no-admin install: `latex-forge setup
  --install-tex --yes` installs a light TinyTeX (asked first, as before) and
  ends with a test compile; `diagnose --json` is read for the distribution and
  whether packages install automatically. Never runs `--tex system` (needs the
  user's password).
- Build guidance: missing packages, fonts and styles are installed by
  `latex-forge build`; with a system TeX Live, the printed `sudo tlmgr`
  command is relayed to the user.
- Moved `SKILL.md` and `references/` from the `latex-forge/` subfolder to
  the repository root, so the skill can be installed with a single
  `git clone` straight into `~/.claude/skills/latex-forge` instead of a
  clone-then-copy dance.
- `SKILL.md` Step 7 now tells Claude to ground the report in its source
  material first: read the project it documents (code repository, dataset,
  notes, draft, folder) before writing, and base every factual claim on
  what is actually there rather than inventing it.

### Fixed

- `create` was documented with `--git`, removed in latex-forge 0.7.0: it now
  uses `--repo none|existing|create` (and `--repo-name`, `--visibility`,
  `--sharing`).

## [1.0.0] - 2026-06-11

### Added

- Initial release of the skill: scaffolds, writes, compiles and exports
  LaTeX documents by driving the `latex-forge` CLI.
- `latex-forge/SKILL.md` playbook covering template selection (built-in
  and gallery), project creation, `AGENTS.md` awareness, metadata filling,
  building, error fixing, and export.
- Reference material in `latex-forge/references/`: CLI command reference
  and the catalog of 80+ gallery templates.
- CI validating the skill structure on every push and pull request.
