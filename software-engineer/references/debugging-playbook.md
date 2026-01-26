# Debugging Playbook

## Table of Contents
1. [Debugging Framework](#debugging-framework)
2. [Common Issue Patterns](#common-issue-patterns)
3. [Tool-Specific Debugging](#tool-specific-debugging)
4. [Production Debugging](#production-debugging)
5. [Post-Incident Process](#post-incident-process)

---

## Debugging Framework

### The Scientific Method for Debugging

```
1. OBSERVE
   - What is the exact symptom?
   - When did it start?
   - Who is affected?
   - What changed recently?

2. HYPOTHESIZE
   - Form a theory about the cause
   - Be specific: "The cache is returning stale data because TTL is not being set"
   - Not vague: "Something is wrong with the cache"

3. EXPERIMENT
   - Design a test for your hypothesis
   - Make ONE change at a time
   - Control other variables

4. ANALYZE
   - Did the experiment confirm or refute your hypothesis?
   - What new information did you learn?
   - Update your mental model

5. REPEAT
   - Form new hypothesis based on findings
   - Continue until root cause is found
```

### Binary Search Debugging

```
When facing a large codebase or complex system:

1. Identify the full scope of where the bug could exist
2. Find the midpoint and test
3. Determine which half contains the bug
4. Repeat until isolated

EXAMPLES:

Git Bisect:
$ git bisect start
$ git bisect bad HEAD           # Current commit is broken
$ git bisect good v1.0.0        # This version worked
# Git checks out middle commit
$ npm test                      # Test if bug exists
$ git bisect good               # or git bisect bad
# Repeat until found

Code Isolation:
- Comment out half the suspicious code
- Does bug still occur?
  - Yes: Bug is in remaining code
  - No: Bug is in commented code
- Repeat on the half that contains bug
```

### Logging Strategy

```
STRUCTURED LOGGING FORMAT:
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "ERROR",
  "service": "order-service",
  "requestId": "req-abc-123",
  "userId": "user-456",
  "action": "processPayment",
  "error": {
    "type": "PaymentGatewayError",
    "message": "Card declined",
    "code": "CARD_DECLINED"
  },
  "context": {
    "orderId": "order-789",
    "amount": 99.99,
    "currency": "USD"
  }
}

LOG LEVELS:
- ERROR: Something failed, requires attention
- WARN: Something unexpected, but handled
- INFO: Significant business events
- DEBUG: Detailed flow for debugging (disable in prod)
- TRACE: Very detailed, performance impact

WHERE TO LOG:
- Entry/exit of important functions
- Before/after external calls
- Decision points (if/else branches)
- Errors and exceptions
- State changes
```

---

## Common Issue Patterns

### Memory Leaks

```
SYMPTOMS:
- Increasing memory usage over time
- OutOfMemoryError eventually
- Slow performance as memory fills

COMMON CAUSES:
- Event listeners not removed
- Global caches without eviction
- Closures holding references
- Circular references (in some languages)

DEBUGGING:
1. Take heap snapshots at intervals
2. Compare snapshots to find growing objects
3. Trace references to find what's holding them

JAVASCRIPT EXAMPLE:
// BAD: Event listener never removed
element.addEventListener('click', handler);
// When element is removed, handler still references it

// GOOD: Clean up on unmount
const controller = new AbortController();
element.addEventListener('click', handler, { signal: controller.signal });
// Later: controller.abort();
```

### Race Conditions

```
SYMPTOMS:
- Intermittent failures
- Works locally, fails in CI (or vice versa)
- "Heisenbug" - disappears when debugging

COMMON CAUSES:
- Shared mutable state
- Async operations completing out of order
- Missing synchronization

DEBUGGING:
1. Add logging with timestamps
2. Look for operations that should be sequential
3. Introduce delays to expose the race
4. Use thread-safe data structures

EXAMPLE:
// BAD: Race condition
let counter = 0;
async function increment() {
  const current = counter;
  await delay(1);
  counter = current + 1;
}
// Two concurrent calls both read 0, both write 1

// GOOD: Atomic operation or mutex
import { Mutex } from 'async-mutex';
const mutex = new Mutex();
async function increment() {
  await mutex.runExclusive(async () => {
    const current = counter;
    await delay(1);
    counter = current + 1;
  });
}
```

### N+1 Query Problem

```
SYMPTOMS:
- Slow API responses
- Database CPU spikes
- Response time proportional to data size

IDENTIFICATION:
- Enable query logging
- Count queries per request
- Look for patterns like "1 query + N queries"

EXAMPLE:
// BAD: N+1 queries
const orders = await Order.findAll(); // 1 query
for (const order of orders) {
  order.customer = await Customer.findById(order.customerId); // N queries
}

// GOOD: Eager loading
const orders = await Order.findAll({
  include: [{ model: Customer }] // 1 query with JOIN
});

// GOOD: Batch loading
const orders = await Order.findAll();
const customerIds = [...new Set(orders.map(o => o.customerId))];
const customers = await Customer.findAll({
  where: { id: customerIds }
}); // 2 queries total
```

### Connection Pool Exhaustion

```
SYMPTOMS:
- "Connection pool exhausted" errors
- Requests hanging then timing out
- Database shows many idle connections

COMMON CAUSES:
- Connections not returned to pool
- Pool size too small for load
- Long-running queries holding connections

DEBUGGING:
1. Monitor active vs idle connections
2. Check for unreturned connections (missing finally blocks)
3. Look for long-running transactions

EXAMPLE:
// BAD: Connection leak
const connection = await pool.getConnection();
const result = await connection.query(sql);
// If query throws, connection never released

// GOOD: Always release
const connection = await pool.getConnection();
try {
  const result = await connection.query(sql);
  return result;
} finally {
  connection.release();
}

// BETTER: Use with pattern if available
await pool.withConnection(async (connection) => {
  return await connection.query(sql);
});
```

### Deadlocks

```
SYMPTOMS:
- Requests hang indefinitely
- Database shows waiting transactions
- Works with low load, fails under high load

IDENTIFICATION:
- Database deadlock detection (most DBs have this)
- Thread dump analysis
- Look for circular wait patterns

PREVENTION:
- Always acquire locks in consistent order
- Use short transactions
- Avoid holding locks during I/O
- Use optimistic locking when possible

EXAMPLE:
// BAD: Deadlock potential
Transaction 1: Lock A, then Lock B
Transaction 2: Lock B, then Lock A

// GOOD: Consistent ordering
Transaction 1: Lock A, then Lock B
Transaction 2: Lock A, then Lock B
```

---

## Tool-Specific Debugging

### Browser DevTools

```
CONSOLE:
console.log(obj)        // Basic output
console.table(array)    // Tabular format
console.trace()         // Stack trace
console.time('label')   // Performance timing
console.timeEnd('label')
console.group('name')   // Group related logs
console.groupEnd()

NETWORK TAB:
- Filter by type (XHR, JS, CSS)
- Check response times
- Inspect headers and payloads
- Throttle network speed
- Block specific requests

PERFORMANCE:
- Record interactions
- Identify long tasks (>50ms)
- Find layout thrashing
- Check memory usage

SOURCES:
- Set breakpoints
- Conditional breakpoints (right-click)
- Watch expressions
- Call stack navigation
```

### Node.js Debugging

```
INSPECTOR:
$ node --inspect app.js
# Connect via Chrome DevTools at chrome://inspect

$ node --inspect-brk app.js
# Break on first line

BUILT-IN DEBUGGING:
process.on('uncaughtException', (err) => {
  console.error('Uncaught:', err);
  // Log, cleanup, exit
});

process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled rejection:', reason);
});

MEMORY DEBUGGING:
$ node --expose-gc app.js
# In code:
global.gc(); // Force garbage collection
console.log(process.memoryUsage());
```

### Database Debugging

```
QUERY ANALYSIS (PostgreSQL):
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123;

Key things to look for:
- Seq Scan (full table scan - often bad)
- Index Scan (using index - usually good)
- Nested Loop (can be slow with large sets)
- Sort (memory usage for ORDER BY)
- Actual vs estimated rows (statistics accuracy)

SLOW QUERY LOG:
# postgresql.conf
log_min_duration_statement = 100  # Log queries over 100ms

# MySQL
slow_query_log = 1
long_query_time = 0.1

LOCK DEBUGGING:
-- PostgreSQL: View locks
SELECT * FROM pg_locks WHERE NOT granted;

-- View blocking queries
SELECT blocked.pid, blocked.query, blocking.pid, blocking.query
FROM pg_stat_activity blocked
JOIN pg_locks blocked_locks ON blocked.pid = blocked_locks.pid
JOIN pg_locks blocking_locks ON blocked_locks.locktype = blocking_locks.locktype
  AND blocked_locks.relation = blocking_locks.relation
  AND blocked_locks.pid != blocking_locks.pid
JOIN pg_stat_activity blocking ON blocking_locks.pid = blocking.pid
WHERE NOT blocked_locks.granted;
```

---

## Production Debugging

### Safe Production Debugging

```
RULES:
1. NEVER debug directly in production database
2. Use read replicas when possible
3. Limit query scope (always use LIMIT)
4. Add execution timeouts
5. Monitor system impact while debugging

TECHNIQUES:
1. Feature flags to isolate
2. Debug endpoints (protected, rate-limited)
3. Increase logging temporarily for specific users
4. Traffic mirroring to debug environment
```

### Distributed Tracing

```
TRACE ANATOMY:
Trace ID: Unique ID for entire request flow
Span: Single operation within trace
Parent Span ID: Links spans together

EXAMPLE TRACE:
TraceID: abc-123
├── Span: API Gateway (10ms)
│   └── Span: Auth Service (5ms)
├── Span: Order Service (50ms)
│   ├── Span: DB Query (20ms)
│   └── Span: Inventory Check (25ms)
└── Span: Payment Service (100ms)
    └── Span: External Gateway (90ms)

Total: 165ms

TOOLS:
- Jaeger
- Zipkin
- AWS X-Ray
- Datadog APM
- OpenTelemetry (standard)
```

### Log Aggregation Queries

```
COMMON PATTERNS (Splunk/ELK syntax varies):

Find errors for specific user:
level:error AND userId:"user-123"

Find slow requests:
responseTime:>1000

Find specific error pattern:
message:"connection refused" AND service:payment

Timeline correlation:
requestId:"req-abc" | sort timestamp

Aggregate errors by type:
level:error | stats count by errorType
```

---

## Post-Incident Process

### Blameless Post-Mortem Template

```markdown
# Incident Post-Mortem: [Title]

## Summary
- **Date**: YYYY-MM-DD
- **Duration**: X hours Y minutes
- **Severity**: P1/P2/P3
- **Impact**: X users affected, Y% error rate

## Timeline (All times in UTC)
- HH:MM - First alert triggered
- HH:MM - Engineer acknowledged
- HH:MM - Root cause identified
- HH:MM - Fix deployed
- HH:MM - Monitoring confirmed resolution

## Root Cause
[Technical explanation of what went wrong]

## What Went Well
- Alert triggered quickly
- Team responded within SLA
- Communication was clear

## What Went Wrong
- Monitoring gap in X area
- Runbook was outdated
- Fix took longer due to Y

## Action Items
| Action | Owner | Due Date |
|--------|-------|----------|
| Add monitoring for X | @engineer | Date |
| Update runbook | @engineer | Date |
| Add test for regression | @engineer | Date |

## Lessons Learned
[Key takeaways for the team]
```

### Five Whys Analysis

```
EXAMPLE:

Problem: Users couldn't log in

Why 1: Authentication service returned errors
Why 2: Database connections were exhausted
Why 3: A query was holding connections too long
Why 4: The query was missing an index
Why 5: Index was dropped during migration

ROOT CAUSE: Migration process doesn't verify indexes exist

ACTION: Add index verification to migration CI checks
```
