---
name: self-improvement-governance
description: Governance rules for bounded self-improvement candidates, promotion gates, and rollback policy.
license: "See repository LICENSE"
user-invocable: false
---

# Self-Improvement Governance

Use this skill for any workflow that proposes, evaluates, or promotes bounded self-improvement candidates.

## Objectives

- Improve the scaffold without changing model weights.
- Keep the improvement loop reversible and independent.
- Prevent self-modification of permissions, routing, control-plane prompts, or verification policy.

## Allowed Targets

Only the dedicated low-risk overlay namespace is auto-mutable:

- `skills/self-improvement-overlays/**`

All other paths are protected by default.

## Prohibited Changes

Do not auto-promote changes that:

- modify `opencode.json`
- modify core `.opencode/agents/*.md` except through explicit human approval
- change permissions, task allowlists, or routing policy
- alter security, review, or memory governance behavior
- change model/provider/tool/plugin selection
- write raw task traces or secrets into durable memory

## Candidate Lifecycle

1. Observe a sanitized signal.
2. Analyst proposes a candidate.
3. Validator checks schema, target path, and policy constraints.
4. Orchestrator creates an isolated worktree.
5. Coder implements the candidate there.
6. Evaluator compares candidate versus baseline.
7. Review and verifier gates run.
8. Promotion or rollback occurs based on the release policy.

## Promotion Policy

Auto-promotion requires:

- allowlisted target path
- low risk tier
- clean schema validation
- no safety/governance findings
- no held-out regression
- budget compliance
- independent review and verifier pass

Otherwise, the candidate must remain `NEEDS_HUMAN` or `REJECT`.

## Rollback Policy

Rollback to the last accepted baseline when:

- a safety finding is raised
- the candidate regresses a held-out scenario
- the budget is exceeded
- the validator or evaluator fails unexpectedly

The rollback must restore the prior baseline and quarantine the rejected candidate.
