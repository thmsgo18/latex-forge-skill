# LaTeX Forge - agent instructions

These are generic instructions for any AI coding agent (Codex CLI, Cursor,
Aider, Windsurf, Gemini CLI, or similar) that has shell and file access. They
explain how to use the [`latex-forge`](https://github.com/thmsgo18/latex-forge)
CLI and its [template gallery](https://github.com/thmsgo18/latex-forge-gallery)
to create, write, compile and export LaTeX documents (project reports,
internship reports, theses, research papers, lab reports, CVs, posters,
presentations, letters, books...).

> **Using Claude Code?** Use the dedicated skill in
> [`latex-forge/SKILL.md`](latex-forge/SKILL.md) instead — it is
> auto-discovered and loads its reference files on demand. This file is the
> portable equivalent for other agents, see
> [README.md](README.md#compatibility) for per-tool notes and limitations.

Always work inside the project that `latex-forge create` generates. Never
hand-roll a LaTeX project structure when a suitable template exists.

## Step 1 - Make sure the CLI is available

```bash
latex-forge --version
```

If the command is not found, install it (small, reversible, user-level
Python package — confirm with the user first if your tool requires
confirmation before running shell commands):

```bash
command -v pipx >/dev/null 2>&1 || python3 -m pip install --user pipx
pipx ensurepath
pipx install latex-forge
```

If `latex-forge` is still not on `PATH` after install, call it via
`~/.local/bin/latex-forge` (or `pipx run latex-forge ...`) for the rest of
the session, or open a new shell.

## Step 2 - Check the LaTeX toolchain

```bash
latex-forge diagnose --json
```

This reports whether a TeX distribution (pdflatex/xelatex/lualatex),
`latexmk` and `biber` are available. If the toolchain is missing, **ask the
user before** running the heavy installer (it downloads a full TeX
distribution):

```bash
latex-forge setup --install-tex
```

If the user just wants the project files (no local compilation), you can
skip this step entirely.

## Step 3 - Choose the right template

Ask the user (briefly, only what's needed): document type (report, thesis,
CV, paper, poster, presentation, letter...), language, and any institutional
requirements (university template, IEEE/ACM/AFNOR style, etc.).

Six templates are built in and need no install:

| Template | Use for |
|---|---|
| `blank` | Minimal document, anything custom |
| `project-report-en` | University project report, ISO/IEEE style (English) |
| `project-report-fr` | Rapport de projet universitaire, AFNOR/ISO (French) |
| `research` | Two-column research article |
| `cv-en` | English CV / résumé |
| `cv-fr` | CV en français |

For everything else (theses, internship reports, lab reports, conference
papers, posters, beamer slides, letters, books, the UPC L3 report set, and
many more CVs), see [`latex-forge/references/templates.md`](latex-forge/references/templates.md)
for the full catalog with install URLs. A gallery template must be installed
once before it can be used:

```bash
latex-forge template install https://github.com/thmsgo18/latex-forge-gallery/tree/main/templates/<category>/<name>
```

The user can also point to **their own template** (any GitHub repo, ZIP, or
local folder with a `main.tex` at its root) — see
[`latex-forge/references/commands.md`](latex-forge/references/commands.md#installing-a-custom-template).

## Step 4 - Create the project

Use the non-interactive form so it works from a script:

```bash
latex-forge create --name <project-name> --template <template> --output <dir> [--git]
```

- `<project-name>`: kebab-case, derive it from the document's subject if the
  user didn't give one.
- `<template>`: a built-in name or the name used at install time for a
  gallery template.
- `--output`: ask where to put it if unclear (defaults to the current
  directory).
- `--git`: pass it if the user wants version control from the start.

## Step 5 - Read `AGENTS.md` first, before touching anything

Every generated project ships its own `AGENTS.md` at its root: a
self-contained briefing written specifically for this project and template.
**Read it before making any edit.** It documents:

- the file structure and what each folder is for
- the exact compile command (and engine: pdflatex/xelatex/lualatex)
- custom LaTeX commands defined by the template's styles
- how to add sections, bibliography entries, images, and appendices
- common compilation errors and their fixes
- files that must **not** be modified (usually `styles/packages/*` and
  `assets/logos/`)

Treat that generated `AGENTS.md` as the source of truth for the project; this
file covers everything *before* and *around* it (choosing/installing the
template, building, exporting).

## Step 6 - Fill in metadata and personal info

Edit `frontmatter/metadata.tex` (or `sections/heading.tex` /
`sections/en-tete.tex` for CV templates) with the user's real information:
title, authors, university, supervisor, contact details, links, etc. The
generated `AGENTS.md` lists the exact commands used by that template (e.g.
`\reporttitle`, `\addauthor{Name}{}`, `\cvname`, `\universityname`...).

If the user wants their info pre-filled automatically on **future** projects
too, see [`latex-forge/references/commands.md`](latex-forge/references/commands.md#profile)
for the profile schema (`~/.latex-forge/profile.toml`) — write it directly
with file tools rather than `latex-forge profile set`, which requires an
interactive terminal.

## Step 7 - Write the content

Following the structure described in the project's `AGENTS.md`:

- one `.tex` file per section under `sections/`, `\input{}` from the main
  file
- bibliography entries go in `bibliography/references.bib`, cited with
  `\cite{}`
- images go in `images/` (or `figures/` for TikZ sources)
- appendices after `\startannexes` (or the template's equivalent)

Write real content based on what the user provides (notes, transcripts,
code, data, existing drafts) — don't leave placeholder text in the final
document.

## Step 8 - Build, fix errors, iterate

```bash
latex-forge build            # compile once -> build/<name>.pdf
latex-forge build --clean    # wipe build artifacts first
latex-forge build --verbose  # full latexmk output
```

`latex-forge build` already auto-installs missing LaTeX packages via `tlmgr`
when possible. If compilation still fails, read `build/<name>.log`, fix the
`.tex` source, and rebuild. Cross-check unexpected errors against the
"Common errors and fixes" table in the project's `AGENTS.md`.

`latex-forge watch` recompiles on every save but runs forever — only use it
if your tool can run commands in the background, otherwise prefer running
`latex-forge build` again after each change.

## Step 9 - Export when the document is done

```bash
latex-forge export                    # -> ../<name>-export.zip
latex-forge export --output FILE.zip  # custom path
```

Bundles the sources and the compiled PDF into a clean ZIP, ready for
submission.

## Other useful commands

```bash
latex-forge rename new-name      # rename project, main file and build artifacts
latex-forge list-templates       # list built-in templates
latex-forge template list        # list built-in + installed templates
latex-forge template update      # update installed gallery templates
```

Full reference: [`latex-forge/references/commands.md`](latex-forge/references/commands.md).
