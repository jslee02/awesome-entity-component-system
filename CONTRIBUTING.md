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

## Inclusion & Exclusion Criteria

This is a **curated** list — not every ECS project belongs here. We use objective criteria to keep the list high-quality and fair.

### Acceptance

**Must-have** (all required):

- [ ] Relevant to ECS (entity-component-system pattern, data-oriented design, or ECS-powered application)
- [ ] Publicly accessible (open source, or well-documented commercial tool)
- [ ] Not a duplicate of an existing entry
- [ ] Has a meaningful description

**Scoring** (need ≥ 3 of 5):

- [ ] **Popularity**: ≥ 50 GitHub stars (or equivalent community adoption for non-GitHub projects)
- [ ] **Activity**: At least one commit within the last 2 years
- [ ] **Documentation**: Has a README with usage examples or API docs
- [ ] **Maturity**: Project is ≥ 6 months old (not premature/experimental)
- [ ] **Uniqueness**: Fills a niche not already covered by existing entries

| Result | Criteria | Action |
|--------|----------|--------|
| ✅ Accept | Meets all must-haves + ≥ 3 scoring points | Add to the main list |
| 🟡 Incubator | Meets all must-haves + 1–2 scoring points | Issue stays open with `incubator` label; re-evaluated when project matures |
| ❌ Reject | Fails any must-have | Issue closed with explanation |

### Removal

An existing entry may be removed if **any** of the following apply:

- Archived **and** superseded by another listed entry
- No commits in 5+ years **and** < 100 stars **and** no historical significance
- URL permanently broken (after link-check CI has flagged it for 3+ months)

### Exceptions

- **Historical significance**: Foundational libraries (e.g., EntityX, Artemis) are kept even if inactive — they remain important references.
- **Commercial tools**: Accepted if widely used in the ECS community, even without a public repo.

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
| Evaluate Submission | On `suggestion` label | Auto-evaluates suggested repos against inclusion criteria |
