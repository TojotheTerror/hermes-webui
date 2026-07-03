# GitHub Wiki seed

These Markdown files are source pages for the GitHub Wiki attached to `TojotheTerror/hermes-webui`.

The GitHub Wiki is stored separately from the main repository. Review these files in a normal pull request, then publish them with the `Publish GitHub Wiki` workflow or by updating the wiki repository directly.

## Page map

| File | Wiki page |
| --- | --- |
| `Home.md` | Home |
| `_Sidebar.md` | custom sidebar navigation |
| `_Footer.md` | custom footer |
| `Project-Setup.md` | Project Setup |
| `Build-Instructions.md` | Build Instructions |
| `Architecture-Overview.md` | Architecture Overview |
| `Roadmap.md` | Roadmap |
| `Issue-and-Label-Triage.md` | Issue and Label Triage |
| `Contribution-Guide.md` | Contribution Guide |
| `Codex-Readiness.md` | Codex Readiness |
| `Mobile-PWA-Checklist.md` | Mobile PWA Checklist |
| `Security-and-Remote-Access.md` | Security and Remote Access |
| `Troubleshooting.md` | Troubleshooting |
| `Release-Notes.md` | Release Notes |
| `Wiki-Maintenance.md` | Wiki Maintenance |
| `FAQ.md` | FAQ |

## Publishing workflow

The `Publish GitHub Wiki` workflow copies the contents of `docs/wiki/` to the separate GitHub Wiki repository. It can be run manually with `workflow_dispatch` and is configured to run after changes reach the Hermes Android branch.

## Manual publishing fallback

When workflow publishing is unavailable, copy every Markdown file from `docs/wiki/` into the wiki repository, including `_Sidebar.md` and `_Footer.md`, then commit and push the wiki repository.

## Checkpoint workflow

The `Hermes Android repository checkpoints` workflow validates the required issue forms, label manifest, wiki pages, wiki navigation, publishing workflow, and triage references.

Keep private machine details and private configuration values out of wiki pages.
