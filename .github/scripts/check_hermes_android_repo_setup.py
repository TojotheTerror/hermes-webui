#!/usr/bin/env python3
"""Repository checkpoint checks for Hermes Android setup docs.

This script intentionally uses only the Python standard library so it can run in
GitHub Actions without extra dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_ISSUE_FORMS = [
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/documentation_task.yml",
    ".github/ISSUE_TEMPLATE/build_install_problem.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
]

REQUIRED_LABELS = [
    "bug",
    "enhancement",
    "documentation",
    "good first issue",
    "question",
    "android",
    "priority: high",
    "needs triage",
    "status:ready-for-codex",
    "status:blocked",
]

REQUIRED_WIKI_PAGES = [
    "Home.md",
    "_Sidebar.md",
    "_Footer.md",
    "Project-Setup.md",
    "Build-Instructions.md",
    "Architecture-Overview.md",
    "Roadmap.md",
    "Issue-and-Label-Triage.md",
    "Contribution-Guide.md",
    "Codex-Readiness.md",
    "Mobile-PWA-Checklist.md",
    "Security-and-Remote-Access.md",
    "Troubleshooting.md",
    "Release-Notes.md",
    "Wiki-Maintenance.md",
    "FAQ.md",
]

ERRORS: list[str] = []


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read(path: str) -> str:
    target = ROOT / path
    if not target.exists():
        ERRORS.append(f"Missing required file: {path}")
        return ""
    return target.read_text(encoding="utf-8")


def require_contains(path: str, needles: list[str]) -> None:
    text = read(path)
    for needle in needles:
        if needle not in text:
            ERRORS.append(f"{path} must contain {needle!r}")


def check_issue_forms() -> None:
    for form in REQUIRED_ISSUE_FORMS:
        text = read(form)
        if not text:
            continue
        if form.endswith("config.yml"):
            require_contains(form, ["blank_issues_enabled: false", "contact_links:"])
            continue
        for field in ["name:", "description:", "title:", "labels:", "body:"]:
            if field not in text:
                ERRORS.append(f"{form} is missing issue-form field {field!r}")
        if "TojotheTerror/hermes-webui" not in text:
            ERRORS.append(f"{form} must state the writable repository boundary")


def check_label_manifest() -> None:
    text = read(".github/labels.yml")
    for label in REQUIRED_LABELS:
        if not re.search(rf"name:\s*[\"']?{re.escape(label)}[\"']?", text):
            ERRORS.append(f".github/labels.yml missing label: {label}")


def check_wiki_pages() -> None:
    wiki_root = ROOT / "docs" / "wiki"
    for page in REQUIRED_WIKI_PAGES:
        path = wiki_root / page
        if not path.exists():
            ERRORS.append(f"Missing wiki page: {rel(path)}")
            continue
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            ERRORS.append(f"Wiki page is empty: {rel(path)}")
        elif not (text.startswith("# ") or page == "_Footer.md"):
            ERRORS.append(f"Wiki page should start with an H1 heading: {rel(path)}")

    home = read("docs/wiki/Home.md")
    sidebar = read("docs/wiki/_Sidebar.md")
    for page in REQUIRED_WIKI_PAGES:
        if page in {"Home.md", "_Sidebar.md", "_Footer.md"}:
            continue
        wiki_name = page.removesuffix(".md")
        if wiki_name not in home and wiki_name not in sidebar:
            ERRORS.append(f"Wiki page {page} is not linked from Home or _Sidebar")


def check_workflows() -> None:
    require_contains(
        ".github/workflows/hermes-android-repo-checkpoints.yml",
        ["workflow_dispatch:", "check_hermes_android_repo_setup.py"],
    )
    require_contains(
        ".github/workflows/publish-wiki.yml",
        ["workflow_dispatch:", ".wiki.git", "docs/wiki"],
    )
    require_contains(
        ".github/workflows/sync-labels.yml",
        ["workflow_dispatch:", "actions/github-script", "issues: write", ".github/labels.yml"],
    )


def check_project_docs() -> None:
    require_contains(
        "docs/hermes-android/README.md",
        ["repository-triage.md", "docs/wiki/", "status:ready-for-codex"],
    )
    require_contains(
        "docs/hermes-android/repository-triage.md",
        ["status:ready-for-codex", ".github/labels.yml", "docs/wiki/"],
    )


def main() -> int:
    check_issue_forms()
    check_label_manifest()
    check_wiki_pages()
    check_workflows()
    check_project_docs()

    if ERRORS:
        print("Hermes Android repository checkpoint failed:")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Hermes Android repository checkpoint passed.")
    print(f"Checked {len(REQUIRED_ISSUE_FORMS)} issue forms, {len(REQUIRED_LABELS)} labels, and {len(REQUIRED_WIKI_PAGES)} wiki pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
