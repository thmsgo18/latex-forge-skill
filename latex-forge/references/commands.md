# Command reference

Full reference for the [`latex-forge`](https://github.com/thmsgo18/latex-forge) CLI.

## Project lifecycle

| Command | Description |
|---|---|
| `latex-forge create --name N --template T --output DIR [--git]` | Create a project. All flags optional; omitted ones are prompted interactively (avoid that from a script — always pass `--name` and `--template`). `--git` runs `git init` with an initial commit. |
| `latex-forge build [DIR] [--clean] [--verbose]` | Compile to PDF with `latexmk`. Auto-installs missing LaTeX packages via `tlmgr` when possible. `--clean` removes `build/` first. `--verbose` shows full `latexmk` output (default: errors only). |
| `latex-forge watch [DIR] [--verbose]` | Recompile on every save (`latexmk -pvc`). Long-running — only use it if the user explicitly wants continuous compilation, and run it in the background. |
| `latex-forge export [DIR] [--output FILE]` | Bundle sources + compiled PDF into a ZIP for submission. Default output: `<project>-export.zip` next to the project. |
| `latex-forge rename [OLD] NEW` | Rename a project: folder, main `.tex` file, and build artifacts. Run from the parent directory with both names, or from inside the project with just the new name. |

## Templates

| Command | Description |
|---|---|
| `latex-forge list-templates` | List the 6 built-in templates with descriptions. |
| `latex-forge template list [--json]` | List built-in + user-installed templates. |
| `latex-forge template install SOURCE [--name N] [--force] [--engine E]` | Install a template from a GitHub URL (repo or `tree/branch/subdir`), a ZIP URL, a local `.zip`, or a local folder. `--engine {lualatex,xelatex,pdflatex}` declares the engine if the template doesn't already (writes `latexforge.toml`). |
| `latex-forge template update [NAME] [--json]` | Update installed gallery templates to their latest version (updates all if `NAME` omitted). |
| `latex-forge template remove NAME` | Remove a user-installed template. |

### Installing a custom template

Any source with a `main.tex` at its root works:

```bash
latex-forge template install https://github.com/someone/their-template
latex-forge template install ~/my-templates/lab-notes --name lab-notes
latex-forge template install https://github.com/someone/their-template --engine xelatex
```

For the template to also get profile auto-fill (title, authors, university...),
its `frontmatter/metadata.tex` should use the standard placeholder commands —
see [Profile](#profile) below. This is optional; without it the template still
installs and compiles, just without auto-fill.

## Environment

| Command | Description |
|---|---|
| `latex-forge setup [--check-only] [--skip-extensions] [--install-tex]` | Check/set up the environment: VS Code extensions and LaTeX toolchain. `--install-tex` installs a full TeX distribution for the current OS — slow, ask the user before running it. |
| `latex-forge diagnose [--json]` | Health check: latex-forge version, pipx, TeX Live (engines + version), `latexmk`, `biber`, profile, defaults. Use `--json` to parse programmatically. |
| `latex-forge completion [--shell SHELL]` | Print shell completion code for bash/zsh/fish. |
| `latex-forge --version` | Show the installed CLI version. |

## Profile

`~/.latex-forge/profile.toml` stores personal info that auto-fills new
projects (title page, contact details, etc.). `latex-forge profile set` is
**interactive only** (it requires a TTY) — from a Claude session, write the
file directly instead, using the schema below, then run `latex-forge create`
as usual (it reads the profile automatically).

| Key | Section | Meaning |
|---|---|---|
| `first_name` | identity | First name |
| `last_name` | identity | Last name |
| `email` | identity | Email |
| `phone` | identity | Phone |
| `website` | identity | Website |
| `github` | online | GitHub username |
| `linkedin` | online | LinkedIn username |
| `university` | academic | University |
| `faculty` | academic | Faculty / UFR |
| `program` | academic | Program / Formation |
| `supervisor` | academic | Supervisor |
| `company` | professional | Company |
| `department` | professional | Department / Service |
| `job_title` | professional | Job title |

Example:

```toml
first_name = "Alice"
last_name = "Martin"
email = "alice.martin@example.com"

github = "alice-martin"

university = "Universite Paris Cite"
program = "Master of Computer Science"
supervisor = "Pr. Sophie Lefebvre"
```

Other commands:

| Command | Description |
|---|---|
| `latex-forge profile show` | Display the current profile. |
| `latex-forge profile clear` | Delete the profile file. |

## Configuration

`~/.latex-forge.toml` sets defaults used when flags are omitted:

```toml
default_template = "project-report-en"
default_output_dir = "~/Documents/projects"
```

| Key | Description |
|---|---|
| `default_template` | Template used when `--template` is omitted |
| `default_output_dir` | Output directory used when `--output` is omitted |

## Generated project structure

```
my-project/
├── my-project.tex            <- main file (named after the project)
├── frontmatter/
│   ├── metadata.tex          <- title, authors, course (start here)
│   └── toc.tex
├── sections/                 <- one .tex file per section
├── backmatter/                <- acknowledgements, appendices
├── bibliography/
│   └── references.bib
├── figures/  images/  assets/logos/
├── styles/packages/           <- embedded styles, do not edit
├── .vscode/                   <- pre-configured for live PDF preview
├── GETTING_STARTED.md         <- guide for the user
├── AGENTS.md                  <- briefing for AI assistants — read first
└── .gitignore
```

Every project is fully self-contained: it compiles, shares, and versions
independently, with no dependency on the `latex-forge` repo itself.
