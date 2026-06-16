#!/usr/bin/env python3
"""Run the core release validation workflow."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    "scripts/build_news_event_database.py",
    "scripts/analyze_event_family_patterns.py",
    "scripts/scenario_similarity.py",
    "scripts/validate_project_data.py",
]


def run_check(script: str) -> tuple[str, int]:
    result = subprocess.run(
        [sys.executable, script],
        cwd=REPO_ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    print(f"\n== {script} ==")
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)
    status = "PASS" if result.returncode == 0 else "FAIL"
    print(f"{status}: {script}")
    return script, result.returncode


def main() -> int:
    results = [run_check(script) for script in CHECKS]
    failures = [script for script, code in results if code != 0]

    print("\nRelease check summary")
    for script, code in results:
        status = "PASS" if code == 0 else "FAIL"
        print(f"- {status}: {script}")

    if failures:
        print("\nRequired checks failed.", file=sys.stderr)
        return 1

    print("\nAll required checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
