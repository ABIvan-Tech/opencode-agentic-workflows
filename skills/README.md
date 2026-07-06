# Skills Catalog

This file is a navigation index for humans and agents.

Use it to quickly identify the narrowest relevant skill for a task before loading the full `SKILL.md`.
The source of truth remains each skill's own `SKILL.md` file and its `description` frontmatter.

## How to use this index

1. Start here when the task domain is clear but the best skill is not.
2. Prefer the narrowest matching skill over a broad fallback.
3. Combine multiple skills when the task spans domains.
4. For implementation and review, pair domain skills with baseline quality and verification skills when relevant.
5. For imported upstream skills, use the local copy in this repository; treat upstream links as provenance only.

## Quick routing hints

- **General Kotlin/KMP architecture** → `kotlin`
- **Kotlin + Spring Data JPA / Hibernate entities** → `kotlin-backend-jpa-entity-mapping`
- **KMP / AGP 9+ migration** → `kotlin-tooling-agp9-migration`
- **Android app architecture / Compose / Koin** → `android`
- **iOS / SwiftUI architecture** → `ios`
- **Pure Swift module design** → `swift`
- **TypeScript application patterns** → `typescript-patterns`
- **Frontend implementation / visual design** → `frontend-design`
- **Frontend architecture / scalability** → `frontend-architecture`
- **Visual UI review / layout / accessibility** → `web-design-reviewer`
- **API design and evolution** → `api-design`
- **Database tuning / schema / query performance** → `database-optimization`
- **ETL / parsing / transformation / loading** → `data-transformation-etl`
- **Planning / decomposition / readiness gates** → `planning-structure`
- **Read-only discovery / routing prep** → `research-discovery`
- **General code quality** → `code-quality`
- **Testing / verification** → `testing-qa`
- **Security review baseline** → `security-best-practices`
- **Shared review contract** → `review-core`
- **Independent review routing / review gates** → `review-orchestration`
- **Multi-model review orchestration** → `multi-model-review`
- **Parallel isolated work using git worktrees** → `git-worktree`
- **Memory boundaries and durable repo memory** → `memory-management`

## Workflow and orchestration skills

| Skill | Use for | Common triggers |
| --- | --- | --- |
| `planning-structure` | Planning tracks, epics, readiness gates, plan delta handling | planning, decomposition, readiness, feature slices, epics |
| `research-discovery` | Fast broad-to-narrow read-only discovery before planning or routing | discover, scout, map codebase, entry points, reuse search |
| `memory-management` | Durable vs session memory rules and memory sync workflow | memory update, durable knowledge, `.agent-memory`, session notes |
| `git-worktree` | Isolated parallel work for risky refactors or overlapping file ownership | worktree, parallel branch, isolation, risky refactor |
| `review-orchestration` | Review routing, independent review gates, and optimization follow-up | review gate, post-implementation review, multi-review, cleanup pass |

## Review and quality skills

| Skill | Use for | Common triggers |
| --- | --- | --- |
| `code-quality` | Cross-stack implementation and review heuristics | refactor, implementation quality, maintainability |
| `testing-qa` | Unit, integration, and end-to-end verification strategy | tests, verification, QA, regressions |
| `security-best-practices` | Secure coding, auth, validation, and defense-in-depth | security, auth, input validation, secrets, hardening |
| `review-core` | Shared contract for independent reviewers and durable findings | audit, review contract, findings normalization |
| `review-orchestration` | When to review, when to skip, and how to route review follow-up | independent review, review gate, reviewer routing |
| `multi-model-review` | Consensus-based multi-review and false-positive triage | multi-review, reviewer consolidation, conflicts |

## Frontend and platform skills

| Skill | Use for | Common triggers |
| --- | --- | --- |
| `frontend-design` | Production-grade web UI implementation and styling | build UI, landing page, dashboard, component styling |
| `frontend-architecture` | Frontend structure, maintainability, and performance | frontend architecture, state, scalability, structure |
| `web-design-reviewer` | Visual UI review for layout, accessibility, and consistency | UI review, visual bugs, accessibility, spacing |
| `android` | Android app architecture, Jetpack Compose, Navigation3 KMP, and Koin DI | Android, Compose, Koin, Navigation |
| `ios` | iOS architecture, SwiftUI view structure, and DI rules | iOS, SwiftUI, view architecture |
| `swift` | Pure Swift module architecture and concurrency patterns | Swift, concurrency, clean architecture |

## Language, backend, and domain skills

| Skill | Use for | Common triggers |
| --- | --- | --- |
| `typescript-patterns` | Safe TypeScript app code, APIs, and UI state | TypeScript, types, frontend state, API client |
| `api-design` | Designing and evolving APIs safely | API design, contracts, versioning, integration |
| `database-optimization` | Query tuning, schema choices, and DB performance work | slow query, indexes, schema, DB performance |
| `data-transformation-etl` | Parsing, validation, transformation, and loading pipelines | ETL, import pipeline, transform, normalize |
| `kotlin` | General Kotlin and KMP architecture, coroutines, repositories, and module structure | Kotlin, KMP, coroutines, use cases, repositories |
| `kotlin-backend-jpa-entity-mapping` | Kotlin persistence modeling for Spring Data JPA and Hibernate | JPA entity, Hibernate, equals/hashCode, N+1, lazy loading |
| `kotlin-tooling-agp9-migration` | Migrating KMP/Android projects to AGP 9+ and built-in Kotlin | AGP 9, KMP migration, built-in Kotlin, plugin swap |

## Imported upstream skills

The following local skills were imported from the official Kotlin skills repository and should be used from their local paths in this repo:

- `kotlin-backend-jpa-entity-mapping` → source: [Kotlin/kotlin-agent-skills](https://github.com/Kotlin/kotlin-agent-skills/tree/main/skills/kotlin-backend-jpa-entity-mapping)
- `kotlin-tooling-agp9-migration` → source: [Kotlin/kotlin-agent-skills](https://github.com/Kotlin/kotlin-agent-skills/tree/main/skills/kotlin-tooling-agp9-migration)

## Selection rules for agents

1. Prefer a specific domain skill over a broad language skill.
   - Example: use `kotlin-backend-jpa-entity-mapping` instead of generic `kotlin` for Hibernate entity modeling.
   - Example: use `kotlin-tooling-agp9-migration` instead of generic `kotlin` for AGP 9 migration.
2. Combine domain + quality skills when reviewing or implementing non-trivial work.
   - Example: `kotlin` + `testing-qa` + `code-quality`
   - Example: `frontend-design` + `web-design-reviewer` + `testing-qa`
3. Use orchestration skills to support execution, not to replace domain skills.
   - Example: `planning-structure` helps make the plan, but it does not replace `api-design` or `kotlin`.
4. If multiple skills seem plausible, start with the narrowest one and add a broad fallback only if needed.
