# Hermes Android / Mobile Client Wiki

Hermes Android is the remote-first mobile client track for Hermes WebUI.

The phone is the client surface. A workstation or server continues to own Hermes Agent execution, tools, sessions, memory, cron, and model access.

## Start here

- [Project Setup](Project-Setup): clone, branches, local run, and safe upstream remotes.
- [Build Instructions](Build-Instructions): run/test commands and Android/PWA build boundaries.
- [Architecture Overview](Architecture-Overview): remote-first topology and runtime ownership.
- [Roadmap](Roadmap): milestone sequence from setup through beta readiness.

## Operations

- [Issue and Label Triage](Issue-and-Label-Triage): intake flow, labels, and triage exits.
- [Contribution Guide](Contribution-Guide): issues, branches, PRs, and upstream safety.
- [Codex Readiness](Codex-Readiness): readiness gate for automation.
- [Mobile PWA Checklist](Mobile-PWA-Checklist): Android browser/PWA verification checklist.
- [Security and Remote Access](Security-and-Remote-Access): access patterns and review gates.

## Maintenance

- [Troubleshooting](Troubleshooting): common setup, access, auth, PWA, and logging problems.
- [Release Notes](Release-Notes): release-note template and mobile rollout checklist.
- [Wiki Maintenance](Wiki-Maintenance): source-of-truth and publishing process.
- [FAQ](FAQ): short answers for recurring Hermes Android questions.

## GitHub Wiki features in use

This wiki uses:

- `Home.md` as the landing page
- `_Sidebar.md` for navigation
- `_Footer.md` for repository-wide safety notes
- topic pages for setup, build, architecture, roadmap, triage, readiness, mobile/PWA checks, remote access, troubleshooting, release notes, maintenance, and FAQ
- a repository workflow to publish `docs/wiki/` into the GitHub Wiki after review

## Default scope

Hermes Android work targets Android browser support, installable PWA behavior, thin wrapper exploration, secure remote access, mobile UI polish, documentation, and triage workflow.

Default non-goals include running the full Hermes Agent runtime on Android, embedding Python in the Android app, moving runtime-owned state onto Android, or writing to upstream `NousResearch/*` repositories.

Experimental local-runtime work requires explicit issue approval and human review.
