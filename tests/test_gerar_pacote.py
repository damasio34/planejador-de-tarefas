import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from scripts.gerar_pacote import build_package


class BuildPackageTests(unittest.TestCase):
    def test_creates_flat_archive_with_skill_and_task_material(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "docs").mkdir()
            (root / "templates").mkdir()
            (root / "tarefas").mkdir()
            (root / "SKILL.md").write_text("skill", encoding="utf-8")
            (root / "AGENTS.md").write_text("agents", encoding="utf-8")
            (root / "README.md").write_text("readme", encoding="utf-8")
            (root / "docs" / "guide.md").write_text("guide", encoding="utf-8")
            (root / "templates" / "task.md").write_text("task", encoding="utf-8")
            (root / "tarefas" / "2026-10-16-exemplo.md").write_text(
                "approved task", encoding="utf-8"
            )
            (root / "gerar_pacote.py").write_text("script", encoding="utf-8")
            (root / "planejador-tarefas-docs.zip").write_text("old zip", encoding="utf-8")

            archive_path = build_package(root)

            with ZipFile(archive_path) as archive:
                self.assertEqual(
                    set(archive.namelist()),
                    {
                        "AGENTS.md",
                        "README.md",
                        "SKILL.md",
                        "docs/guide.md",
                        "templates/task.md",
                        "tarefas/2026-10-16-exemplo.md",
                    },
                )
                self.assertEqual(archive.read("SKILL.md"), b"skill")


if __name__ == "__main__":
    unittest.main()
