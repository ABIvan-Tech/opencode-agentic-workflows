---
name: data-transformation-etl
description: Practical ETL rules for parsing, validation, transformation, and safe loading.
license: "See repository LICENSE"
user-invocable: false
---

# Data Transformation & ETL

Use this skill for data ingestion, cleanup, normalization, migration, and loading workflows.

## Priorities

1. **Correctness of data**
2. **Repeatability**
3. **Observability**
4. **Recovery from partial failure**
5. **Performance at scale**

## Core Rules

### 1. Validate at every boundary

- Validate file shape, schema, headers, and required fields before heavy processing.
- Parse untrusted input defensively.
- Distinguish malformed rows from recoverable business-rule failures.

### 2. Normalize before business logic

- Convert transport formats into stable internal records first.
- Normalize casing, whitespace, null conventions, timestamps, units, and IDs before downstream logic.
- Keep raw input and normalized output conceptually separate.

### 3. Make pipelines idempotent

- Re-running the same batch should not duplicate or corrupt data.
- Prefer deterministic keys, upserts, checkpoints, or watermarks.
- Avoid pipelines that are safe only if they run exactly once.

### 4. Handle partial failure deliberately

- Decide whether the unit of failure is row, file, batch, or whole run.
- Log and count rejected records explicitly.
- If partial success is allowed, make the boundary visible in metrics and outputs.

### 5. Keep transforms readable

- Prefer a sequence of named transformation steps over one giant pipeline.
- Separate parsing, validation, enrichment, deduplication, and loading.
- Avoid clever one-liners that make data loss hard to detect.

### 6. Preserve provenance

- Keep enough metadata to trace where a record came from.
- Include source file, batch ID, import timestamp, or checkpoint when the system needs auditability.
- Never destroy raw provenance before the load is verified.

### 7. Design for scale without hiding semantics

- Stream or chunk large inputs when full in-memory processing is risky.
- Parallelize only when ordering, deduplication, and side effects remain correct.
- Optimize the hot path after correctness and restart safety are established.

## Parsing Rules

- Fail fast on missing required structure.
- Be explicit about encoding, delimiter, locale, and timestamp assumptions.
- Treat schema drift as a first-class risk.
- Prefer typed records or schema validation where the stack supports it.

## Transformation Rules

- Make field derivations explicit.
- Keep unit conversions centralized.
- Deduplicate using business keys, not incidental row order.
- Flag suspicious records instead of silently coercing them into validity.

## Loading Rules

- Define transaction boundaries intentionally.
- Use staging tables or temporary sinks when the load must be validated before publish.
- Prefer bulk operations when they preserve correctness and failure visibility.
- Avoid per-row write loops for large imports unless the scale is genuinely small.

## Incremental Sync Rules

- Use durable checkpoints or watermarks.
- Handle late-arriving and out-of-order data intentionally.
- Decide what happens when a source mutates historical data.
- Document replay strategy.

## Observability

Every meaningful ETL job should expose:

- records read
- records written
- records rejected
- batches retried
- time spent per stage
- checkpoint / watermark used

Log enough context to debug a bad batch without dumping sensitive data.

## Review Heuristics

Look for:

- hidden schema assumptions
- non-idempotent inserts
- silent row drops
- transforms that mix parsing with business logic
- missing checkpoints or replay strategy
- poor failure visibility
- memory-heavy processing where streaming/chunking is safer

## Anti-Patterns

Avoid:

- loading raw external data straight into domain tables
- silently coercing bad records into "valid" values
- pipelines that cannot be rerun safely
- giant monolithic transform functions
- success reports that ignore rejected rows
- batch jobs with no checkpoint or audit trail

## Quick Checklist

- [ ] Input schema is validated
- [ ] Raw and normalized records are separated
- [ ] Pipeline is idempotent
- [ ] Failure boundary is explicit
- [ ] Checkpoints/watermarks are defined where needed
- [ ] Metrics and rejection counts are visible
- [ ] Loading strategy is safe for reruns and partial failures
