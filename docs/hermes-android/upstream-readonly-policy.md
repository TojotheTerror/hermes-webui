# Upstream read-only policy

Hermes Android development must never write to upstream Hermes repositories.

## Writable repositories

Only these repositories are writable for Hermes Android work:

- `TojotheTerror/hermes-webui`
- `TojotheTerror/hermes-agent` when an issue explicitly requires agent/runtime changes

## Read/reference-only repositories

These repositories are reference-only:

- `NousResearch/hermes-webui`
- `NousResearch/hermes-agent`
- any other upstream source repository used for comparison

Do not push branches, commits, tags, issues, pull requests, labels, releases,
workflow changes, or project metadata to upstream repositories.

## Required local remote layout

Recommended WebUI clone:

```bash
git clone git@github.com:TojotheTerror/hermes-webui.git hermes-webui
cd hermes-webui
git remote add upstream https://github.com/NousResearch/hermes-webui.git
git remote set-url --push upstream DISABLED
git remote -v
```

Recommended Agent clone:

```bash
git clone git@github.com:TojotheTerror/hermes-agent.git hermes-agent
cd hermes-agent
git remote add upstream https://github.com/NousResearch/hermes-agent.git
git remote set-url --push upstream DISABLED
git remote -v
```

Expected shape:

```text
origin    git@github.com:TojotheTerror/<repo>.git (fetch)
origin    git@github.com:TojotheTerror/<repo>.git (push)
upstream  https://github.com/NousResearch/<repo>.git (fetch)
upstream  DISABLED (push)
```

## Optional local pre-push hook

Add this to `.git/hooks/pre-push` in each local checkout and mark it executable:

```bash
#!/usr/bin/env bash
set -euo pipefail

remote_name="${1:-}"
remote_url="${2:-}"

case "$remote_name $remote_url" in
  *NousResearch*|*upstream*)
    echo "Blocked: Hermes Android policy forbids pushing to upstream/reference remotes." >&2
    echo "Remote: ${remote_name} ${remote_url}" >&2
    exit 1
    ;;
esac

exit 0
```

Then run:

```bash
chmod +x .git/hooks/pre-push
```

## Codex and automation rule

Any Codex task, shell command, workflow, script, or tool call that would write to
an upstream repository must stop before execution and report the unsafe target.

Allowed upstream operations:

- `git fetch upstream`
- `git log upstream/<branch>`
- `git diff upstream/<branch>...HEAD`
- read-only GitHub file/issue/PR inspection

Disallowed upstream operations:

- `git push upstream ...`
- creating upstream branches or tags
- opening upstream PRs or issues
- updating upstream metadata
- running release or workflow actions against upstream
