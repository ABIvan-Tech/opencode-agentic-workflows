# Shared agent assets

This directory is the canonical home for reusable agent-facing assets that should be shared across LLM tooling.

## Structure

- `.agents/skills/` — canonical reusable skill catalog and skill definitions for OpenCode and compatible agents
- `.agents/skills/README.md` — human-readable catalog for selecting the narrowest relevant skill

## Compatibility

OpenCode discovers skills from `.opencode/skills`, which is a compatibility symlink to this directory. The canonical location for shared agent assets remains `.agents/`.

If you add or rename skills, keep the layout consistent so both paths remain valid.
