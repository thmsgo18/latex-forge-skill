---
name: latex-forge
description: Create, fill in, compile and export LaTeX documents (project reports, internship reports, theses, research papers, lab reports, CVs, posters, presentations, letters, books...) using the latex-forge CLI and its 80+ template gallery. Use this skill whenever the user asks to write a report, paper, thesis, CV or any academic/professional LaTeX document, or to scaffold, build, watch or export a latex-forge project.
---

# LaTeX Forge

LaTeX Forge turns a single command into a complete, self-contained, ready-to-write
LaTeX project: folder structure, embedded styles, bibliography setup, and a
pre-configured VS Code workspace with live PDF preview. This skill drives the
[`latex-forge`](https://github.com/thmsgo18/latex-forge) CLI and its
[template gallery](https://github.com/thmsgo18/latex-forge-gallery) (80+ templates)
to scaffold the project, then writes the actual content for the user.

Always work inside the project that `latex-forge create` generates. Never hand-roll
a LaTeX project structure when a suitable template exists.

## Step 1 - Make sure the CLI is available

```bash
latex-forge --version
```

If the command is not found, install it without asking (it is a small, reversible,
user-level tool — no admin rights, no Python needed beforehand):

```bash
# Installs uv if needed (it brings its own Python), then latex-forge.
# LATEX_FORGE_TEX=none: LaTeX itself is handled in Step 2.
curl -LsSf https://raw.githubusercontent.com/thmsgo18/latex-forge/main/install.sh | LATEX_FORGE_TEX=none sh
```

On Windows (PowerShell): `$env:LATEX_FORGE_TEX='none'; irm https://raw.githubusercontent.com/thmsgo18/latex-forge/main/install.ps1 | iex`.
If uv or pipx is already set up, `uv tool install latex-forge` / `pipx install latex-forge` work too. If
`latex-forge` is still not on `PATH` after install, call it via
`~/.local/bin/latex-forge` for the rest of the session, or open a new shell.

## Step 2 - Check the LaTeX toolchain

```bash
latex-forge diagnose --json
```

This reports whether a TeX distribution (pdflatex/xelatex/lualatex), `latexmk`
and `biber` are available (`texlive.ok` and `latexmk.ok`), which distribution it
is (`tex_distribution.label`) and whether missing LaTeX packages can be
installed automatically (`tex_distribution.can_install_packages`). TeX is found
even when it isn't on PATH, so trust this rather than `which lualatex`.

If the toolchain is missing, **ask the user before** installing it. The default
is light (TinyTeX in the home folder, ~500 MB, a few minutes, no admin password);
offer `--tex full` (all of TeX Live, ~2 GB) if they want everything offline:

```bash
latex-forge setup --install-tex --yes --skip-extensions
```

It ends with a test compile; exit code 0 means LaTeX works. Never run
`--tex system` yourself: it needs the user's administrator password in a
terminal.

If the user just wants the project files (no local compilation), you can skip
this step entirely.

## Step 3 - Choose the right template

Ask the user (briefly, only what's needed): document type (report, thesis, CV,
paper, poster, presentation, letter...), language, and any institutional
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
many more CVs), see [references/templates.md](references/templates.md) for
the full catalog with install URLs. A gallery template must be installed once
before it can be used:

```bash
latex-forge template install https://github.com/thmsgo18/latex-forge-gallery/tree/main/templates/<category>/<name>
```

The user can also point to **their own template** (any GitHub repo, ZIP, or
local folder with a `main.tex` at its root) — see
[references/commands.md](references/commands.md#installing-a-custom-template).

## Step 4 - Create the project

Use the non-interactive form so it works from a script:

```bash
latex-forge create --name <project-name> --template <template> --output <dir> --repo none
```

- `<project-name>`: kebab-case, derive it from the document's subject if the
  user didn't give one.
- `<template>`: a built-in name or the name used at install time for a gallery
  template.
- `--output`: ask where to put it if unclear (defaults to the current directory).
- `--repo`: `none` (default), `existing` if the folder already lives inside a
  git repository, or `create` to also create a new GitHub repository (needs the
  GitHub CLI, authenticated — ask the user first, and add `--repo-name` and
  `--visibility private|public`). With `create`/`existing`, `--sharing
  full|pdf-only` sets what the `.gitignore` tracks.
- On a light TinyTeX, `create` also installs the LaTeX packages the template
  needs (a few seconds to a minute); `--skip-packages` skips that when offline.

## Step 5 - Read `AGENTS.md` first, before touching anything

Every generated project ships an `AGENTS.md` at its root: a self-contained
briefing written specifically for this project and template. **Read it before
making any edit.** It documents:

- the file structure and what each folder is for
- the exact compile command (and engine: pdflatex/xelatex/lualatex)
- custom LaTeX commands defined by the template's styles
- how to add sections, bibliography entries, images, and appendices
- common compilation errors and their fixes
- files that must **not** be modified (usually `styles/packages/*` and
  `assets/logos/`)

Treat `AGENTS.md` as the source of truth for that project; this skill covers
everything *before* and *around* it (choosing/installing the template,
building, exporting).

## Step 6 - Fill in metadata and personal info

Edit `frontmatter/metadata.tex` (or `sections/heading.tex` / `sections/en-tete.tex`
for CV templates) with the user's real information: title, authors, university,
supervisor, contact details, links, etc. `AGENTS.md` lists the exact commands
used by that template (e.g. `\reporttitle`, `\addauthor{Name}{}`, `\cvname`,
`\universityname`...).

If the user wants their info pre-filled automatically on **future** projects
too, see [references/commands.md](references/commands.md#profile) for the
profile schema (`~/.latex-forge/profile.toml`) — write it directly with the
file tools rather than `latex-forge profile set`, which requires an
interactive terminal.

## Step 7 - Write the content

**Ground the report in its source material first.** A report documents real work, not
imagination. If the user points you to a project — a code repository, a dataset,
notes, an existing draft, a folder — read it thoroughly before writing, and base every
factual claim, code excerpt, architecture description and result on what is actually
there. If you are writing in-place inside an existing project, that surrounding project
*is* the source. Where a needed result or figure isn't available, mark it with a
`% TODO` rather than inventing it.

Following the structure described in `AGENTS.md`:

- one `.tex` file per section under `sections/`, `\input{}` from the main file
- bibliography entries go in `bibliography/references.bib`, cited with `\cite{}`
- images go in `images/` (or `figures/` for TikZ sources)
- appendices after `\startannexes` (or the template's equivalent)

Write real content based on what the user provides (notes, transcripts, code,
data, existing drafts) — don't leave placeholder text in the final document.

## Step 8 - Build, fix errors, iterate

```bash
latex-forge build            # compile once -> build/<name>.pdf
latex-forge build --clean    # wipe build artifacts first
latex-forge build --verbose  # full latexmk output
latex-forge watch            # recompile on every save
```

`latex-forge build` already installs missing LaTeX packages, fonts and
bibliography styles via `tlmgr` and recompiles, whenever the distribution allows
it (the light TinyTeX does). With a system-wide TeX Live it prints the
`sudo tlmgr install ...` command instead: relay it to the user rather than running
sudo yourself. If compilation still fails, read `build/<name>.log`, fix the
`.tex` source, and rebuild. Cross-check unexpected errors against the "Common
errors and fixes" table in `AGENTS.md`.

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

Full reference: [references/commands.md](references/commands.md).
