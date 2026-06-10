<p align="right"><b>English</b> | <a href="./README.fr.md">Français</a></p>

<p align="center">
  <img src="logo.png" alt="LaTeX Forge Skill" width="420">
</p>

<p align="center">
  <b>Tell Claude what document you need. It scaffolds, writes, and compiles the LaTeX for you.</b>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License MIT"></a>
  <a href="https://github.com/thmsgo18/latex-forge"><img src="https://img.shields.io/badge/works_with-latex--forge-blue?style=for-the-badge" alt="Works with latex-forge"></a>
  <img src="https://img.shields.io/badge/claude-skill-d97757?style=for-the-badge" alt="Claude Skill">
</p>

<p align="center">
  <a href="#install">Install</a> •
  <a href="#what-it-does">What it does</a> •
  <a href="#example">Example</a> •
  <a href="#how-it-works">How it works</a> •
  <a href="#related-projects">Related projects</a>
</p>

---

## What is this?

A [Claude](https://claude.com) skill that turns [LaTeX Forge](https://github.com/thmsgo18/latex-forge)
into something you can drive entirely from a conversation: ask for a project
report, a CV, a thesis chapter, a paper, a poster, or any other document, and
Claude scaffolds a ready-to-write project from the [template gallery](https://github.com/thmsgo18/latex-forge-gallery),
fills in your title page and content, compiles it to PDF, and exports it for
submission.

It does not duplicate the LaTeX Forge ecosystem: it teaches Claude how to use
the `latex-forge` CLI, how to pick a template from the 80+ available, and how
to follow each generated project's own `AGENTS.md` briefing.

## Install

This is a plain [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills):
a folder with a `SKILL.md` that Claude loads automatically when relevant.

**Personal skill** (available in every project):

```bash
git clone https://github.com/thmsgo18/latex-forge-skill.git /tmp/latex-forge-skill
mkdir -p ~/.claude/skills
cp -r /tmp/latex-forge-skill/latex-forge ~/.claude/skills/
rm -rf /tmp/latex-forge-skill
```

**Project skill** (only for the current repository):

```bash
git clone https://github.com/thmsgo18/latex-forge-skill.git /tmp/latex-forge-skill
mkdir -p .claude/skills
cp -r /tmp/latex-forge-skill/latex-forge .claude/skills/
rm -rf /tmp/latex-forge-skill
```

That's it — no configuration. The skill installs the `latex-forge` CLI itself
(via `pipx`) the first time it's needed.

## What it does

- **Picks the right template**: built-in templates (project report, research
  article, CV...) or any of the 80+ gallery templates (theses, internship
  reports, lab reports, conference papers, posters, beamer slides, letters,
  books...)
- **Scaffolds the project** with `latex-forge create`: folder structure,
  embedded styles, bibliography, VS Code live preview, all self-contained
- **Reads the project's `AGENTS.md`** before touching anything — every
  generated project ships its own briefing with file structure, custom
  commands, and common error fixes
- **Fills in the title page** (title, authors, university, supervisor,
  contacts...) from what you tell it
- **Writes the content**: sections, bibliography entries, figures,
  appendices, based on your notes, drafts, or data
- **Compiles and fixes errors** with `latex-forge build` / `watch`
- **Exports** the final sources + PDF as a submission-ready ZIP with
  `latex-forge export`

## Example

```
You: I need a project report for my Master's, AFNOR/ISO style, in French.
     Title is "Plateforme de gestion documentaire collaborative", three
     authors: me, Alice Martin and Baptiste Durand, supervised by
     Pr. Sophie Lefebvre. Here are my notes on the architecture and tests: ...

Claude: [creates the project from project-report-fr, fills in
        frontmatter/metadata.tex, writes sections/architecture.tex and
        sections/tests.tex from your notes, compiles, and reports any
        LaTeX errors]
```

## How it works

1. Make sure the `latex-forge` CLI is installed (`pipx install latex-forge`
   if missing)
2. Pick a template — built in, or installed from the
   [gallery](https://github.com/thmsgo18/latex-forge-gallery)
3. `latex-forge create --name ... --template ... --output ...`
4. Read the generated `AGENTS.md` — the authoritative guide for that project
5. Fill in `frontmatter/metadata.tex` and write the content in `sections/`
6. `latex-forge build`, fix any LaTeX errors, repeat
7. `latex-forge export` for a clean, submission-ready ZIP

The full instructions and template catalog live in
[`latex-forge/SKILL.md`](latex-forge/SKILL.md) and
[`latex-forge/references/`](latex-forge/references/).

## Requirements

- [Claude Code](https://docs.claude.com/en/docs/claude-code) (or any Claude
  client that supports skills)
- Python 3.10+ and [pipx](https://pipx.pypa.io) (the skill installs
  `latex-forge` for you if missing)
- A LaTeX distribution to compile locally — `latex-forge setup --install-tex`
  installs one if needed

## Related projects

| Project | What it adds |
|---|---|
| [**latex-forge**](https://github.com/thmsgo18/latex-forge) | The CLI this skill drives: scaffold, build, watch, export LaTeX projects |
| [**latex-forge-gallery**](https://github.com/thmsgo18/latex-forge-gallery) | The curated template gallery (80+ templates) and its [browsable website](https://thmsgo18.github.io/latex-forge-gallery/) |
| [**latex-forge-vscode**](https://github.com/thmsgo18/latex-forge-vscode) | The VS Code companion: create projects and browse the gallery without a terminal |

## Author

Made by [thmsgo18](https://github.com/thmsgo18)
