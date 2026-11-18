"""Fixed-verb entrypoint; delegate to the canonical DotAgents adapter."""
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] != "--project":
        print("Usage: run.py --project ABSOLUTE_PATH [operation arguments]", file=sys.stderr)
        sys.exit(2)
    adapter = Path(__file__).resolve().parents[2] / "dotagents/scripts/dotagents.py"
    if not adapter.is_file():
        print("BLOCKED: canonical DotAgents adapter unavailable", file=sys.stderr)
        sys.exit(1)
    sys.exit(subprocess.run([sys.executable, "-I", "-B", str(adapter), *sys.argv[1:3], "install", *sys.argv[3:]], check=False).returncode)
