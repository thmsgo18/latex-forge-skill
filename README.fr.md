<p align="right"><a href="./README.md">English</a> | <b>Français</b></p>

<p align="center">
  <b>Décrivez le document dont vous avez besoin à votre assistant IA. Il génère, rédige et compile le LaTeX pour vous.</b>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License MIT"></a>
  <a href="https://github.com/thmsgo18/latex-forge"><img src="https://img.shields.io/badge/works_with-latex--forge-blue?style=for-the-badge" alt="Works with latex-forge"></a>
  <img src="https://img.shields.io/badge/claude-skill-d97757?style=for-the-badge" alt="Claude Skill">
  <img src="https://img.shields.io/badge/AGENTS.md-compatible-555?style=for-the-badge" alt="AGENTS.md compatible">
</p>

<p align="center">
  <a href="#cest-quoi">Installation</a> •
  <a href="#ce-que-ça-fait">Ce que ça fait</a> •
  <a href="#exemple">Exemple</a> •
  <a href="#fonctionnement">Fonctionnement</a> •
  <a href="#compatibilité">Compatibilité</a> •
  <a href="#projets-liés">Projets liés</a>
</p>

---

## C'est quoi ?

Un skill pour assistants IA qui permet de piloter [LaTeX Forge](https://github.com/thmsgo18/latex-forge)
entièrement depuis une conversation : demandez un rapport de projet, un CV,
un chapitre de thèse, un article, un poster ou tout autre document, et votre
assistant génère un projet prêt à écrire depuis la
[galerie de templates](https://github.com/thmsgo18/latex-forge-gallery),
remplit votre page de garde et votre contenu, compile le PDF, et exporte le
résultat pour le rendu.

Ce skill ne duplique pas l'écosystème LaTeX Forge : il apprend à l'assistant
à utiliser la CLI `latex-forge`, à choisir un template parmi les 80+
disponibles, et à suivre le fichier `AGENTS.md` propre à chaque projet généré.

Deux versions sont fournies :

| Fichier | Pour | Expérience |
|---|---|---|
| [`latex-forge/SKILL.md`](latex-forge/SKILL.md) | [Claude Code](https://docs.claude.com/en/docs/claude-code/skills) | Complète : chargé automatiquement, charge son catalogue de templates et sa référence de commandes à la demande |
| [`AGENTS.md`](AGENTS.md) | Tout autre agent IA (Codex CLI, Cursor, Aider, Windsurf, Gemini CLI...) | Le même workflow, voir [Compatibilité](#compatibilité) pour les notes par outil |

## Installation

### Claude Code

Un [skill Claude Code](https://docs.claude.com/en/docs/claude-code/skills)
classique : un dossier contenant un `SKILL.md` que Claude charge
automatiquement quand c'est pertinent.

**Skill personnel** (disponible dans tous vos projets) :

```bash
git clone https://github.com/thmsgo18/latex-forge-skill.git /tmp/latex-forge-skill
mkdir -p ~/.claude/skills
cp -r /tmp/latex-forge-skill/latex-forge ~/.claude/skills/
rm -rf /tmp/latex-forge-skill
```

**Skill de projet** (uniquement pour le dépôt courant) :

```bash
git clone https://github.com/thmsgo18/latex-forge-skill.git /tmp/latex-forge-skill
mkdir -p .claude/skills
cp -r /tmp/latex-forge-skill/latex-forge .claude/skills/
rm -rf /tmp/latex-forge-skill
```

### Autres agents IA

Clonez (ou copiez) ce dépôt, puis pointez votre agent vers
[`AGENTS.md`](AGENTS.md) :

```bash
git clone https://github.com/thmsgo18/latex-forge-skill.git
```

- **Codex CLI** : copiez `AGENTS.md` (et le dossier
  `latex-forge/references/`) à la racine de votre projet, ou dans
  `~/.codex/AGENTS.md` pour des instructions globales — Codex lit
  `AGENTS.md` automatiquement.
- **Cursor / Windsurf / autres** : copiez le contenu de `AGENTS.md` dans le
  fichier de convention de votre outil (`.cursor/rules/latex-forge.mdc`,
  `.windsurfrules`, `GEMINI.md`, etc.), ou collez-le dans le chat / les
  instructions personnalisées.
- **Assistants sans accès au shell** : collez la section pertinente de
  `AGENTS.md` pour demander du contenu `.tex`, puis exécutez vous-même les
  commandes `latex-forge`.

Aucune configuration nécessaire dans les deux cas. Les instructions installent
elles-mêmes la CLI `latex-forge` (via `pipx`) la première fois que c'est
nécessaire.

## Ce que ça fait

- **Choisit le bon template** : templates intégrés (rapport de projet,
  article de recherche, CV...) ou l'un des 80+ templates de la galerie
  (thèses, rapports de stage, comptes rendus de TP, articles de conférence,
  posters, slides beamer, lettres, livres...)
- **Génère le projet** avec `latex-forge create` : arborescence, styles
  intégrés, bibliographie, prévisualisation PDF dans VS Code, le tout
  autonome
- **Lit le `AGENTS.md`** du projet avant toute modification — chaque projet
  généré embarque sa propre notice avec sa structure, ses commandes
  personnalisées et les erreurs courantes
- **Remplit la page de garde** (titre, auteurs, université, encadrant,
  contacts...) à partir de ce que vous lui indiquez
- **Rédige le contenu** : sections, références bibliographiques, figures,
  annexes, à partir de vos notes, brouillons ou données
- **Compile et corrige les erreurs** avec `latex-forge build` / `watch`
- **Exporte** les sources et le PDF final dans une archive prête à rendre
  avec `latex-forge export`

## Exemple

```
Vous : J'ai besoin d'un rapport de projet pour mon Master, style AFNOR/ISO,
       en français. Le titre est "Plateforme de gestion documentaire
       collaborative", trois auteurs : moi, Alice Martin et Baptiste Durand,
       encadrés par la Pr. Sophie Lefebvre. Voici mes notes sur
       l'architecture et les tests : ...

Assistant : [crée le projet à partir de project-report-fr, remplit
         frontmatter/metadata.tex, rédige sections/architecture.tex et
         sections/tests.tex à partir de vos notes, compile et signale
         les éventuelles erreurs LaTeX]
```

## Fonctionnement

1. Vérifie que la CLI `latex-forge` est installée (`pipx install latex-forge`
   si besoin)
2. Choisit un template — intégré, ou installé depuis la
   [galerie](https://github.com/thmsgo18/latex-forge-gallery)
3. `latex-forge create --name ... --template ... --output ...`
4. Lit le `AGENTS.md` généré — le guide de référence pour ce projet
5. Remplit `frontmatter/metadata.tex` et rédige le contenu dans `sections/`
6. `latex-forge build`, corrige les erreurs LaTeX, recommence
7. `latex-forge export` pour une archive propre, prête à rendre

## Compatibilité

Les deux fichiers décrivent le même workflow. Les différences viennent de ce
que chaque écosystème d'agent supporte réellement :

| Capacité | Claude Code (`latex-forge/SKILL.md`) | Autres agents (`AGENTS.md`) |
|---|---|---|
| Découverte automatique | Oui — Claude associe la description du skill à votre demande et le charge tout seul | Selon l'outil : Codex CLI et similaires lisent `AGENTS.md` automatiquement ; d'autres (Cursor, Windsurf, Gemini CLI...) ont besoin que le fichier soit copié dans leur propre convention, ou collé manuellement |
| Chargement à la demande des références | Oui — `references/templates.md` et `references/commands.md` ne sont lus que si nécessaire, ce qui limite le contexte utilisé | L'agent peut toujours les lire sur demande, mais pas de façon aussi automatique |
| `latex-forge watch` (compilation continue) | Supporté — Claude Code peut l'exécuter en arrière-plan et revenir vers vous | Seulement si votre agent gère les processus en arrière-plan ; sinon relancez `latex-forge build` après chaque modification |
| Installation de `latex-forge` via `pipx` sans demander | Oui, par conception | Dépend du modèle de permissions de votre outil — certains demanderont confirmation avant d'exécuter une commande shell, ce qui est normal |
| Aucun accès shell/fichiers (assistants en chat seul) | Non applicable | Le workflow ne peut pas s'exécuter ; l'assistant peut seulement vous aider à rédiger du contenu `.tex` à utiliser manuellement |

En résumé : tout fonctionne en conversation avec **Claude Code**. Avec
d'autres agents, les mêmes instructions s'appliquent, mais il faudra parfois
les déclencher manuellement, accepter des confirmations supplémentaires, ou
utiliser `build` à la place de `watch`.

## Prérequis

- Un assistant IA avec accès au shell et aux fichiers (Claude Code, Codex
  CLI, Cursor, Aider, Windsurf, Gemini CLI...)
- Python 3.10+ et [pipx](https://pipx.pypa.io) (les instructions installent
  `latex-forge` si nécessaire)
- Une distribution LaTeX pour compiler en local — `latex-forge setup --install-tex`
  en installe une si besoin

## Projets liés

| Projet | Ce qu'il apporte |
|---|---|
| [**latex-forge**](https://github.com/thmsgo18/latex-forge) | La CLI pilotée par ce skill : génération, build, watch, export de projets LaTeX |
| [**latex-forge-gallery**](https://github.com/thmsgo18/latex-forge-gallery) | La galerie de templates curée (80+) et son [site web](https://thmsgo18.github.io/latex-forge-gallery/) |
| [**latex-forge-vscode**](https://github.com/thmsgo18/latex-forge-vscode) | L'extension VS Code compagnon : créer des projets et parcourir la galerie sans terminal |

## Auteur

Créé par [thmsgo18](https://github.com/thmsgo18)
