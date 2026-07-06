---
name: swift
description: Clean Architecture, concurrency, and patterns for pure Swift modules.
user-invocable: false
---

# Swift Architecture Standards

Use this skill for pure Swift modules where clean boundaries, concurrency, and testability matter.

## 1. Clean Architecture Rules (Domain Layer)

When writing Swift business logic (Domain/Core modules):

1. **UseCases (Interactors)**:
   - A UseCase MUST contain only one primary public function: `func execute() async -> Result<T, Error>`.
   - Do NOT use `callAsFunction` for this to maintain explicit naming.
   - UseCases MUST always return a standard Swift `Result<T, Error>`.
   - Any external `Helper` or `Manager` MUST be injected into the UseCase, not the Repository.

2. **Repositories and DataSources**:
   - **Repositories** return raw data types (e.g., `User`, `[Item]`) via `async throws`, NOT `Result<T, Error>`. The UseCase catches compilation errors and maps them to `Result`.
   - Repositories depend ONLY on DataSources. A Repository MUST NOT depend on another Repository.
   - **DataSources** depend only on external APIs/DBs/Network. A DataSource MUST NOT depend on another DataSource.
   - Use `protocol` for Repositories to allow easy mocking in unit tests.

3. **Dependency Graph**:
   - `UI/ViewModel` -> `UseCase` -> `Repository` -> `DataSource`

## 2. Swift Language Patterns

- **Concurrency**: Prefer modern Swift Concurrency (`async`/`await`, `Task`, `TaskGroup`) over GCD (`DispatchQueue`) or Combine publishers for one-shot operations.
- **Actors**: Use `actor` for shared mutable state to avoid data races.
- **Value Semantics**: Default to `struct` for models. Use `class` ONLY when reference semantics or Identity are strictly required.
- **Serialization**: Use `Codable`.
- **Error Handling Boundary**: Do NOT leak raw network or database `Error` types directly to the View. The `Result<T, Error>` from a UseCase must be mapped by the ViewModel/Reducer into specific, UI-friendly State enumerations or One-Time Events.
- **Swift Strict Concurrency**: Code should be safe under strict concurrency checking. Use `@Sendable` closures and explicitly mark isolated boundaries.
- **Closures**: Avoid strong reference cycles by explicitly using `[weak self]` in escaping closures. However, with `async`/`await`, prefer async functions over escaping closures to eliminate this risk entirely.
