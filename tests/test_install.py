"""Installer behavior: self-contained copies, non-overwrite and safe archives."""

import io
from pathlib import Path
import tempfile
import unittest
import zipfile

import install


class InstallerTests(unittest.TestCase):
    def test_copies_all_skill_files_and_preserves_existing_install(self):
        source = Path(__file__).resolve().parents[1] / "skills" / install.SKILL_NAME
        with tempfile.TemporaryDirectory() as temporary:
            target = install.install_skill(source, Path(temporary))
            for item in source.rglob("*"):
                if item.is_file():
                    self.assertEqual(item.read_bytes(), (target / item.relative_to(source)).read_bytes())
            sentinel = target / "user-customization.txt"
            sentinel.write_text("keep me")
            with self.assertRaises(FileExistsError):
                install.install_skill(source, Path(temporary))
            self.assertEqual(sentinel.read_text(), "keep me")

    def test_existing_symlink_is_not_followed_or_replaced(self):
        source = Path(__file__).resolve().parents[1] / "skills" / install.SKILL_NAME
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / install.SKILL_NAME).symlink_to(root / "absent", target_is_directory=True)
            with self.assertRaises(FileExistsError):
                install.install_skill(source, root)
            self.assertTrue((root / install.SKILL_NAME).is_symlink())

    def test_archive_cannot_write_outside_skill(self):
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as archive:
            archive.writestr("repo/skills/landing-page-strategist/../../escape.txt", "bad")
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaises(ValueError):
                install.extract_skill(buffer.getvalue(), Path(temporary))
            self.assertEqual(list(Path(temporary).iterdir()), [])

    def test_archive_extracts_only_skill_and_rejects_missing_references(self):
        source = Path(__file__).resolve().parents[1] / "skills" / install.SKILL_NAME
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as archive:
            archive.writestr("repo/README.md", "not installed")
            for item in source.rglob("*"):
                if item.is_file():
                    archive.writestr("repo/skills/landing-page-strategist/" + item.relative_to(source).as_posix(), item.read_bytes())
        with tempfile.TemporaryDirectory() as temporary:
            result = install.extract_skill(buffer.getvalue(), Path(temporary))
            self.assertFalse((result / "README.md").exists())
            self.assertTrue((result / "agents" / "openai.yaml").is_file())
            (result / "references" / "entrevista.md").unlink()
            with self.assertRaises(ValueError):
                install.validate_source(result)

    def test_dry_run_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "not-created"
            self.assertEqual(install.main(["--dest", str(destination), "--dry-run"]), 0)
            self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
