---
name: android
description: Architecture, Jetpack Compose, Navigation3 KMP, and Koin DI rules for Android apps.
user-invocable: false
---

# Android & Compose Architecture Standards

Use this skill for Android work built with Kotlin, Compose, and related modern app architecture patterns.

## 1. Jetpack Compose UI Rules

1. **Model-View-Intent (MVI) & UDF**:
   - **Model**: Expose a single, immutable `ViewState` (Data Class) from the ViewModel. Do not expose multiple independent state flows unless strictly isolated.
   - **View**: A pure function rendering the Model. State flows down.
   - **Intent**: User actions are routed to the ViewModel as explicit Intents/Events. Events flow up.
2. **Screen vs View Approach**:
   - `<Name>Screen`: Handles DI, Navigation3 KMP routing, and connects the `ViewModel` to the UI.
   - `<Name>View(state, onEvent)`: A completely pure, stateless Composable.
3. **Minimize Logic in Compose**:
   - Do NOT use `remember` for business logic. Business logic belongs in the ViewModel.
4. **Performance**:
   - Assume **Strong Skipping Mode** is enabled. Do not manually wrap lambdas in `remember`.
   - Pass modifier chains explicitly: `modifier: Modifier = Modifier`.
5. **Visibility**:
   - `@Preview` Composables MUST be `private` or restricted visibility.
   - Do NOT make Composable functions `public` unless intended as an external design system component.

## 2. Navigation3 KMP (Routing & State)

If using Navigation3 KMP for architecture:

1. **ViewModel = Logic + State**: The ViewModel handles all business logic, manages the CoroutineScope, and exposes state to the UI.
2. **ViewModel Interface**:
   - Public functions inside a ViewModel MUST represent user intents/events and generally return `Unit`.
   - Any function computing values internally should be `private`.
   - State should be exposed as an immutable `StateFlow`.
3. **Routing (Navigation3 KMP)**:
   - Treat navigation strictly as **state management** (part of the ViewModel or Component).
   - Keep navigation execution strictly inside the `<Name>Screen` wrapper, NOT inside the pure `<Name>View`.
   - Use strongly typed destinations (Objects or Data Classes).
   - **Crucial**: Apply polymorphic `@Serializable` annotations to your destination keys so they serialize correctly across non-JVM platforms (iOS/Web).

## 3. Dependency Injection (Koin)

If using Koin:

- Prefer `single` and `factory` instead of `bind` with generic provider/singleton blocks for clearer syntax and safety.

## 4. Project Structure & Layering

Prefer a clear 3-layer layout and keep boundaries strict:

- `data/`: implementations (local DB, remote APIs, repository impls)
- `domain/`: pure business logic (models, repository interfaces, use cases)
- `ui/`: Compose screens, reusable components, theme
- `di/`: DI wiring only (no business logic)

Rule: UI depends on domain, domain depends on nothing, data depends on domain (interfaces).

## 5. Coroutines, Flow, and State

1. **UI state**:
   - Use `MutableStateFlow` internally and expose `StateFlow` via `asStateFlow()`.
   - Update state via `update { it.copy(...) }` to keep changes atomic.

Example (micro):

```kotlin
private val _state = MutableStateFlow(ViewState())
val state: StateFlow<ViewState> = _state.asStateFlow()
_state.update { it.copy(isLoading = true) }
```
2. **Long-running streams**:
   - Use `flowOn(Dispatchers.IO)` for data layer work.
   - Prefer injecting a `CoroutineDispatcher` for testability.
3. **Error handling**:
   - Catch at the right boundary (usually data/usecase) and surface a user-safe error state.

## 6. Result Modeling (Optional)

For operations that can be loading/success/error, prefer a sealed result type over nullable juggling.

Rule: keep it small (`Loading`, `Success(data)`, `Error(exception)`), and map/transform explicitly.

## 7. Testing (Unit-first)

Recommended stack (when it fits the repo):

- `kotlinx-coroutines-test` for deterministic coroutine tests
- `MockK` for mocking
- `Turbine` for testing `Flow`/`StateFlow` emissions

Rules:

1. Tests must be deterministic (no real network, no timing races).
2. Prefer injecting dispatchers and using test dispatchers.
3. For flows: assert emission order and terminal states, not implementation details.

Example (micro):

```kotlin
@Test fun emitsLoadingThenData() = runTest {
  // collect state/flow and assert emissions (use Turbine if available)
}
```

## 8. Lint + CI (Keep It Boring)

1. Run static checks in CI:
   - detekt (complexity/style)
   - ktlint (formatting)
   - unit tests
2. Keep thresholds explicit (e.g., long method/parameter limits) and fail CI on violations.
3. If the repo uses GitHub Actions, keep Android CI minimal:
   - checkout
   - JDK setup
   - Gradle cache
   - detekt/ktlint
   - unit tests
   - assemble (optional)
