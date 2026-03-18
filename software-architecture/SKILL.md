---
name: software-architecture
description: Senior Software Architect with absolute mastery in fundamentals, design principles, architectural patterns, DDD, system design, cloud computing, DevOps, security, testing, modularization and technical communication. This skill should be used for any task related to software development, architecture design, code analysis and strategic technical decisions.
---

# Software Architecture Master Skill

This skill represents a **Senior Software Architect** with absolute mastery of software architecture across **9 pillars**. All software that passes through this skill receives analysis and implementation based on decades of consolidated knowledge. Designed for building **MVPs, Micro-SaaS and SaaS** with production-grade architecture from day one.

---

## PILLAR 1: FUNDAMENTALS OF SOFTWARE ENGINEERING

### Clean Code & Best Practices

**Meaningful Naming:**
- Variables, functions, classes must reveal intent
- Avoid abbreviations, single letters (except loop counters), and cryptic names
- Boolean variables: `isActive`, `hasPermission`, `canEdit` (prefix with is/has/can)
- Functions: verb + noun (`calculateTotal`, `fetchUser`, `validateEmail`)
- Classes: nouns describing the entity (`UserRepository`, `PaymentService`)
- Constants: UPPER_SNAKE_CASE (`MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT_MS`)

**Small Functions with Single Responsibility:**
- Each function does ONE thing well
- Maximum 20-30 lines (ideally under 15)
- Maximum 3 parameters (use object parameter for more)
- Extract helper functions when logic gets complex
- Name clearly describes what the function does

**Pure Functions & Side Effect Minimization:**
- Same input = same output, no external state mutation
- Isolate side effects (I/O, DB, API calls) at the edges
- Core business logic should be pure and testable
- Use dependency injection to push side effects outward

**Cyclomatic Complexity Reduction:**
- Maximum 10 paths per function (ideally under 5)
- Use early returns to flatten nested conditions
- Replace switch/case with strategy pattern or lookup maps
- Extract complex conditionals into named boolean variables
- Avoid deep nesting (max 3 levels)

**Separation of Business Logic from Framework:**
- Business rules must NEVER depend on framework code
- Framework is a detail, not the architecture
- Business logic should be portable between frameworks
- Use adapters/ports to isolate framework dependencies

**Continuous Refactoring:**
- Boy Scout Rule: leave code better than you found it
- Refactor in small, safe steps with tests as safety net
- Address code smells immediately, don't let tech debt accumulate
- Refactoring is not rewriting - preserve behavior while improving structure

### Programming Paradigms

**Structured Programming:**
- Sequential execution with control structures (if/else, loops, switch)
- Functions and procedures as organizational units
- Top-down decomposition of problems
- Appropriate for: scripts, automations, linear processing pipelines

**Object-Oriented Programming (OOP):**
- Encapsulation: data and behaviors united in classes, hide internal state
- Inheritance: reuse through hierarchies (use with GREAT caution, prefer composition)
- Polymorphism: same interface, multiple implementations
- Abstraction: hide complexity, expose only what's necessary
- Apply when: modeling complex domains, enterprise systems, stateful entities

**Functional Programming:**
- Immutability: data is never altered, only transformed
- Pure functions: same input = same output, no side effects
- Composition: small functions combined to create complex behaviors
- Higher-order functions: functions that receive/return functions
- Currying and partial application for reusable logic
- Apply when: data transformation, pipelines, pure domain logic, React components

---

## PILLAR 2: DESIGN PRINCIPLES

### SOLID Principles (Mandatory Application)

```
S - Single Responsibility Principle
    Each module/class has ONE single reason to change
    VIOLATION: UserService that authenticates, sends email and generates report
    CORRECT: AuthService, EmailService, ReportService separated

O - Open/Closed Principle
    Open for extension, closed for modification
    VIOLATION: giant switch/case that needs to be edited for each new type
    CORRECT: Strategy pattern or polymorphism for new behaviors

L - Liskov Substitution Principle
    Subtypes must be substitutable for their base types
    VIOLATION: Square extends Rectangle but breaks when setting width/height
    CORRECT: Segregated interfaces or composition

I - Interface Segregation Principle
    Clients should not depend on interfaces they don't use
    VIOLATION: IWorker interface with work() and eat() - robots don't eat
    CORRECT: IWorkable and IFeedable separated

D - Dependency Inversion Principle
    Depend on abstractions, not concrete implementations
    VIOLATION: OrderService instantiates MySQLRepository directly
    CORRECT: OrderService receives IOrderRepository via injection
```

### Essential Design Principles

**DRY (Don't Repeat Yourself):**
- Knowledge should have a single, authoritative representation
- Duplication of LOGIC is forbidden (copying validation code)
- Duplication of DATA is acceptable when necessary (denormalization)
- BUT: don't over-DRY - premature abstraction is worse than duplication

**KISS (Keep It Simple, Stupid):**
- The simplest solution that solves the problem is the correct one
- Complexity is only added when NECESSARY, not by anticipation
- Code cleverness is an antipattern - clarity always wins

**YAGNI (You Aren't Gonna Need It):**
- DO NOT implement features "for the future"
- DO NOT create abstractions for "flexibility" without real need
- Cost of maintaining unused code > cost of implementing later

**Composition over Inheritance:**
- Prefer composing objects via interfaces over class hierarchies
- Inheritance creates tight coupling and fragile base classes
- Composition enables flexible behavior mixing at runtime
- Use inheritance only for true "is-a" relationships (rare)
- In React: use hooks and composition, never inheritance

**Command Query Separation (CQS):**
- Commands: change state, return nothing (void)
- Queries: return data, change nothing (no side effects)
- A method should either command or query, NEVER both
- Exception: stack.pop() - but document the exception clearly

**Law of Demeter (Tell, Don't Ask):**
- An object should only talk to its immediate friends
- VIOLATION: `order.getCustomer().getAddress().getCity()` (train wreck)
- CORRECT: `order.getDeliveryCity()` - encapsulate the traversal
- Reduces coupling, improves encapsulation
- Each unit should have limited knowledge of other units

**Fail-Fast Design:**
- Detect and report errors as early as possible
- Validate inputs at system boundaries immediately
- Throw exceptions rather than propagating invalid state
- Use assertions for programming errors (invariants)
- Fail loudly in development, gracefully in production

**Hollywood Principle ("Don't call us, we'll call you"):**
- High-level modules define the flow, low-level modules plug in
- Framework calls your code, not the other way around
- Foundation of IoC containers and plugin architectures
- Event-driven systems naturally follow this principle

**GRASP (General Responsibility Assignment Software Patterns):**
```
Information Expert: assign responsibility to the class that has the data
Creator: assign creation to the class that has the initializing data
Controller: assign system events to a non-UI class (use case handler)
Low Coupling: minimize dependencies between classes
High Cohesion: keep related responsibilities together
Polymorphism: use polymorphism to handle type-based variations
Indirection: add intermediate objects to reduce direct coupling
Pure Fabrication: create service classes that don't represent domain concepts
Protected Variations: wrap instability behind stable interfaces
```

---

## PILLAR 3: DESIGN PATTERNS

### GoF Patterns

**Creational:**
- Factory Method: create objects without specifying concrete class
- Abstract Factory: families of related objects
- Builder: step-by-step construction of complex objects
- Singleton: single instance (use with GREAT caution - global state)
- Prototype: clone existing objects

**Structural:**
- Adapter: make incompatible interfaces compatible
- Bridge: separate abstraction from implementation
- Composite: treat individual and composite objects uniformly
- Decorator: add responsibilities dynamically
- Facade: simplified interface for complex subsystem
- Proxy: substitute/placeholder to control access
- Flyweight: share common state between objects to save memory

**Behavioral:**
- Strategy: family of interchangeable algorithms
- Observer: notification of state changes
- Command: encapsulate request as object (undo/redo, queuing)
- State: alter behavior based on state
- Template Method: algorithm skeleton with customizable steps
- Mediator: reduce chaotic dependencies via central coordinator
- Chain of Responsibility: pass requests along a chain of handlers
- Iterator: traverse collections without exposing internals
- Visitor: add operations to objects without changing their classes
- Memento: capture and restore object state (snapshots)

### Application Patterns

**Repository Pattern:**
- Abstraction layer between domain and data persistence
- Domain works with collections-like interface, not DB queries
- Enables swapping persistence mechanisms without domain changes
- Use for: any entity that needs persistence

**Unit of Work:**
- Track all changes in a business transaction
- Commit or rollback all changes atomically
- Coordinate writes across multiple repositories
- Use for: complex operations spanning multiple aggregates

**Specification Pattern:**
- Encapsulate business rules as composable objects
- Combine with AND, OR, NOT operators
- Use for: complex filtering, validation rules, query criteria

**Value Objects:**
- Immutable objects defined by their attributes, not identity
- Override equality by value (not reference)
- Examples: Money, Email, Address, DateRange
- Use for: any concept where identity doesn't matter, only value

**DTOs (Data Transfer Objects):**
- Simple objects for data transfer between layers/systems
- No business logic, only data
- Separate from domain entities - never expose domain entities directly
- Transform at boundaries: Entity <-> DTO

**Use Cases / Interactors:**
- One class per use case (application service)
- Orchestrate domain objects to fulfill a specific business operation
- Single entry point, clear input/output
- Use for: every application operation (CreateOrder, ProcessPayment, etc.)

**REPR (Request-Endpoint-Response):**
- Each API endpoint has its own Request, Handler, and Response types
- No shared DTOs between endpoints
- Minimal coupling between endpoints
- Use for: API design in vertical slice architectures

---

## PILLAR 4: ARCHITECTURAL STYLES & PATTERNS

### Fundamental Architectures

**Clean Architecture (Uncle Bob):**
```
Layers from outside to inside:
[Frameworks/Drivers] -> [Interface Adapters] -> [Use Cases] -> [Entities]

- Entities: enterprise business rules, independent of everything
- Use Cases: specific application rules, orchestrate entities
- Interface Adapters: data conversion between formats
- Frameworks: technical details (DB, Web, UI)

DEPENDENCY RULE: dependencies point only INWARD
Inner layers NEVER know about outer layers
```

**Hexagonal Architecture (Ports & Adapters):**
```
        [Primary Adapter: REST API, CLI, GraphQL]
                       |
                       v
[Adapter] -> [PORT] -> [DOMAIN] <- [PORT] <- [Adapter]
                       ^
                       |
        [Secondary Adapter: DB, Queue, Email]

- Domain: pure business logic, no external dependencies
- Ports: interfaces that the domain exposes/requires
- Primary Ports: driven by external actors (incoming)
- Secondary Ports: domain drives external systems (outgoing)
- Adapters: concrete implementations of ports
```

**Onion Architecture:**
```
Concentric layers:
[Infrastructure] -> [Application Services] -> [Domain Services] -> [Domain Model]

- Domain Model: entities and value objects at the center
- Domain Services: logic that doesn't belong to a single entity
- Application Services: orchestration, use cases
- Infrastructure: persistence, external APIs, UI
```

**Vertical Slice Architecture:**
```
Instead of horizontal layers, organize by FEATURE:

Feature A: [API -> Handler -> DB]
Feature B: [API -> Handler -> DB]
Feature C: [API -> Handler -> DB]

- Each slice is independent and self-contained
- Changes to one feature don't affect others
- Mix patterns per slice (simple CRUD vs complex DDD)
- IDEAL for: MVPs, rapid iteration, reducing coupling
- Combine with: CQRS, MediatR, feature folders
```

**Layered / N-Tier Architecture:**
```
[Presentation Layer]
        |
[Business Logic Layer]
        |
[Data Access Layer]
        |
[Database]

- Simple, well-understood pattern
- Each layer only communicates with adjacent layers
- Good starting point for most applications
- Risk: becomes coupled if layers leak abstractions
```

**MVC / MVVM:**
```
MVC (Model-View-Controller):
- Model: data and business logic
- View: presentation/UI
- Controller: handles input, updates model, selects view
- Use for: server-rendered web apps, traditional backends

MVVM (Model-View-ViewModel):
- Model: data and business logic
- View: UI (declarative binding)
- ViewModel: state + logic for the view
- Use for: React (hooks as ViewModel), mobile apps, SPAs
```

### Distributed Architectures

**Modular Monolith:**
```
Single deployment unit, BUT internally modular:

[Module A] [Module B] [Module C]
     \         |         /
      [Shared Kernel]
           |
      [Single DB]

- Modules communicate via well-defined interfaces (not direct DB access)
- Each module owns its domain and data
- Can extract to microservices later if needed
- BEST STARTING POINT for MVPs and SaaS

Benefits over pure monolith:
- Clear boundaries and encapsulation
- Easier to reason about and test
- Natural migration path to microservices
```

**Microservices:**
```
- Independent services per bounded context
- Database per service (mandatory)
- Communication via network (sync/async)

Advantages:
- Granular scalability, independent deploy
- Autonomous teams per service
- Heterogeneous technology possible

Disadvantages:
- MUCH greater operational complexity
- Distributed debugging is difficult
- Eventual consistency (CAP theorem)
- Network overhead and latency

USE WHEN: Real scale needed, large teams, complex domains
NEVER START WITH MICROSERVICES - extract from mature monolith/modular monolith
```

**Service Oriented Architecture (SOA):**
```
- Enterprise-level service organization
- Services communicate via ESB (Enterprise Service Bus)
- Heavier than microservices, more governance
- Use when: large enterprise integration, legacy modernization
```

**Event-Driven Architecture:**
```
Patterns:
- Event Notification: notify that something happened
- Event-Carried State Transfer: event contains all data needed
- Event Sourcing: persist events as source of truth, derive state
- CQRS: separate read/write models

Advantages:
- Temporal and spatial decoupling
- Natural scalability, audit and replay
- Loose coupling between components

Disadvantages:
- Eventual consistency mandatory
- More complex debugging, event ordering is challenging
```

**Serverless Architecture:**
```
- Functions as a Service (FaaS): AWS Lambda, Vercel Functions, Cloudflare Workers
- Backend as a Service (BaaS): Firebase, Supabase, Neon
- Zero infrastructure management
- Auto-scaling from zero to massive

Advantages:
- No server management, pay-per-execution
- Infinite scalability, fast time to market
- IDEAL for MVPs and Micro-SaaS

Disadvantages:
- Cold start latency
- Vendor lock-in
- Limited execution time and memory
- Complex local development/testing

Use for: APIs, webhooks, scheduled jobs, data processing
```

**BFF (Backend for Frontend):**
```
[Web App] -> [BFF Web] ----\
[Mobile]  -> [BFF Mobile] ---> [Microservices]
[Admin]   -> [BFF Admin] ---/

- Dedicated backend per frontend type
- Each BFF tailored to its client's needs
- Aggregates calls to downstream services
- Use when: multiple clients with different data needs
```

### Domain-Driven Design (DDD)

```
STRATEGIC DDD:

Ubiquitous Language:
- Shared vocabulary between devs and domain experts
- Code uses the SAME terms as the business
- No translation layer - if business says "Order", code has Order class

Bounded Contexts:
- Explicit boundaries where a model applies
- Same term can mean different things in different contexts
- "Product" in Catalog vs "Product" in Shipping = different models
- Each context has its own model, its own database (ideally)

Context Mapping:
- Shared Kernel: two contexts share a subset
- Customer/Supplier: upstream provides, downstream consumes
- Conformist: downstream conforms to upstream model
- Anti-Corruption Layer: translates between contexts
- Open Host Service: well-defined protocol for integration
- Published Language: shared schema (JSON Schema, Protobuf)

TACTICAL DDD:

Entities:
- Objects with identity that persists through state changes
- Equality by ID, not by attributes
- Example: User, Order, Product

Value Objects:
- Immutable, equality by value
- No identity - defined entirely by attributes
- Example: Money(100, "BRL"), Email("user@test.com"), Address

Aggregates:
- Cluster of entities and value objects with consistency boundary
- One entity is the Aggregate Root (entry point)
- External references only to the root, never internal entities
- Transactions align with aggregate boundaries
- Keep aggregates SMALL

Domain Events:
- Something meaningful that happened in the domain
- Named in past tense: OrderPlaced, PaymentProcessed, UserRegistered
- Immutable records of facts
- Enable loose coupling between bounded contexts

Domain Services:
- Logic that doesn't naturally belong to any entity
- Stateless operations involving multiple entities
- Example: PricingService, TransferService

Repositories:
- Persistence abstraction for aggregates
- One repository per aggregate root
- Collection-like interface (find, save, delete)

Factories:
- Complex aggregate creation logic
- Ensure aggregates are created in valid state
```

### Architectural Patterns

**CQRS (Command Query Responsibility Segregation):**
```
[Commands] -> [Write Model] -> [Write DB]
                                    |
                              [Projection/Sync]
                                    |
[Queries]  -> [Read Model]  -> [Read DB]

- Separate models optimized for read and write
- Write model: normalized, consistent, domain-rich
- Read model: denormalized, fast, query-optimized
- Can use different databases for each side
- Use for: systems with high read/write ratio disparity, complex domains
- Combine with: Event Sourcing, Domain Events
```

**Event Sourcing:**
```
Traditional: Store current STATE in database
Event Sourcing: Store EVENTS that led to current state

Events: [OrderCreated] -> [ItemAdded] -> [ItemAdded] -> [OrderPaid]
State:  Replay events to derive current state

Advantages:
- Complete audit trail
- Time travel (rebuild state at any point)
- Event replay for projections and analytics
- Natural fit with CQRS

Disadvantages:
- Eventual consistency
- Event schema evolution is complex
- Storage grows indefinitely (need snapshots)

Use for: financial systems, audit-critical domains, complex state machines
```

**Saga Pattern:**
```
Distributed transactions across services without 2PC:

Choreography (event-based):
[Service A] -event-> [Service B] -event-> [Service C]
Each service listens and reacts, publishes compensating events on failure

Orchestration (coordinator-based):
[Saga Orchestrator] -> [Service A]
                    -> [Service B]
                    -> [Service C]
Central coordinator manages the flow and compensations

Use Choreography when: few steps, simple flow
Use Orchestration when: many steps, complex flow, visibility needed
```

**Outbox / Inbox Pattern:**
```
Problem: ensure event publishing + DB write are atomic

Outbox Pattern:
1. Write entity + event to SAME database (same transaction)
2. Background process reads outbox table and publishes events
3. Mark events as published

Inbox Pattern:
1. Consumer writes received event to inbox table
2. Process inbox idempotently
3. Prevents duplicate processing

Use for: reliable event publishing in distributed systems
```

---

## PILLAR 5: SYSTEM DESIGN & SCALABILITY

### Core Concepts

**CAP Theorem:**
```
In a distributed system, you can only guarantee 2 of 3:

C - Consistency: every read receives the most recent write
A - Availability: every request receives a response
P - Partition Tolerance: system works despite network failures

In practice, P is non-negotiable, so you choose:
- CP: Consistency + Partition Tolerance (banking, inventory)
  Examples: MongoDB, Redis, HBase
- AP: Availability + Partition Tolerance (social media, caching)
  Examples: Cassandra, CouchDB, DynamoDB

PACELC Extension:
If Partition -> choose A or C
Else (normal operation) -> choose Latency or Consistency
```

**Consistency Patterns:**
```
Strong Consistency:
- All nodes see the same data at the same time
- Higher latency, lower throughput
- Use for: financial transactions, inventory

Eventual Consistency:
- All nodes will eventually converge to same state
- Lower latency, higher throughput
- Use for: social feeds, analytics, notifications

Read-Your-Writes Consistency:
- User always sees their own writes
- Others may see stale data temporarily
- Good compromise for user-facing applications
```

**Availability Patterns:**
```
99.9% (Three Nines): ~8.7 hours downtime/year
99.99% (Four Nines): ~52 minutes downtime/year
99.999% (Five Nines): ~5 minutes downtime/year

Strategies:
- Active-Passive Failover: standby takes over on failure
- Active-Active: multiple nodes handle traffic simultaneously
- Multi-Region: deploy across geographic regions
- Health checks + Auto-healing
```

**Performance Metrics:**
```
Latency: time to process a single request (p50, p95, p99)
Throughput: number of requests processed per time unit
Scalability: ability to handle increased load
Bandwidth: maximum data transfer rate

Scalability Types:
- Vertical (Scale Up): more CPU/RAM (limited, requires downtime)
- Horizontal (Scale Out): more instances (unlimited, needs stateless)
PREFER HORIZONTAL - design for scale out from day one
```

### System Components

**Load Balancers:**
```
Layer 4 (Transport):
- Routes based on IP and port
- Faster, less flexible
- Cannot inspect HTTP headers/content
- Use for: TCP/UDP traffic, raw performance

Layer 7 (Application):
- Routes based on HTTP headers, URL, cookies
- Can do SSL termination, compression, caching
- Content-based routing
- Use for: HTTP traffic, path-based routing, A/B testing

Algorithms:
- Round Robin: sequential distribution
- Least Connections: send to least busy server
- IP Hash: same client always on same server (sticky sessions)
- Weighted: servers with different capacities
- Least Response Time: fastest server gets next request

Tools: NGINX, HAProxy, AWS ALB/NLB, Cloudflare
```

**CDN (Content Delivery Networks):**
```
- Cache static content at edge locations worldwide
- Reduce latency for geographically distributed users
- Offload origin server traffic
- DDoS protection at the edge

Cache Strategy:
- Static assets (JS, CSS, images): long TTL, cache-bust with hashes
- API responses: short TTL or no cache
- HTML pages: varies (SSG = cache, SSR = no cache or short TTL)

Providers: Cloudflare, AWS CloudFront, Vercel Edge, Fastly
```

**DNS & Reverse Proxy:**
```
DNS:
- Domain name resolution
- DNS-based load balancing (round robin, geolocation)
- TTL management for failover
- Use Route53, Cloudflare DNS

Reverse Proxy:
- Sits between client and servers
- SSL termination, compression, caching
- Request routing, rate limiting
- Hide internal infrastructure
- Tools: NGINX, Traefik, Caddy
```

**Caching Strategies:**
```
Cache-Aside (Lazy Loading):
- App checks cache first, on miss fetches from DB and populates cache
- Most common pattern, simple to implement
- Risk: cache stampede on cold cache

Read-Through:
- Cache itself fetches from DB on miss
- Simpler app code, cache manages loading

Write-Through:
- Write to cache AND DB synchronously
- Consistent but slower writes

Write-Behind (Write-Back):
- Write to cache, async write to DB
- Fast writes, risk of data loss

Cache Invalidation Strategies:
- TTL (Time To Live): simplest, eventually consistent
- Event-based: invalidate on write events
- Version-based: cache key includes version number

Tools: Redis, Memcached, Vercel KV, Upstash
```

**Message Queues & Event Streaming:**
```
RabbitMQ:
- Traditional broker with AMQP
- Exchanges, Queues, Bindings
- Strong delivery guarantees
- Use for: task queues, RPC, simple pub/sub

Apache Kafka:
- Distributed log, not traditional queue
- Configurable message retention
- Consumer groups for parallelism
- Use for: event streaming, data pipelines, event sourcing

NATS:
- Lightweight, high-performance
- Simple pub/sub and request/reply
- JetStream for persistence
- Use for: microservices communication, IoT

Amazon SQS:
- Managed serverless queue
- Standard (at-least-once) vs FIFO (exactly-once)
- Use for: simple decoupling in AWS

BullMQ (Node.js):
- Redis-based queue for Node.js
- Job scheduling, retries, priorities
- Use for: background jobs in Node.js/Next.js apps
```

**Databases:**
```
SQL (Relational):
- Rigid schema, ACID transactions
- Complex queries with JOINs
- Use for: structured data, financial, referential integrity
- Examples: PostgreSQL, MySQL, PlanetScale, Neon

NoSQL Document (MongoDB, Firestore):
- Flexible JSON documents
- Use for: product catalogs, CMS, user profiles

Key-Value (Redis, DynamoDB):
- Access by key, extremely fast
- Use for: cache, sessions, rate limiting

Column-Family (Cassandra, ScyllaDB):
- Optimized for massive writes
- Use for: time-series, IoT, analytics

Graph (Neo4j, Neptune):
- Nodes and edges as first-class citizens
- Use for: social networks, recommendations, fraud detection

Scaling Strategies:
- Replication: primary-replica for read scaling
- Sharding: horizontal partitioning across servers
- Federation: split by function (users DB, orders DB)
- Denormalization: duplicate data for read performance
```

**API Styles:**
```
REST:
- Stateless, resources via URLs
- HTTP verbs (GET, POST, PUT, DELETE)
- Simple, widely supported, cacheable
- Use for: public APIs, simple CRUD, general purpose

GraphQL:
- Client defines response shape
- Single endpoint, no over/under fetching
- Subscriptions for real-time
- Use for: complex frontends, mobile (bandwidth), BFF

gRPC:
- Protocol Buffers (binary), HTTP/2
- Bidirectional streaming, strong typing
- Code generation for multiple languages
- Use for: internal service-to-service communication

WebSockets:
- Persistent bidirectional connection
- Low latency real-time communication
- Use for: chat, games, live updates, collaborative editing

Server-Sent Events (SSE):
- Server-to-client one-directional stream
- Simpler than WebSockets for one-way data
- Use for: notifications, live feeds, AI streaming responses

tRPC:
- End-to-end type safety between client and server
- No schema generation or code gen needed
- Use for: TypeScript full-stack apps, Next.js
```

**Service Discovery & Service Mesh:**
```
Service Discovery:
- Services find each other dynamically
- Registry: Consul, etcd, Eureka
- DNS-based: Kubernetes DNS
- Client-side vs Server-side discovery

Service Mesh:
- Infrastructure layer for service-to-service communication
- Handles: mTLS, load balancing, observability, retries
- Sidecar proxy pattern (Envoy)
- Tools: Istio, Linkerd, Consul Connect
- Use when: many microservices need consistent cross-cutting concerns
```

### Cloud Design Patterns

```
Resilience Patterns:
- Circuit Breaker: prevent cascade failures (Closed -> Open -> Half-Open)
- Bulkhead: isolate resources per component (separate thread/connection pools)
- Retry with Exponential Backoff: retry with increasing wait + jitter
- Timeout: ALWAYS define timeouts on external calls
- Throttling/Rate Limiting: protect services from overload

Migration Patterns:
- Strangler Fig: incrementally replace legacy system piece by piece
- Anti-Corruption Layer: translate between old and new models
- Branch by Abstraction: switch implementations behind interface

Structural Patterns:
- Ambassador: offload cross-cutting concerns to proxy
- Sidecar: deploy helper components alongside main service
- Gateway Aggregation: aggregate multiple service calls into one
- Gateway Routing: route requests to appropriate services

Data Patterns:
- Outbox: reliable event publishing with DB transaction
- Inbox: idempotent event consumption
- Saga: distributed transactions via choreography or orchestration
- CQRS: separate read and write models
- Materialized View: pre-computed read-optimized views
```

---

## PILLAR 6: DEVOPS & CLOUD

### Containers

```
Docker:
- Package application with all dependencies
- Consistent environment across dev/staging/production
- Dockerfile: declarative image definition
- Multi-stage builds to minimize image size
- Best practices:
  - Use specific base image versions (not :latest)
  - Minimize layers, use .dockerignore
  - Run as non-root user
  - Scan for vulnerabilities (Trivy, Snyk)

Docker Compose:
- Define multi-container applications
- Local development environment
- Service dependencies and networking
- Use for: local dev with DB, Redis, queues
```

### Orchestration

```
Kubernetes (K8s):
- Container orchestration at scale
- Deployments, Services, Ingress, ConfigMaps, Secrets
- Auto-scaling (HPA), self-healing, rolling updates
- Helm charts for package management
- Use when: multiple services, need auto-scaling, production-grade

Simpler Alternatives:
- Docker Compose + Swarm: small-scale deployments
- Railway, Render, Fly.io: managed container platforms
- Vercel/Netlify: serverless for Next.js/React
- AWS ECS/Fargate: managed containers on AWS

RULE: Don't use K8s for a single service. Match orchestration to complexity.
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
- Use when: team prefers TypeScript over HCL

SST (Serverless Stack):
- IaC for serverless on AWS
- Built for Next.js, Remix, Astro
- Live Lambda Development
- Use for: serverless full-stack apps

RULE: ALL infrastructure must be in code. No manual console clicks in production.
```

### CI/CD Pipelines

```
Pipeline Stages:
1. Lint & Format: ESLint, Prettier, Biome
2. Type Check: tsc --noEmit
3. Unit Tests: fast, isolated
4. Build: compile and bundle
5. Integration Tests: with real dependencies
6. Security Scan: dependency vulnerabilities
7. Deploy to Staging: automatic
8. E2E Tests: against staging
9. Deploy to Production: manual gate or auto

Tools:
- GitHub Actions: most common for GitHub repos
- GitLab CI: built into GitLab
- CircleCI, Jenkins: enterprise
- Vercel/Netlify: auto-deploy on push

Best Practices:
- Fast feedback: lint + unit tests < 5 minutes
- Branch protection: require passing CI for merge
- Trunk-based development: short-lived feature branches
- Feature flags for gradual rollout
```

### Monitoring & Observability

```
Three Pillars of Observability:

1. Logging:
   - Structured logs (JSON format)
   - Log levels: ERROR, WARN, INFO, DEBUG
   - Correlation IDs for request tracing
   - Tools: Pino, Winston + ELK Stack, Loki, Datadog

2. Metrics:
   - Request rate, error rate, latency (RED method)
   - Saturation: CPU, memory, disk, connections
   - Business metrics: signups, conversions, revenue
   - Tools: Prometheus, Grafana, Datadog, New Relic

3. Distributed Tracing:
   - Follow a request across services
   - Identify bottlenecks and slow dependencies
   - Tools: OpenTelemetry, Jaeger, Zipkin, Datadog APT

Alerting:
- Alert on symptoms, not causes
- Actionable alerts only (no noise)
- Escalation policies and on-call rotation
- Tools: PagerDuty, OpsGenie, Grafana Alerting

Health Checks:
- Liveness: is the process alive?
- Readiness: can the service handle traffic?
- Startup: has the service finished initializing?
```

---

## PILLAR 7: SECURITY & RESILIENCE

### Authentication & Authorization

```
OAuth 2.0:
- Authorization framework for third-party access
- Grant types: Authorization Code, Client Credentials, Device Code
- Access tokens (short-lived) + Refresh tokens (long-lived)
- PKCE extension for public clients (SPAs, mobile)

OpenID Connect (OIDC):
- Identity layer on top of OAuth 2.0
- ID token (JWT) with user identity claims
- Standard scopes: openid, profile, email
- Use for: "Login with Google/GitHub/etc."

JWT (JSON Web Tokens):
- Stateless authentication tokens
- Header.Payload.Signature
- NEVER store secrets in JWT payload (it's base64, not encrypted)
- Short expiration + refresh token rotation
- Verify signature server-side, validate claims (exp, iss, aud)

Session-Based Auth:
- Server stores session state
- Cookie with session ID
- Use for: traditional web apps, when you need server-side revocation

Auth Providers (recommended for MVPs):
- Clerk, Auth0, Supabase Auth, NextAuth.js/Auth.js
- DON'T build auth from scratch unless you have specific requirements
```

### API Security

```
Best Practices:
- HTTPS everywhere (TLS 1.3)
- Rate limiting per user/IP
- Input validation and sanitization (Zod, Joi)
- CORS configuration (whitelist specific origins)
- Helmet.js for HTTP security headers
- SQL injection prevention (parameterized queries, ORMs)
- XSS prevention (Content Security Policy, output encoding)
- CSRF protection (SameSite cookies, CSRF tokens)

API Authentication:
- API Keys: simple, for server-to-server
- Bearer tokens (JWT): for user authentication
- OAuth 2.0: for third-party integrations
- HMAC signatures: for webhooks verification

Secrets Management:
- NEVER commit secrets to code
- Environment variables for configuration
- Key Vault / Secrets Manager for sensitive data
- Rotate secrets regularly
- Tools: AWS Secrets Manager, Vault, Doppler, Infisical
```

### Idempotency

```
Definition: same operation applied multiple times = same result

Critical for:
- Payment processing (charge exactly once)
- API retries (network failures)
- Event handlers (at-least-once delivery)

Implementation Strategies:
- Idempotency key: client sends unique key per request
- Database unique constraints: prevent duplicate writes
- Conditional updates: UPDATE WHERE version = X
- Inbox pattern: track processed event IDs

HTTP Methods:
- GET, PUT, DELETE: naturally idempotent
- POST: NOT idempotent - needs explicit idempotency mechanism
```

### Distributed Systems Safety

```
Distributed Locking:
- Prevent concurrent access to shared resources
- Redis-based locks (Redlock algorithm)
- Database advisory locks
- Lease-based locks with TTL (prevent deadlocks)
- Use sparingly - prefer idempotent designs

Distributed Transactions:
- 2PC (Two-Phase Commit): coordinator-based, blocking (avoid when possible)
- Saga Pattern: compensating transactions (preferred)
- Outbox Pattern: reliable event publishing
- Eventual consistency: embrace it, don't fight it

High Availability Patterns:
- No single point of failure
- Graceful degradation: serve partial functionality when components fail
- Chaos engineering: intentionally break things to find weaknesses
- Circuit breaker + fallback: return cached/default data on failure
```

---

## PILLAR 8: QUALITY, TESTING & MODELING

### Testing Strategy

```
Test Pyramid:
         /  E2E  \        <- Few, slow, expensive
        / Integration \    <- Moderate amount
       /    Unit Tests  \  <- Many, fast, cheap

Unit Tests:
- Test a single unit in isolation
- Mock external dependencies
- FAST (< 1ms per test)
- Use for: business logic, utility functions, domain models

Integration Tests:
- Test interaction between components
- Real database, real API calls (test containers)
- Moderate speed (< 5s per test)
- Use for: repositories, API endpoints, middleware

End-to-End Tests:
- Test complete user flows
- Real browser, real backend
- Slow but high confidence
- Use for: critical paths (signup, checkout, payment)
- Tools: Playwright, Cypress
```

**F.I.R.S.T. Principles:**
```
F - Fast: tests run quickly, encourage frequent execution
I - Independent: tests don't depend on each other or execution order
R - Repeatable: same result every time, in any environment
S - Self-Validating: pass or fail, no manual inspection needed
T - Timely: written before or with the code, not after
```

### Code Review Best Practices

```
What to Review:
- Correctness: does it solve the problem?
- Design: is the approach appropriate?
- Readability: can others understand it easily?
- Security: any vulnerabilities introduced?
- Performance: any obvious bottlenecks?
- Tests: adequate coverage for changes?

How to Review:
- Review in < 400 lines of code per session
- Be constructive, suggest alternatives
- Distinguish between blocking and nit-pick comments
- Automate what can be automated (lint, format, types)
```

### Anti-Patterns to Avoid

```
ARCHITECTURE:
- Big Ball of Mud: system without clear structure
- Distributed Monolith: worst of both worlds
- Golden Hammer: use same solution for everything
- Premature Optimization: optimize before measuring
- Resume Driven Development: choose tech for CV
- Accidental Complexity: complexity without business value

CODE:
- God Class/Object: class that does everything
- Spaghetti Code: impossible to follow flow
- Copy-Paste Programming: duplication without abstraction
- Magic Numbers/Strings: unexplained literals
- Deep Nesting: more than 3 levels
- Leaky Abstractions: implementation details leaking through interface
- Static Cling: hard coupling to static methods
- Primitive Obsession: using primitives instead of value objects
- Feature Envy: method uses data from another class more than its own
- Shotgun Surgery: one change requires modifications in many places

INFRASTRUCTURE:
- Single Point of Failure
- Hardcoded Configurations
- No Monitoring/Alerting
- No Backup Strategy
- Credentials in Code
```

### Domain Modeling Techniques

```
Event Storming:
- Workshop technique for domain discovery
- Orange sticky notes = Domain Events (past tense)
- Blue sticky notes = Commands (actions that trigger events)
- Yellow sticky notes = Actors/Users
- Pink sticky notes = External Systems
- Purple sticky notes = Policies (reactive logic)
- Result: bounded contexts, aggregates, event flows

Event Modeling:
- Visual blueprint of the entire system
- Timeline of events from left to right
- Shows: commands -> events -> read models
- Four patterns: entry, automation, translation, view

Domain Storytelling:
- Pictographic language for domain narratives
- Actors, work objects, activities
- Sequential numbering of interactions
- Great for discovering ubiquitous language

C4 Model (Diagrams):
- Context: system + external actors
- Container: applications, databases, queues
- Component: modules within a container
- Code: classes and interfaces (optional)

Entity Relationship Diagrams (ERD):
- Entities, attributes, relationships
- Cardinalities (1:1, 1:N, N:N)
- Essential for database design
```

---

## PILLAR 9: MODULARIZATION & FRONTEND ARCHITECTURE

### React / Next.js Architecture

```
Feature-Based Folder Structure (recommended):
src/
├── app/                    # Next.js App Router pages
│   ├── (auth)/            # Route groups for layouts
│   ├── (dashboard)/
│   └── api/               # API routes
├── features/              # Feature modules (core of the app)
│   ├── auth/
│   │   ├── components/    # Feature-specific components
│   │   ├── hooks/         # Feature-specific hooks
│   │   ├── actions/       # Server actions
│   │   ├── schemas/       # Zod validation schemas
│   │   ├── types/         # Feature types
│   │   └── utils/         # Feature utilities
│   ├── billing/
│   ├── dashboard/
│   └── settings/
├── shared/                # Shared across features
│   ├── components/        # Reusable UI components
│   │   ├── ui/           # Primitive UI (Button, Input, Card)
│   │   └── layouts/      # Layout components
│   ├── hooks/            # Shared hooks
│   ├── lib/              # Shared utilities (db, auth, api clients)
│   ├── types/            # Global types
│   └── constants/        # Global constants
└── styles/               # Global styles
```

**Component Architecture:**
```
Component Hierarchy:
1. Pages (app/): route entry points, data fetching (Server Components)
2. Features (features/): business logic, stateful components
3. Shared Components (shared/): reusable, business-agnostic

Rules:
- Features can import from shared/, NEVER from other features
- Shared components are generic, no business logic
- Server Components by default, Client Components only when needed
- Colocation: keep related files together in features
- One component per file, file name = component name
```

**State Management:**
```
Local State:
- useState/useReducer for component state
- Form state: React Hook Form + Zod

Server State:
- Next.js Server Components (preferred for Next.js)
- TanStack Query (React Query) for client-side data fetching
- SWR for simple cases
- NEVER manually sync server state with client state

Global Client State:
- Zustand: simple, minimal boilerplate (recommended)
- Jotai: atomic state management
- Context API: for small, rarely-changing state (theme, locale)
- AVOID Redux unless complex state machines are needed

URL State:
- nuqs or next-usequerystate for search params
- Use URL as single source of truth for filters, pagination, sorting
```

**Server Components vs Client Components (Next.js):**
```
Server Components (default):
- Render on server, zero JS sent to client
- Direct database/API access
- Use for: data fetching, static content, layouts
- Can import Client Components

Client Components ('use client'):
- Render on client, interactive
- useState, useEffect, event handlers
- Use for: interactivity, browser APIs, third-party client libs
- CANNOT import Server Components (pass as children)

Pattern: Server Component fetches data, passes to Client Component as props
```

### Monorepo Architecture

```
Monorepo Structure (Turborepo recommended):
monorepo/
├── apps/
│   ├── web/               # Main Next.js app
│   ├── admin/             # Admin dashboard
│   ├── mobile/            # React Native app
│   └── docs/              # Documentation site
├── packages/
│   ├── ui/                # Shared component library
│   ├── database/          # Prisma schema + client
│   ├── auth/              # Shared auth logic
│   ├── email/             # Email templates + sending
│   ├── config-eslint/     # Shared ESLint config
│   ├── config-typescript/ # Shared TS config
│   └── utils/             # Shared utilities
├── turbo.json             # Turborepo pipeline config
├── package.json           # Root workspace config
└── pnpm-workspace.yaml    # pnpm workspaces

Tools:
- Turborepo: build system, caching, task orchestration
- pnpm workspaces: dependency management
- Changesets: versioning and changelogs

Rules:
- packages/ are LIBRARIES (no app-specific logic)
- apps/ are APPLICATIONS (can depend on packages)
- Shared packages have clear, minimal APIs
- Each package has its own tsconfig, eslint config
- Remote caching for CI speed (Vercel Remote Cache)
```

### Module Boundaries & Dependency Rules

```
Dependency Direction:
app/ -> features/ -> shared/ -> packages/

NEVER:
- Feature importing from another feature directly
- Shared importing from features
- Circular dependencies between modules

Communication Between Features:
- Via shared state (Zustand store)
- Via URL state (query params)
- Via events (custom events or event emitter)
- Via parent component props (composition)

Barrel Exports (index.ts):
- Each feature/module exports only its public API
- Internal implementation is private
- Makes refactoring safe within module boundaries
- Example: features/auth/index.ts exports only AuthForm, useAuth, etc.
```

### Performance Patterns (Frontend)

```
Code Splitting:
- Dynamic imports: next/dynamic or React.lazy
- Route-based splitting (automatic in Next.js)
- Component-based splitting for heavy components

Rendering Strategies (Next.js):
- SSG (Static Site Generation): build-time rendering, CDN cached
- SSR (Server-Side Rendering): request-time rendering
- ISR (Incremental Static Regeneration): SSG + revalidation
- PPR (Partial Prerendering): static shell + dynamic holes
- Streaming: progressive rendering with Suspense

Image Optimization:
- next/image for automatic optimization
- WebP/AVIF formats, responsive sizes
- Lazy loading below-the-fold images
- Blur placeholder for perceived performance

Bundle Optimization:
- Analyze with @next/bundle-analyzer
- Tree shaking: use named imports
- Avoid barrel file re-exports for large libraries
- External heavy dependencies (dayjs over moment)
```

---

## PRACTICAL APPLICATION

When receiving any software task, this skill automatically applies:

1. **Clean Code Analysis:** Does the code follow clean code principles? Meaningful names? Small functions? Low complexity?

2. **Design Principles Check:** SOLID compliance? Correct application of DRY/KISS/YAGNI? Proper separation of concerns?

3. **Pattern Selection:** Appropriate design patterns for the problem? Not over-engineered? Not under-designed?

4. **Architecture Evaluation:** Adequate architectural style for the context? Well-defined boundaries? Correct communication patterns?

5. **DDD Alignment:** Are bounded contexts identified? Aggregates correctly defined? Ubiquitous language in use?

6. **System Design Review:** Scalable? Resilient? Available? Correct data storage? Appropriate caching?

7. **Security Assessment:** Authentication/authorization correct? Input validation? Secrets management? OWASP top 10 addressed?

8. **Testing Strategy:** Adequate test coverage? Right types of tests? F.I.R.S.T. principles followed?

9. **Modularization Check:** Feature boundaries clear? Dependency rules respected? Component architecture sound?

10. **Clear Communication:** Document decisions with justifications and trade-offs via ADRs when appropriate

---

## DECISION FRAMEWORK FOR MVPs & SaaS

```
Starting a new MVP/Micro-SaaS:

Architecture: Modular Monolith or Serverless (Next.js + Vercel)
Database: PostgreSQL (Neon/Supabase) or PlanetScale
ORM: Prisma or Drizzle
Auth: Clerk or NextAuth.js
Payments: Stripe
Email: Resend
Queue: Inngest or BullMQ (if needed)
Cache: Upstash Redis (if needed)
Monitoring: Vercel Analytics + Sentry
CI/CD: GitHub Actions + Vercel auto-deploy

Scale Evolution Path:
1. MVP: Next.js monolith on Vercel
2. Growth: Add caching, optimize queries, background jobs
3. Scale: Extract hot paths to separate services
4. Enterprise: Microservices (only if truly needed)

NEVER over-architect an MVP. Ship fast, iterate based on real data.
BUT: maintain clean boundaries so scaling is possible later.
```

---

## CODE STYLE RULES

### General Principles

- **Early return pattern**: Always use early returns instead of nested conditions
- Avoid duplication through reusable functions and modules
- Decompose long components/functions (>80 lines) into smaller units
- Files with more than 200 lines should be split
- Prefer arrow functions when possible
- Use TypeScript strict mode always
- Prefer `const` over `let`, never use `var`

### Library-First Approach

- **ALWAYS search for existing solutions before custom code**
- Evaluate npm libraries, SaaS services, third-party APIs
- Custom code only for: unique business logic, performance-critical paths, special security requirements

### Code Quality

- Error handling with typed catch blocks
- Maximum 3 levels of nesting
- Focused functions, less than 50 lines when possible
- Focused files, less than 200 lines when possible
- Use Zod for runtime validation at boundaries
- Prefer composition and hooks over inheritance
