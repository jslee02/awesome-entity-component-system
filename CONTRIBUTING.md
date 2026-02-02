# Contributing

Thank you for improving this list! This guide explains how to add libraries, fix entries, and work with the project.

## How It Works

This repository uses a **YAML-first** workflow:

```
data/*.yaml  -->  scripts/generate_readme.py  -->  README.md
```

- **Source of truth**: YAML files in `data/` (one per section)
- **Schema**: `schema/entry.schema.json` defines valid entry fields
- **Generator**: `scripts/generate_readme.py` builds README.md from YAML
- **Do not edit README.md by hand** — changes will be overwritten on the next generation

## Adding a Library

1. Find the right YAML file in `data/` (e.g., `data/ecs-libraries.yaml`, `data/game-engines.yaml`)

2. Add your entry in alphabetical order within the file:

   ```yaml
   - name: MyECSLibrary
     url: https://myecslibrary.org
     github: owner/repo
     description: One-line description of what it does
     _subsection: "C/C++"
   ```

3. Regenerate README.md:

   ```bash
   pixi run generate
   ```

4. Commit both the YAML file and README.md:

   ```bash
   git add data/ecs-libraries.yaml README.md
   git commit --signoff -m "content: add MyECSLibrary to ecs-libraries"
   ```

> **Tip**: If you cannot run the generator locally, submit your PR with just the YAML change and note it in the PR description. A maintainer will regenerate README.md for you.

### Entry Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Library display name |
| `url` | | Project website |
| `github` | | GitHub `owner/repo` (e.g., `skypjack/entt`) |
| `gitlab` | | GitLab path |
| `description` | | Brief description |
| `archived` | | Set `true` if the project is archived |
| `_subsection` | | Language grouping within a section (e.g., "C/C++", "Rust") |

### Which YAML File?

| Section | File |
|---------|------|
| ECS Libraries | `data/ecs-libraries.yaml` |
| Game Engines | `data/game-engines.yaml` |
| Graphics Engines | `data/graphics-engines.yaml` |
| Physics Libraries | `data/physics-libraries.yaml` |
| Benchmarks | `data/benchmarks.yaml` |
| Blog Posts | `data/blog-posts.yaml` |
| Talks & Slides | `data/talks.yaml` |
| Books | `data/books.yaml` |
| Tutorials | `data/tutorials.yaml` |
| Lists | `data/lists.yaml` |
| ETC | `data/etc.yaml` |

## Editing Existing Entries

Edit the corresponding field in the relevant `data/*.yaml` file, then regenerate README.md.

Common edits:
- **Fix a URL**: update `url` or `github`
- **Update description**: update `description`
- **Mark as archived**: add `archived: true`
- **Remove an entry**: delete the entire entry block

## Editing Non-Data Content

Content that is not per-entry data (section headings, table of contents, descriptions, contributing/license text) is defined in `scripts/generate_readme.py`. Edit the script directly for these changes.

## Local Development

### Prerequisites

- Python 3.10+

### Validate entries

```bash
pip install pyyaml jsonschema
python3 scripts/validate_entries.py
```

### Regenerate README.md

```bash
pip install pyyaml
python3 scripts/generate_readme.py
```

### Check links (optional)

Install [lychee](https://lychee.cli.rs/) and run:

```bash
lychee --config .lychee.toml '**/*.md'
```

## What CI Checks

Every pull request that touches `data/`, `schema/`, or `scripts/` runs these checks:

| Check | Description |
|-------|-------------|
| **Validate Data** | YAML entries pass JSON schema validation |
| **README Freshness** | README.md matches the generated output from YAML |
| **Check Links** | All URLs in markdown files are reachable |

## Guidelines

- One library per pull request (when possible)
- Alphabetical order within each section
- Keep descriptions short and descriptive
- Sign your commits: `git commit --signoff`
- Check your spelling and grammar

## For Maintainers

### Regenerating README for a contributor

If a contributor submits a YAML-only PR without regenerating README.md:

```bash
gh pr checkout <PR-NUMBER>
pip install pyyaml
python3 scripts/generate_readme.py
git add README.md
git commit --signoff -m "docs: regenerate README.md"
git push
```

### Automated workflows

| Workflow | Schedule | Description |
|----------|----------|-------------|
| Check Links | Weekly (Mon 8am UTC) | Checks for broken links; auto-creates fix PRs |
| Update Metadata | Weekly (Mon 6am UTC) | Fetches GitHub stars/activity; creates update PR |
| Validate Data | On PR | Validates YAML schema and README freshness |
