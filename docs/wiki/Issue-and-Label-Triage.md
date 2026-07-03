# Issue and Label Triage

Use this page during first-pass issue review.

## Intake steps

1. Confirm the issue belongs in `TojotheTerror/hermes-webui`.
2. Confirm upstream `NousResearch/*` repositories are read/reference only.
3. Confirm the report is safe to keep public.
4. Apply one primary type label.
5. Keep `needs triage` until scope, owner, and next step are clear.
6. Add `android` for Android browser, PWA, wrapper, or mobile-access work.
7. Add priority or status labels only when justified.

## Core labels

| Label | Use |
| --- | --- |
| `bug` | Broken behavior or reproducible defect. |
| `enhancement` | New capability or improvement. |
| `documentation` | Docs, examples, wiki, guides, or release-note work. |
| `good first issue` | Small, clear, low-risk task for a first contribution. |
| `question` | Question, clarification, or support-style discussion. |
| `android` | Android browser, PWA, wrapper, or mobile-client work. |
| `priority: high` | Urgent work that blocks a milestone or serious user/security concern. |
| `needs triage` | New issue awaiting review and routing. |
| `status:ready-for-codex` | Human-approved automation-ready issue. |
| `status:blocked` | Waiting on a dependency, credential, decision, or prerequisite. |

## Removing `needs triage`

Remove `needs triage` only after:

- the issue type is clear
- owner or next step is clear
- acceptance criteria exist or are not needed
- unsafe upstream writes are out of scope
- required human gates are stated

## Applying `good first issue`

Apply `good first issue` only when:

- scope is small
- expected files or docs are named
- validation is straightforward
- the task does not touch auth, CSRF, service-worker caching, remote exposure, runtime/API boundaries, Android signing, or automation hooks

## Applying `status:ready-for-codex`

Apply this label only after human review confirms that automation can proceed safely.

Do not apply it to issues that require a decision, credential, external dependency, or security-sensitive approval that has not happened yet.
