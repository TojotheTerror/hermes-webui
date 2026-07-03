#!/usr/bin/env python3
"""Synchronize GitHub labels from .github/labels.yml.

The manifest is intentionally simple, so this parser avoids non-stdlib YAML
dependencies in GitHub Actions.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / ".github" / "labels.yml"


def parse_manifest(path: Path) -> list[dict[str, str]]:
    labels: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- name:"):
            if current:
                labels.append(current)
            current = {"name": line.split(":", 1)[1].strip().strip('"').strip("'")}
            continue
        if current is None or ":" not in line:
            continue
        key, value = line.split(":", 1)
        current[key.strip()] = value.strip().strip('"').strip("'")

    if current:
        labels.append(current)
    return labels


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def main() -> int:
    repo = os.environ.get("GITHUB_REPOSITORY", "TojotheTerror/hermes-webui")
    labels = parse_manifest(MANIFEST)
    if not labels:
        print(f"No labels found in {MANIFEST}", file=sys.stderr)
        return 1

    failed: list[str] = []
    for label in labels:
        name = label["name"]
        color = label.get("color", "ededed")
        description = label.get("description", "")

        edit = run([
            "gh",
            "label",
            "edit",
            name,
            "--repo",
            repo,
            "--color",
            color,
            "--description",
            description,
        ])
        if edit.returncode == 0:
            print(f"updated label: {name}")
            continue

        create = run([
            "gh",
            "label",
            "create",
            name,
            "--repo",
            repo,
            "--color",
            color,
            "--description",
            description,
        ])
        if create.returncode == 0:
            print(f"created label: {name}")
        else:
            failed.append(f"{name}: {create.stderr.strip() or edit.stderr.strip()}")

    if failed:
        print("Label sync failed:", file=sys.stderr)
        for item in failed:
            print(f"- {item}", file=sys.stderr)
        return 1

    print(f"Synced {len(labels)} labels for {repo}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
