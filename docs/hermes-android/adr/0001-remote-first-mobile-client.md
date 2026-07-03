# ADR-0001: Remote-first Hermes Android client

## Status

Proposed

## Context

The original Hermes Android idea considered running the full Hermes Agent on an
Android phone, including Python runtime, tools, session store, and local
execution. That path remains technically possible as a separate research track,
but it is not the fastest path to a useful Android experience.

The immediate product need is simpler: use an Android application or PWA to
access a Hermes Agent already running on a workstation or server.

## Decision

Hermes Android will be remote-first.

The Android surface will connect to a workstation-hosted Hermes WebUI, Gateway,
or Agent API. The workstation/server remains the execution owner for:

- agent loop
- model/provider routing
- tool execution
- sessions and transcript persistence
- memory and skills
- cron and scheduled jobs
- filesystem/workspace operations
- active run lifecycle
- approvals and clarify semantics

## Consequences

Positive:

- Faster MVP.
- Reuses existing Hermes WebUI mobile/PWA work.
- Avoids Android Python packaging and dependency issues.
- Keeps desktop/workstation tool parity.
- Keeps long-running tasks and cron off the phone.
- Reduces battery/background execution complexity.

Negative:

- Requires a reachable workstation/server.
- Requires secure remote access setup.
- PWA installability depends on origin/security behavior.
- Native Android features may require a later wrapper.

## Upstream policy

Upstream Hermes repositories are read/reference only for this project. All
branches, commits, issues, pull requests, automation, and project metadata must
be created only in `TojotheTerror/*` repositories unless a human explicitly
changes this policy.

Local clones should disable upstream pushes:

```bash
git remote set-url --push upstream DISABLED
```

## Deferred work

- Embedded Android Python runtime.
- Local model inference.
- Local Hermes session database on Android.
- Local Android tool execution.
- Android cron/always-on agent execution.
- Full native Android client over stable runtime API.
