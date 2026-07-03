# Project Setup

This page covers the safe repository and local setup for Hermes Android / Mobile Client work.

## Repository target

Writable repository:

```text
TojotheTerror/hermes-webui
```

Read/reference-only upstream repositories:

```text
NousResearch/hermes-webui
NousResearch/hermes-agent
```

Do not push branches, commits, tags, issues, pull requests, labels, releases, workflow changes, or project metadata to upstream repositories.

## Clone

```bash
git clone git@github.com:TojotheTerror/hermes-webui.git hermes-webui
cd hermes-webui
```

Add upstream as fetch-only:

```bash
git remote add upstream https://github.com/NousResearch/hermes-webui.git
git remote set-url --push upstream DISABLED
git remote -v
```

Expected remote shape:

```text
origin    git@github.com:TojotheTerror/hermes-webui.git (fetch)
origin    git@github.com:TojotheTerror/hermes-webui.git (push)
upstream  https://github.com/NousResearch/hermes-webui.git (fetch)
upstream  DISABLED (push)
```

## Branches

Use branch names under one of these prefixes:

```text
hermes-android/
codex/hermes-android/
```

Keep one logical change per pull request.

## First read

Before changing code or docs, read:

1. `README.md`
2. `CONTRIBUTING.md`
3. `AGENTS.md`
4. `docs/hermes-android/README.md`
5. `docs/hermes-android/upstream-readonly-policy.md`

For onboarding, reinstall, or failed first-run work, also read:

```text
docs/onboarding-agent-checklist.md
```

## Local trial state

Use isolated state for experiments unless a human explicitly asks to use real state:

```bash
HERMES_HOME=/tmp/hermes-webui-agent-home \
HERMES_WEBUI_STATE_DIR=/tmp/hermes-webui-agent-state \
HERMES_WEBUI_PORT=8789 \
python3 bootstrap.py
```

Do not delete or overwrite a real `~/.hermes` directory without explicit approval.
