# Hermes Android / Mobile Client Wiki

Hermes Android is the remote-first mobile client track for Hermes WebUI.

The phone is the client surface. A workstation or server continues to own Hermes Agent execution, tools, sessions, memory, cron, and model access.

## Start here

- [Project Setup](Project-Setup): clone, branches, local run, and safe upstream remotes.
- [Build Instructions](Build-Instructions): run/test commands and Android/PWA build boundaries.
- [Architecture Overview](Architecture-Overview): remote-first topology and runtime ownership.
- [Contribution Guide](Contribution-Guide): issues, labels, branches, PRs, and Codex readiness.
- [Release Notes](Release-Notes): release-note template and mobile rollout checklist.
- [Troubleshooting](Troubleshooting): common setup, access, auth, PWA, and logging problems.

## Default scope

Hermes Android work targets:

- Android browser support
- installable PWA behavior
- thin Android wrapper or TWA exploration
- secure remote access from Android to Hermes WebUI
- mobile UI and onboarding polish
- documentation and triage workflow

Default non-goals:

- running the full Hermes Agent runtime on Android
- embedding Python in the Android app
- moving sessions, memory, skills, cron, tools, or models onto Android
- writing to upstream `NousResearch/*` repositories

Experimental local-runtime work requires explicit issue approval and human review.
