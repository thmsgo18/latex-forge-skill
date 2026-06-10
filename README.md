<p align="right"><b>English</b> | <a href="./README.fr.md">Français</a></p>

<p align="center">
  <b>Tell your AI assistant what document you need. It scaffolds, writes, and compiles the LaTeX for you.</b>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License MIT"></a>
  <a href="https://github.com/thmsgo18/latex-forge"><img src="https://img.shields.io/badge/works_with-latex--forge-blue?style=for-the-badge" alt="Works with latex-forge"></a>
  <img src="https://img.shields.io/badge/claude-skill-d97757?style=for-the-badge" alt="Claude Skill">
  <img src="https://img.shields.io/badge/AGENTS.md-compatible-555?style=for-the-badge" alt="AGENTS.md compatible">
</p>

<p align="center">
  <a href="#install">Install</a> •
  <a href="#what-it-does">What it does</a> •
  <a href="#example">Example</a> •
  <a href="#how-it-works">How it works</a> •
  <a href="#compatibility">Compatibility</a> •
  <a href="#related-projects">Related projects</a>
</p>

---

## What is this?

A skill for AI coding assistants that turns [LaTeX Forge](https://github.com/thmsgo18/latex-forge)
into something you can drive entirely from a conversation: ask for a project
report, a CV, a thesis chapter, a paper, a poster, or any other document, and
your assistant scaffolds a ready-to-write project from the
[template gallery](https://github.com/thmsgo18/latex-forge-gallery), fills in
your title page and content, compiles it to PDF, and exports it for
submission.

It does not duplicate the LaTeX Forge ecosystem: it teaches the assistant how
to use the `latex-forge` CLI, how to pick a template from the 80+ available,
and how to follow each generated project's own `AGENTS.md` briefing.

Two flavors are included:

| File | For | Experience |
|---|---|---|
| [`latex-forge/SKILL.md`](latex-forge/SKILL.md) | [Claude Code](https://docs.claude.com/en/docs/claude-code/skills) | Full: auto-discovered, loads its template/command reference on demand |
| [`AGENTS.md`](AGENTS.md) | Any other AI coding agent (Codex CLI, Cursor, Aider, Windsurf, Gemini CLI...) | Same workflow, see [Compatibility](#compatibility) for per-tool notes |

## Install

### Claude Code

A plain [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills):
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

### Other AI coding agents

Clone (or copy) this repository, then point your agent at
[`AGENTS.md`](AGENTS.md):

```bash
git clone https://github.com/thmsgo18/latex-forge-skill.git
```

- **Codex CLI**: copy `AGENTS.md` (and the `latex-forge/references/` folder)
  to your project root, or to `~/.codex/AGENTS.md` for a global instruction
  set — Codex reads `AGENTS.md` automatically.
- **Cursor / Windsurf / others**: copy `AGENTS.md`'s content into your
  tool's convention file (`.cursor/rules/latex-forge.mdc`,
  `.windsurfrules`, `GEMINI.md`, etc.), or paste it into the chat / custom
  instructions.
- **Chat-only assistants** (no shell access): paste the relevant section of
  `AGENTS.md` to ask for `.tex` content, then run the `latex-forge` commands
  yourself.

No configuration either way. The instructions install the `latex-forge` CLI
themselves (via `pipx`) the first time it's needed.

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

Assistant: [creates the project from project-report-fr, fills in
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

## Compatibility

Both files describe the same workflow. The differences come from what each
agent ecosystem actually supports:

| Capability | Claude Code (`latex-forge/SKILL.md`) | Other agents (`AGENTS.md`) |
|---|---|---|
| Automatic discovery | Yes — Claude matches the skill's description to your request and loads it on its own | Depends on the tool: Codex CLI and similar auto-read `AGENTS.md`; others (Cursor, Windsurf, Gemini CLI...) need the file copied to their own convention, or pasted manually |
| On-demand reference loading | Yes — `references/templates.md` and `references/commands.md` are only read when needed, keeping context small | The agent can still read them on request, but won't do it automatically the same way |
| Long-running `latex-forge watch` | Supported — Claude Code can run it in the background and report back | Only if your agent supports background processes; otherwise re-run `latex-forge build` after each change |
| Installing `latex-forge` via `pipx` without asking | Yes, by design | Depends on your tool's permission model — some will ask for confirmation before running shell commands, which is expected |
| No shell/file access at all (chat-only assistants) | Not applicable | The workflow can't run; the assistant can only help draft `.tex` text for you to use manually |

In short: everything works as a conversation with **Claude Code**. With other
agents, the same instructions apply, but you may need to trigger them
manually, accept extra confirmation prompts, or run `build` instead of
`watch`.

## Requirements

- An AI coding assistant with shell and file access (Claude Code, Codex CLI,
  Cursor, Aider, Windsurf, Gemini CLI...)
- Python 3.10+ and [pipx](https://pipx.pypa.io) (the instructions install
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
