#!/usr/bin/env python3
"""Fetch GitHub metadata for entries with a github field."""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import TypedDict, cast
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

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


def load_yaml(path: Path) -> list[Entry]:
    with path.open() as f:
        data = cast(object, yaml.safe_load(f))
        if not isinstance(data, list):
            return []
        return cast(list[Entry], data)


def dump_yaml(path: Path, data: list[Entry]) -> None:
    with path.open("w") as f:
        yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False)


def request_json(url: str, headers: dict[str, str]) -> object:
    request = Request(url, headers=headers)
    with urlopen(request) as response:
        body = cast(bytes, response.read())
        text = body.decode("utf-8")
        return json.loads(text)


def fetch_repo_metadata(owner_repo: str, headers: dict[str, str]) -> EntryMeta:
    repo_url = f"https://api.github.com/repos/{owner_repo}"
    repo_data = request_json(repo_url, headers)
    repo = repo_data if isinstance(repo_data, dict) else {}
    commits_url = f"{repo_url}/commits?per_page=1"
    commits = request_json(commits_url, headers)
    last_commit = None
    if isinstance(commits, list) and commits:
        commit = commits[0]
        if isinstance(commit, dict):
            commit_info = commit.get("commit")
            if isinstance(commit_info, dict):
                committer = commit_info.get("committer")
                if isinstance(committer, dict):
                    date_value = committer.get("date")
                    if isinstance(date_value, str):
                        last_commit = date_value[:10]
    license_info = repo.get("license") if isinstance(repo, dict) else None
    if not isinstance(license_info, dict):
        license_info = {}
    license_id = license_info.get("spdx_id") or license_info.get("name")
    if license_id == "NOASSERTION":
        license_id = None
    meta: EntryMeta = {}
    stars = repo.get("stargazers_count") if isinstance(repo, dict) else None
    if isinstance(stars, int):
        meta["stars"] = stars
    if isinstance(last_commit, str):
        meta["last_commit"] = last_commit
    archived = repo.get("archived") if isinstance(repo, dict) else None
    if isinstance(archived, bool):
        meta["archived"] = archived
    if isinstance(license_id, str):
        meta["license"] = license_id
    language = repo.get("language") if isinstance(repo, dict) else None
    if isinstance(language, str):
        meta["language"] = language
    return meta


def update_entries(entries: list[Entry], headers: dict[str, str]) -> bool:
    updated = False
    for entry in entries:
        github = entry.get("github")
        if not github or not isinstance(github, str):
            continue
        try:
            meta = fetch_repo_metadata(github, headers)
        except (HTTPError, URLError, KeyError, ValueError) as e:
            print(f"WARNING: Failed to fetch {github}: {e}", file=sys.stderr)
            continue
        meta_store = entry.get("_meta")
        existing_meta: EntryMeta = {}
        if isinstance(meta_store, dict):
            stored_stars = meta_store.get("stars")
            if isinstance(stored_stars, int):
                existing_meta["stars"] = stored_stars
            stored_last_commit = meta_store.get("last_commit")
            if isinstance(stored_last_commit, str):
                existing_meta["last_commit"] = stored_last_commit
            stored_archived = meta_store.get("archived")
            if isinstance(stored_archived, bool):
                existing_meta["archived"] = stored_archived
            stored_license = meta_store.get("license")
            if isinstance(stored_license, str):
                existing_meta["license"] = stored_license
            stored_language = meta_store.get("language")
            if isinstance(stored_language, str):
                existing_meta["language"] = stored_language
        existing_meta.update(meta)
        entry["_meta"] = existing_meta
        updated = True
        time.sleep(0.5 if headers.get("Authorization") else 2)
    return updated


def main() -> int:
    root = Path(__file__).parent.parent
    data_dir = root / "data"
    yaml_files = sorted(data_dir.glob("*.yaml"))
    if not yaml_files:
        print(f"WARNING: No YAML files in {data_dir}")
        return 0
    headers = {
        "User-Agent": "awesome-ecs-metadata-bot",
        "Accept": "application/vnd.github+json",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for path in yaml_files:
        entries = load_yaml(path)
        if not entries:
            continue
        if update_entries(entries, headers):
            dump_yaml(path, entries)
            print(f"Updated {path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
