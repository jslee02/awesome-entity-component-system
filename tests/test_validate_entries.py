"""The validator must reject data the README generator would silently drop."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import validate_entries  # noqa: E402


class DroppedDataTest(unittest.TestCase):
    def check(self, files: dict[str, str]) -> bool:
        with tempfile.TemporaryDirectory() as tmp:
            for name, text in files.items():
                path = Path(tmp) / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            return validate_entries.validate_entries(tmp)

    def test_valid_category(self):
        self.assertTrue(self.check({"ecs-libraries.yaml": "- name: Tool\n  github: o/r\n"}))

    def test_entries_without_a_list(self):
        self.assertFalse(self.check({"ecs-libraries.yaml": "name: Tool\ngithub: o/r\n"}))  # missing "- "

    def test_file_that_is_not_a_category(self):
        for name in ("ecs-library.yaml", "ecs-libraries.yml", "ecs-library.yml",
                     "nested/ecs-libraries.yaml", "nested/ecs-libraries.yml"):
            with self.subTest(name=name):
                self.assertFalse(self.check({name: "- name: Tool\n  github: o/r\n"}))

    def test_github_path_pattern(self):
        self.assertTrue(self.check({"ecs-libraries.yaml": "- name: Tool\n  github: owner-name/repo._-\n"}))
        for github in ("-owner/repo", "owner-/repo", "owner/repo/extra", "owner name/repo", "owner/repo?x"):
            with self.subTest(github=github):
                self.assertFalse(self.check({"ecs-libraries.yaml": f"- name: Tool\n  github: {github}\n"}))

    def test_dates_are_checked(self):
        for field in ("_meta: {last_commit: '2026-02-30'}", "_meta: {gone_since: 'yesterday'}"):
            with self.subTest(field=field):
                self.assertFalse(self.check({"ecs-libraries.yaml": f"- name: Tool\n  {field}\n"}))

    def test_metadata_and_existing_fields(self):
        self.assertTrue(self.check({"ecs-libraries.yaml": """- name: Tool
  github: o/r
  gitlab: o/r
  description: An ECS library
  archived: false
  _subsection: C/C++
  _meta:
    id: 123
    stars: 5
    last_commit: '2026-10-12'
    gone_since: '2026-10-12'
    language: C++
    license: MIT
    archived: false
"""}))


if __name__ == "__main__":
    unittest.main()
