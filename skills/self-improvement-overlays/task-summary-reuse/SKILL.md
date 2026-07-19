---
name: task-summary-reuse
description: Low-risk overlay that improves reusable task summaries and handoff clarity without changing routing or permissions.
license: "See repository LICENSE"
user-invocable: false
---

# Task Summary Reuse Overlay

This overlay is the first auto-mutable low-risk improvement surface.

## Intent

Use this overlay to improve task summaries and handoff quality when the repository already has a clear execution plan. It must not alter control-plane routing, permissions, or review gates.

## Allowed Scope

- adjust summary phrasing inside the allowlisted low-risk overlay namespace
- add non-governance reusable checklist content
- keep changes additive and narrowly scoped

## Prohibited Scope

- change orchestrator, planner, verifier, or reviewer prompts
- change permissions or task allowlists
- alter memory or security governance policy
- expand the change beyond the overlay namespace
