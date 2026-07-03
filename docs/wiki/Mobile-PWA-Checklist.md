# Mobile PWA Checklist

Use this checklist for Android browser and PWA changes.

## Scope check

- [ ] The phone remains the client surface.
- [ ] The workstation/server remains the runtime owner.
- [ ] The change does not embed Python or the full Hermes Agent runtime on Android.
- [ ] The change does not move sessions, memory, skills, cron, tools, or model execution onto Android.

## Layout and interaction

- [ ] Narrow viewport layout is usable.
- [ ] Main navigation is reachable without desktop hover behavior.
- [ ] Chat composer remains visible and usable with the Android keyboard open.
- [ ] Touch targets are large enough for common actions.
- [ ] Scroll behavior is predictable in chat, sidebars, modals, and settings.
- [ ] Long messages and code blocks do not break the viewport.

## PWA behavior

- [ ] Manifest behavior is reviewed when changed.
- [ ] Service-worker/cache behavior is reviewed when changed.
- [ ] Install flow is tested when relevant.
- [ ] Reload/update behavior is documented when cache changes can affect users.

## Remote access

- [ ] The tested access method is named: local LAN, Tailscale, SSH tunnel, HTTPS reverse proxy, or other.
- [ ] Authentication works from Android.
- [ ] Logout works from Android.
- [ ] Connection errors are understandable and do not leak secrets.

## Evidence for PRs

Include the following when relevant:

- screenshots or screen recordings for UI changes
- viewport/device used for testing
- access method used for testing
- commands run
- automated test result or reason tests were not run
- security notes for auth, CSRF, service-worker, remote exposure, or runtime/API changes
