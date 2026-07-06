---
name: database-optimization
description: Practical rules for query tuning, schema choices, and safe database performance work.
license: "See repository LICENSE"
user-invocable: false
---

# Database Optimization

Use this skill when improving query performance, schema layout, indexing, or database-heavy code paths.

## Priorities

1. **Correctness**
2. **Measured bottlenecks**
3. **Query and index simplicity**
4. **Write/read tradeoff awareness**
5. **Operational safety**

## Core Rules

### 1. Measure before tuning

- Start with the real slow query, workload, or access pattern.
- Use the database's plan/explain tooling before changing indexes or schema.
- Do not optimize based on intuition alone.

### 2. Fix query shape before adding indexes

- Remove unnecessary joins, scans, sorting, or selected columns first.
- Prefer predicates and access paths the optimizer can use well.
- Avoid `SELECT *` in hot paths unless the query genuinely needs the full row.

### 3. Index for actual access patterns

- Add indexes for repeated filters, joins, sorting, or uniqueness constraints.
- Composite index order should match the real query pattern.
- Every index has write and storage cost; do not index everything.

### 4. Keep schema changes conservative

- Prefer narrow schema or index changes tied to a measured problem.
- Avoid denormalization unless read-path gains justify the extra write and consistency cost.
- If changing cardinality or ownership boundaries, think through migrations and rollback first.

### 5. Optimize application behavior too

- Eliminate N+1 access patterns.
- Batch reads or writes where semantics allow it.
- Cache only after correctness and invalidation strategy are understood.

## Query Heuristics

Look for:

- full scans on large tables
- repeated per-row subqueries
- sorts that could be supported by an index
- predicates that prevent index use
- unnecessary wide row fetches
- queries that join far more than the caller needs

## Index Heuristics

Add or adjust indexes when:

- a query is hot and selective enough to benefit
- a join key is repeatedly used
- a uniqueness rule should be enforced at the database layer
- a filtered/partial index can shrink work meaningfully

Avoid indexes when:

- the table is tiny
- the predicate is rarely used
- the column has poor selectivity and the workload is write-heavy

## Schema and Data Rules

- Keep data types aligned with actual semantics.
- Store derived data only when the recomputation or query cost is proven to matter.
- Use constraints to protect invariants whenever the database can enforce them.
- Partition only when scale, retention, or operational boundaries justify the complexity.

## Transaction Rules

- Keep transactions as short as practical.
- Be explicit about isolation expectations in correctness-sensitive flows.
- Avoid holding locks while doing non-database work.
- Tune retry logic for contention and deadlocks deliberately, not blindly.

## Review Heuristics

Look for:

- missing indexes on repeated hot paths
- over-indexed write-heavy tables
- app-level N+1 patterns
- expensive ORM defaults
- schema changes with unclear migration risk
- caching without invalidation clarity
- optimization work without measurements

## Anti-Patterns

Avoid:

- adding indexes before inspecting the actual query plan
- denormalizing just to avoid learning the real bottleneck
- premature partitioning
- relying on ORM convenience while ignoring generated SQL
- "fixing" slow queries by adding hardware assumptions to the code path

## Quick Checklist

- [ ] Slow path is measured, not guessed
- [ ] Query shape is reviewed before index changes
- [ ] Index cost vs benefit is understood
- [ ] N+1 and batching concerns are checked
- [ ] Constraints protect important invariants
- [ ] Transaction boundaries are deliberate
- [ ] Migration and rollback risk is understood
