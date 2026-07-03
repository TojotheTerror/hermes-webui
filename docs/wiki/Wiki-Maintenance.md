# Wiki Maintenance

The canonical wiki source lives in `docs/wiki/` on the repository branch. The GitHub Wiki is the published copy.

## Source and publish flow

1. Edit Markdown pages under `docs/wiki/`.
2. Open or update a pull request.
3. Let the repository checkpoint workflow validate the page set.
4. Merge after review.
5. Publish to the GitHub Wiki with the wiki publishing workflow or by updating the wiki repository directly.

## Required pages

- `Home.md`
- `_Sidebar.md`
- `_Footer.md`
- `Project-Setup.md`
- `Build-Instructions.md`
- `Architecture-Overview.md`
- `Roadmap.md`
- `Issue-and-Label-Triage.md`
- `Contribution-Guide.md`
- `Codex-Readiness.md`
- `Mobile-PWA-Checklist.md`
- `Security-and-Remote-Access.md`
- `Troubleshooting.md`
- `Release-Notes.md`
- `FAQ.md`

## Publishing workflow

The wiki publishing workflow copies `docs/wiki/` into the separate GitHub Wiki repository.

Run it after merge, or let it run on configured branch updates. If the wiki repository has not been initialized yet, create the first wiki page in the GitHub UI or run the workflow once after confirming Wiki is enabled.

## Manual publishing fallback

When workflow publishing is unavailable, copy every Markdown page from `docs/wiki/` into the wiki repository, including `_Sidebar.md` and `_Footer.md`, then commit and push the wiki repository.

## Review cadence

Review the wiki when:

- a milestone changes
- a new access method is added
- auth, remote exposure, or service-worker behavior changes
- Android wrapper/signing decisions change
- issue templates or labels change
- onboarding or troubleshooting guidance changes
