# Architecture Overview

Hermes Android is remote-first.

## Topology

```text
Android browser / PWA / thin wrapper
  -> secure private or HTTPS connection
  -> workstation/server-hosted Hermes WebUI
  -> Hermes Agent runtime, tools, sessions, memory, cron, and models
```

The Android device presents the client UI. The workstation/server remains the execution boundary.

## Runtime ownership

Owned by workstation/server:

- Hermes Agent process
- model/provider access
- tool execution
- terminal and workspace access
- sessions
- memory
- skills
- cron jobs
- credentials and runtime config

Owned by Android client:

- browser/PWA shell
- mobile layout
- touch interaction
- viewport behavior
- optional wrapper navigation and install affordances

## Security-sensitive areas

Human review is required for changes that affect:

- authentication
- CSRF behavior
- service-worker caching rules
- remote exposure defaults
- runtime/API boundaries
- Android signing or distribution assets
- automation hooks or workflow behavior

## Repository boundaries

Writable:

```text
TojotheTerror/hermes-webui
TojotheTerror/hermes-agent only for explicitly scoped runtime/API work
```

Read/reference only:

```text
NousResearch/hermes-webui
NousResearch/hermes-agent
```

Any automation that would write to upstream must stop before execution and report the unsafe target.
