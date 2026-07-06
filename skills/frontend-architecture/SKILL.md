---
name: frontend-architecture
description: Practical frontend architecture rules for scalable UI, performance, and maintainability.
license: "See repository LICENSE"
user-invocable: false
---

# Frontend Architecture & Performance

Use this skill for UI architecture, component boundaries, state placement, and frontend performance work.

## Priorities

1. **Clear ownership**
2. **Predictable state flow**
3. **Usable performance**
4. **Composition over duplication**
5. **Maintainable delivery**

## Core Rules

### 1. Split by responsibility, not by hype

- Components should have clear ownership.
- Keep screen/container concerns separate from presentational concerns when that improves clarity.
- Do not create a new architectural layer unless it reduces real complexity.

### 2. Keep state as local as possible

- Start with local component state.
- Lift state only when multiple consumers truly need it.
- Global state should be reserved for cross-cutting or shared application concerns, not convenience.

### 3. Make data flow obvious

- Prefer one clear direction of data flow.
- Keep fetching, normalization, and rendering responsibilities understandable.
- Avoid passing unstable props or context values through large trees without reason.

### 4. Reuse patterns intentionally

- Reuse component, layout, and styling conventions already present in the repo.
- Prefer composition over giant configurable mega-components.
- Extract shared primitives only after repetition becomes real.

### 5. Design for loading, error, and empty states

- Every meaningful async screen should define:
  - loading state
  - error state
  - empty state
  - success state
- Do not optimize only the happy path.

## Performance Rules

### 6. Optimize the right thing

- Prioritize user-visible slowness: route transitions, large lists, blocking renders, image weight, bundle size, and repeated network work.
- Measure with the platform tools available in the repo before adding memoization or architectural complexity.

### 7. Keep renders cheap

- Avoid unnecessary derived work in render paths.
- Memoization is a tool, not a default.
- Stabilize props and callbacks only when it measurably helps or prevents correctness issues.

### 8. Be deliberate about bundles

- Lazy-load heavy routes or features when it helps real startup cost.
- Keep dependency additions conservative.
- Avoid shipping large helpers for tiny benefits.

## Styling and Structure Rules

- Respect the repo's styling system.
- Keep layout primitives and page-specific styling separate when possible.
- Avoid one-off CSS or utility explosions that are hard to reason about later.
- Accessibility is architecture too: semantics, focus flow, labels, and contrast should be built in, not patched in at the end.

## Review Heuristics

Look for:

- oversized components with mixed responsibilities
- state lifted too high
- duplicated fetching/normalization logic
- missing loading/error/empty states
- performance work added without measurement
- giant shared components that became bottlenecks
- unnecessary global state or context churn

## Anti-Patterns

Avoid:

- mega-components that own unrelated concerns
- storing server state and transient UI state in the same generic bucket without boundaries
- premature abstraction of every repeated markup fragment
- memoization everywhere "just in case"
- component APIs with too many mode flags

## Quick Checklist

- [ ] Component ownership is clear
- [ ] State lives at the lowest reasonable level
- [ ] Async states are all accounted for
- [ ] Shared abstractions are justified by real reuse
- [ ] Performance issues are measured, not guessed
- [ ] Accessibility and semantics are part of the structure
