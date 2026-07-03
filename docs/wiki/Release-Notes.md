# Release Notes

Use this page to stage Hermes Android / Mobile Client release notes before they are folded into the repository release process.

## Unreleased

### Added

- Repository issue templates for bug reports, feature requests, documentation tasks, and build/install problems.
- Initial label manifest for triage and Codex readiness.
- Seed pages for the GitHub Wiki.

### Changed

- GitHub Issues and Wiki are available for repository planning and documentation.

### Fixed

- Nothing yet.

### Known issues

- Actual GitHub labels must be created or synchronized from `.github/labels.yml`.
- Wiki seed pages must be published to the separate GitHub Wiki after review.

## Release checklist

Before a mobile-facing release:

- [ ] Mobile/PWA issues are triaged.
- [ ] `priority: high` issues are resolved or explicitly deferred.
- [ ] Android browser/PWA smoke test is complete.
- [ ] Authentication and logout behavior are checked.
- [ ] Remote access documentation is current.
- [ ] Service-worker/cache behavior is checked when changed.
- [ ] No private machine details or secrets appear in docs or release notes.
- [ ] Release-note wording is included in the PR body when `CHANGELOG.md` is not edited directly.
