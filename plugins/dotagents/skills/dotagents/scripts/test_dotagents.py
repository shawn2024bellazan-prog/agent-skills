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

    @patch("dotagents.shutil.which", return_value="/trusted/dotagents")
    @patch("dotagents.subprocess.run", return_value=subprocess.CompletedProcess([], 0))
    def test_new_verbs_require_apply_and_forward_exact_arguments(self, run, _which):
        (self.root / "agents.toml").touch()
        for args in (["install"], ["add", "owner/repo", "skill"], ["remove", "skill"],
                     ["mcp", "remove", "sample"], ["trust", "add", "owner/repo"], ["doctor", "--fix"]):
            self.assertEqual(self.invoke(*args), 1)
        run.assert_not_called()
        pairs = [(["install", "--apply"], ["install"]),
                 (["add", "owner/repo", "skill", "--ref", "v1", "--apply"], ["add", "owner/repo", "skill", "--ref", "v1"]),
                 (["remove", "skill", "--apply"], ["remove", "skill", "--yes"]),
                 (["list", "--json"], ["list", "--json"]),
                 (["mcp", "add", "sample", "--url", "http://127.0.0.1:8080/mcp", "--apply"], ["mcp", "add", "sample", "--url", "http://127.0.0.1:8080/mcp"]),
                 (["mcp", "remove", "sample", "--apply"], ["mcp", "remove", "sample"]),
                 (["trust", "add", "owner/repo", "--apply"], ["trust", "add", "owner/repo"]),
                 (["trust", "remove", "owner/repo", "--apply"], ["trust", "remove", "owner/repo"]),
                 (["trust", "list", "--json"], ["trust", "list", "--json"]),
                 (["doctor", "--fix", "--apply"], ["doctor", "--fix"])]
        for given, expected in pairs:
            self.assertEqual(self.invoke(*given), 0, given)
            self.assertEqual(run.call_args.args[0], ["/trusted/dotagents", "--project", *expected])

    @patch("dotagents.shutil.which", return_value="/trusted/dotagents")
    @patch("dotagents.subprocess.run")
    def test_unsafe_mutations_refused(self, run, _which):
        (self.root / "agents.toml").touch()
        for args in (["add", "../outside", "skill", "--apply"],
                     ["add", "https://token@example.org/repo", "skill", "--apply"],
                     ["add", "owner/repo", "--apply"],
                     ["trust", "add", "*", "--apply"],
                     ["mcp", "add", "server", "--url", "https://example.org/mcp?key=secret", "--apply"],
                     ["mcp", "add", "server", "--command", "server", "--env", "KEY=value", "--apply"]):
            self.assertEqual(self.invoke(*args), 1, args)
        run.assert_not_called()

    @patch("dotagents.shutil.which", return_value="/trusted/dotagents")
    @patch("dotagents.subprocess.run", return_value=subprocess.CompletedProcess([], 0))
    def test_local_source_uses_native_path_syntax(self, run, _which):
        (self.root / "agents.toml").touch()
        (self.root / "fixture").mkdir()
        self.assertEqual(self.invoke("add", "./fixture", "--all", "--apply"), 0)
        self.assertEqual(run.call_args.args[0], ["/trusted/dotagents", "--project", "add", "path:fixture", "--all"])

    @patch("dotagents.shutil.which", return_value="/trusted/dotagents")
    @patch("dotagents.subprocess.run", return_value=subprocess.CompletedProcess([], 0, stdout='[{"name":"sample","transport":"stdio","target":"secret-value","env":["TOKEN"]}]'))
    def test_mcp_list_uses_provider_and_hides_targets(self, run, _which):
        (self.root / "agents.toml").touch()
        with contextlib.redirect_stdout(io.StringIO()) as stdout:
            self.assertEqual(dotagents.main(["--project", str(self.root), "mcp", "list"]), 0)
        self.assertIn('"name": "sample"', stdout.getvalue())
        self.assertNotIn("secret-value", stdout.getvalue())
        self.assertEqual(run.call_args.args[0], ["/trusted/dotagents", "--project", "mcp", "list", "--json"])

    @patch("dotagents.subprocess.run")
    def test_unsupported_config_never_invoked(self, run):
        with self.assertRaises(SystemExit) as exc:
            self.invoke("config")
        self.assertEqual(exc.exception.code, 2)
        run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
