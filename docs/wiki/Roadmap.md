# Roadmap

This roadmap keeps the Hermes Android / Mobile Client track anchored to the remote-first scope.

## M0 — Project setup, guardrails, and environment readiness

Goal: make repository work safe and repeatable.

Checklist:

- [ ] Issues and Wiki enabled.
- [ ] Issue forms available from the GitHub issue chooser.
- [ ] Labels synced from `.github/labels.yml`.
- [ ] Wiki pages published from `docs/wiki/`.
- [ ] Repository checkpoint workflow passing.
- [ ] Upstream read-only policy documented and visible.

## M1 — Remote mobile PWA MVP

Goal: make Hermes WebUI usable from Android browser/PWA against a workstation-hosted runtime.

Candidate scope:

- narrow viewport layout checks
- touch-friendly chat composer
- reliable session list behavior on mobile
- installable PWA review
- basic mobile smoke test checklist

## M2 — Secure remote access and connection hardening

Goal: document and validate safe Android-to-host access patterns.

Candidate scope:

- local LAN access guidance
- Tailscale/private network guidance
- SSH tunnel guidance
- HTTPS reverse proxy notes
- authentication/logout checks
- CSRF and service-worker cache review gates

## M3 — Android wrapper / TWA decision

Goal: decide whether a thin Android wrapper or Trusted Web Activity is worth maintaining.

Candidate scope:

- wrapper requirements
- signing and distribution risk review
- comparison with plain browser/PWA
- maintenance cost estimate
- human approval gate before implementation

## M4 — Mobile UX parity and polish

Goal: make the Android surface comfortable for real use.

Candidate scope:

- touch targets
- scroll and keyboard behavior
- file browser usability
- settings usability
- theme contrast
- offline/cache behavior where appropriate

## M5 — Codex automation, hooks, reviews, and CI hardening

Goal: keep automation useful without allowing unsafe repository or runtime changes.

Candidate scope:

- `status:ready-for-codex` triage practice
- repository checkpoint workflow
- label sync workflow
- wiki publish workflow
- PR evidence checklist

## M6 — Beta readiness and maintenance loop

Goal: define the recurring release, documentation, and support process.

Candidate scope:

- beta checklist
- known-issues page
- release-note process
- recurring triage cadence
- documentation freshness review
