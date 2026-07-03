# Repository triage workflow

This page defines the first-pass GitHub issue and label workflow for Hermes Android / Mobile Client work in `TojotheTerror/hermes-webui`.

## Issue intake

Use the templates in `.github/ISSUE_TEMPLATE/`:

- Bug report: broken behavior in WebUI, mobile/PWA, remote access, auth, onboarding, or docs.
- Feature request: new WebUI, Android/PWA, wrapper, or remote-access capability.
- Documentation task: setup, architecture, troubleshooting, release notes, or wiki work.
- Build or install problem: bootstrap, run, test, reinstall, PWA install, or Android access setup failures.

Blank issues are disabled so new reports start with enough routing and safety information.

## Required triage labels

The repository should contain the labels defined in `.github/labels.yml`.

Minimum labels:

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

The `Sync GitHub labels` workflow keeps actual repository labels aligned with the manifest after merge.

## Triage sequence

1. Confirm the issue belongs in `TojotheTerror/hermes-webui`.
2. Confirm upstream `NousResearch/*` repositories stay read/reference only.
3. Confirm the report is safe to keep public.
4. Apply the appropriate type label: `bug`, `enhancement`, `documentation`, or `question`.
5. Keep `needs triage` until scope, owner, and next step are clear.
6. Add `android` for Android browser, PWA, wrapper, or mobile access work.
7. Add `priority: high` only when delay materially blocks milestone progress or exposes a serious user/security problem.
8. Add `good first issue` only when the task has a small scope, clear acceptance criteria, and low risk.
9. Add `status:blocked` when work cannot proceed without a human decision, credential, external dependency, or prerequisite PR.
10. Add `status:ready-for-codex` only after a human confirms the issue is ready for automation.

## Codex readiness

`status:ready-for-codex` is the GitHub replacement for the previous external readiness gate.

Before applying it, confirm:

- the issue has clear acceptance criteria
- repository target is writable and safe
- upstream repositories remain read/reference only
- human review gates are stated for auth, CSRF, service-worker caching, remote exposure, runtime/API boundaries, Android signing/distribution, or automation hooks
- expected validation is named

Automation must stop before any action that would write to an upstream `NousResearch/*` repository.

## Checkpoints

The repository now has explicit checkpoints:

- `Hermes Android repository checkpoints` validates issue forms, label manifest, wiki pages, workflow references, and triage documentation.
- `Publish GitHub Wiki` publishes the reviewed `docs/wiki/` source pages to the GitHub Wiki.
- `Sync GitHub labels` creates or updates actual repository labels from `.github/labels.yml`.

Run the checkpoint workflow after changes to issue templates, labels, Hermes Android docs, wiki source pages, or publishing workflows. Correct the source files before publishing the wiki or marking the setup issue complete.

## Wiki publishing

The staged wiki pages live in `docs/wiki/`. After review, publish them into the GitHub Wiki with the repository workflow or by updating the separate wiki repository directly.

The wiki repository may need to be initialized once before direct wiki publishing works consistently.
