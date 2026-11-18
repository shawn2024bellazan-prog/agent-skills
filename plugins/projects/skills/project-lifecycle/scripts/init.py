#!/usr/bin/env python3
"""Scaffold PMCR-O workspace without replacement."""
import argparse
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys

MANIFEST = Path(__file__).resolve().parents[1] / "assets" / "directory-template.json"

def kind(path):
    try:
        s = path.lstat()
    except FileNotFoundError:
        return "missing"
    if stat.S_ISLNK(s.st_mode) or getattr(s, "st_file_attributes", 0) & 0x400:
        return "link"
    if stat.S_ISDIR(s.st_mode):
        return "directory"
    if stat.S_ISREG(s.st_mode):
        return "file"
    return "special"

def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.root.absolute()
    mode = "check" if args.check else "dry-run" if args.dry_run else "init"
    out = {"root": str(root), "mode": mode, "created": [], "preserved": [], "missing": [], "errors": []}
    try:
        if kind(root) != "directory":
            raise ValueError("Root must be an existing real directory.")
        root = root.resolve(strict=True)
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        files = manifest["files"]
        dirs = set(manifest["directories"])
        for entry in [*dirs, *files]:
            p = Path(entry)
            if p.is_absolute() or ".." in p.parts or "\\" in entry or ":" in entry:
                raise ValueError("Unsafe template path: " + entry)
            dirs.update(x.as_posix() for x in p.parents if x != Path("."))
        ordered = [(d, "directory") for d in sorted(dirs, key=lambda d: (d.count("/"), d))]
        ordered += [(f, "file") for f in files]
        blocked = set()
        for rel, expected in ordered:
            if any(rel.startswith(b + "/") for b in blocked):
                continue
            actual = kind(root / rel)
            if actual == "missing":
                out["missing"].append(rel)
            elif actual == expected:
                out["preserved"].append(rel)
            else:
                blocked.add(rel)
                out["errors"].append(f"{rel}: expected {expected}, found {actual}")
        if out["errors"]:
            raise ValueError("Conflicting paths; no changes made.")
        ignore = root / ".gitignore"
        if kind(ignore) == "file":
            lines = ignore.read_text(encoding="utf-8").splitlines()
            for rule in manifest["required_ignore_rules"]:
                if rule not in lines or any(l.startswith("!") for l in lines[len(lines)-1-lines[::-1].index(rule)+1:]):
                    out["errors"].append("Existing .gitignore lacks safe exclusion: " + rule)
        in_git = shutil.which("git") and git(root, "rev-parse", "--is-inside-work-tree").returncode == 0
        probes = (".pmcro/probe", ".agents/settings.local.json", ".agents/AGENTS.local.md", "trails/probe")
        if in_git:
            tracked = git(root, "ls-files", "--", ".pmcro", ".agents/settings.local.json", ".agents/AGENTS.local.md", "trails")
            if tracked.returncode or tracked.stdout.strip():
                out["errors"].append("Private paths are tracked or could not be checked.")
            if kind(ignore) == "file":
                for probe in probes:
                    if git(root, "check-ignore", "--no-index", "--", probe).returncode != 0:
                        out["errors"].append("Effective Git ignore missing: " + probe)
        if not out["errors"] and mode == "init":
            missing = set(out["missing"])
            if ".gitignore" in missing:
                with ignore.open("x", encoding="utf-8", newline="\n") as f:
                    f.write(files[".gitignore"])
                out["created"].append(".gitignore")
            if in_git:
                for probe in probes:
                    if git(root, "check-ignore", "--no-index", "--", probe).returncode != 0:
                        raise ValueError("Effective Git ignore missing: " + probe)
            for rel, expected in ordered:
                if rel not in missing or rel == ".gitignore":
                    continue
                path = root / rel
                if expected == "directory":
                    path.mkdir(mode=0o700 if rel.startswith(".pmcro") else 0o755)
                else:
                    with path.open("x", encoding="utf-8", newline="\n") as f:
                        f.write(files[rel])
                out["created"].append(rel)
            out["missing"] = []
    except (OSError, ValueError, KeyError) as exc:
        out["errors"].append(str(exc))
    ok = not out["errors"] and not (mode == "check" and out["missing"])
    out["status"] = "PASS" if ok else "BLOCKED"
    print(json.dumps(out, indent=2))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
