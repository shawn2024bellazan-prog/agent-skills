"""Verify existence and privacy of an explicitly scoped PMCR-O memory index."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "project-lifecycle" / "scripts"))
from project_lifecycle import run

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--pmcro-root", type=Path, default=Path.home() / ".pmcro")
    args = parser.parse_args()
    args.action, args.apply = "runtime", False
    try:
        record, _, _ = run(args)
        print(json.dumps({"status": "PASS", "project_id": args.project_id,
                          "state": record["state"], "index_exists": True,
                          "memory_content_read": False}))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}))
        return 1

if __name__ == "__main__":
    sys.exit(main())
