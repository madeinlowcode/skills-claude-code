# Code Review Checklist

## Table of Contents
1. [Review Process](#review-process)
2. [Technical Checklist](#technical-checklist)
3. [Feedback Guidelines](#feedback-guidelines)
4. [Common Review Comments](#common-review-comments)
5. [Review Templates](#review-templates)

---

## Review Process

### Before Starting Review

```
PRE-REVIEW CHECKLIST:
[ ] Read the PR description and linked tickets
[ ] Understand the business context
[ ] Check if tests pass in CI
[ ] Note the scope (how many files/lines changed)
[ ] Allocate appropriate time based on complexity
```

### Review Order

```
1. HIGH-LEVEL PASS (5 min)
   - Does the approach make sense?
   - Does it fit the architecture?
   - Are there any red flags?

2. DETAILED REVIEW (variable)
   - Walk through the code logically
   - Start from entry point, follow the flow
   - Review tests alongside implementation

3. FINAL PASS (5 min)
   - Edge cases covered?
   - Error handling complete?
   - Documentation updated?
```

### Review Priorities

```
MUST ADDRESS (Block approval):
- Security vulnerabilities
- Data loss risks
- Breaking changes without migration
- Incorrect business logic
- Missing critical tests

SHOULD ADDRESS (Strong suggestion):
- Performance concerns
- Missing error handling
- Code duplication
- Unclear naming

COULD ADDRESS (Nice to have):
- Style preferences
- Minor optimizations
- Alternative approaches
- Documentation improvements
```

---

## Technical Checklist

### Correctness

```
[ ] Does the code do what the PR claims?
[ ] Are edge cases handled?
[ ] Are error conditions handled?
[ ] Are there any off-by-one errors?
[ ] Are null/undefined cases handled?
[ ] Does it handle empty collections?
[ ] Are async operations awaited properly?
[ ] Are race conditions possible?
```

### Security

```
[ ] Input validation present?
[ ] No SQL injection vulnerabilities?
[ ] No XSS vulnerabilities?
[ ] Authentication/authorization checked?
[ ] Sensitive data not logged?
[ ] Secrets not hardcoded?
[ ] HTTPS used for sensitive data?
[ ] Rate limiting for public endpoints?
```

### Performance

```
[ ] No N+1 query patterns?
[ ] Appropriate indexing considered?
[ ] Large data sets paginated?
[ ] Expensive operations cached?
[ ] No unnecessary database calls in loops?
[ ] Memory usage reasonable?
[ ] No blocking operations in async code?
```

### Testing

```
[ ] Unit tests for new logic?
[ ] Edge cases tested?
[ ] Error conditions tested?
[ ] Integration tests for API changes?
[ ] Test names clearly describe scenarios?
[ ] Tests are independent (no shared state)?
[ ] No flaky test patterns?
```

### Code Quality

```
[ ] Follows project conventions?
[ ] No code duplication?
[ ] Functions are focused (single responsibility)?
[ ] No deep nesting (>3 levels)?
[ ] Clear naming for variables/functions?
[ ] Magic numbers explained or named?
[ ] Complex logic has comments?
```

### Design

```
[ ] Fits with existing architecture?
[ ] Appropriate abstractions?
[ ] Dependencies injected (testable)?
[ ] Changes are backward compatible?
[ ] API changes documented?
[ ] Database migrations reversible?
```

---

## Feedback Guidelines

### Writing Good Comments

```
STRUCTURE:
[Category] [Issue] + [Reason] + [Suggestion]

CATEGORIES:
- [Blocker]: Must fix before merge
- [Major]: Should fix, or explain why not
- [Minor]: Nice to have
- [Question]: Seeking clarification
- [Praise]: Something done well
- [Nitpick]: Style preference only

EXAMPLES:

[Blocker] This SQL query is vulnerable to injection.
Use parameterized queries instead of string concatenation.
```sql
// Instead of: `SELECT * FROM users WHERE id = ${id}`
await db.query('SELECT * FROM users WHERE id = $1', [id])
```

[Major] This could cause an N+1 query problem.
Consider eager loading the relationships:
```javascript
// Instead of: Order.findAll() then loop to get Customer
Order.findAll({ include: [Customer] })
```

[Minor] Consider extracting this into a named constant
for clarity: `const MAX_RETRY_ATTEMPTS = 3;`

[Question] What happens if `userData` is null here?

[Praise] Great use of the builder pattern here!
This makes the tests very readable.

[Nitpick] I'd prefer `getUserById` over `getUser` for
clarity, but this is just personal preference.
```

### Tone Guidelines

```
DO:
- Use "we" instead of "you" ("We should add tests here")
- Ask questions ("What happens if...?")
- Offer alternatives ("Consider using X because...")
- Acknowledge trade-offs ("I see why you did it this way, but...")
- Praise good solutions ("Nice approach!")

DON'T:
- Be condescending ("Obviously you should...")
- Use absolutist language ("Never do this")
- Make personal attacks ("This is lazy")
- Leave vague feedback ("This is wrong")
- Nitpick excessively (automate style with linters)
```

### Asking for Clarification

```
GOOD QUESTIONS:
"Can you help me understand why we need this abstraction?"
"What's the expected behavior if this service is unavailable?"
"Is this intentional, or should it match the pattern in X?"
"Could you add a comment explaining this logic?"

AVOID:
"Why would you do it this way?" (sounds judgmental)
"This doesn't make sense" (not constructive)
```

---

## Common Review Comments

### Error Handling

```
ISSUE: Missing error handling

// Problematic
const data = await fetchData();
process(data);

// Better
try {
  const data = await fetchData();
  process(data);
} catch (error) {
  logger.error('Failed to fetch data', { error });
  throw new ApplicationError('Data unavailable', { cause: error });
}

COMMENT: "What happens if fetchData() throws? Consider
adding error handling with appropriate logging."
```

### Input Validation

```
ISSUE: Trusting user input

// Problematic
app.post('/api/users', (req, res) => {
  const user = db.users.create(req.body);
  res.json(user);
});

// Better
app.post('/api/users', (req, res) => {
  const validated = userSchema.parse(req.body);
  const user = db.users.create(validated);
  res.json(user);
});

COMMENT: "We should validate req.body before using it.
Consider using Zod/Joi for schema validation."
```

### Async/Await Issues

```
ISSUE: Sequential when could be parallel

// Problematic
const user = await getUser(id);
const orders = await getOrders(id);
const preferences = await getPreferences(id);

// Better
const [user, orders, preferences] = await Promise.all([
  getUser(id),
  getOrders(id),
  getPreferences(id),
]);

COMMENT: "These three async calls are independent.
Consider using Promise.all() to run them in parallel."
```

### Hardcoded Values

```
ISSUE: Magic numbers/strings

// Problematic
if (retryCount > 3) {
  throw new Error('Too many retries');
}
setTimeout(callback, 86400000);

// Better
const MAX_RETRIES = 3;
const ONE_DAY_MS = 24 * 60 * 60 * 1000;

if (retryCount > MAX_RETRIES) {
  throw new Error(`Exceeded maximum retries (${MAX_RETRIES})`);
}
setTimeout(callback, ONE_DAY_MS);

COMMENT: "Consider extracting these magic numbers into
named constants for clarity and maintainability."
```

### Logging Sensitive Data

```
ISSUE: Logging PII or secrets

// Problematic
logger.info('User login', { email, password, token });

// Better
logger.info('User login', {
  email: maskEmail(email),
  userId: user.id,
});

COMMENT: "[Blocker] We're logging password and token here.
Never log credentials or tokens. Consider masking the
email as well since it's PII."
```

---

## Review Templates

### Approval Template

```markdown
LGTM! :white_check_mark:

**What I reviewed:**
- Logic flow for the new feature
- Error handling and edge cases
- Test coverage

**Minor suggestions (non-blocking):**
- Consider adding a comment in X for clarity
- The variable name Y could be more descriptive

Ship it! :rocket:
```

### Request Changes Template

```markdown
Thanks for working on this! I found a few issues that should
be addressed before merging.

**Blocking issues:**
1. [Security] SQL injection vulnerability in `getUserQuery`
2. [Bug] Race condition possible in `updateCounter`

**Suggestions:**
- Consider adding test for empty array case
- The error message could be more user-friendly

Let me know if you'd like to discuss any of these!
```

### Question Template

```markdown
I'd like to understand a few things before completing review:

1. What's the expected behavior when X happens?
2. Is Y intentional or should it follow the pattern in Z?
3. How will this perform with large datasets?

I'll complete the review once these are clarified.
```

### PR Author Response Template

```markdown
Thanks for the review! Here's how I addressed your feedback:

- **SQL injection**: Fixed, using parameterized queries now
- **Race condition**: Added mutex lock
- **Test for empty array**: Added in test file line 45
- **Error message**: Updated to be more user-friendly

Please take another look when you have a chance!
```
