---
name: kotlin
description: Clean Architecture, project structure, and patterns for pure Kotlin modules.
user-invocable: false
---

# Kotlin & KMP Architecture Standards

Use this skill for pure Kotlin or Kotlin Multiplatform modules where clean boundaries and testable async code matter.

## 1. Clean Architecture Rules (Domain Layer)

When writing Kotlin business logic (Core/Domain modules):

1. **UseCases (Interactors)**:
   - A UseCase MUST contain only one public function: `fun execute(): Result<T>`.
   - Do NOT use `operator fun invoke`.
   - UseCases MUST always return a Kotlin `Result<T>` (success or failure) to explicitly model outcomes.
   - UseCases can depend on other UseCases or Repositories.
   - Any external `Helper` or `Manager` MUST be injected into the UseCase, not the Repository.

2. **Repositories and DataSources**:
   - **Repositories** return raw data types (e.g., `User`, `List<Item>`), NOT `Result<T>`. The UseCase handles error mapping into `Result`.
   - Repositories depend ONLY on DataSources. A Repository MUST NOT depend on another Repository.
   - **DataSources** depend only on external APIs/DBs. A DataSource MUST NOT depend on another DataSource.
   - Prefer concrete classes for Repositories unless multi-platform swapping (expect/actual) or strict test mocking requires an `interface`.

3. **Dependency Graph**:
   - `UI/Component` -> `UseCase` -> `Repository` -> `DataSource`

## 2. Kotlin Language Patterns

- **Coroutines & Flow**:
  - Prefer `suspend` functions for one-shot async operations and `Flow` for streams of reactive data.
  - **Dispatcher Injection**: NEVER hardcode `Dispatchers.IO` or `Dispatchers.Default` inside UseCases or Repositories. Pass them via constructor injection so they can be easily replaced with `UnconfinedTestDispatcher` in unit tests.
  - **Structured Concurrency**: Prefer `coroutineScope` and `supervisorScope` over `GlobalScope`. Never launch unmanaged coroutines.
  - **Context-Preservation (Safe Suspend)**: A `suspend` function should be safe to call from any dispatcher (main-safe). If a function performs blocking I/O, it MUST shift its own execution context internally using `withContext(dispatcher)`.
  - **Coroutine Error Handling**:
    - **Never swallow `CancellationException`**. If catching a generic `Exception` inside a coroutine, explicitly check and rethrow `CancellationException` to avoid breaking structured concurrency and memory leaks.
    - Use `CoroutineExceptionHandler` exclusively for uncaught exceptions in root coroutines (`launch`). Note that it does NOT work for `async` (where exceptions are deferred until `await()`).
- **Scope Functions**: Avoid excessive or nested scope functions (`run`, `also`, `apply`, `let`). Only use them when they significantly improve readability.
- **Serialization**: Prefer `kotlinx.serialization` over Jackson/Gson for multiplatform readiness.
- **Networking (Ktor)**: Prefer Ktor Client for HTTP requests in KMP projects. Use `ContentNegotiation` with `kotlinx.serialization` for JSON parsing. Define separate request/response DTOs rather than exposing domain models directly to the network layer.
- **Error Handling Boundary**: Do NOT leak raw Exceptions to the UI. The `Result<T>` from a UseCase must be mapped by the ViewModel/Component into a precise, UI-friendly Error State or a One-Time UI Event.
- **Compiler & API**: Use the **K2 Compiler** defaults. Enable Explicit API mode in core modules (require explicit visibility and return types) to reduce LLM/IDE inferencing errors.

## 3. Project Structure

- Prefer a **Multi-Module Gradle (Kotlin DSL)** setup (`build.gradle.kts`).
- Use **Version Catalogs** (`gradle/libs.versions.toml`) for all dependencies and plugins.
- Separate `core` (pure Kotlin, no framework dependencies) from framework-specific modules (like `app`, `backend`, `android`, etc.).
