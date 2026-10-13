"""Tests for removing deleted repositories in scripts/fetch_metadata.py."""

import sys
import tempfile
import unittest
import urllib.error
from datetime import date
from pathlib import Path
from unittest import mock

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import fetch_metadata  # noqa: E402


class GoneRepoTest(unittest.TestCase):
    def refresh(self, entries, today, results):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "x.yaml"
            path.write_text(yaml.dump(entries), encoding="utf-8")
            with mock.patch.object(fetch_metadata, "fetch_repo_metadata", side_effect=lambda r: results[r]), \
                    mock.patch.object(fetch_metadata.time, "sleep"):
                fetch_metadata.process_yaml_file(path, today=today)
            return yaml.safe_load(path.read_text(encoding="utf-8"))

    def test_marks_then_removes_after_a_week(self):
        entries = [{"name": "Gone", "github": "a/gone"}, {"name": "Alive", "github": "a/alive"}]
        results = {"a/gone": fetch_metadata.GONE, "a/alive": ({"stars": 5}, "a/alive")}
        first = self.refresh(entries, date(2026, 10, 12), results)
        self.assertEqual(first[0]["_meta"]["gone_since"], "2026-10-12")
        self.assertEqual(len(self.refresh(first, date(2026, 10, 15), results)), 2)  # grace period
        self.assertEqual([e["name"] for e in self.refresh(first, date(2026, 10, 19), results)], ["Alive"])

    def test_back_again_clears_the_mark(self):
        entries = [{"name": "Back", "github": "a/back", "_meta": {"gone_since": "2026-10-12"}}]
        back = self.refresh(entries, date(2026, 10, 19), {"a/back": ({"stars": 1}, "a/back")})
        self.assertEqual(back[0]["_meta"], {"stars": 1})


    def test_failed_commit_lookup_keeps_the_previous_date(self):
        entries = [{"name": "X", "github": "a/x", "_meta": {"id": 1, "stars": 1, "last_commit": "2026-01-02"}}]
        kept = self.refresh(entries, date(2026, 10, 19),
                            {"a/x": ({"id": 1, "stars": 2, "_commit_lookup_failed": True}, "a/x")})
        self.assertEqual(kept[0]["_meta"], {"id": 1, "stars": 2, "last_commit": "2026-01-02"})
        # A link corrected to another repository doesn't inherit the old repository's date.
        moved = self.refresh(entries, date(2026, 10, 19),
                             {"a/x": ({"id": 2, "stars": 2, "_commit_lookup_failed": True}, "a/x")})
        self.assertEqual(moved[0]["_meta"], {"id": 2, "stars": 2})

    def test_no_commit_or_unknown_id_does_not_keep_the_previous_date(self):
        for previous, fetched in [
            ({"id": 1, "last_commit": "2026-01-02"}, {"id": 1}),
            ({"last_commit": "2026-01-02"}, {"_commit_lookup_failed": True}),
        ]:
            with self.subTest(previous=previous):
                entries = [{"name": "X", "github": "a/x", "_meta": previous}]
                refreshed = self.refresh(entries, date(2026, 10, 19), {"a/x": (fetched, "a/x")})
                self.assertNotIn("last_commit", refreshed[0]["_meta"])
                self.assertNotIn("_commit_lookup_failed", refreshed[0]["_meta"])

    def test_failed_commit_lookup_does_not_keep_legacy_date_after_a_manual_correction(self):
        entries = [{"name": "X", "github": "a/x", "_meta": {"last_commit": "2022-01-02"}}]
        entries[0]["github"] = "new/x"
        for full_name in ("new/x", "New/X"):
            with self.subTest(full_name=full_name):
                refreshed = self.refresh(entries, date(2026, 10, 19),
                                         {"new/x": ({"id": 2, "_commit_lookup_failed": True}, full_name)})
                self.assertEqual(refreshed[0]["_meta"], {"id": 2})

    def test_failed_commit_lookup_does_not_keep_legacy_date_after_a_rename(self):
        entries = [{"name": "X", "github": "a/x", "_meta": {"last_commit": "2022-01-02"}}]
        refreshed = self.refresh(entries, date(2026, 10, 19),
                                 {"a/x": ({"id": 1, "_commit_lookup_failed": True}, "new/x")})
        self.assertEqual(refreshed[0]["_meta"], {"id": 1})

    def test_rename_updates_the_link_and_preserves_entry_fields(self):
        entries = [{"name": "X", "github": "old/x", "url": "https://example.com", "_subsection": "C/C++"}]
        refreshed = self.refresh(entries, date(2026, 10, 19), {"old/x": ({"id": 1}, "new/x")})
        self.assertEqual(refreshed, [{**entries[0], "github": "new/x", "_meta": {"id": 1}}])

    def test_transient_repository_failure_keeps_existing_metadata(self):
        entries = [{"name": "X", "github": "a/x", "_meta": {"id": 1, "last_commit": "2026-01-02"}}]
        self.assertEqual(self.refresh(entries, date(2026, 10, 19), {"a/x": None}), entries)


class LookupTest(unittest.TestCase):
    def test_lookup_follows_the_link_and_never_pushed_at(self):
        urls = []
        repo = {"id": 99, "full_name": "new/correct", "stargazers_count": 3, "default_branch": "main",
                "pushed_at": "2026-10-01T00:00:00Z"}
        with mock.patch.object(fetch_metadata, "fetch_json", side_effect=lambda url, *a: urls.append(url) or repo), \
                mock.patch.object(fetch_metadata, "fetch_default_branch_commit_date", return_value=None) as commits:
            meta, full_name = fetch_metadata.fetch_repo_metadata("new/correct")
        # A corrected link wins over a stale stored ID, and its repository's ID is recorded.
        self.assertEqual(urls, ["https://api.github.com/repos/new/correct"])
        self.assertEqual((meta["id"], full_name), (99, "new/correct"))
        self.assertEqual(commits.call_args[0][0], "new/correct")
        self.assertNotIn("last_commit", meta)  # never pushed_at, which counts other branches

    def test_commit_lookup_marks_only_transient_errors(self):
        repo = {"id": 99, "default_branch": "main"}
        cases = [(urllib.error.URLError("offline"), True), (TimeoutError(), True)]
        for code in (403, 429, 500, 404, 409):
            cases.append((urllib.error.HTTPError("url", code, "error", None, None), code in (403, 429, 500)))
        for error, transient in cases:
            with self.subTest(error=error), \
                    mock.patch.object(fetch_metadata, "fetch_json", return_value=repo), \
                    mock.patch.object(fetch_metadata, "fetch_default_branch_commit_date", side_effect=error):
                meta, _ = fetch_metadata.fetch_repo_metadata("a/x")
                self.assertEqual(bool(meta.get("_commit_lookup_failed")), transient)
                self.assertNotIn("last_commit", meta)

    def test_repository_gone_and_transient_errors(self):
        for code in (404, 451, 403, 500):
            with self.subTest(code=code), mock.patch.object(fetch_metadata, "fetch_json",
                    side_effect=urllib.error.HTTPError("url", code, "error", None, None)):
                self.assertEqual(fetch_metadata.fetch_repo_metadata("a/x"),
                                 fetch_metadata.GONE if code in (404, 451) else None)

    def test_license_name_fallback(self):
        with mock.patch.object(fetch_metadata, "fetch_json", return_value={
                "id": 99, "license": {"spdx_id": "NOASSERTION", "name": "Custom License"}}):
            meta, _ = fetch_metadata.fetch_repo_metadata("a/x")
        self.assertEqual(meta["license"], "Custom License")


class ManualReviewGoneTest(unittest.TestCase):
    def test_a_resource_keeps_its_entry_when_its_code_is_gone(self):
        entries = [{"name": "Paper", "url": "https://arxiv.org/abs/1", "github": "a/code",
                    "_meta": {"gone_since": "2026-10-01"}}]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "books.yaml"
            path.write_text(yaml.dump(entries), encoding="utf-8")
            with mock.patch.object(fetch_metadata, "fetch_repo_metadata", return_value=fetch_metadata.GONE), \
                    mock.patch.object(fetch_metadata.time, "sleep"):
                fetch_metadata.process_yaml_file(path, today=date(2026, 10, 12))
            self.assertEqual(yaml.safe_load(path.read_text(encoding="utf-8")),
                             [{"name": "Paper", "url": "https://arxiv.org/abs/1"}])

    def test_a_resource_whose_home_was_the_repository_goes_with_it(self):
        entries = [{"name": "Tutorial", "url": "https://github.com/a/code", "github": "a/code",
                    "_meta": {"gone_since": "2026-10-01"}}]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "books.yaml"
            path.write_text(yaml.dump(entries), encoding="utf-8")
            with mock.patch.object(fetch_metadata, "fetch_repo_metadata", return_value=fetch_metadata.GONE), \
                    mock.patch.object(fetch_metadata.time, "sleep"):
                fetch_metadata.process_yaml_file(path, today=date(2026, 10, 12))
            self.assertEqual(yaml.safe_load(path.read_text(encoding="utf-8")), [])


class RepositoryUrlTest(unittest.TestCase):
    def test_urls_into_the_repository_however_written(self):
        for url in ("https://github.com/a/code#readme", "https://github.com/a/code?tab=readme-ov-file",
                    "http://www.github.com/A/Code.git", "https://github.com/a/code/blob/main/x.pdf"):
            self.assertTrue(fetch_metadata.in_repository(url, "a/code"), url)
        for url in ("https://raw.githubusercontent.com/a/code/main/paper.pdf", "https://github.com/a/code.git/"):
            self.assertTrue(fetch_metadata.in_repository(url, "a/code"), url)
        for url in ("https://github.com/a/code2", "https://arxiv.org/abs/1", ""):
            self.assertFalse(fetch_metadata.in_repository(url, "a/code"), url)

    def test_links_follow_a_renamed_repository(self):
        self.assertEqual(fetch_metadata.moved("https://github.com/Old/Code/wiki/Tutorial#top", "old/code", "new/code"),
                         "https://github.com/new/code/wiki/Tutorial#top")
        self.assertEqual(fetch_metadata.moved("https://arxiv.org/abs/1", "old/code", "new/code"), "https://arxiv.org/abs/1")


if __name__ == "__main__":
    unittest.main()
