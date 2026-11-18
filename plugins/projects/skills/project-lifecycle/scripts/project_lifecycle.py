#!/usr/bin/env python3
"""Private project-registry adapter; reuse the existing local scaffold engine."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile

SCRIPT = Path(__file__).resolve().with_name("init.py")
ID = re.compile(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?\Z")
STATES = {"registered", "initialized", "active", "archived"}
TRANSITIONS = {("register", None, "registered"),
               ("initialize", "registered", "initialized"),
               ("initialize", "initialized", "initialized"),
               ("activate", "initialized", "active"),
               ("deactivate", "active", "initialized"),
               ("archive", "registered", "archived"),
               ("archive", "initialized", "archived")}
RESERVED = {"con", "prn", "aux", "nul"} | {f"{p}{i}" for p in ("com", "lpt") for i in range(1, 10)}
HOSTS = {"claude", "cursor", "codex", "copilot", "vscode", "opencode", "grok", "pi"}
SHA256 = re.compile(r"[0-9a-f]{64}\Z")

def path_kind(p):
    try:
        s = p.lstat()
    except FileNotFoundError:
        return "missing"
    if stat.S_ISLNK(s.st_mode) or getattr(s, "st_file_attributes", 0) & 0x400:
        raise ValueError(f"Unsafe link or reparse point: {p}")
    if stat.S_ISDIR(s.st_mode):
        return "directory"
    if stat.S_ISREG(s.st_mode) and s.st_nlink == 1:
        return "file"
    raise ValueError(f"Unsafe path type: {p}")

def absolute(p):
    if not p.is_absolute() or ".." in p.parts:
        raise ValueError("Use an absolute path without parent traversal.")
    for item in reversed([p, *p.parents]):
        path_kind(item)
    return p.resolve(strict=False)

def private_dir(p, create=False):
    k = path_kind(p)
    if k == "missing" and create:
        p.mkdir(mode=0o700)
        k = path_kind(p)
    if k != "directory":
        raise ValueError(f"Private directory missing or invalid: {p}")
    if os.name != "nt" and p.stat().st_mode & 0o077:
        raise ValueError(f"Unsafe private directory permissions: {p}")

def read_record(p, project_id):
    if path_kind(p) != "file":
        raise ValueError("Project record not found.")
    if os.name != "nt" and p.stat().st_mode & 0o077:
        raise ValueError("Unsafe project record permissions.")
    with p.open("rb") as stream:
        raw = stream.read(1_048_577)
    if len(raw) > 1_048_576:
        raise ValueError("Record too large.")
    r = json.loads(raw)
    if (not isinstance(r, dict) or type(r.get("version")) is not int or r.get("version") != 1 or r.get("project_id") != project_id
            or not isinstance(r.get("project_root"), str) or not Path(r["project_root"]).is_absolute()
            or r.get("state") not in STATES or not isinstance(r.get("events"), list)
            or not r["events"] or not all(isinstance(x, dict) for x in r["events"])
            or r["events"][-1].get("to") != r["state"]):
        raise ValueError("Invalid project record.")
    previous = None
    for event in r["events"]:
        transition = (event.get("action"), event.get("from"), event.get("to"))
        if transition not in TRANSITIONS or transition[1] != previous:
            raise ValueError("Invalid project event history.")
        date = datetime.datetime.fromisoformat(event["timestamp"])
        if date.utcoffset() is None:
            raise ValueError("Project event timestamp must include timezone.")
        previous = transition[2]
    binding = r.get("configuration")
    if binding is not None and (not isinstance(binding, dict) or binding.get("provider") != "dotagents"
            or not isinstance(binding.get("adapter"), str) or not Path(binding["adapter"]).is_absolute()
            or not isinstance(binding.get("sha256"), str) or not SHA256.fullmatch(binding["sha256"])
            or type(binding.get("doctor_exit")) is not int or binding["doctor_exit"] != 0 or r["state"] == "registered"):
        raise ValueError("Invalid configuration provider binding.")
    return r

def commit(p, record, action, state):
    old = record.get("state")
    record = dict(record, state=state, events=[*record.get("events", []), {
        "action": action, "from": old, "to": state,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()}])
    data = json.dumps(record, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    if len(data.encode("utf-8")) > 1_048_576:
        raise ValueError("Record size limit exceeded.")
    fd, tmp = tempfile.mkstemp(prefix=".project-", dir=p.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        path_kind(p)
        os.replace(tmp, p)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    return read_record(p, record["project_id"])

def scaffold(root, mode):
    args = [sys.executable, "-B", str(SCRIPT), "--root", str(root)]
    if mode:
        args.append(mode)
    proc = subprocess.run(args, capture_output=True, text=True, timeout=60)
    result = json.loads(proc.stdout)
    if proc.returncode or result.get("status") != "PASS":
        raise ValueError("Local scaffold blocked: " + "; ".join(result.get("errors", [])))
    return result

def requested_binding(a):
    adapter = getattr(a, "dotagents_adapter", None)
    digest = getattr(a, "dotagents_sha256", None)
    agents = getattr(a, "agents", None)
    if not (adapter or digest or agents):
        return None
    if a.action != "initialize" or not adapter or not digest or not SHA256.fullmatch(digest):
        raise ValueError("DotAgents initialization requires an explicit adapter path and SHA-256 pin.")
    if agents and (not set(agents.split(",")) <= HOSTS or len(agents.split(",")) != len(set(agents.split(",")))):
        raise ValueError("Invalid or duplicate DotAgents host targets.")
    adapter = absolute(adapter)
    binding = {"provider": "dotagents", "adapter": str(adapter), "sha256": digest, "doctor_exit": 0}
    verify_adapter(binding)
    return binding

def verify_adapter(binding):
    path = absolute(Path(binding["adapter"]))
    if path_kind(path) != "file" or hashlib.sha256(path.read_bytes()).hexdigest() != binding["sha256"]:
        raise ValueError("DotAgents adapter integrity mismatch.")
    return path

def invoke_dotagents(root, binding, operation, agents=None):
    adapter = verify_adapter(binding)
    args = [sys.executable, "-I", "-B", str(adapter), "--project", str(root), operation]
    if operation == "init":
        args.extend(["--agents", agents])
    proc = subprocess.run(args, cwd=root, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=180)
    if proc.returncode != 0 or "Provider exit: 0" not in proc.stdout.splitlines():
        raise ValueError(f"DotAgents {operation} blocked (adapter exit {proc.returncode}).")

def configure_dotagents(root, binding, agents):
    existing = path_kind(root / "agents.toml")
    if existing == "missing":
        if not agents:
            raise ValueError("Specify --agents for a new DotAgents project.")
        invoke_dotagents(root, binding, "init", agents)
    elif existing == "file":
        if agents:
            raise ValueError("Existing agents.toml owns host targets; omit --agents for sync.")
        invoke_dotagents(root, binding, "sync")
    else:
        raise ValueError("Invalid agents.toml.")
    invoke_dotagents(root, binding, "doctor")

def runtime_ready(root, folder, record):
    if record["state"] not in ("initialized", "active"):
        raise ValueError("Project runtime requires initialized or active state.")
    scaffold(root, "--check")
    memory_ready(folder)
    if record.get("configuration"):
        invoke_dotagents(root, record["configuration"], "doctor")

def memory_ready(folder, create=False):
    for name in ("memory", "tasks", "trails"):
        private_dir(folder / name, create=create)
    index = folder / "memory" / "MEMORY.md"
    if path_kind(index) == "missing" and create:
        fd = os.open(index, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write("# Project memory\n\nAdd scoped topic links as evidence becomes available.\n")
    if path_kind(index) != "file" or (os.name != "nt" and index.stat().st_mode & 0o077):
        raise ValueError("Private memory index missing or unsafe.")

def memory_preflight(folder):
    for name in ("memory", "tasks", "trails"):
        path = folder / name
        if path_kind(path) != "missing":
            private_dir(path)
    index = folder / "memory" / "MEMORY.md"
    k = path_kind(index)
    if k != "missing" and (k != "file" or (os.name != "nt" and index.stat().st_mode & 0o077)):
        raise ValueError("Unsafe existing private memory index.")

def run(a):
    if not ID.fullmatch(a.project_id) or a.project_id in RESERVED or "--" in a.project_id:
        raise ValueError("Invalid project ID.")
    root, state = absolute(a.project_root), absolute(a.pmcro_root)
    binding = requested_binding(a)
    if path_kind(root) != "directory":
        raise ValueError("Project root must exist.")
    if root == state or root in state.parents or state in root.parents:
        raise ValueError("Project and private state roots must not overlap.")
    registry = state / "projects"
    folder = registry / a.project_id
    p = folder / "project.json"
    if a.action in ("status", "runtime"):
        for d in (state, registry, folder):
            private_dir(d)
        r = read_record(p, a.project_id)
        if os.path.normcase(r["project_root"]) != os.path.normcase(str(root)):
            raise ValueError("Registered project root mismatch.")
        if a.action == "runtime":
            runtime_ready(root, folder, r)
        return r, False, []
    if not a.apply:
        raise ValueError("Explicit --apply is required for mutations.")
    private_dir(state, create=a.action == "register")
    private_dir(registry, create=a.action == "register")
    lock = registry / ".registry-lock"
    lock.mkdir(mode=0o700)
    try:
        if path_kind(folder) == "missing":
            if a.action != "register":
                raise ValueError("Register the project first.")
            for item in registry.iterdir():
                if item == lock:
                    continue
                if not ID.fullmatch(item.name):
                    raise ValueError("Unrecognized registry entry; inspect before registering.")
                private_dir(item)
                existing = read_record(item / "project.json", item.name)
                if os.path.normcase(existing["project_root"]) == os.path.normcase(str(root)):
                    raise ValueError("Project root already registered.")
            private_dir(folder, create=True)
            return commit(p, {"version": 1, "project_id": a.project_id,
                              "project_root": str(root)}, "register", "registered"), True, []
        private_dir(folder)
        r = read_record(p, a.project_id)
        if os.path.normcase(r["project_root"]) != os.path.normcase(str(root)):
            raise ValueError("Registered project root mismatch.")
        s = r["state"]
        if a.action == "register":
            return r, False, []
        if a.action == "initialize" and s in ("initialized", "active"):
            runtime_ready(root, folder, r)
            if binding:
                if r.get("configuration") == binding:
                    return r, False, []
                if s == "active" or r.get("configuration"):
                    raise ValueError("Provider already bound or project active; do not replace it implicitly.")
                configure_dotagents(root, binding, a.agents)
                scaffold(root, "--check")
                return commit(p, dict(r, configuration=binding), a.action, s), True, []
            return r, False, []
        if a.action == "initialize" and s == "registered":
            memory_preflight(folder)
            scaffold(root, "--dry-run")
            result = scaffold(root, None)
            if binding:
                configure_dotagents(root, binding, a.agents)
            scaffold(root, "--check")
            memory_ready(folder, create=True)
            if binding:
                r = dict(r, configuration=binding)
            return commit(p, r, a.action, "initialized"), True, result["created"]
        if a.action == "activate" and s in ("initialized", "active"):
            runtime_ready(root, folder, r)
            if s == "active":
                return r, False, []
            return commit(p, r, a.action, "active"), True, []
        if a.action == "deactivate" and s == "initialized":
            return r, False, []
        if a.action == "deactivate" and s == "active":
            return commit(p, r, a.action, "initialized"), True, []
        if a.action == "archive" and s in ("registered", "initialized"):
            return commit(p, r, a.action, "archived"), True, []
        if a.action == "archive" and s == "archived":
            return r, False, []
        raise ValueError(f"Invalid transition: {a.action} from {s}")
    finally:
        lock.rmdir()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["register", "initialize", "status", "runtime", "activate", "deactivate", "archive"])
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--pmcro-root", type=Path, default=Path.home() / ".pmcro")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--dotagents-adapter", type=Path)
    parser.add_argument("--dotagents-sha256")
    parser.add_argument("--agents")
    a = parser.parse_args()
    try:
        if a.action in ("status", "runtime") and a.apply:
            raise ValueError("Read-only action; omit --apply.")
        record, changed, paths = run(a)
        result = {"status": "PASS", "action": a.action, "changed": changed,
                  "project_id": a.project_id, "state": record["state"],
                  "event_count": len(record["events"]), "created_local_paths": paths,
                  "privacy": "posix-permissions-checked" if os.name != "nt" else "windows-acl-unverified",
                  "runtime_started": False, "host_project_created": False}
        result["configuration_provider"] = "dotagents" if record.get("configuration") else "local-scaffold"
        if a.action == "runtime":
            result["runtime_provider"] = "pmcro-private-project-registry"
            result["runtime_scope"] = {name: f"projects/{a.project_id}/{path}" for name, path in
                                       (("memory_index", "memory/MEMORY.md"), ("tasks", "tasks"), ("trails", "trails"))}
            result["memory_content_read"] = False
        print(json.dumps(result))
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "BLOCKED", "action": a.action, "error": str(exc),
                          "runtime_started": False, "host_project_created": False}))
        return 1

if __name__ == "__main__":
    sys.exit(main())
