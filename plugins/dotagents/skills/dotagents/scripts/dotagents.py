"""Project-scoped adapter for the installed DotAgents CLI."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import urlsplit

HOSTS = {"claude", "cursor", "codex", "copilot", "vscode", "opencode", "grok", "pi"}
MANAGED = (".agents", "agents.toml", "agents.lock", ".gitignore", ".mcp.json", ".claude", ".cursor", ".codex", ".github", ".vscode", ".opencode", ".grok", ".pi")
NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]*\Z")
TRUST = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]*(?:/[A-Za-z0-9][A-Za-z0-9_.-]*)?\Z")
ENV = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")


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


def validate_url(value, *, loopback=False):
    url = urlsplit(value)
    if (not url.hostname or url.username is not None or url.password is not None or url.query or url.fragment
            or any(c.isspace() for c in value)
            or not (url.scheme == "https" or (loopback and url.scheme == "http" and url.hostname in {"localhost", "127.0.0.1", "::1"}))):
        raise ValueError("Use an HTTPS URL without credentials, query or fragment (HTTP allowed only for loopback MCP).")
    return value


def source_arg(value, root):
    if value.startswith(("path:", "./", "../", ".\\")) or Path(value).is_absolute():
        local = value.removeprefix("path:")
        path = (root / local).resolve(strict=True)
        check_path(path, root)
        if path == root or not path.is_dir():
            raise ValueError("Local source must be an existing directory within the project.")
        # Local source contents must not project private data or external links.
        for directory, dirs, files in os.walk(path, followlinks=False):
            for entry in (*dirs, *files):
                candidate = Path(directory) / entry
                if entry == ".pmcro" or candidate.is_symlink():
                    raise ValueError("Local source contains private state or a symbolic link.")
        return "path:" + path.relative_to(root).as_posix()
    if value.startswith("git:https://"):
        return "git:" + validate_url(value.removeprefix("git:"))
    if value.startswith("https://"):
        return validate_url(value)
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*", value):
        return value
    raise ValueError("Use an explicit owner/repo, HTTPS URL, git:HTTPS URL, or project-local path: source.")


def require_apply(args):
    if not args.apply:
        raise ValueError("Explicit --apply is required for this mutation.")


def arguments(args, root):
    op = args.operation
    command = [op]
    if op == "init":
        command += ["--agents", args.agents]
    elif op == "install":
        require_apply(args)
    elif op == "add":
        require_apply(args)
        if args.all and args.names:
            raise ValueError("Choose explicit names or --all, not both.")
        if not args.all and not args.names:
            raise ValueError("Specify dependency names or --all explicitly.")
        if not all(NAME.fullmatch(name) for name in args.names):
            raise ValueError("Invalid dependency name.")
        command += [source_arg(args.source, root), *args.names]
        if args.ref:
            if args.ref.startswith("-") or not re.fullmatch(r"[A-Za-z0-9_./-]+", args.ref):
                raise ValueError("Invalid Git ref.")
            command += ["--ref", args.ref]
        if args.all:
            command += ["--all"]
    elif op == "remove":
        require_apply(args)
        target = args.target if NAME.fullmatch(args.target) else source_arg(args.target, root)
        command += [target, "--yes"]
    elif op == "list" and args.json:
        command += ["--json"]
    elif op == "doctor" and args.fix:
        require_apply(args)
        command += ["--fix"]
    elif op in {"mcp", "trust"}:
        command += [args.subcommand]
        if args.subcommand == "list":
            # MCP targets can contain private command arguments or URLs; never print them.
            if op == "mcp" or args.json:
                command += ["--json"]
        else:
            require_apply(args)
            if op == "trust":
                if not TRUST.fullmatch(args.source):
                    raise ValueError("Use an exact org, owner/repo or Git domain; no wildcard trust.")
                command += [args.source]
            else:
                if not re.fullmatch(r"[A-Za-z0-9_-]+", args.name):
                    raise ValueError("Invalid MCP server name.")
                command += [args.name]
                if args.subcommand == "add":
                    if args.url:
                        command += ["--url", validate_url(args.url, loopback=True)]
                    else:
                        if not args.command.strip() or any(c in args.command for c in "\r\n\0"):
                            raise ValueError("Invalid MCP command declaration.")
                        command += ["--command", args.command]
                    for env in args.env:
                        if not ENV.fullmatch(env):
                            raise ValueError("Pass environment variable names only, never values.")
                        command += ["--env", env]
    return command


def add_apply(parser):
    parser.add_argument("--apply", action="store_true")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    sub = parser.add_subparsers(dest="operation", required=True)
    init = sub.add_parser("init")
    init.add_argument("--agents", required=True)
    sub.add_parser("sync")
    doctor = sub.add_parser("doctor")
    doctor.add_argument("--fix", action="store_true")
    add_apply(doctor)
    add_apply(sub.add_parser("install"))
    add = sub.add_parser("add")
    add.add_argument("source")
    add.add_argument("names", nargs="*")
    add.add_argument("--ref")
    add.add_argument("--all", action="store_true")
    add_apply(add)
    remove = sub.add_parser("remove")
    remove.add_argument("target")
    add_apply(remove)
    listing = sub.add_parser("list")
    listing.add_argument("--json", action="store_true")
    for operation in ("mcp", "trust"):
        group = sub.add_parser(operation).add_subparsers(dest="subcommand", required=True)
        listing = group.add_parser("list")
        listing.add_argument("--json", action="store_true")
        for action in ("add", "remove"):
            parser2 = group.add_parser(action)
            parser2.add_argument("name" if operation == "mcp" else "source")
            add_apply(parser2)
            if operation == "mcp" and action == "add":
                transport = parser2.add_mutually_exclusive_group(required=True)
                transport.add_argument("--url")
                transport.add_argument("--command")
                parser2.add_argument("--env", action="append", default=[])
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
        command = [provider, "--project", *arguments(args, root)]
        print(f"Project: {root}", flush=True)
        display = command[1:4] if args.operation in {"mcp", "trust"} else command[1:3]
        print(f"Invoke: dotagents {' '.join(display)}", flush=True)
        if args.operation == "mcp" and args.subcommand == "list":
            result = subprocess.run(command, cwd=root, stdin=subprocess.DEVNULL, check=False, capture_output=True, text=True)
            if result.returncode == 0:
                if result.stdout.strip() == "No MCP servers declared in agents.toml.":
                    records = []
                else:
                    records = json.loads(result.stdout)
                print(json.dumps([{"name": row["name"], "transport": row["transport"], "env": row["env"]} for row in records]), flush=True)
        else:
            result = subprocess.run(command, cwd=root, stdin=subprocess.DEVNULL, check=False)
        print(f"Provider exit: {result.returncode}", flush=True)
        return 0 if result.returncode == 0 else 1
    except (OSError, ValueError, RuntimeError, KeyError, TypeError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
