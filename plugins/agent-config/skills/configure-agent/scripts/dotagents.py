"""Project-scoped adapter for the installed DotAgents CLI."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys

HOSTS = {"claude", "cursor", "codex", "copilot", "vscode", "opencode", "grok", "pi"}
MANAGED = (".agents", "agents.toml", ".claude", ".cursor", ".codex", ".github", ".vscode", ".opencode", ".grok", ".pi")


def check_path(path: Path, root: Path) -> None:
    resolved = path.resolve()
    if not resolved.is_relative_to(root) or ".pmcro" in resolved.relative_to(root).parts:
        raise ValueError(f"Unsafe managed path: {path.name}")


def preflight(root: Path, operation: str) -> None:
    if not root.is_dir():
        raise ValueError("Project must be an existing directory")
    if ".pmcro" in root.parts:
        raise ValueError("Private PMCR-O state is not a project configuration root")
    # DotAgents resolves project scope at the containing Git root.
    for parent in (root, *root.parents):
        if (parent / ".git").exists():
            if parent != root:
                raise ValueError("Select the Git repository root, not a subdirectory")
            break
    for name in MANAGED:
        path = root / name
        check_path(path, root)
        if path.is_dir():
            for directory, dirs, files in os.walk(path, followlinks=False):
                for entry in (*dirs, *files):
                    candidate = Path(directory) / entry
                    if candidate.is_symlink():
                        check_path(candidate, root)
    config = root / "agents.toml"
    if operation == "init" and (config.exists() or config.is_symlink()):
        raise ValueError("Existing agents.toml; use sync or doctor")
    if operation != "init" and not config.is_file():
        raise ValueError("Missing agents.toml; initialize project explicitly first")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    sub = parser.add_subparsers(dest="operation", required=True)
    init = sub.add_parser("init")
    init.add_argument("--agents", required=True)
    sub.add_parser("sync")
    sub.add_parser("doctor")
    args = parser.parse_args(argv)
    if args.operation == "init":
        hosts = args.agents.split(",")
        if not set(hosts) <= HOSTS or len(hosts) != len(set(hosts)):
            parser.error("--agents must be a comma-separated list of unique supported hosts")
    try:
        root = args.project.resolve(strict=True)
        preflight(root, args.operation)
        provider = shutil.which("dotagents")
        if not provider:
            raise ValueError("DotAgents CLI unavailable; install a trusted provider separately")
        command = [provider, "--project", args.operation]
        if args.operation == "init":
            command.extend(["--agents", args.agents])
        print(f"Project: {root}", flush=True)
        print(f"Invoke: dotagents {' '.join(command[1:])}", flush=True)
        result = subprocess.run(command, cwd=root, stdin=subprocess.DEVNULL, check=False)
        print(f"Provider exit: {result.returncode}", flush=True)
        return 0 if result.returncode == 0 else 1
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
