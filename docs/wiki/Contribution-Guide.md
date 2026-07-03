# Contribution Guide

This page summarizes the Hermes Android contribution workflow.

## Issues

Use the repository issue templates:

- Bug report
- Feature request
- Documentation task
- Build or install problem

Each issue should include scope, expected behavior, affected surface, and validation expectations.

## Labels

Core labels:

- `bug`
- `enhancement`
- `documentation`
- `good first issue`
- `question`
- `android`
- `priority: high`
- `needs triage`
- `status:ready-for-codex`
- `status:blocked`

Keep `needs triage` until scope, owner, and next step are clear.

Apply `status:ready-for-codex` only after human review confirms the issue is safe for automation.

## Branches

Use project-scoped branches:

```text
hermes-android/<short-topic>
codex/hermes-android/<short-topic>
```

## Pull requests

A pull request should include:

- summary
- changed files or user-visible behavior
- security/runtime boundary notes
- validation performed
- screenshots or before/after evidence for UI changes
- release-note wording when relevant

Keep one logical change per pull request.

## Upstream safety

Do not write to upstream `NousResearch/*` repositories.

Allowed upstream operations are read-only, such as:

```bash
git fetch upstream
git log upstream/<branch>
git diff upstream/<branch>...HEAD
```

Disallowed upstream operations include pushing, opening upstream PRs/issues, creating upstream labels, updating upstream metadata, or running upstream release/workflow actions.
