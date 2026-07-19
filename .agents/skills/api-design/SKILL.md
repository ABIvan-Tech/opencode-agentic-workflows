---
name: api-design
description: Practical rules for designing, evolving, and integrating APIs safely.
license: "See repository LICENSE"
user-invocable: false
---

# API Design & Integration

Use this skill for REST, GraphQL, and third-party integrations when you need stable contracts and operable behavior.

## Priorities

1. **Clear contract**
2. **Backward compatibility**
3. **Validation and safety**
4. **Observability**
5. **Performance**

## Contract Rules

### 1. Design the contract before the handler

- Start from the consumer-facing shape: paths, fields, mutations, errors, pagination, auth, and compatibility rules.
- If the repo uses OpenAPI, schema files, generated clients, or GraphQL SDL, update the contract source first.
- Keep the contract smaller than the implementation would naturally drift toward.

### 2. Use resource-oriented shapes

For REST:

- prefer nouns over verbs
- use standard methods where semantics are clear
- keep nested resources shallow

For GraphQL:

- expose explicit object types and input types
- avoid catch-all fields that return overly generic blobs
- keep mutations specific and auditable

### 3. Preserve compatibility by default

- Additive changes are safer than breaking ones.
- Renaming, removing, or changing semantics requires an explicit migration plan.
- If a response field is optional, define when and why it may be absent.
- Do not overload one field with multiple meanings across versions or callers.

## Request / Response Rules

### 4. Validate all external input

Validate:

- path params
- query params
- headers
- request bodies
- webhook payloads
- third-party responses before mapping them into domain models

Return validation failures in a stable, structured way.

### 5. Use a consistent error envelope

Errors should be:

- machine-readable
- safe to expose
- stable enough for clients to act on

Prefer a structure that includes:

- code
- user-safe message
- optional field/details metadata
- request or trace ID when available

Do not leak internal stack traces or provider-specific raw failures to clients.

### 6. Make success and async semantics explicit

- Use `200/201/204` deliberately for REST.
- Use idempotency for retry-prone create/side-effect operations when needed.
- For async work, make polling, callback, or event-driven completion explicit.
- Do not hide eventual consistency behind a synchronous-looking contract.

## Collection Rules

### 7. Be explicit about pagination, filtering, and sorting

- Large collections should paginate by default.
- Prefer cursor pagination for unstable or large datasets.
- Keep filtering and sorting syntax consistent across related endpoints.
- Document default sort order and limits.

## Auth / Safety Rules

### 8. Treat auth and authorization as part of the contract

- Define who can call the endpoint and under which conditions.
- Check authorization close to the business action, not only at the routing layer.
- Keep scopes/roles coarse enough to reason about, but not so coarse they become unsafe.

### 9. Protect the API operationally

- apply sensible timeouts
- rate-limit abuse-prone endpoints
- make retries safe before adding them
- log provider failures with enough context to debug
- add trace/request IDs where the stack supports them

## Third-Party Integration Rules

### 10. Isolate external providers

- Wrap providers behind a local adapter or service boundary.
- Normalize provider-specific payloads before they reach the rest of the app.
- Define timeout, retry, and error-mapping policy explicitly.
- Circuit breakers and retry loops are useful only when the side effects are understood.

## GraphQL-Specific Rules

- Avoid N+1 query patterns in resolvers.
- Separate read models from write inputs.
- Use explicit pagination types for list fields.
- Keep resolver logic thin; business rules belong in services/domain logic.

## Review Heuristics

Look for:

- breaking contract changes without migration plan
- inconsistent error shapes
- missing validation at boundaries
- missing pagination on potentially large collections
- auth checks that are too early, too late, or missing
- unsafe retries on non-idempotent operations
- provider-specific details leaking into domain contracts

## Anti-Patterns

Avoid:

- action-style REST paths when resources would be clearer
- one endpoint doing multiple unrelated operations
- stringly typed error handling
- undocumented optional behavior
- passing third-party payloads straight through to clients without normalization
- hiding expensive joins or fan-out calls behind innocent-looking fields

## Quick Checklist

- [ ] Contract shape is explicit and reviewable
- [ ] Compatibility impact is understood
- [ ] Inputs are validated at the boundary
- [ ] Error responses are structured and safe
- [ ] Pagination/filtering/sorting rules are defined where needed
- [ ] Auth and authorization are explicit
- [ ] Integration timeouts/retries/error mapping are defined
- [ ] Observability is good enough to debug production issues
