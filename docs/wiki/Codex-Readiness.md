# Codex Readiness

Use `status:ready-for-codex` as the explicit GitHub readiness gate for automation.

## Start conditions

Automation may proceed only after a human confirms:

- the issue targets a writable `TojotheTerror/*` repository
- upstream `NousResearch/*` repositories remain read/reference only
- acceptance criteria are clear
- expected validation is named
- security and runtime review gates are identified
- reports and comments contain only redacted, publishable context

## Human gates

A human must approve work that affects:

- authentication
- CSRF behavior
- service-worker caching rules
- remote exposure defaults
- runtime/API boundaries
- Android signing or distribution assets
- workflow or automation behavior

## Issue shape

A ready issue should state:

- summary
- acceptance criteria
- repository target
- files or areas likely touched
- validation expected
- security/runtime notes

## Stop conditions

Automation must stop and report the reason when the requested action would:

- write to an upstream `NousResearch/*` repository
- change upstream repository metadata
- alter real local Hermes state without explicit approval
- publish private credentials or private machine details
- move the default Android track into local Android runtime work without explicit experimental approval

## PR evidence

A ready PR should include:

- summary
- validation performed
- screenshots for UI changes where practical
- upstream-safety statement
- security/runtime notes when relevant
- release-note wording when user-facing behavior changes
