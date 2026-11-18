import contextlib
import io
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import dotagents


class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        self.root.mkdir()

    def invoke(self, *args):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return dotagents.main(["--project", str(self.root), *args])

    @patch("dotagents.shutil.which", return_value="/trusted/dotagents")
    @patch("dotagents.subprocess.run", return_value=subprocess.CompletedProcess([], 0))
    def test_init_invokes_exact_project_command(self, run, _which):
        self.assertEqual(self.invoke("init", "--agents", "claude,codex"), 0)
        run.assert_called_once_with(["/trusted/dotagents", "--project", "init", "--agents", "claude,codex"], cwd=self.root, stdin=subprocess.DEVNULL, check=False)

    @patch("dotagents.shutil.which", return_value="/trusted/dotagents")
    @patch("dotagents.subprocess.run", return_value=subprocess.CompletedProcess([], 0))
    def test_sync_and_doctor_use_explicit_scope(self, run, _which):
        (self.root / "agents.toml").touch()
        for operation in ("sync", "doctor"):
            self.assertEqual(self.invoke(operation), 0)
            self.assertEqual(run.call_args.args[0], ["/trusted/dotagents", "--project", operation])

    @patch("dotagents.subprocess.run")
    def test_missing_config_blocks_sync(self, run):
        self.assertEqual(self.invoke("sync"), 1)
        run.assert_not_called()

    @patch("dotagents.subprocess.run")
    def test_existing_config_blocks_init(self, run):
        (self.root / "agents.toml").touch()
        self.assertEqual(self.invoke("init", "--agents", "claude"), 1)
        run.assert_not_called()

    @patch("dotagents.shutil.which", return_value=None)
    @patch("dotagents.subprocess.run")
    def test_missing_provider_is_blocked(self, run, _which):
        self.assertEqual(self.invoke("init", "--agents", "claude"), 1)
        run.assert_not_called()

    @patch("dotagents.shutil.which", return_value="/trusted/dotagents")
    @patch("dotagents.subprocess.run", return_value=subprocess.CompletedProcess([], 7))
    def test_provider_failure_is_not_success(self, _run, _which):
        self.assertEqual(self.invoke("init", "--agents", "claude"), 1)

    @patch("dotagents.subprocess.run")
    def test_external_symlink_blocks(self, run):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (self.root / ".agents").symlink_to(outside, target_is_directory=True)
        self.assertEqual(self.invoke("init", "--agents", "claude"), 1)
        run.assert_not_called()

    @patch("dotagents.subprocess.run")
    def test_private_runtime_symlink_blocks(self, run):
        private = self.root / ".pmcro"
        private.mkdir()
        (self.root / ".agents").mkdir()
        (self.root / ".agents" / "memory").symlink_to(private, target_is_directory=True)
        self.assertEqual(self.invoke("init", "--agents", "claude"), 1)
        run.assert_not_called()

    @patch("dotagents.subprocess.run")
    def test_subdirectory_of_git_root_blocks(self, run):
        (self.root.parent / ".git").mkdir()
        self.assertEqual(self.invoke("init", "--agents", "claude"), 1)
        run.assert_not_called()

    @patch("dotagents.subprocess.run")
    def test_invalid_hosts_rejected(self, run):
        for hosts in ("unknown", "claude,claude", "claude,--force"):
            with self.assertRaises(SystemExit) as exc:
                self.invoke("init", "--agents", hosts)
            self.assertEqual(exc.exception.code, 2)
        run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
