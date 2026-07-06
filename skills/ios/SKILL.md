---
name: ios
description: Architecture, SwiftUI, View architecture, and DI rules for iOS apps.
user-invocable: false
---

# iOS & SwiftUI Architecture Standards

Use this skill for iOS work built with SwiftUI, Swift Concurrency, and unidirectional state flow.

## 1. SwiftUI UI Rules

1. **Model-View-Intent (MVI) & UDF**:
   - **Model**: Expose single, immutable State properties from your ViewModel (or Reducer if using TCA).
   - **View**: A pure function rendering the Model. State flows down.
   - **Intent**: User actions are submitted to the ViewModel as explicit Intents/Events (e.g., via a `func send(_ event: Event)` pattern). Events flow up.
2. **Screen vs View Approach**:
   - `<Name>Screen` or `<Name>Coordinator`: Handles Environment injection, Navigation, and connects the `ViewModel` (or Reducer) to the UI.
   - `<Name>View`: A completely pure, stateless (or strictly internal view-state) SwiftUI `View` that accepts data via inputs and emits events via closures.
3. **Minimize Logic in Views**:
   - Do NOT put complex business validation or network requests in `.task` or `.onAppear` inside the `View` struct.
   - All business logic belongs in the injected `@Observable` ViewModel or TCA Reducer.
4. **Swift 6 Concurrency in UI**:
   - SwiftUI `View` structs must be implicitly or explicitly `@MainActor` isolated.
   - Never use unstructured `Task { }` without understanding the actor context; use `.task { }` modifiers tied to view lifecycle.
5. **Visibility & Previews**:
   - Keep helper Views `private` or `fileprivate` if they are only used within a single screen.
   - Provide `#Preview` blocks for every distinct state of the `View` (loading, error, success).
6. **Component Granularity**:
   - Minimize nesting. Extract deep view hierarchies into smaller computed properties returning `some View` or separate `View` structs.

## 2. State Management & Navigation

1. **Logic + State Separation**:
   - Public functions inside a ViewModel MUST represent user intents/events and generally return `Void`.
   - Any function computing values internally should be `private`.
   - State is exposed as published/observable properties.
2. **Observation**:
   - Use the `@Observable` macro exclusively. Do NOT use legacy `ObservableObject`, `@Published`, or `Combine` bindings for State management unless interacting with legacy code.

## 3. Dependency Injection

- Inject dependencies into ViewModels/UseCases via `init`.
- Use the SwiftUI `Environment` (`@Environment`) ONLY for UI-specific dependencies (like formatters, themes, or global view routers), NOT for Repositories or UseCases.
