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
    ("etc", "ETC", 3, "resource", None),
]

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
    "etc": "Other ECS-related resources.",
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

TOC = [
    "## Contents",
    "* [ECS Libraries](#ecs-libraries)",
    "* [Applications powered by ECS](#applications-powered-by-ecs)",
    "  * [Game Engines](#game-engines)",
    "  * [Graphics Engines](#graphics-engines)",
    "  * [Physics Libraries](#physics-libraries)",
    "* [Other Resources](#other-resources)",
    "  * [Benchmarks](#benchmarks)",
    "  * [Blog Posts](#blog-posts)",
    "  * [Talks & Slides](#talks--slides)",
    "  * [Books](#books)",
    "  * [Tutorials](#tutorials)",
    "  * [Lists](#lists)",
    "  * [ETC](#etc)",
]


def load_yaml(path: Path) -> list[Entry]:
    if not path.exists():
        return []
    with path.open() as f:
        data = yaml.safe_load(f)
    if not isinstance(data, list):
        return []
    return cast(list[Entry], data)


def format_stars(stars: int) -> str:
    if stars >= 1_000_000:
        return f"{stars / 1_000_000:.1f}m".rstrip("0").rstrip(".")
    if stars >= 1_000:
        return f"{stars / 1_000:.1f}k".rstrip("0").rstrip(".")
    return str(stars)


def activity_emoji(entry: Entry) -> str:
    if entry.get("archived"):
        return "💀"
    meta = entry.get("_meta") or {}
    if meta.get("archived"):
        return "💀"
    last_commit = meta.get("last_commit")
    if not last_commit:
        return ""
    try:
        last_date = date.fromisoformat(last_commit)
    except ValueError:
        return ""
    days = (date.today() - last_date).days
    if days < 365:
        return "🟢"
    if days < 730:
        return "🟡"
    return "🔴"


def repo_url(entry: Entry) -> str | None:
    github = entry.get("github")
    if github:
        return f"https://github.com/{github}"
    gitlab = entry.get("gitlab")
    if gitlab:
        return f"https://gitlab.com/{gitlab}"
    return None


def render_repo_link(entry: Entry) -> str | None:
    repo = repo_url(entry)
    if not repo:
        return None
    meta = entry.get("_meta") or {}
    stars = meta.get("stars")
    if isinstance(stars, int):
        return f"[⭐ {format_stars(stars)}]({repo})"
    if entry.get("github"):
        return f"[github]({repo})"
    return f"[gitlab]({repo})"


def render_library_entry(entry: Entry) -> str:
    name = entry.get("name", "")
    url = entry.get("url")
    description = entry.get("description")
    emoji = activity_emoji(entry)
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
    return line


def render_resource_entry(entry: Entry) -> str:
    name = entry.get("name", "")
    url = entry.get("url")
    description = entry.get("description")
    name_part = f"[{name}]({url})" if url else name
    line = f"* {name_part}"
    if description:
        line = f"{line} - {description}"
    return line


def sort_entries(entries: list[Entry]) -> list[Entry]:
    return sorted(entries, key=lambda e: (e.get("name") or "").lower())


def render_section(section_id: str, title: str, level: int, _kind: str) -> list[str]:
    lines: list[str] = []
    heading = "#" * level
    lines.append(f"{heading} [{title}](#contents)")
    description = SECTION_DESCRIPTIONS.get(section_id)
    if description:
        lines.append("")
        lines.append(f"_{description}_")
    lines.append("")
    entries = sort_entries(
        load_yaml(Path(__file__).parent.parent / "data" / f"{section_id}.yaml")
    )
    subsections = SUBSECTION_ORDER.get(section_id)
    if subsections:
        grouped: dict[str, list[Entry]] = {}
        for entry in entries:
            grouped.setdefault(entry.get("_subsection") or "", []).append(entry)
        for subsection in subsections:
            items = grouped.get(subsection, [])
            if not items:
                continue
            lines.append(f"#### {subsection}")
            lines.append("")
            for entry in sort_entries(items):
                lines.append(render_library_entry(entry))
            lines.append("")
        known = set(subsections)
        other = [e for key, es in grouped.items() for e in es if key not in known]
        if other:
            lines.append("#### Other")
            lines.append("")
            for entry in sort_entries(other):
                lines.append(render_library_entry(entry))
            lines.append("")
    else:
        for entry in entries:
            if section_id == "benchmarks":
                lines.append(render_library_entry(entry))
            else:
                lines.append(render_resource_entry(entry))
        lines.append("")
    return lines


def generate_readme() -> str:
    lines: list[str] = []
    lines.append("# Awesome ECS")
    lines.append("")
    lines.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append(
        "A curated list of Entity-Component-System (ECS) libraries and resources."
    )
    lines.append("")
    lines.extend(TOC)
    lines.append("")
    lines.append(
        "> **Legend**: 🟢 Active (<1yr) · 🟡 Slow (1-2yr) · 🔴 Stale (>2yr) · 💀 Archived"
    )
    lines.append("")

    inserted_apps = False
    inserted_resources = False

    for section_id, title, level, kind, _depth in SECTIONS:
        if section_id == "game-engines" and not inserted_apps:
            lines.append("## [Applications powered by ECS](#contents)")
            lines.append("")
            inserted_apps = True
        if section_id == "benchmarks" and not inserted_resources:
            lines.append("## [Other Resources](#contents)")
            lines.append("")
            inserted_resources = True
        lines.extend(render_section(section_id, title, level, kind))

    lines.append("## [Contributing](#contents)")
    lines.append("")
    lines.append(
        "Contributions are very welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first. Also, please feel free to report any error."
    )
    lines.append("")
    lines.append("## [License](#contents)")
    lines.append("")
    lines.append(
        "[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)"
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
