# Hermes Android / Mobile Client

Hermes Android is a remote-first mobile client track for Hermes WebUI. The goal
is to make a workstation-hosted Hermes Agent usable from Android through an
installable PWA or thin Android wrapper while keeping all agent execution on the
remote workstation/server.

## Product scope

Primary target:

```text
Android browser / PWA / app wrapper
  -> secure private or HTTPS connection
  -> workstation-hosted Hermes WebUI
  -> Hermes Agent runtime, tools, sessions, memory, cron, and models
```

The phone is the client surface. The workstation remains the execution owner.

## Explicit non-goals for the default track

- Do not run the full Hermes Agent runtime on Android.
- Do not embed a Python runtime in the Android app.
- Do not move session stores, memory, skills, or cron ownership onto Android.
- Do not add local Android model execution.
- Do not port desktop terminal/tool sandbox behavior to Android.

Those may be explored later only through explicitly approved experimental-local-runtime work.

## Repositories

Writable project repositories:

- `TojotheTerror/hermes-webui`
- `TojotheTerror/hermes-agent` only when a scoped runtime/API change is required

Read/reference-only upstream repositories:

- `NousResearch/hermes-webui`
- `NousResearch/hermes-agent`

Never push branches, commits, tags, issues, labels, pull requests, releases,
workflow changes, or project metadata to upstream repositories.

## First milestones

1. M0 — Project setup, guardrails, and environment readiness
2. M1 — Remote mobile PWA MVP
3. M2 — Secure remote access and connection hardening
4. M3 — Android wrapper / TWA decision
5. M4 — Mobile UX parity and polish
6. M5 — Codex automation, hooks, reviews, and CI hardening
7. M6 — Beta readiness and maintenance loop

## Codex dispatch rule

Implementation issues should be explicitly marked ready before Codex starts.
The GitHub replacement for the previous Linear readiness gate is:

```text
status:ready-for-codex
```

If an issue has or implies a human gate, Codex should not proceed until a human
explicitly approves the run.
