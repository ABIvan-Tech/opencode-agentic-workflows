---
name: typescript-patterns
description: Practical TypeScript rules for safe application code, APIs, and UI state.
license: "See repository LICENSE"
user-invocable: false
---

# TypeScript Patterns

Use this skill when changing TypeScript code and you need strong, practical defaults instead of a catalog of language features.

## Goals

1. Make invalid states hard to represent
2. Keep inference helpful, not magical
3. Validate runtime boundaries
4. Avoid type gymnastics that reduce readability

## Core Rules

### 1. Prefer inference until the contract matters

- Let TypeScript infer obvious locals.
- Add explicit types for public APIs, exported functions, complex return types, and shared constants.
- If inference produces a weak or widened type, annotate deliberately.

### 2. Avoid `any`

- Prefer `unknown` at boundaries, then narrow it.
- If you must use `any`, keep it local, document the reason, and do not let it leak into shared types.

### 3. Model state with discriminated unions

Use tagged unions for async state, UI state, workflow state, and domain outcomes.

Prefer:

- `{ status: 'idle' | 'loading' | 'success' | 'error' }`
- tagged result objects with distinct shapes

Avoid:

- multiple loosely related booleans
- objects where every property is optional

### 4. Separate transport types from domain types

- DTOs from APIs, forms, and storage should not automatically become domain models.
- Convert at the boundary.
- Keep mapping logic explicit when names, nullability, or semantics differ.

### 5. Validate runtime input

- TypeScript checks compile-time assumptions, not runtime truth.
- Parse and validate untrusted data from:
  - HTTP responses
  - request bodies
  - environment variables
  - local storage
  - message queues
- Prefer schema validation if the repo already uses it.

### 6. Use narrow utility types, not type puzzles

- `Pick`, `Omit`, `Partial`, `Readonly`, and simple mapped types are fine.
- Avoid deeply nested conditional types unless they clearly pay for themselves.
- If a type takes longer to understand than the runtime code it protects, simplify it.

### 7. Prefer string unions over enums by default

- Use string literal unions for most application state and protocol tags.
- Use enums only when the repo already standardizes on them or interop requires them.

### 8. Use assertions sparingly

- Avoid `as` unless you know something the compiler cannot.
- Never use assertions to suppress a real typing problem.
- Prefer narrowing, parsing, helper guards, or better function signatures.

## Error and Result Modeling

- Prefer explicit result shapes or domain-specific errors at service boundaries.
- Do not throw raw strings.
- If using exceptions, throw `Error` subclasses or a well-known error type.
- If using result objects, keep success and failure shapes distinct and easy to narrow.

## React / UI Rules

Apply when the repo includes React or similar TSX-based UI:

- Prefer plain function components over `React.FC` unless the repo already standardizes on `React.FC`.
- Keep prop types local to the component unless shared elsewhere.
- Use discriminated unions or small state machines for UI state.
- Type event handlers explicitly when inference is weak.
- Avoid enormous prop types built from many intersected utility types.

## Node / Service Rules

Apply when the repo includes backend TypeScript:

- Type request/response boundaries explicitly.
- Parse config and env vars into a typed config object near startup.
- Keep shared error and result contracts small and stable.
- Do not let framework types bleed everywhere; wrap or narrow when needed.

## tsconfig Expectations

Prefer these when you control the config or when reviewing a TS repo:

- `strict: true`
- `noImplicitOverride: true`
- `noUncheckedIndexedAccess: true` when the repo can sustain it
- `exactOptionalPropertyTypes: true` when the team is ready for the stricter contract

Do not expand the compiler surface casually in a small task; align with the repo.

## Review Heuristics

Look for:

- `any` creeping into shared code
- unsafe assertions
- DTOs passed deep into domain/UI without normalization
- optional fields used as hidden state machines
- impossible branches that should be encoded in types
- missing runtime validation at external boundaries
- utility types that obscure the real contract

## Anti-Patterns

Avoid:

- exporting giant global types barrels without need
- reusing one interface for API input, API output, DB row, and UI state
- boolean soup for async/UI state
- assertion chains like `foo as Bar as Baz`
- type-level cleverness that future maintainers will fear touching

## Quick Checklist

- [ ] Public contracts are explicit
- [ ] Runtime boundaries are validated
- [ ] `any` is absent or tightly contained
- [ ] State is modeled with clear tagged shapes
- [ ] Transport and domain types are not casually mixed
- [ ] Assertions are justified
- [ ] Types improve readability instead of reducing it
