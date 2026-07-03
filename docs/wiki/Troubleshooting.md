# Troubleshooting

Use this page for common Hermes Android / Mobile Client setup and access problems.

## WebUI does not start

Check:

```bash
./ctl.sh status
python3 --version
```

If running a trial, use isolated state:

```bash
HERMES_HOME=/tmp/hermes-webui-agent-home \
HERMES_WEBUI_STATE_DIR=/tmp/hermes-webui-agent-state \
HERMES_WEBUI_PORT=8789 \
python3 bootstrap.py
```

Do not delete or overwrite real `~/.hermes` state without explicit approval.

## Android cannot reach WebUI

Check:

- the WebUI host and port are reachable from the Android device
- the selected access method is working: local LAN, Tailscale, SSH tunnel, HTTPS reverse proxy, or other
- authentication is configured as expected
- browser mixed-content, certificate, or private DNS settings are not blocking the connection

Do not paste private IPs, hostnames, VPN identifiers, tokens, cookies, or credentials into public issues.

## PWA install does not appear

Check:

- the page is served from a compatible origin
- manifest and service-worker behavior are valid for the browser
- the browser supports install prompts for the current context
- cache state has been cleared after service-worker changes

## Chat or session state looks wrong

Check:

- the WebUI branch and commit under test
- active `HERMES_HOME`
- active `HERMES_WEBUI_STATE_DIR`
- whether the test uses real state or isolated trial state
- browser console errors

Redact session content and credentials before sharing logs.

## Reporting a problem

Open a `Build or install problem` or `Bug report` issue and include:

- command or action
- redacted output
- Android device/browser
- host OS
- WebUI branch/commit
- access method
- whether the setup uses fresh or existing state
