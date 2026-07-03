# Security and Remote Access

Hermes Android connects an Android client surface to a workstation/server-hosted Hermes WebUI and Hermes Agent runtime. Treat every remote access change as security-sensitive.

## Supported access patterns

Document and test the access pattern used by each issue or PR:

- local LAN
- Tailscale or another private network
- SSH tunnel
- HTTPS reverse proxy
- other explicitly approved access method

Do not publish private IP addresses, private hostnames, VPN identifiers, tokens, cookies, passwords, or full local config dumps.

## Human review gates

Human review is required before changes that affect:

- authentication
- CSRF behavior
- service-worker caching rules
- remote exposure defaults
- runtime/API boundaries
- Android signing or distribution assets
- automation hooks or workflow behavior

## Authentication checks

For mobile-facing changes, verify:

- login works from Android browser/PWA
- logout clears expected client state
- expired sessions recover cleanly
- protected routes do not render private data before auth is confirmed
- error messages do not leak credentials or private paths

## Service-worker and cache checks

When service-worker behavior changes, verify:

- stale assets do not keep broken UI active after deployment
- authenticated content is not cached unsafely
- logout or auth changes do not leave sensitive data visible through back/forward navigation
- users can recover from a bad cache state

## Remote exposure notes

Default documentation should prefer private or explicitly secured access. If a PR changes bind addresses, reverse-proxy assumptions, headers, CORS, cookies, or tunnel behavior, include the security impact in the PR body.

## Issue reporting hygiene

Reports should include enough evidence to reproduce a problem, but must redact:

- API keys
- OAuth tokens
- cookies
- private hostnames
- private IPs where not required
- full `.env` files
- full `auth.json` files
- password hashes
