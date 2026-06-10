# Template catalog

Source of truth: [latex-forge-gallery](https://github.com/thmsgo18/latex-forge-gallery)
([browsable website](https://thmsgo18.github.io/latex-forge-gallery/)).

## Built in (no install needed)

| Name | Language | Description |
|---|---|---|
| `blank` | English | Minimal document: title, one section, ready to grow |
| `project-report-en` | English | ISO/IEEE project report: requirements, architecture, testing, bibliography |
| `project-report-fr` | French | AFNOR/ISO project report: cahier des charges, architecture, tests, bibliographie |
| `research` | English | Two-column research article: related work, methodology, experiments, bibliography |
| `cv-en` | English | CV / resume: education, experience, projects, skills |
| `cv-fr` | French | CV: formation, experience, projets, competences |

Use directly: `latex-forge create --name <project> --template <name> --output <dir>`

## Gallery templates

Install with:

```bash
latex-forge template install https://github.com/thmsgo18/latex-forge-gallery/tree/main/templates/<category>/<name>
```

then `latex-forge create --name <project> --template <name> --output <dir>`.
The `<category>` folder for each template is the leftmost column below.

### cv

| Name | Description | Engine |
|---|---|---|
| `awesome-cv` | Elegant CV with colored sections and FontAwesome icons | XeLaTeX |
| `deedy-resume` | Two-column resume with a clean, professional layout | XeLaTeX |
| `altacv` | CV with TikZ skill bars and timeline | LuaLaTeX |
| `moderncv` | Highly customizable CV with multiple styles | pdfLaTeX |
| `hipster-cv` | Colorful sidebar CV design | XeLaTeX |
| `twenty-seconds-cv` | Sidebar CV designed to be skimmed in 20 seconds | pdfLaTeX |
| `developer-cv` | Academic CV with automatic BibTeX publication list | pdfLaTeX |
| `sidebar-cv` | Modern CV with styled sidebar | pdfLaTeX |
| `friggeri-cv` | Stylish A4 CV with colored section bars and BibTeX publications | XeLaTeX |
| `resume-openfont` | Minimalist single-page resume using open-source fonts | pdfLaTeX |
| `billryan-resume` | Elegant bilingual (English/Chinese) resume with FontAwesome | XeLaTeX |
| `mcdowell-cv` | McDowell-style ATS-friendly CV | pdfLaTeX |
| `rover-resume` | ATS-friendly resume with unique styling | pdfLaTeX |
| `classic-cv` | Traditional single-column CV | pdfLaTeX |
| `two-column-cv` | Two-column CV with photo and QR code | pdfLaTeX |
| `infographic-cv` | Infographic-style CV with visual skill bars | XeLaTeX |
| `minimalist-cv` | Ultra-minimalist single-page CV | pdfLaTeX |
| `modern-cv` | Modern CV with colored sidebar and skill bars | XeLaTeX |
| `rows-cv` | Row-based CV layout with clean horizontal sections | XeLaTeX |
| `sidebarleft-cv` | CV with left-aligned sidebar and icon-based contact info | XeLaTeX |
| `infographics2-cv` | Second infographic-style CV with visual skill bars and timeline | XeLaTeX |
| `cv-en` | English CV with FontAwesome icons (also built in) | LuaLaTeX |
| `cv-fr` | French CV with FontAwesome icons (also built in) | LuaLaTeX |

### thesis

| Name | Description | Engine |
|---|---|---|
| `clean-thesis` | Clean, simple, and elegant thesis style | pdfLaTeX |
| `cambridge-thesis` | PhD thesis template for Cambridge University | pdfLaTeX |
| `memoir-thesis` | Professional dissertation with polished typography | pdfLaTeX |
| `dissertate` | Pre-formatted templates for Harvard, Princeton, and NYU | XeLaTeX |
| `tufte-thesis` | Elegant book-style thesis inspired by Edward Tufte | pdfLaTeX |
| `mimosis-thesis` | Beautiful minimalist thesis with elegant typography | pdfLaTeX |
| `oxford-thesis` | PhD thesis template for the University of Oxford | pdfLaTeX |
| `tuda-thesis` | Official TU Darmstadt thesis following university corporate design | pdfLaTeX |

### article

| Name | Description | Engine |
|---|---|---|
| `neurips-paper` | Scientific paper template for modern academic conferences | pdfLaTeX |
| `ieee-article` | IEEE-style article using IEEEtran class | pdfLaTeX |
| `acm-article` | LNCS/Springer-style article for CS conferences | pdfLaTeX |
| `cvpr-paper` | CVPR/ICCV paper template, up-to-date for 2026 | pdfLaTeX |
| `arxiv-template` | Clean arXiv-style preprint template | pdfLaTeX |
| `elsarticle` | Elsevier CAS journal article template | pdfLaTeX |
| `springer-lncs` | Enhanced Springer LNCS article template for CS conferences | pdfLaTeX |
| `elegantpaper` | Elegant working paper and preprint template | pdfLaTeX |
| `research` | Two-column academic research article (also built in) | LuaLaTeX |

### report

| Name | Description | Engine |
|---|---|---|
| `elegant-report` | Clean and elegant report with bibliography support | pdfLaTeX |
| `technical-report` | Professional technical/term paper template | pdfLaTeX |
| `internship-report` | UTBM-style internship report with professional formatting | pdfLaTeX |
| `project-report` | Academic project report with certificate pages | pdfLaTeX |
| `math-notes` | Minimalist math notes with theorem environments | pdfLaTeX |
| `elegant-notes` | Beautiful note-taking template with theorem environments | pdfLaTeX |
| `homework-template` | Clean university homework template with problem/solution environments | pdfLaTeX |
| `lab-report` | Laboratory report template in article style | pdfLaTeX |
| `essay-collection` | Multi-essay collection report with individual abstracts and bibliography | pdfLaTeX |
| `project-report-en` | University project report, requirements/architecture/testing/bibliography (also built in) | LuaLaTeX |
| `project-report-fr` | Rapport de projet universitaire, AFNOR/ISO (also built in) | LuaLaTeX |

### presentation

| Name | Description | Engine |
|---|---|---|
| `beamer-metropolis` | Modern, minimal Beamer theme | XeLaTeX |
| `beamer-focus` | Minimalist Beamer theme with dark color scheme | pdfLaTeX |
| `beamer-elegant` | Elegant Beamer slides with figure support | pdfLaTeX |
| `beamer-corporate` | Professional Beamer slides with configurable colors | pdfLaTeX |
| `beamer-simple` | Simple Beamer template focused on content | pdfLaTeX |
| `beamer-auriga` | Dark-themed Beamer presentation with a modern, polished look | pdfLaTeX |

### letter

| Name | Description | Engine |
|---|---|---|
| `cover-letter-modern` | Modern cover letter with clean typography | XeLaTeX |
| `formal-letter` | Journal-style cover letter with professional formatting | pdfLaTeX |
| `motivation-letter` | Motivation letter for academic and job applications | pdfLaTeX |
| `moderncv-letter` | Cover letter using the moderncv class | pdfLaTeX |

### poster

| Name | Description | Engine |
|---|---|---|
| `beamerposter-landscape` | Landscape academic poster built with Beamer | pdfLaTeX |
| `tikzposter` | Academic poster using TikZposter | pdfLaTeX |
| `academic-poster` | Gemini-themed academic conference poster | pdfLaTeX |
| `gemini-poster` | Gemini beamerposter template with clean, modern design | pdfLaTeX |

### book

| Name | Description | Engine |
|---|---|---|
| `elegantbook` | Elegant book template with beautiful chapter styling | XeLaTeX |
| `legrand-orange-book` | Structured book template with color-coded chapters | XeLaTeX |

### cheatsheet

| Name | Description | Engine |
|---|---|---|
| `cheatsheet` | Compact multi-column cheatsheet template for quick reference cards | pdfLaTeX |

### misc

| Name | Description | Engine |
|---|---|---|
| `invoice-simple` | Clean single-page invoice template using the scrlttr2 class | pdfLaTeX |
| `invoice-multipage` | Multi-page invoice template with itemized table and totals | pdfLaTeX |
| `timesheet` | Monthly timesheet template with daily hours tracking table | pdfLaTeX |
| `poem` | Elegant poem typesetting template with verse environments | pdfLaTeX |

### project-upc — Projet Informatique L3 (Universite Paris Cite)

8 templates for the standard documents of the L3 Computer Science Project at
Universite Paris Cite. UPC visual identity, fully in French, pdfLaTeX.

| Name | Description |
|---|---|
| `upc-cahier-des-charges` | Requirements specification |
| `upc-rapport-final` | Final report |
| `upc-conception-detaillee` | Detailed design |
| `upc-manuel-installation` | Installation manual |
| `upc-manuel-utilisation` | User manual |
| `upc-rapport-tests` | Test report |
| `upc-documentation-technique` | Technical documentation |
| `upc-cahier-recette` | Acceptance test plan |

## Picking a template — quick heuristics

- "Rapport de projet / project report" (university, with requirements +
  architecture + tests + biblio) -> `project-report-en` / `project-report-fr`
  (built in), or `report/internship-report`, `report/technical-report`,
  `report/project-report` for other styles.
- "These / PhD thesis" -> `thesis/*` (pick by university style requested).
- "Article / paper for a conference or journal" -> `article/*` (match the
  venue: `ieee-article`, `acm-article`, `neurips-paper`, `cvpr-paper`,
  `arxiv-template`, `elsarticle`, `springer-lncs`, or `research` built in).
- "CV / resume" -> `cv-en` / `cv-fr` (built in) or any `cv/*` for a specific
  visual style.
- "Slides / presentation" -> `presentation/*` (Beamer themes).
- "Poster" -> `poster/*`.
- "Lettre de motivation / cover letter" -> `letter/*`.
- "Rapport L3 UPC" (cahier des charges, conception, manuel, recette...) ->
  the matching `project-upc/upc-*` template.

When unsure, ask the user which institution/venue style they need, or browse
the [gallery website](https://thmsgo18.github.io/latex-forge-gallery/) for
previews.
