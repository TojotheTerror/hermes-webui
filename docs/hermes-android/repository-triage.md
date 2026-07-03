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

## Triage sequence

1. Confirm the issue belongs in `TojotheTerror/hermes-webui`.
2. Confirm it does not require writes to `NousResearch/*` upstream repositories.
3. Remove or redact secrets, tokens, cookies, private URLs, and private local-machine details.
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

Codex must stop before any tool call, shell command, or Git operation that would write to an upstream `NousResearch/*` repository.

## Wiki publishing

The staged wiki pages live in `docs/wiki/`. After review, copy them into the GitHub Wiki or push them to the separate wiki repository:

```bash
git clone git@github.com:TojotheTerror/hermes-webui.wiki.git
cp docs/wiki/*.md hermes-webui.wiki/
cd hermes-webui.wiki
git add .
git commit -m "Initialize Hermes Android wiki"
git push
```

The wiki repository may not exist until the first wiki page is created in GitHub.
