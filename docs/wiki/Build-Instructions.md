# Build Instructions

Hermes WebUI is primarily a Python and vanilla JavaScript web application. Hermes Android work should first target mobile browser and PWA behavior unless an issue explicitly scopes native wrapper work.

## Run locally

From the repository root:

```bash
python3 bootstrap.py
```

Use the repository scripts when available:

```bash
./start.sh
./ctl.sh status
```

Prefer isolated state for trials:

```bash
HERMES_HOME=/tmp/hermes-webui-agent-home \
HERMES_WEBUI_STATE_DIR=/tmp/hermes-webui-agent-state \
HERMES_WEBUI_PORT=8789 \
python3 bootstrap.py
```

## Run tests

Use the repository test script instead of invoking pytest directly:

```bash
./scripts/test.sh
```

The script manages the repository virtual environment and supported Python versions.

## Mobile/PWA verification

For Android browser or PWA work, verify:

- narrow viewport layout
- touch targets and scrolling
- session and chat rendering
- composer behavior
- authentication and logout behavior
- service-worker and cache behavior when relevant
- remote access path used by the issue: local LAN, Tailscale, SSH tunnel, HTTPS reverse proxy, or other

Do not include private network identifiers, tokens, cookies, full `.env` contents, or full `auth.json` contents in issue reports or PRs.

## Native wrapper boundary

Native Android wrapper, TWA, signing, distribution, or store packaging work must be explicitly scoped in an issue.

Default Hermes Android work must not:

- embed the full Hermes Agent runtime
- embed a Python runtime
- move sessions, memory, cron, tools, or models onto Android
- add local Android model execution
