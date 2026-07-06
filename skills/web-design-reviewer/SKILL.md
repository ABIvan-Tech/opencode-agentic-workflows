---
name: web-design-reviewer
description: Visual UI review workflow for finding and fixing layout, accessibility, and consistency issues.
user-invocable: false
---

# Web Design Reviewer

Use this skill when reviewing or fixing a running website's visual quality, responsiveness, and accessibility.

## Preconditions

1. The target URL is known and reachable.
2. Browser/screenshot automation is available.
3. Source code is available if fixes are expected.

## Review Priorities

1. **Broken layout or overlap**
2. **Accessibility blockers**
3. **Responsive breakage**
4. **Visual inconsistency**
5. **Polish issues**

## Workflow

### 1. Gather context

- Confirm the target URL.
- Identify framework, styling system, and likely source locations.
- Determine whether the task is review-only or includes code fixes.

### 2. Inspect visually

Check the key pages and flows for:

- overflow
- overlap
- broken spacing/alignment
- clipped text
- poor contrast
- missing focus states
- inaccessible controls
- inconsistent typography, spacing, or color treatment

### 3. Test key viewports

At minimum:

- mobile
- tablet
- desktop
- wide desktop when the layout suggests it matters

### 4. Trace issues to source

- Search by component names, class names, text, route files, and style files.
- Follow the repo's styling system rather than forcing a new one.
- Keep changes as local as possible.

### 5. Fix with minimal blast radius

- Preserve existing design language unless the task explicitly asks for redesign.
- Improve semantics, focus behavior, and contrast along with visual fixes when relevant.
- Avoid changing business logic unless the UI bug truly depends on a small UI-state change.

### 6. Re-verify

- Reload and recheck the affected view.
- Confirm the issue is fixed at the relevant breakpoints.
- Check that nearby areas did not regress.

## Source-Finding Heuristics

- layout issues -> page/layout containers, grid/flex wrappers, width/overflow rules
- typography issues -> design tokens, global styles, shared text primitives
- component breakage -> component file plus nearest style module/theme usage
- responsive issues -> breakpoint utilities, media queries, container sizing

## Review Heuristics

Look for:

- content outside viewport
- controls that are hard to tap/click
- missing labels or focus states
- visual hierarchy that hides the main action
- repeated one-off spacing or color fixes
- page-specific overrides fighting shared components

## Anti-Patterns

Avoid:

- redesigning when a local fix is enough
- fixing visuals by hardcoding brittle pixel offsets everywhere
- adding comments instead of addressing the actual style problem
- changing product logic for a purely presentational issue

## Output Expectations

Final output should clearly separate:

1. issues found
2. changes made
3. accessibility notes
4. remaining concerns, if any
