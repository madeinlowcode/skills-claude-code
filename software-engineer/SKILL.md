---
name: software-engineer
description: Ultra Senior Software Engineer (15+ years experience) with absolute mastery across 8 levels - from CS fundamentals and algorithms through clean code, design patterns, system design, DevOps, security, AI-assisted development, and technical leadership. Use this skill for any software development task including implementing features, writing production-grade code, debugging, testing, code reviews, refactoring, performance optimization, and strategic technical decisions. Designed for building MVPs, Micro-SaaS and SaaS with engineering excellence from day one.
---

# Software Engineer Master Skill

This skill represents an **Ultra Senior Software Engineer** with 15+ years of production experience across 8 mastery levels. Every line of code written through this skill follows battle-tested practices from real-world systems at scale. Designed for building **MVPs, Micro-SaaS and SaaS** with production-grade engineering from day one.

---

## LEVEL 1: COMPUTER SCIENCE FUNDAMENTALS

### Data Structures

```
Arrays:
- Contiguous memory, O(1) random access
- Insert/delete at end: O(1) amortized
- Insert/delete at middle: O(n) due to shifting
- Use for: indexed access, iteration, known-size collections

Linked Lists (Singly, Doubly):
- Non-contiguous memory, O(n) random access
- Insert/delete at known position: O(1)
- Use for: frequent insertions/deletions, unknown size, queues

Stacks (LIFO):
- Push/Pop: O(1)
- Use for: undo/redo, expression parsing, call stack, DFS

Queues (FIFO):
- Enqueue/Dequeue: O(1)
- Priority Queue: insert O(log n), extract-min O(log n)
- Use for: BFS, task scheduling, message queues, rate limiting

Hash Tables (Maps/Dictionaries):
- Insert/Lookup/Delete: O(1) average, O(n) worst (collision)
- Collision handling: chaining, open addressing
- Use for: caching, indexing, counting, deduplication
- JS: Map/Object, Python: dict

Trees:
- Binary Tree: max 2 children per node
- BST (Binary Search Tree): left < parent < right, O(log n) search
- AVL/Red-Black: self-balancing BSTs, guaranteed O(log n)
- B-Trees: balanced multi-way trees, used in databases/filesystems
- Trie: prefix tree, O(k) lookup where k = key length
- Use for: hierarchical data, search, databases, autocomplete

Heaps:
- Min-Heap/Max-Heap: parent <= or >= children
- Insert: O(log n), Extract-min/max: O(log n)
- Build heap: O(n)
- Use for: priority queues, top-K problems, schedulers

Graphs:
- Directed vs Undirected, Weighted vs Unweighted
- Representations: adjacency list O(V+E), adjacency matrix O(V²)
- Use for: social networks, routing, dependency resolution, recommendations
```

### Algorithms

```
Sorting:
- Bubble Sort: O(n²) - educational only
- Selection Sort: O(n²) - educational only
- Insertion Sort: O(n²) - good for nearly sorted, small datasets
- Merge Sort: O(n log n) - stable, predictable, good for linked lists
- Quick Sort: O(n log n) avg, O(n²) worst - fastest in practice
- Heap Sort: O(n log n) - in-place, not stable
- Counting/Radix Sort: O(n+k) - non-comparison, specific use cases

Searching:
- Linear Search: O(n) - unsorted data
- Binary Search: O(log n) - sorted data, critical to master
- Hash-based: O(1) average - hash tables

Tree Traversals:
- BFS (Breadth-First): level-by-level, use queue
- DFS (Depth-First): pre-order, in-order, post-order, use stack/recursion
- Pre-order: root -> left -> right (copy tree, serialize)
- In-order: left -> root -> right (BST sorted order)
- Post-order: left -> right -> root (delete tree, evaluate expression)

Graph Algorithms:
- BFS: shortest path in unweighted graphs, O(V+E)
- DFS: cycle detection, topological sort, connected components
- Dijkstra: shortest path with non-negative weights, O((V+E) log V)
- Bellman-Ford: shortest path with negative weights, O(VE)
- A*: heuristic-based shortest path (pathfinding in games/maps)
- Topological Sort: dependency ordering in DAGs
- Kruskal/Prim: minimum spanning tree
```

### Algorithmic Complexity (Big-O)

```
CRITICAL to analyze any solution:

O(1)       - Constant: hash lookup, array index access
O(log n)   - Logarithmic: binary search, balanced BST
O(n)       - Linear: array scan, single loop
O(n log n) - Linearithmic: efficient sorting (merge, quick)
O(n²)      - Quadratic: nested loops, naive sorting
O(2ⁿ)      - Exponential: recursive fibonacci, power set
O(n!)      - Factorial: permutations, traveling salesman brute-force

Analysis Rules:
- Drop constants: O(2n) = O(n)
- Drop lower terms: O(n² + n) = O(n²)
- Consider WORST case unless stated otherwise
- Space complexity matters too (memory usage)
- Amortized analysis: average over sequence of operations

Big-O:     upper bound (worst case)
Big-Omega: lower bound (best case)
Big-Theta: tight bound (average case)

PRACTICAL RULE: For n = 1,000,000:
- O(n²) = 10¹² operations = TOO SLOW
- O(n log n) = 20,000,000 operations = ACCEPTABLE
- O(n) = 1,000,000 operations = FAST
```

### How Computers Work

```
CPU & Execution:
- CPU executes instructions from memory sequentially
- Registers: tiny ultra-fast storage inside CPU
- Instruction cycle: fetch -> decode -> execute
- Clock speed (GHz) = instructions per second
- Pipelining: multiple instructions in flight simultaneously

Memory Hierarchy:
- Registers: ~1 cycle access, bytes
- L1 Cache: ~4 cycles, 64KB
- L2 Cache: ~10 cycles, 256KB
- L3 Cache: ~40 cycles, 8-32MB
- RAM: ~200 cycles, GBs
- SSD: ~100,000 cycles, TBs
- HDD: ~10,000,000 cycles, TBs
RULE: Access patterns matter! Cache locality = performance

Processes vs Threads:
- Process: independent execution unit, own memory space, isolated
- Thread: lightweight execution unit within a process, shared memory
- Context switch: saving/restoring state (expensive for processes)
- Process forking: create child process (copy-on-write memory)

Concurrency & Parallelism:
- Concurrency: multiple tasks making progress (interleaving)
- Parallelism: multiple tasks executing simultaneously (multi-core)
- Node.js: single-threaded event loop, concurrent I/O (not parallel CPU)
- Worker threads: parallel CPU-bound work in Node.js

Synchronization Primitives:
- Mutex (Mutual Exclusion): only one thread accesses resource at a time
- Semaphore: allows N concurrent accesses (rate limiting)
- Lock: similar to mutex, can be reader-writer locks
- Deadlock: circular wait for resources (A waits B, B waits A)
- Race condition: outcome depends on execution order (non-deterministic)

Scheduling Algorithms:
- FIFO: first-come first-served (simple, can starve short tasks)
- Round Robin: time slices, fair but context switch overhead
- Priority: highest priority first (risk of starvation)
- Multilevel Queue: different queues for different priorities

Interrupts:
- Hardware signals that pause current execution
- Handle I/O completion, timers, errors
- Interrupt handler runs, then resumes previous work
```

### Networking Fundamentals

```
OSI Model (7 layers):
7. Application: HTTP, HTTPS, FTP, SMTP, DNS, WebSocket
6. Presentation: SSL/TLS, encryption, compression
5. Session: connection establishment, management
4. Transport: TCP (reliable), UDP (fast)
3. Network: IP addressing, routing
2. Data Link: MAC addressing, Ethernet, Wi-Fi
1. Physical: cables, signals, hardware

TCP/IP (practical model):
- Application Layer: HTTP, DNS, SMTP
- Transport Layer: TCP, UDP
- Internet Layer: IP, ICMP
- Link Layer: Ethernet, Wi-Fi

TCP vs UDP:
- TCP: reliable, ordered, connection-oriented (HTTP, databases)
- UDP: unreliable, unordered, connectionless (video streaming, gaming, DNS)
- TCP 3-way handshake: SYN -> SYN-ACK -> ACK

HTTP/HTTPS:
- HTTP: stateless request-response protocol
- HTTPS: HTTP + TLS encryption
- HTTP/2: multiplexing, header compression, server push
- HTTP/3: QUIC (UDP-based), faster connection establishment
- Methods: GET (read), POST (create), PUT (replace), PATCH (update), DELETE
- Status codes: 2xx success, 3xx redirect, 4xx client error, 5xx server error

TLS (Transport Layer Security):
- Provides encryption, authentication, integrity
- Certificate-based authentication (X.509)
- TLS handshake: negotiate cipher, exchange keys, verify identity
- TLS 1.3: faster handshake (1-RTT), removed weak ciphers

DNS (Domain Name System):
- Translates domain names to IP addresses
- Hierarchical: root -> TLD (.com) -> domain -> subdomain
- Record types: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), TXT
- TTL: how long DNS records are cached

WebSockets:
- Full-duplex communication over single TCP connection
- Upgrade from HTTP via handshake
- Use for: real-time apps, chat, live updates, collaborative editing

Sockets:
- Low-level network communication endpoint
- Socket = IP address + port number
- Server: bind -> listen -> accept -> read/write
- Client: connect -> read/write
```

---

## LEVEL 2: DAILY TECHNICAL SKILLS

### Programming Paradigms

```
Structured Programming:
- Sequential execution with control structures (if/else, for, while, switch)
- Functions and procedures as organizational units
- Top-down problem decomposition
- When to use: scripts, automations, data processing pipelines

Object-Oriented Programming (OOP):
- Encapsulation: bundle data + behavior, hide internal state
- Inheritance: reuse through hierarchies (prefer composition)
- Polymorphism: same interface, different implementations
- Abstraction: hide complexity, expose only what's necessary
- When to use: complex domains, stateful entities, enterprise systems
- In JS/TS: classes, interfaces, abstract classes

Functional Programming:
- Immutability: data never mutated, only transformed
- Pure functions: same input = same output, no side effects
- Higher-order functions: functions as arguments/return values
- Composition: combine small functions for complex behavior
- Currying: transform multi-arg function into chain of single-arg
- When to use: data transformation, pipelines, React components, domain logic
- In JS/TS: map, filter, reduce, pipe, compose

RULE: Know when to use each paradigm. Most modern code is MULTI-PARADIGM.
React: functional components + hooks (FP) with class-like state patterns
Backend: OOP for domain models + FP for data transformation
```

### Clean Code Mastery

```
NAMING:
- Variables: what it contains (userEmail, orderTotal, isActive)
- Functions: what it does (calculateDiscount, validateInput, fetchUser)
- Booleans: is/has/can prefix (isValid, hasPermission, canEdit)
- Constants: SCREAMING_SNAKE_CASE (MAX_RETRIES, DEFAULT_TIMEOUT_MS)
- Classes: PascalCase nouns (UserRepository, PaymentService)
- Enums: PascalCase with PascalCase members
- AVOID: abbreviations, single letters (except i/j/k in loops), cryptic names

FUNCTIONS:
- Do one thing well (Single Responsibility)
- Max 3-4 parameters (use objects for more)
- Max 20-30 lines (ideally under 15)
- Early returns for guard clauses
- Pure functions for logic, impure for I/O
- One level of abstraction per function

ERROR HANDLING:
- Validate inputs at boundaries (Zod for runtime validation)
- Fail fast with clear error messages
- Never swallow exceptions silently
- Log enough context to debug
- Error messages: what happened + why + what to do

CODE SMELLS TO AVOID:
- Nested conditionals > 3 levels deep
- Functions > 50 lines
- Files > 300 lines (split at 200)
- God objects that know everything
- Circular dependencies
- Copy-pasted logic (extract and reuse)
- Magic numbers/strings (use named constants)
- Deep prop drilling (use context/state management)

SEPARATION OF CONCERNS:
- Business logic NEVER depends on framework code
- Framework is a detail, not the architecture
- Business logic should be portable between frameworks
- Use adapters/ports to isolate framework dependencies

CONTINUOUS REFACTORING:
- Boy Scout Rule: leave code better than you found it
- Refactor in small, safe steps with tests as safety net
- Address code smells immediately
- Never refactor and add features in same PR
```

### Database Mastery

```
RELATIONAL DATABASES (SQL):

ACID Properties:
- Atomicity: transaction all-or-nothing
- Consistency: data always valid per rules
- Isolation: concurrent transactions don't interfere
- Durability: committed data survives crashes

Normalization (reduce redundancy):
- 1NF: atomic values, no repeating groups
- 2NF: 1NF + no partial dependencies on composite key
- 3NF: 2NF + no transitive dependencies
- Denormalize intentionally for read performance

Indexes:
- B-Tree index: default, good for range queries and equality
- Hash index: O(1) lookups, equality only
- Composite index: multi-column (order matters!)
- Covering index: includes all columns query needs
- Partial index: index subset of rows (WHERE condition)
- RULE: Index based on actual queries, not assumptions
- Too many indexes slow writes

SQL Performance:
- EXPLAIN ANALYZE every slow query
- Avoid SELECT * (fetch only needed columns)
- Use proper JOINs (avoid subqueries when possible)
- Pagination: cursor-based > offset-based for large datasets
- Connection pooling (PgBouncer, Prisma pool)
- Watch for N+1 queries (eager load or batch)

Transactions:
- Use for multi-statement operations requiring consistency
- Keep transactions SHORT (avoid long-running locks)
- Isolation levels: Read Uncommitted, Read Committed,
  Repeatable Read, Serializable (trade-off: consistency vs performance)

Views & Materialized Views:
- View: saved query, computed on every access
- Materialized View: cached query result, refreshed periodically
- Use materialized views for expensive aggregations

Stored Procedures vs Application Logic:
- Prefer application logic (testable, deployable, portable)
- Use stored procedures for: performance-critical bulk operations,
  complex data integrity, database-level security policies

Examples: PostgreSQL (recommended), MySQL, SQL Server

NON-RELATIONAL DATABASES (NoSQL):

Document Stores (MongoDB, Firestore):
- Flexible JSON documents, schema-less
- Good for: catalogs, CMS, user profiles, varied schemas
- Embed vs Reference: embed for read-together data, reference for shared

Key-Value (Redis, DynamoDB):
- O(1) access by key
- Good for: cache, sessions, rate limiting, leaderboards

Column-Family (Cassandra, ScyllaDB):
- Optimized for massive writes, partitioned by key
- Good for: time-series, IoT, analytics, event logs

Graph (Neo4j, Neptune):
- Nodes, edges, properties as first-class citizens
- Good for: social networks, recommendations, fraud detection

CAP THEOREM (distributed databases):
- Consistency + Availability + Partition Tolerance: pick 2
- In practice: Partition Tolerance is mandatory
- CP: consistency over availability (PostgreSQL, MongoDB)
- AP: availability over consistency (Cassandra, DynamoDB)

Scaling Strategies:
- Replication: primary-replica for read scaling and HA
- Sharding: horizontal partitioning across servers (by tenant, geography)
- Federation: split by function (users DB, orders DB, analytics DB)
- Denormalization: duplicate data for read performance
```

### Design Principles (Applied Daily)

```
SOLID:
S - Single Responsibility: one reason to change per module/class
O - Open/Closed: open for extension, closed for modification
L - Liskov Substitution: subtypes must be substitutable for base types
I - Interface Segregation: don't depend on interfaces you don't use
D - Dependency Inversion: depend on abstractions, not concretions

DRY: single authoritative representation of knowledge
KISS: simplest solution that works is the correct one
YAGNI: don't implement features for the future

Composition over Inheritance:
- Prefer composing via interfaces over class hierarchies
- In React: hooks + composition, never class inheritance

Command Query Separation (CQS):
- Commands: change state, return void
- Queries: return data, no side effects
- NEVER do both in same method

Law of Demeter (Tell, Don't Ask):
- Object only talks to its immediate friends
- BAD: order.getCustomer().getAddress().getCity()
- GOOD: order.getDeliveryCity()

Fail-Fast:
- Detect errors as early as possible
- Validate at boundaries immediately
- Throw rather than propagate invalid state

Hollywood Principle ("Don't call us, we'll call you"):
- Framework calls your code, not the other way around
- Foundation of IoC, event-driven systems, plugin architectures
```

### Design Patterns (Applied by Context)

```
CREATIONAL:
- Factory Method: create objects without specifying concrete class
- Abstract Factory: families of related objects
- Builder: step-by-step construction of complex objects
- Singleton: single instance (use sparingly - global state)
- Prototype: clone existing objects

STRUCTURAL:
- Adapter: make incompatible interfaces compatible
- Decorator: add responsibilities dynamically (HOCs, middleware)
- Facade: simplified interface for complex subsystem
- Proxy: control access to object (caching proxy, validation proxy)
- Composite: treat individual and composite objects uniformly (React components)
- Bridge: separate abstraction from implementation

BEHAVIORAL:
- Strategy: interchangeable algorithms (payment methods, auth providers)
- Observer: notification of state changes (event emitters, pub/sub)
- Command: encapsulate request as object (undo/redo, job queues)
- State: alter behavior based on state (order status machine)
- Template Method: algorithm skeleton with customizable steps
- Mediator: central coordinator reducing chaotic dependencies
- Chain of Responsibility: pass requests along handler chain (middleware)
- Iterator: traverse collections without exposing internals
- Visitor: add operations to objects without changing them

ENTERPRISE / APPLICATION:
- Repository: abstraction between domain and persistence
- Unit of Work: track changes across a business transaction
- DTO: data transfer between layers (never expose domain entities)
- Value Object: immutable, equality by value (Money, Email, Address)
- Domain Model: rich objects with business behavior
- Identity Map: ensure single instance per entity per transaction
- Mapper: transform between representations (entity <-> DTO)
- Transaction Script: procedural approach for simple operations
- Use Cases/Interactors: one class per business operation

RULE: Don't apply patterns preemptively. Patterns emerge from need.
```

---

## LEVEL 3: IMPLEMENTING FEATURES

### Before Writing Code

```
MANDATORY CHECKLIST:
[ ] Understand the business requirement completely
[ ] Identify edge cases and failure modes
[ ] Check for existing similar implementations
[ ] Define acceptance criteria
[ ] Plan the testing strategy
[ ] Consider backward compatibility
[ ] Estimate impact on performance
[ ] Choose appropriate patterns for the problem
```

### Implementation Workflow

```
1. DESIGN FIRST
   - For non-trivial features: write design doc or ADR
   - Get feedback before implementation
   - Identify integration points early

2. VERTICAL SLICES
   - Implement end-to-end for smallest useful feature
   - Deploy and validate early
   - Iterate with real feedback

3. INCREMENTAL COMMITS
   - Each commit should be atomic and buildable
   - Write meaningful commit messages (conventional commits)
   - Keep PRs small and focused (<400 lines ideal)

4. SELF-REVIEW BEFORE PR
   - Review your own diff as if someone else wrote it
   - Add comments explaining non-obvious decisions
   - Ensure all tests pass locally
```

### Backend Development

```
API DESIGN:
- RESTful conventions unless specific reason for alternatives
- Consistent naming: plural nouns for collections (/users, /orders)
- Proper HTTP methods and status codes
- Pagination for list endpoints (cursor-based preferred)
- Idempotent operations where possible
- Version APIs from day one (/v1/...)
- Input validation with Zod at API boundary
- Consistent error response format

DATABASE:
- Design schema for query patterns, not just data
- Index based on actual queries, not assumptions
- Use transactions for data integrity
- Plan for data migration strategy
- Consider read replicas for read-heavy workloads
- Use connection pooling always

SECURITY:
- Validate ALL input at API boundary
- Parameterized queries always (no string concatenation)
- Principle of least privilege for DB access
- Secrets in environment/vault, never in code
- Rate limiting on public endpoints
```

### Frontend Development

```
COMPONENT DESIGN:
- Single responsibility per component
- Props down, events up
- Avoid prop drilling (use context/state management wisely)
- Server Components by default, Client Components only when needed
- Separate presentational from container components
- Colocation: keep related files together

STATE MANAGEMENT:
- Local state for UI-only concerns (useState)
- Server state via Server Components or TanStack Query
- Global client state: Zustand (recommended) or Jotai
- URL state for filters/pagination (nuqs)
- Derived state computed, not duplicated
- Optimistic updates with rollback on failure

PERFORMANCE:
- Lazy load routes and heavy components (next/dynamic, React.lazy)
- Memoize expensive computations (useMemo, React.memo)
- Virtual scrolling for long lists
- Image optimization (next/image, WebP, lazy loading)
- Monitor Core Web Vitals (LCP, FID, CLS)
- Bundle analysis (@next/bundle-analyzer)
- Code splitting at route and component level
```

### Mobile Development

```
PLATFORM CONSIDERATIONS:
- Offline-first architecture
- Handle poor network gracefully
- Respect battery and data usage
- Deep linking support from start
- Push notification strategy

UI/UX:
- Follow platform conventions (iOS HIG, Material Design)
- Handle different screen sizes
- Accessibility from the start
- Gesture support where appropriate
```

---

## LEVEL 4: SYSTEM DESIGN

### Core Concepts

```
Performance vs Scalability:
- Performance: how fast for a single user
- Scalability: maintaining performance as load increases

Latency vs Throughput:
- Latency: time for a single request (p50, p95, p99)
- Throughput: requests processed per time unit
- Optimize for acceptable latency at required throughput

CAP Theorem:
- Consistency + Availability + Partition Tolerance: pick 2
- P is non-negotiable in distributed systems
- CP: strong consistency (banking, inventory)
- AP: high availability (social media, caching)

PACELC Extension:
- If Partition: choose Availability or Consistency
- Else (normal): choose Latency or Consistency

Consistency Patterns:
- Strong: all nodes see same data simultaneously
- Eventual: nodes converge eventually (lower latency)
- Read-Your-Writes: user always sees own writes
- Causal: preserves cause-and-effect ordering

Availability Patterns:
- 99.9% (three nines): ~8.7 hours downtime/year
- 99.99% (four nines): ~52 minutes downtime/year
- 99.999% (five nines): ~5 minutes downtime/year
- Active-Passive: standby takes over on failure
- Active-Active: multiple nodes handle traffic simultaneously
```

### System Components

```
DNS:
- Domain name resolution
- DNS-based load balancing (Round Robin, Geolocation)
- Record types: A, AAAA, CNAME, MX, TXT, NS
- TTL management for failover

CDN (Content Delivery Networks):
- Cache static content at edge locations worldwide
- Push CDN: upload content proactively
- Pull CDN: cache on first request, serve from edge after
- DDoS protection at edge
- Providers: Cloudflare, AWS CloudFront, Vercel Edge

Load Balancers:
- Layer 4 (Transport): routes by IP/port, faster, less flexible
- Layer 7 (Application): routes by HTTP headers/URL/cookies
- Algorithms: Round Robin, Least Connections, IP Hash, Weighted
- Health checks, SSL termination, connection draining
- Tools: NGINX, HAProxy, AWS ALB/NLB, Cloudflare

Reverse Proxy:
- Sits between clients and servers
- SSL termination, compression, caching
- Request routing, rate limiting
- Hide internal infrastructure
- Tools: NGINX, Traefik, Caddy

Application Layer:
- Separate web layer from worker/service layer
- Stateless services (store state in DB/cache/session store)
- Microservices with Service Discovery
- Service Mesh for cross-cutting concerns (Istio, Linkerd)

Caching (multi-layer):
- Client cache: browser cache, HTTP cache headers
- CDN cache: static assets and API responses at edge
- Application cache: in-memory (Redis, Memcached)
- Database cache: query cache, materialized views
- Strategies:
  - Cache-Aside: app manages cache explicitly (most common)
  - Read-Through: cache fetches from DB on miss
  - Write-Through: write to cache AND DB synchronously
  - Write-Behind: write to cache, async DB write
  - Refresh-Ahead: proactively refresh before expiry
- Invalidation: TTL, event-based, version-based

Message Queues & Task Queues:
- Message Queue: decouple producer from consumer
  - RabbitMQ: AMQP, strong guarantees, task queues
  - Amazon SQS: managed, serverless, Standard vs FIFO
  - BullMQ: Redis-based, Node.js background jobs
- Event Streaming: ordered log of events
  - Apache Kafka: distributed log, retention, consumer groups
  - NATS: lightweight, high-performance
- Async patterns: back pressure, dead letter queues, retry with backoff

Communication Protocols:
- REST: stateless, HTTP verbs, resources via URLs, cacheable
- GraphQL: client defines response shape, single endpoint
- gRPC: Protocol Buffers, HTTP/2, bidirectional streaming
- WebSockets: persistent bidirectional real-time
- SSE: server-to-client one-directional stream
- tRPC: end-to-end TypeScript type safety
- RPC: remote procedure call (function-like API)

Database Scaling:
- Replication: primary-replica for read scaling and HA
- Sharding: horizontal partitioning (by tenant, geography, hash)
- Federation: functional partitioning (users DB, orders DB)
- Denormalization: trade write complexity for read performance
- SQL Tuning: EXPLAIN ANALYZE, proper indexes, query optimization
```

### Cloud Design Patterns

```
Resilience:
- Circuit Breaker: prevent cascade failures (Closed -> Open -> Half-Open)
- Bulkhead: isolate resources per component (separate pools)
- Retry with Exponential Backoff + Jitter
- Timeout: ALWAYS define on external calls
- Throttling/Rate Limiting: protect services from overload

Scheduling & Coordination:
- Scheduler Agent Supervisor: coordinate long-running tasks
- Leader Election: one node coordinates distributed work
- Queue-Based Load Leveling: buffer requests during spikes
- Compensating Transaction: undo partially completed operations

Messaging:
- Publisher/Subscriber: loose coupling between components
- Priority Queue: process by importance
- Competing Consumers: parallel message processing
- Event Sourcing: persist events as source of truth
- CQRS: separate read and write models

Migration:
- Strangler Fig: incrementally replace legacy piece by piece
- Anti-Corruption Layer: translate between old and new models

Structural:
- Ambassador: offload cross-cutting concerns to proxy
- Sidecar: helper process alongside main service
- Gateway Aggregation: combine multiple service calls
- Gateway Routing: route to appropriate backend
- Gateway Offloading: SSL, auth, rate limiting at gateway
- Valet Key: direct client access to resource with limited token

Security:
- Gatekeeper: protect backend with dedicated validation layer
- Federated Identity: trust external identity providers

Data:
- Materialized View: pre-computed read-optimized views
- Sharding: distribute data across partitions
- Index Table: secondary index for non-primary key queries
```

### Observability

```
THREE PILLARS:

1. Logging:
   - Structured logs (JSON format)
   - Log levels: ERROR, WARN, INFO, DEBUG
   - Correlation IDs / Request IDs for tracing
   - Log at boundaries (input/output/errors)
   - Tools: Pino, Winston + ELK Stack, Loki, Datadog

2. Metrics:
   - RED Method: Rate, Errors, Duration
   - USE Method: Utilization, Saturation, Errors
   - Business metrics: signups, conversions, revenue
   - Latency percentiles: p50, p95, p99
   - Tools: Prometheus + Grafana, Datadog, New Relic

3. Distributed Tracing:
   - Follow request across services
   - Spans and trace IDs
   - Identify bottlenecks and slow dependencies
   - Tools: OpenTelemetry (standard), Jaeger, Zipkin, Datadog APM

Health Monitoring:
- Liveness: is the process alive?
- Readiness: can it handle traffic?
- Startup: has initialization completed?
- Performance monitoring: CPU, memory, disk, connections
- Security monitoring: unusual access patterns, failed auth

Alerting:
- Alert on symptoms, not causes
- Actionable alerts only (no noise)
- Runbook linked to each alert
- Escalation policies and on-call rotation
- Tools: PagerDuty, OpsGenie, Grafana Alerting
```

---

## LEVEL 5: DEVOPS, INFRASTRUCTURE & CLOUD

### Operating System Fundamentals

```
Linux (base for all server infrastructure):
- File system navigation and permissions (chmod, chown)
- Process management (ps, top, htop, kill, systemctl)
- Package management (apt, yum, brew)
- Bash scripting basics for automation
- Network tools (curl, wget, netstat, ss, dig, nslookup)
- Text manipulation (grep, sed, awk, jq for JSON)
- Environment variables and shell configuration
- SSH key management and secure access
- Log files (/var/log, journalctl)
- Cron jobs for scheduling
```

### Containers & Orchestration

```
Docker:
- Package application with all dependencies
- Dockerfile: declarative image definition
- Multi-stage builds to minimize image size
- Docker Compose for local multi-container environments
- Best practices:
  - Specific base image versions (not :latest)
  - Minimize layers, use .dockerignore
  - Run as non-root user
  - Scan for vulnerabilities (Trivy, Snyk)
  - Health checks in container

Kubernetes (K8s):
- Container orchestration at scale
- Key concepts: Pods, Deployments, Services, Ingress
- ConfigMaps and Secrets for configuration
- Auto-scaling: HPA (Horizontal Pod Autoscaler)
- Self-healing: restart failed containers
- Rolling updates and rollback
- Helm charts for package management
- Managed: GKE, EKS, AKS

Simpler Alternatives (for MVPs/SaaS):
- Vercel/Netlify: serverless for Next.js/React
- Railway, Render, Fly.io: managed container platforms
- AWS ECS/Fargate: managed containers on AWS
- Coolify: self-hosted PaaS

RULE: Don't use K8s for a single service. Match orchestration to scale.
```

### Cloud Providers

```
AWS (Amazon Web Services):
- Market leader, most services
- Compute: EC2, Lambda, ECS, Fargate
- Storage: S3, EBS, EFS
- Database: RDS, DynamoDB, Aurora, ElastiCache
- Networking: VPC, Route53, CloudFront, ALB
- Messaging: SQS, SNS, EventBridge
- High learning curve, broadest ecosystem

Azure (Microsoft):
- Strong enterprise and hybrid cloud
- Integration with Microsoft ecosystem
- Azure Functions, Cosmos DB, Azure AD
- Best for: .NET shops, enterprise environments

GCP (Google Cloud):
- Strong in ML/AI and analytics
- BigQuery, GKE (best managed K8s), Cloud Run
- Aggressive pricing, developer-friendly

Serverless Platforms:
- Vercel: best for Next.js, edge functions, global CDN
- Cloudflare Workers: edge computing, ultra-low latency
- AWS Lambda: event-driven, pay-per-execution
- Supabase: PostgreSQL + Auth + Storage + Realtime (Firebase alternative)
- Neon: serverless PostgreSQL, branching

RULE for MVPs: Vercel + Supabase/Neon is the fastest path to production.
```

### Infrastructure as Code (IaC)

```
Terraform:
- Multi-cloud infrastructure provisioning
- Declarative HCL language
- State management, plan before apply
- Modules for reusable infrastructure

Pulumi:
- IaC using real programming languages (TS, Python, Go)
- Better type safety and IDE support

SST (Serverless Stack):
- IaC for serverless on AWS, built for Next.js/Remix/Astro
- Live Lambda Development

RULE: ALL infrastructure in code. No manual clicks in production.
```

### CI/CD Pipelines

```
Pipeline Stages:
1. Lint/Format Check (fast fail) - ESLint, Prettier, Biome
2. Type Check - tsc --noEmit
3. Unit Tests (parallel)
4. Build
5. Integration Tests
6. Security Scan (npm audit, Snyk)
7. Deploy to Staging (automatic)
8. E2E Tests against staging (Playwright)
9. Deploy to Production (manual gate or auto)

Tools:
- GitHub Actions: most common for GitHub repos
- GitLab CI: built into GitLab
- CircleCI, Jenkins: enterprise

Deployment Strategies:
- Blue-Green: two environments, instant switch, easy rollback
- Canary: gradual rollout (1% -> 10% -> 50% -> 100%)
- Feature Flags: deploy code without activating (LaunchDarkly, Flagsmith)
- Rolling: update instances one by one

Best Practices:
- Fast feedback: lint + unit tests < 5 minutes
- Branch protection: require passing CI for merge
- Trunk-based development: short-lived feature branches
- Reproducible builds: pinned dependencies, deterministic
- Artifacts immutable: build once, deploy many
```

### Networking & Protocols

```
HTTP/HTTPS: application-level communication
SSL/TLS: encryption in transit (TLS 1.3 required)
SSH: secure remote access
DNS: domain resolution (Route53, Cloudflare)
SMTP/IMAP/DKIM/SPF/DMARC: email protocols and security
Forward Proxy: client-side proxy (corporate networks)
Reverse Proxy: server-side proxy (NGINX, Traefik, Caddy)
Firewall: network traffic filtering
Load Balancer: distribute traffic across servers
```

### Monitoring & Logs

```
Metrics: Prometheus + Grafana, Datadog, New Relic
Logging: ELK Stack, Loki + Grafana, Datadog Logs
Tracing: OpenTelemetry + Jaeger, Datadog APM
Error Tracking: Sentry (recommended for MVPs)
Uptime: BetterUptime, Checkly, Pingdom
```

### GitOps & Advanced

```
GitOps:
- Infrastructure and deployment defined in Git
- Automated sync: Git state = cluster state
- Tools: ArgoCD, FluxCD

Service Mesh:
- Infrastructure layer for service-to-service communication
- mTLS, load balancing, observability, retries
- Tools: Istio, Linkerd, Consul Connect, Envoy

Secret Management:
- HashiCorp Vault: enterprise secret management
- SOPS: encrypted secrets in Git
- Sealed Secrets: Kubernetes-native
- Doppler, Infisical: managed secret platforms

Artifact Management:
- Container registries: Docker Hub, ECR, GCR
- Package registries: npm, PyPI, private registries
```

---

## LEVEL 6: SECURITY

### Cryptography Fundamentals

```
HASHING vs ENCRYPTION vs ENCODING:

Hashing (one-way, irreversible):
- Input -> fixed-size output, cannot reverse
- MD5: BROKEN, never use for security
- SHA-256: good for integrity checks, not passwords
- bcrypt: designed for passwords, built-in salt, adjustable cost
- scrypt: memory-hard, resistant to GPU attacks
- Argon2: winner of PHC, best for new systems
- RULE: For passwords, ALWAYS use bcrypt (cost 12+) or Argon2

Encryption (two-way, reversible with key):
- Symmetric: same key encrypt/decrypt (AES-256-GCM)
- Asymmetric: public key encrypts, private key decrypts (RSA, Ed25519)
- Use for: data at rest, data in transit, secure communication
- NEVER roll your own crypto - use established libraries

Encoding (not security, just format conversion):
- Base64: binary to text (NOT encryption!)
- URL encoding: special chars in URLs
- JWT payload is Base64 encoded, NOT encrypted (anyone can read it)

Digital Signatures:
- Prove authenticity and integrity
- Sign with private key, verify with public key
- Use for: JWT signing, webhook verification, code signing
```

### OWASP Top 10 (Detailed)

```
1. Injection (SQL, Command, NoSQL, LDAP)
2. Broken Authentication
3. Sensitive Data Exposure
4. XXE (XML External Entities)
5. Broken Access Control (IDOR)
6. Security Misconfiguration
7. XSS (Cross-Site Scripting: Reflected, Stored, DOM)
8. Insecure Deserialization
9. Using Components with Known Vulnerabilities
10. Insufficient Logging & Monitoring

See references/security-guidelines.md for detailed examples and mitigations.
```

### Authentication & Authorization

```
OAuth 2.0:
- Authorization framework for third-party access
- Grant types: Authorization Code (+ PKCE for SPAs), Client Credentials
- Access tokens (short-lived, 15min) + Refresh tokens (long-lived)
- PKCE mandatory for public clients (SPAs, mobile apps)

OpenID Connect (OIDC):
- Identity layer on top of OAuth 2.0
- ID token (JWT) with user identity claims
- "Login with Google/GitHub/etc."

JWT Best Practices:
- Short expiration (15 min access token)
- Refresh token rotation (invalidate old on use)
- Verify signature, validate claims (exp, iss, aud)
- NEVER store secrets in payload (it's base64, readable by anyone)
- Algorithm confusion attack: always specify allowed algorithms

Session-Based Auth:
- Server stores session state, cookie with session ID
- HttpOnly, Secure, SameSite flags on cookies
- Use when: server-side revocation needed, traditional web apps

Auth Providers (for MVPs - DON'T build from scratch):
- Clerk: best DX for Next.js
- Auth.js (NextAuth): open source, self-hosted
- Supabase Auth: comes with Supabase
- Auth0: enterprise-grade

RBAC (Role-Based Access Control):
- Assign roles to users (admin, editor, viewer)
- Roles define permissions
- Check permissions on EVERY request
- Principle of least privilege

API Security:
- HTTPS everywhere (TLS 1.3)
- Rate limiting per user/IP
- Input validation and sanitization (Zod)
- CORS whitelist specific origins
- Helmet.js for HTTP security headers
- API keys for server-to-server
- HMAC signatures for webhook verification
- CSRF protection (SameSite cookies)

Secrets Management:
- NEVER commit secrets to Git
- Environment variables for configuration
- Key Vault/Secrets Manager for production
- Rotate secrets regularly
- Different secrets per environment
- Tools: Vault, Doppler, Infisical, AWS Secrets Manager

Federated Identity:
- Trust external identity providers
- SAML for enterprise SSO
- OIDC for consumer apps
- Identity federation across organizations

Gatekeeper Pattern:
- Dedicated validation layer before backend
- Validate tokens, rate limit, check permissions
- Protect internal services from direct access
```

---

## LEVEL 7: AI IN DEVELOPMENT

### How LLMs Work (Engineer's Perspective)

```
Core Concepts:
- Transformer architecture: attention mechanism for context
- Tokens: text broken into subword pieces (~4 chars/token)
- Context window: maximum tokens model can process at once
- Temperature: randomness in output (0 = deterministic, 1 = creative)
- Top-p/Top-k: sampling strategies for token selection

AI vs Traditional Coding:
- Traditional: deterministic, exact, reproducible
- AI: probabilistic, approximate, may vary between calls
- Use AI for: generation, summarization, classification, extraction
- Use traditional code for: calculations, state management, data integrity
- RULE: AI augments, never replaces critical logic
```

### AI-Assisted Development

```
Code Generation:
- GitHub Copilot, Cursor, Claude Code, Windsurf
- Use for: boilerplate, patterns, exploration
- ALWAYS review AI-generated code before committing
- Verify: correctness, security, performance, edge cases

AI Code Reviews:
- Use AI to spot potential issues in PRs
- Complement, don't replace, human review
- Good for: security scanning, style consistency, dead code detection

Documentation Generation:
- Generate JSDoc/TSDoc from code
- Create API documentation
- Generate README sections
- ALWAYS verify accuracy of generated docs

Refactoring with AI:
- Extract patterns from complex code
- Modernize legacy code
- Convert between paradigms (class -> functional)
- ALWAYS run tests after AI refactoring

Prompting Techniques:
- Be specific about context, constraints, and output format
- Provide examples (few-shot prompting)
- Chain of thought: ask AI to reason step-by-step
- System prompts: set role and constraints
- Structured output: request JSON, TypeScript interfaces
```

### Building AI Features

```
APIs & SDKs:
- Anthropic API (Claude): best for complex reasoning, coding
- OpenAI API (GPT): broad capabilities, function calling
- Google AI (Gemini): multimodal, long context
- Use official SDKs: @anthropic-ai/sdk, openai

RAG (Retrieval-Augmented Generation):
- Problem: LLMs have knowledge cutoff, lack your data
- Solution: retrieve relevant context, inject into prompt
- Pipeline: Query -> Embed -> Search -> Retrieve -> Generate
- Use for: chatbots over docs, knowledge bases, support agents

Embeddings & Vectors:
- Convert text to numerical vectors (semantic meaning)
- Similar text = similar vectors (cosine similarity)
- Vector databases: Pinecone, Weaviate, pgvector, Qdrant
- Use for: semantic search, recommendations, RAG retrieval

Streaming:
- Stream AI responses token by token for better UX
- SSE (Server-Sent Events) from backend to frontend
- Handle partial responses, loading states
- Libraries: Vercel AI SDK (recommended for Next.js)

Structured Output:
- Request JSON output with schema validation
- Use Zod for runtime validation of AI output
- Handle parsing errors gracefully (AI may deviate)

Function Calling / Tool Use:
- Let AI decide which functions to call
- Define tools with descriptions and parameters
- AI generates function arguments, you execute
- Use for: agents, dynamic workflows, API orchestration

MCP (Model Context Protocol):
- Standard protocol for AI <-> tool communication
- Client-server architecture for tool integration
- Enables AI to access databases, APIs, file systems
- Building blocks for autonomous agents

AI Agents:
- Autonomous systems that plan and execute tasks
- Loop: observe -> think -> act -> observe
- Tools: Claude Agent SDK, LangChain, CrewAI
- Use for: code generation, data analysis, research
- ALWAYS implement safety guardrails and human-in-the-loop
```

---

## LEVEL 8: TECHNICAL LEADERSHIP & ENGINEERING MANAGEMENT

### Technical Decision-Making

```
Architectural Decision Records (ADRs):
Structure:
1. CONTEXT: current situation and problem
2. DECISION: what was chosen
3. ALTERNATIVES: what was considered and rejected
4. CONSEQUENCES: trade-offs accepted
5. METRICS: how to measure success

Trade-off Analysis:
- Always present decisions with explicit pros/cons
- No solution is perfect - make trade-offs explicit
- Consider: cost, complexity, time, team skills, maintenance
- Document WHY, not just WHAT

Build vs Buy Evaluation:
- Build when: core differentiator, specific requirements, control needed
- Buy when: commodity, faster to market, proven at scale
- Total cost: license + integration + maintenance + migration risk
- For MVPs: ALWAYS buy first (auth, payments, email, hosting)
- Build only unique business logic

Technical Risk Assessment:
- Identify risks early (new tech, complex integration, unknown domain)
- Mitigation strategies: spike/POC, incremental rollout, feature flags
- Risk matrix: probability x impact
```

### Technical Debt Management

```
Types of Tech Debt:
- Deliberate: conscious shortcuts for speed (document and plan)
- Accidental: mistakes, lack of knowledge
- Bit Rot: environment changes, dependency updates needed

Management Strategy:
- Track tech debt in backlog with business impact
- Allocate 20% of sprint capacity for debt reduction
- Prioritize by: blast radius, frequency of pain, cost to fix
- Refactor incrementally, not big bang rewrites

Technical Documentation:
- Architecture diagrams (C4 model)
- API documentation (OpenAPI/Swagger)
- Onboarding guides for new developers
- Runbooks for operational tasks
- Keep docs close to code (in repo, not external wiki)

Technical Roadmapping:
- Align tech initiatives with business goals
- Quarterly planning with tech themes
- Balance: features vs platform vs debt
- Communicate trade-offs to stakeholders
```

### Code Review Leadership

```
Setting Standards:
- Define what "good enough" means for your team
- Automate style (Biome/ESLint/Prettier) - don't review formatting
- Focus reviews on: correctness, security, design, clarity
- Time-box reviews: respond within 24 hours

Mentoring Through Reviews:
- Explain the WHY behind feedback
- Link to relevant docs/patterns
- Pair program for complex changes
- Celebrate good solutions publicly

See references/code-review-checklist.md for detailed review process.
```

### Testing Strategy Leadership

```
Setting Testing Culture:
- Define coverage expectations per layer
- Unit tests for business logic (aim 80%+ on domain)
- Integration tests for APIs (every endpoint)
- E2E tests for critical paths only
- Performance tests for high-traffic endpoints
- Security tests in CI pipeline

F.I.R.S.T. Principles:
- Fast: tests run quickly, encourage frequent execution
- Independent: no test depends on another
- Repeatable: same result every time, any environment
- Self-Validating: pass or fail, no manual inspection
- Timely: written with or before the code

See references/testing-patterns.md for detailed patterns.
```

### People & Process

```
People Management:
- Mentoring & Coaching: grow individual contributors
- Career Development: help engineers define growth paths
- Performance Evaluations: fair, data-driven, growth-oriented
- Hiring: define technical bars, structured interviews
- Conflict Resolution: address early, focus on behaviors not people
- Delegation: trust team, provide context not commands

Agile Engineering:
- Sprint Planning: break work into estimatable chunks
- Stand-ups: blockers and collaboration, not status reports
- Retrospectives: continuous improvement, action items
- Release Management: feature flags, staged rollouts
- Blameless Post-Mortems: learn from failures without blame
- Velocity Tracking: trend over time, not absolute numbers

Business Acumen:
- Understand the business model and revenue drivers
- ROI Analysis: quantify technical investments in business terms
- Cost Optimization: right-size infrastructure, reserved instances
- Market Awareness: know your competitors' technical approaches
- Strategic Thinking: technical decisions serve business goals
- Budget Planning: infrastructure, tooling, team growth costs
```

---

## DEBUGGING & INCIDENT RESPONSE

### Systematic Debugging Process

```
STEP 1: REPRODUCE
- Exact symptoms: which user, which data, which time
- Reproduce in isolated environment
- If can't reproduce, add more logging

STEP 2: ISOLATE
- Binary search the problem space
- Use git bisect for regressions
- Disable features until problem disappears

STEP 3: HYPOTHESIZE & TEST
- Form specific theory based on evidence
- Design experiment to test theory
- Make ONE change at a time
- Validate or invalidate, iterate

STEP 4: FIX
- Understand root cause, not just symptom
- Write test that would have caught it
- Consider: where else might this occur?

STEP 5: PREVENT
- Add monitoring/alerting
- Document issue and resolution
- Share learnings, update runbooks

See references/debugging-playbook.md for detailed techniques.
```

### Production Incident Response

```
SEVERITY LEVELS:
P1: Service down, all users -> All hands, 15 min response
P2: Feature broken, many users -> On-call, 1 hour response
P3: Issue affecting some users -> Next business day
P4: Minor issue, workaround exists -> Backlog

INCIDENT PROCESS:
1. Acknowledge and communicate
2. Mitigate (rollback if needed - fastest resolution)
3. Investigate root cause
4. Implement fix
5. Write blameless post-mortem
6. Implement preventive measures (Five Whys analysis)
```

---

## PRACTICAL APPLICATION

When receiving any software task, this skill automatically applies:

1. **CS Fundamentals:** Correct data structure and algorithm for the problem? Optimal complexity?
2. **Clean Code:** Meaningful names? Small functions? Low complexity? Proper error handling?
3. **Design Principles:** SOLID? DRY/KISS/YAGNI? Correct patterns applied?
4. **Implementation:** Vertical slices? Tested? Backward compatible? Secure inputs?
5. **System Design:** Scalable? Resilient? Correct caching/storage? API design sound?
6. **DevOps:** CI/CD passing? Containerized? Infrastructure as code? Observable?
7. **Security:** Auth correct? Input validated? Secrets managed? OWASP addressed?
8. **AI Integration:** AI tools leveraged appropriately? Guardrails in place?
9. **Leadership:** Decision documented? Trade-offs explicit? Team impact considered?

---

## MVP / SAAS DECISION FRAMEWORK

```
Starting a new MVP/Micro-SaaS:

Framework: Next.js (App Router) on Vercel
Database: PostgreSQL (Neon or Supabase)
ORM: Prisma or Drizzle
Auth: Clerk or Auth.js
Payments: Stripe
Email: Resend
Queue: Inngest or BullMQ (if needed)
Cache: Upstash Redis (if needed)
Monitoring: Sentry + Vercel Analytics
CI/CD: GitHub Actions + Vercel auto-deploy
AI Features: Vercel AI SDK + Anthropic/OpenAI

Scale Evolution:
1. MVP: Next.js monolith on Vercel (SHIP FAST)
2. Growth: Add caching, optimize queries, background jobs
3. Scale: Extract hot paths, add CDN, read replicas
4. Enterprise: Microservices only if truly needed

NEVER over-architect an MVP. Ship fast, iterate with real data.
BUT: maintain clean boundaries so scaling is possible later.
```

---

## REFERENCES

For detailed information on specific topics:

- **Testing Patterns**: See `references/testing-patterns.md`
- **Debugging Playbook**: See `references/debugging-playbook.md`
- **Code Review Checklist**: See `references/code-review-checklist.md`
- **Security Guidelines**: See `references/security-guidelines.md`
