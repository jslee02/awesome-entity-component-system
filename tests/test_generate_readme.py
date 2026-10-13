"""README ordering, folding, and snapshot dates must preserve every entry."""

import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from unittest import mock

import yaml

from scripts import generate_readme as generator


class GenerateReadmeTest(unittest.TestCase):
    def test_sort_keeps_zero_stars_before_missing_stars_and_breaks_ties_by_name(self):
        entries = [
            {"name": "Zulu"},
            {"name": "Beta", "_meta": {"stars": 10}},
            {"name": "Zero", "_meta": {"stars": 0}},
            {"name": "Alpha", "_meta": {"stars": 10}},
            {"name": "No stars"},
        ]
        self.assertEqual(
            [e["name"] for e in generator.sort_entries(entries)],
            ["Alpha", "Beta", "Zero", "No stars", "Zulu"],
        )

    def test_activity_matches_reference_boundaries(self):
        as_of = date(2026, 10, 12)
        for days, emoji, inactive in [(365, "🟢", False), (366, "🟡", False),
                                      (1095, "🟡", False), (1096, "", True)]:
            entry = {"name": "Example", "_meta": {"last_commit": (as_of - timedelta(days=days)).isoformat()}}
            with self.subTest(days=days):
                self.assertEqual(generator.is_inactive(entry, as_of), inactive)
                self.assertEqual(generator.activity_emoji(entry, as_of, folded=inactive), emoji)
                self.assertEqual(generator.activity_emoji(entry, as_of), emoji)
        self.assertFalse(generator.is_inactive({"name": "Unknown"}, as_of))
        for entry in [{"name": "Archived", "archived": True},
                      {"name": "Archived", "_meta": {"archived": True}}]:
            self.assertTrue(generator.is_inactive(entry, as_of))
            self.assertEqual(generator.activity_emoji(entry, as_of, folded=True), "💀")

    def test_snapshot_folding_resources_and_generated_contents(self):
        software = [
            {"name": "Low", "_subsection": "C/C++", "_meta": {"stars": 1, "last_commit": "2026-05-01"}},
            {"name": "Old", "_subsection": "C/C++", "_meta": {"stars": 100, "last_commit": "2020-01-01"}},
            {"name": "High", "_subsection": "C/C++", "_meta": {"stars": 10, "last_commit": "2026-05-01"}},
            {"name": "Archived", "_subsection": "Rust", "archived": True},
        ]
        resources = [{"name": "Zulu", "archived": True}, {"name": "Alpha"}]
        with tempfile.TemporaryDirectory() as tmp:
            data_dir = Path(tmp)
            (data_dir / "as-of.txt").write_text("2026-10-12\n", encoding="utf-8")
            for key, entries in [("ecs-libraries", software), ("books", resources),
                                 ("benchmarks", resources), ("extra", resources)]:
                (data_dir / f"{key}.yaml").write_text(yaml.dump(entries), encoding="utf-8")
            with mock.patch.object(generator, "SECTIONS", generator.SECTIONS + [("extra", "Extra & Resources", 3, "resource", None)]):
                readme = generator.generate_readme(data_dir)
                with mock.patch.object(generator, "date", wraps=date) as clock:
                    clock.today.return_value = date(2030, 1, 1)
                    self.assertEqual(generator.generate_readme(data_dir), readme)
            self.assertEqual(generator.as_of_date(data_dir), date(2026, 10, 12))
            (data_dir / "as-of.txt").unlink()
            self.assertEqual(generator.as_of_date(data_dir), date.today())
        self.assertIn("* [Extra & Resources](#extra--resources)", readme)
        self.assertLess(readme.index("* 🟢 High"), readme.index("* 🟢 Low"))
        self.assertLess(readme.index("* 🟢 Low"), readme.index("<details>"))
        self.assertIn("<summary>Inactive (2): archived or no commits for 3+ years</summary>", readme)
        self.assertIn("* Old · last commit 2020", readme)
        self.assertIn("* 💀 Archived", readme)
        self.assertEqual(readme.count("<details>"), 1)
        self.assertIn("_Books on ECS and data-oriented design._\n\n* Zulu\n* Alpha", readme)
        self.assertIn("_Performance benchmarks comparing ECS frameworks._\n\n* 💀 Zulu\n* Alpha", readme)


class TriageEntryTest(unittest.TestCase):
    """Entries as the shared suggestion triage writes them."""

    def test_language_picks_the_subsection(self):
        subsections = generator.SUBSECTION_ORDER["ecs-libraries"]
        rust = {"name": "X", "github": "o/x", "_meta": {"language": "Rust"}}
        cpp = {"name": "Y", "github": "o/y", "_meta": {"language": "C++"}}
        self.assertEqual(generator.language_subsection(rust, subsections), "Rust")
        self.assertEqual(generator.language_subsection(cpp, subsections), "C/C++")
        self.assertEqual(generator.language_subsection({"name": "Z"}, subsections), "")

    def test_repository_links_for_every_host(self):
        self.assertEqual(generator.repo_url({"bitbucket": "w/r"}), "https://bitbucket.org/w/r")
        self.assertEqual(generator.repo_url({"code_url": "https://x.example/r.zip"}), "https://x.example/r.zip")
        self.assertEqual(generator.render_repo_link({"name": "R", "bitbucket": "w/r"}), "[[bitbucket](https://bitbucket.org/w/r)]")

    def test_resource_without_a_website_links_its_repository(self):
        entry = {"name": "Tutorial", "github": "o/tutorial", "description": "Learn ECS."}
        self.assertEqual(generator.render_resource_entry(entry), "* [Tutorial](https://github.com/o/tutorial) - Learn ECS.")


if __name__ == "__main__":
    unittest.main()
