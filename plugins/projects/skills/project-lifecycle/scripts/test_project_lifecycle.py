import json
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("project_lifecycle.py")

class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name).resolve()
        self.root = self.base / "project"
        self.root.mkdir()
        self.private = self.base / ".pmcro"
        self.record = self.private / "projects" / "demo" / "project.json"

    def call(self, action, *, apply=True, project="demo", root=None, private=None, code=0, extra=()):
        args = [sys.executable, "-B", str(SCRIPT), action, "--project-id", project,
                "--project-root", str(root or self.root), "--pmcro-root", str(private or self.private)]
        if apply and action not in ("status", "runtime"):
            args.append("--apply")
        args.extend(extra)
        p = subprocess.run(args, capture_output=True, text=True, timeout=30)
        self.assertEqual(p.returncode, code, p.stdout + p.stderr)
        result = json.loads(p.stdout)
        self.assertFalse(result["runtime_started"])
        self.assertFalse(result["host_project_created"])
        return result

    def init(self):
        self.call("register")
        return self.call("initialize")

    def test_full_lifecycle(self):
        self.assertEqual(self.call("register")["state"], "registered")
        self.assertEqual(self.call("initialize")["state"], "initialized")
        self.assertEqual(self.call("activate")["state"], "active")
        self.assertEqual(self.call("deactivate")["state"], "initialized")
        self.assertEqual(self.call("archive")["state"], "archived")
        self.assertEqual(self.call("status")["event_count"], 5)
        self.call("activate", code=1)
        self.assertTrue(self.root.is_dir())

    def test_global_private_local_portable(self):
        self.init()
        self.assertFalse((self.root / ".pmcro").exists())
        self.assertTrue((self.root / ".agents/settings.json").is_file())
        self.assertTrue((self.record.parent / "memory/MEMORY.md").is_file())
        self.assertTrue((self.record.parent / "tasks").is_dir())
        self.assertTrue((self.record.parent / "trails").is_dir())
        if os.name != "nt":
            for p in (self.private, self.record.parent, self.record):
                self.assertEqual(p.stat().st_mode & 0o077, 0)

    def test_memory_index_adapter(self):
        self.init()
        script = SCRIPT.resolve().parents[2] / "manage-auto-memory/scripts/check_index.py"
        p = subprocess.run([sys.executable, "-B", str(script), "--project-id", "demo",
                            "--project-root", str(self.root), "--pmcro-root", str(self.private)],
                           capture_output=True, text=True, timeout=30)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        record = json.loads(p.stdout)
        self.assertTrue(record["index_exists"])
        self.assertFalse(record["memory_content_read"])

    def test_read_only_and_no_implicit_authority(self):
        self.call("status", code=1)
        self.call("register", apply=False, code=1)
        self.assertFalse(self.private.exists())
        self.assertFalse((self.root / ".agents").exists())

    def test_idempotence_and_memory_preserved(self):
        self.init()
        record_before = self.record.read_bytes()
        m = self.record.parent / "memory/MEMORY.md"
        m.write_text("existing memory", encoding="utf-8")
        self.assertFalse(self.call("register")["changed"])
        self.assertFalse(self.call("initialize")["changed"])
        self.assertEqual(self.record.read_bytes(), record_before)
        self.assertEqual(m.read_text(), "existing memory")

    def test_source_instructions_preserved(self):
        (self.root / "AGENTS.md").write_text("existing", encoding="utf-8")
        old = self.root / ".pmcro"
        old.mkdir()
        (old / "old-memory").write_text("keep", encoding="utf-8")
        self.init()
        self.assertEqual((self.root / "AGENTS.md").read_text(), "existing")
        self.assertEqual((old / "old-memory").read_text(), "keep")

    def test_conflicting_id_and_root(self):
        self.call("register")
        other = self.base / "other"
        other.mkdir()
        self.call("register", root=other, code=1)
        self.call("register", project="duplicate", code=1)
        self.assertFalse((self.private / "projects/duplicate").exists())

    def test_invalid_order(self):
        self.call("register")
        self.call("activate", code=1)
        self.call("initialize")
        self.call("activate")
        self.call("archive", code=1)
        self.assertEqual(self.call("status")["state"], "active")

    def test_unsafe_ids_and_overlap(self):
        for invalid in ("../escape", "CON", "con", "A", "x--y"):
            self.call("register", project=invalid, code=1)
        self.call("register", private=self.root / ".pmcro", code=1)
        self.assertFalse(self.private.exists())

    def test_conflict_preflight(self):
        self.call("register")
        (self.root / ".agents").write_text("not a directory", encoding="utf-8")
        self.call("initialize", code=1)
        self.assertEqual(self.call("status")["state"], "registered")
        self.assertFalse((self.root / ".gitignore").exists())

    def test_unsafe_ignore(self):
        self.call("register")
        (self.root / ".gitignore").write_text("unrelated\n", encoding="utf-8")
        self.call("initialize", code=1)
        self.assertFalse((self.root / ".agents").exists())

    def test_busy_lock(self):
        self.call("register")
        lock = self.private / "projects/.registry-lock"
        lock.mkdir()
        self.call("initialize", code=1)
        self.assertTrue(lock.exists())
        self.assertEqual(self.call("status")["state"], "registered")

    def test_invalid_history_fails_closed(self):
        self.init()
        record = json.loads(self.record.read_text())
        record["events"][0]["to"] = "active"
        self.record.write_text(json.dumps(record))
        self.call("status", code=1)
        self.call("activate", code=1)

    def test_activation_rechecks_prerequisites(self):
        self.init()
        (self.record.parent / "memory/MEMORY.md").unlink()
        self.call("activate", code=1)
        self.assertEqual(self.call("status")["state"], "initialized")

    def adapter_fixture(self, fail=False):
        # Protocol test double only; live CLI is verified separately.
        adapter = self.base / "adapter.py"
        adapter.write_text("import sys\nfrom pathlib import Path\n"
                           "root = Path(sys.argv[2]); op = sys.argv[3]\n"
                           "if op == 'init': (root / 'agents.toml').write_text('version = 1\\n')\n"
                           + ("if op == 'doctor': sys.exit(7)\n" if fail else "")
                           + "print('Provider exit: 0')\n", encoding="utf-8")
        digest = hashlib.sha256(adapter.read_bytes()).hexdigest()
        return adapter, ("--dotagents-adapter", str(adapter), "--dotagents-sha256", digest)

    def test_bound_provider_and_private_runtime_scope(self):
        adapter, opts = self.adapter_fixture()
        self.call("register")
        result = self.call("initialize", extra=(*opts, "--agents", "claude,codex"))
        self.assertEqual(result["configuration_provider"], "dotagents")
        self.assertTrue((self.root / "agents.toml").exists())
        runtime = self.call("runtime")
        self.assertEqual(runtime["runtime_provider"], "pmcro-private-project-registry")
        self.assertEqual(runtime["runtime_scope"]["memory_index"], "projects/demo/memory/MEMORY.md")
        self.assertFalse(runtime["memory_content_read"])
        self.assertFalse((self.root / ".pmcro").exists())
        before = self.record.read_bytes()
        self.assertFalse(self.call("initialize", extra=(*opts, "--agents", "claude,codex"))["changed"])
        self.assertEqual(before, self.record.read_bytes())
        adapter.write_text("changed", encoding="utf-8")
        self.call("runtime", code=1)
        self.call("activate", code=1)

    def test_provider_failure_does_not_advance_registry(self):
        _, opts = self.adapter_fixture(fail=True)
        self.call("register")
        self.call("initialize", extra=(*opts, "--agents", "claude"), code=1)
        self.assertEqual(self.call("status")["state"], "registered")
        self.call("runtime", code=1)
        self.assertFalse((self.record.parent / "memory").exists())

    def test_provider_pin_mismatch_refuses_before_scaffold(self):
        adapter, opts = self.adapter_fixture()
        self.call("register")
        adapter.write_text("changed", encoding="utf-8")
        self.call("initialize", extra=(*opts, "--agents", "claude"), code=1)
        self.assertFalse((self.root / ".agents").exists())

    def test_existing_initialized_project_can_bind_once(self):
        self.init()
        _, opts = self.adapter_fixture()
        self.assertEqual(self.call("initialize", extra=(*opts, "--agents", "claude"))["event_count"], 3)
        self.assertEqual(self.call("runtime")["configuration_provider"], "dotagents")

    def test_runtime_scope_denies_registered_archived_or_wrong_root(self):
        self.call("register")
        self.call("runtime", code=1)
        self.call("initialize")
        other = self.base / "other"
        other.mkdir()
        self.call("runtime", root=other, code=1)
        self.call("archive")
        self.call("runtime", code=1)

    @unittest.skipIf(os.name == "nt", "POSIX permissions only")
    def test_unsafe_state_permissions(self):
        self.private.mkdir(mode=0o755)
        self.call("register", code=1)

    @unittest.skipIf(os.name == "nt", "symlink privilege may be unavailable")
    def test_symlink_rejected(self):
        self.call("register")
        other = self.base / "outside"
        other.mkdir()
        (self.record.parent / "memory").symlink_to(other, target_is_directory=True)
        self.call("initialize", code=1)
        self.assertEqual(list(other.iterdir()), [])
        self.assertFalse((self.root / ".agents").exists())
        self.assertEqual(self.call("status")["state"], "registered")

if __name__ == "__main__":
    unittest.main(verbosity=2)
