#!/usr/bin/env python3
"""Generate README.md from data/*.yaml files."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path
from typing import TypedDict, cast

import yaml


class EntryMeta(TypedDict, total=False):
    stars: int
    last_commit: str
    archived: bool
    license: str
    language: str


class Entry(TypedDict, total=False):
    name: str
    url: str
    github: str
    gitlab: str
    description: str
    archived: bool
    _meta: EntryMeta
    _subsection: str


SECTIONS = [
    ("ecs-libraries", "ECS Libraries", 2, "bullet", 4),
    ("game-engines", "Game Engines", 3, "bullet", 4),
    ("graphics-engines", "Graphics Engines", 3, "bullet", 4),
    ("physics-libraries", "Physics Libraries", 3, "bullet", 4),
    ("benchmarks", "Benchmarks", 3, "resource", None),
    ("blog-posts", "Blog Posts", 3, "resource", None),
    ("talks", "Talks & Slides", 3, "resource", None),
    ("books", "Books", 3, "resource", None),
    ("tutorials", "Tutorials", 3, "resource", None),
    ("lists", "Lists", 3, "resource", None),
    ("references", "References", 3, "resource", None),
]

# Non-software categories, reviewed by hand by the shared suggestion triage even when they link
# a GitHub repository.
MANUAL_REVIEW = {"blog-posts", "talks", "books", "tutorials", "references"}

SECTION_DESCRIPTIONS = {
    "ecs-libraries": "Libraries and frameworks implementing the Entity-Component-System pattern.",
    "game-engines": "Game engines built on ECS architecture.",
    "graphics-engines": "Graphics and rendering engines using ECS.",
    "physics-libraries": "Physics simulation libraries organized as ECS.",
    "benchmarks": "Performance benchmarks comparing ECS frameworks.",
    "blog-posts": "Articles and blog posts about ECS and data-oriented design.",
    "talks": "Conference talks and presentations about ECS.",
    "books": "Books on ECS and data-oriented design.",
    "tutorials": "Tutorial series for learning ECS.",
    "lists": "Related curated lists.",
    "references": "Wikis, FAQs, glossaries, and other reference material on ECS.",
}

SUBSECTION_ORDER = {
    "ecs-libraries": [
        "C/C++",
        "C#",
        "Common Lisp",
        "Dart",
        "Elixir",
        "Python",
        "Rust",
        "Go",
        "Lua",
        "Java",
        "Julia",
        "Kotlin",
        "JavaScript / TypeScript",
        "Zig",
        "Haskell",
    ],
    "game-engines": ["C++", "Go", "Rust", "Zig"],
    "graphics-engines": ["C++"],
    "physics-libraries": ["C++"],
}

GROUP_HEADINGS = {
    "game-engines": "Applications powered by ECS",
    "benchmarks": "Other Resources",
}

ACTIVE_DAYS = 365
INACTIVE_DAYS = 3 * 365
AS_OF_FILE = "as-of.txt"


def load_yaml(path: Path) -> list[Entry]:
    if not path.exists():
        return []
    with path.open() as f:
        data = yaml.safe_load(f)
    if not isinstance(data, list):
        return []
    return cast(list[Entry], data)


def format_stars(stars: int) -> str:
    if stars >= 1_000:
        return f"{stars / 1_000:.1f}k".replace(".0k", "k")
    return str(stars)


def as_of_date(data_dir: Path) -> date:
    """Use the metadata snapshot date so README activity stays reproducible."""
    path = data_dir / AS_OF_FILE
    if path.exists():
        return date.fromisoformat(path.read_text(encoding="utf-8").strip())
    return date.today()


def stars(entry: Entry) -> int | None:
    return (entry.get("_meta") or {}).get("stars")


def is_archived(entry: Entry) -> bool:
    return bool(entry.get("archived") or (entry.get("_meta") or {}).get("archived"))


def idle_days(entry: Entry, as_of: date) -> int | None:
    last_commit = (entry.get("_meta") or {}).get("last_commit")
    if not last_commit:
        return None
    try:
        return (as_of - date.fromisoformat(str(last_commit))).days
    except ValueError:
        return None


def is_inactive(entry: Entry, as_of: date) -> bool:
    days = idle_days(entry, as_of)
    return is_archived(entry) or (days is not None and days > INACTIVE_DAYS)


def activity_emoji(entry: Entry, as_of: date, folded: bool = False) -> str:
    if is_archived(entry):
        return "💀"
    days = idle_days(entry, as_of)
    if not folded and days is not None and days <= INACTIVE_DAYS:
        return "🟢" if days <= ACTIVE_DAYS else "🟡"
    return ""


REPO_HOSTS = (("github", "https://github.com/"), ("gitlab", "https://gitlab.com/"),
              ("bitbucket", "https://bitbucket.org/"), ("code_url", ""))


def repo_url(entry: Entry) -> str | None:
    return next((prefix + entry[key] for key, prefix in REPO_HOSTS if entry.get(key)), None)


def render_repo_link(entry: Entry) -> str | None:
    repo = repo_url(entry)
    if not repo:
        return None
    meta = entry.get("_meta") or {}
    stars = meta.get("stars")
    if isinstance(stars, int):
        return f"[⭐ {format_stars(stars)}]({repo})"
    label = next(key for key, _ in REPO_HOSTS if entry.get(key))
    return f"[[{'code' if label == 'code_url' else label}]({repo})]"


def render_library_entry(entry: Entry, as_of: date, folded: bool = False) -> str:
    name = entry.get("name", "")
    url = entry.get("url")
    description = entry.get("description")
    emoji = activity_emoji(entry, as_of, folded)
    name_part = f"[{name}]({url})" if url else name
    parts = ["*", emoji, name_part]
    line = " ".join(part for part in parts if part)
    if description:
        line = f"{line} - {description}"
    repo_link = render_repo_link(entry)
    if repo_link:
        if line.endswith((".", "!", "?")):
            line = f"{line} {repo_link}"
        else:
            line = f"{line}. {repo_link}"
    last_commit = (entry.get("_meta") or {}).get("last_commit")
    if folded and last_commit:
        line = f"{line} · last commit {str(last_commit)[:4]}"
    return line


def render_resource_entry(entry: Entry) -> str:
    name = entry.get("name", "")
    url = entry.get("url") or repo_url(entry)
    description = entry.get("description")
    name_part = f"[{name}]({url})" if url else name
    line = f"* {name_part}"
    if description:
        line = f"{line} - {description}"
    return line


def language_subsection(entry: Entry, subsections: list[str]) -> str:
    """The subsection named for the repository's language ("C++" goes under "C/C++"), or ""."""
    language = (entry.get("_meta") or {}).get("language") or ""
    return next((sub for sub in subsections if language in {part.strip() for part in sub.split("/")}), "")


def sort_entries(entries: list[Entry]) -> list[Entry]:
    return sorted(
        entries,
        key=lambda e: (stars(e) is None, -(stars(e) or 0), e["name"].lower()),
    )


def render_section(
    section_id: str, title: str, level: int, kind: str, entries: list[Entry], as_of: date
) -> list[str]:
    lines: list[str] = []
    heading = "#" * level
    lines.append(f"{heading} [{title}](#contents)")
    description = SECTION_DESCRIPTIONS.get(section_id)
    if description:
        lines.append("")
        lines.append(f"_{description}_")
    lines.append("")
    if kind == "resource":
        for entry in entries:
            lines.append(
                render_library_entry(entry, as_of)
                if section_id == "benchmarks"
                else render_resource_entry(entry)
            )
        return lines + [""]

    inactive = [e for e in entries if is_inactive(e, as_of)]
    entries = sort_entries([e for e in entries if not is_inactive(e, as_of)])
    subsections = SUBSECTION_ORDER.get(section_id)
    if subsections:
        grouped: dict[str, list[Entry]] = {}
        for entry in entries:
            grouped.setdefault(entry.get("_subsection") or language_subsection(entry, subsections), []).append(entry)
        for subsection in subsections:
            items = grouped.get(subsection, [])
            if not items:
                continue
            lines.append(f"#### {subsection}")
            lines.append("")
            for entry in items:
                lines.append(render_library_entry(entry, as_of))
            lines.append("")
        known = set(subsections)
        other = [e for key, es in grouped.items() for e in es if key not in known]
        if other:
            lines.append("#### Other")
            lines.append("")
            for entry in sort_entries(other):
                lines.append(render_library_entry(entry, as_of))
            lines.append("")
    else:
        for entry in entries:
            lines.append(render_library_entry(entry, as_of))
        lines.append("")
    if inactive:
        lines += [
            "<details>",
            f"<summary>Inactive ({len(inactive)}): archived or no commits for 3+ years</summary>",
            "",
        ]
        lines += [render_library_entry(e, as_of, folded=True) for e in sort_entries(inactive)]
        lines += ["", "</details>", ""]
    return lines


def anchor(title: str) -> str:
    """GitHub heading anchor: lowercase, drop punctuation, spaces to hyphens."""
    kept = "".join(ch for ch in title.lower() if ch.isalnum() or ch in " -")
    return kept.replace(" ", "-")


def generate_readme(data_dir: Path | None = None) -> str:
    data_dir = data_dir or Path(__file__).resolve().parent.parent / "data"
    as_of = as_of_date(data_dir)
    sections = [
        (*section, load_yaml(data_dir / f"{section[0]}.yaml"))
        for section in SECTIONS
    ]
    lines: list[str] = []
    lines.append("# Awesome ECS")
    lines.append("")
    lines.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append(
        "A curated list of Entity-Component-System (ECS) libraries and resources."
    )
    lines.append("")
    lines.append("## Contents")
    for section_id, title, level, *_rest in sections:
        if section_id in GROUP_HEADINGS:
            group = GROUP_HEADINGS[section_id]
            lines.append(f"* [{group}](#{anchor(group)})")
        indent = "  " if level == 3 else ""
        lines.append(f"{indent}* [{title}](#{anchor(title)})")
    lines.append("* [Contributing](#contributing)")
    lines.append("")
    lines.append(
        "> **Legend**: 🟢 commit within 1 yr · 🟡 commit within 3 yr · 💀 archived · "
        f"⭐ GitHub stars as of {as_of.isoformat()}. Software entries are ordered by stars; "
        "inactive entries (archived, or no commits for 3+ years) are folded at the end of "
        "each software category. Other resources keep their existing order."
    )
    lines.append("")

    for section_id, title, level, kind, _depth, entries in sections:
        if section_id in GROUP_HEADINGS:
            lines += [f"## [{GROUP_HEADINGS[section_id]}](#contents)", ""]
        lines.extend(render_section(section_id, title, level, kind, entries, as_of))

    lines.append("## [Contributing](#contents)")
    lines.append("")
    lines.append(
        "Contributions are very welcome! Please read the "
        "[contribution guidelines](https://github.com/jslee02/awesome-entity-component-system/blob/main/CONTRIBUTING.md)"
        " first. Also, please feel free to report any error."
    )
    lines.append("")
    lines.append("## [Star History](#contents)")
    lines.append("")
    lines.append(
        '<a href="https://www.star-history.com/?repos=jslee02%2Fawesome-entity-component-system">\n'
        "  <picture>\n"
        '    <source media="(prefers-color-scheme: dark)" '
        'srcset="https://api.star-history.com/chart?repos=jslee02/awesome-entity-component-system&type=date&theme=dark&legend=top-left" />\n'
        '    <source media="(prefers-color-scheme: light)" '
        'srcset="https://api.star-history.com/chart?repos=jslee02/awesome-entity-component-system&type=date&legend=top-left" />\n'
        '    <img alt="Star History Chart" '
        'src="https://api.star-history.com/chart?repos=jslee02/awesome-entity-component-system&type=date&legend=top-left" />\n'
        "  </picture>\n"
        "</a>"
    )
    lines.append("")
    lines.append("## [License](#contents)")
    lines.append("")
    lines.append(
        "[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)"
    )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate README.md from YAML data")
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output file path (default: README.md in repo root)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    readme = generate_readme()

    output_path = Path(args.output) if args.output else repo_root / "README.md"
    _ = output_path.write_text(readme, encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
