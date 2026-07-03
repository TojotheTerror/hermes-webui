# FAQ

## Is Hermes Android a native Android runtime?

No. The default track is remote-first. Android is the client surface. The workstation/server owns Hermes Agent execution, tools, sessions, memory, cron, and model access.

## Can local Android runtime work happen later?

Yes, but only through an explicitly approved experimental issue.

## Which repository should issues target?

Use `TojotheTerror/hermes-webui` for PWA, mobile UI, remote access documentation, wrapper documentation, and WebUI behavior.

Use `TojotheTerror/hermes-agent` only when an issue explicitly requires runtime/API changes that cannot be solved in WebUI.

Upstream `NousResearch/*` repositories are read/reference only.

## What is the readiness label for automation?

Use `status:ready-for-codex`. Apply it only after human review confirms the issue is safe and clear enough for automation.

## Where do wiki pages live?

The source pages live in `docs/wiki/`. The published GitHub Wiki is generated from those files.

## What should be included in a mobile/PWA PR?

Include summary, validation performed, tested Android browser or viewport, access method tested, screenshots for UI changes, and security/runtime notes when relevant.

## When should the wiki be updated?

Update the wiki when setup, build, architecture, remote access, triage, troubleshooting, release, or Android wrapper guidance changes.
