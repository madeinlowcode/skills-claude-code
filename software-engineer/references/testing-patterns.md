# Testing Patterns Reference

## Table of Contents
1. [Unit Testing Patterns](#unit-testing-patterns)
2. [Integration Testing Patterns](#integration-testing-patterns)
3. [Mocking Strategies](#mocking-strategies)
4. [Test Data Management](#test-data-management)
5. [Testing Anti-Patterns](#testing-anti-patterns)

---

## Unit Testing Patterns

### Arrange-Act-Assert (AAA)

```javascript
// PATTERN: Clear separation of test phases
test('calculateTotal applies discount correctly', () => {
  // Arrange
  const cart = new ShoppingCart();
  cart.addItem({ price: 100, quantity: 2 });
  const discount = new PercentageDiscount(10);

  // Act
  const total = cart.calculateTotal(discount);

  // Assert
  expect(total).toBe(180);
});
```

### Given-When-Then (BDD Style)

```javascript
describe('User Authentication', () => {
  describe('given valid credentials', () => {
    describe('when user attempts to login', () => {
      it('then returns authentication token', async () => {
        const credentials = { email: 'user@test.com', password: 'valid' };
        const result = await authService.login(credentials);
        expect(result.token).toBeDefined();
      });
    });
  });

  describe('given invalid password', () => {
    describe('when user attempts to login', () => {
      it('then throws AuthenticationError', async () => {
        const credentials = { email: 'user@test.com', password: 'wrong' };
        await expect(authService.login(credentials))
          .rejects.toThrow(AuthenticationError);
      });
    });
  });
});
```

### Parameterized Tests

```javascript
// PATTERN: Test multiple inputs with same logic
describe('validateEmail', () => {
  const validEmails = [
    'user@example.com',
    'user.name@example.com',
    'user+tag@example.co.uk',
  ];

  const invalidEmails = [
    'not-an-email',
    '@example.com',
    'user@',
    '',
  ];

  test.each(validEmails)('accepts valid email: %s', (email) => {
    expect(validateEmail(email)).toBe(true);
  });

  test.each(invalidEmails)('rejects invalid email: %s', (email) => {
    expect(validateEmail(email)).toBe(false);
  });
});
```

### Test Fixtures

```javascript
// PATTERN: Reusable test data factories
const createUser = (overrides = {}) => ({
  id: 'user-123',
  email: 'test@example.com',
  name: 'Test User',
  role: 'user',
  createdAt: new Date('2024-01-01'),
  ...overrides,
});

const createOrder = (overrides = {}) => ({
  id: 'order-456',
  userId: 'user-123',
  items: [],
  total: 0,
  status: 'pending',
  ...overrides,
});

// Usage in tests
test('admin can view any order', () => {
  const admin = createUser({ role: 'admin' });
  const order = createOrder({ userId: 'other-user' });

  expect(canViewOrder(admin, order)).toBe(true);
});
```

---

## Integration Testing Patterns

### Database Testing with Transactions

```javascript
// PATTERN: Rollback transaction after each test
describe('UserRepository', () => {
  let connection;
  let transaction;

  beforeEach(async () => {
    connection = await getConnection();
    transaction = await connection.beginTransaction();
  });

  afterEach(async () => {
    await transaction.rollback();
  });

  test('creates user with correct data', async () => {
    const repo = new UserRepository(connection);
    const user = await repo.create({
      email: 'test@example.com',
      name: 'Test User',
    });

    expect(user.id).toBeDefined();
    expect(user.email).toBe('test@example.com');
  });
});
```

### API Integration Tests

```javascript
// PATTERN: Test full HTTP cycle
describe('POST /api/orders', () => {
  let app;
  let authToken;

  beforeAll(async () => {
    app = await createTestApp();
    authToken = await getTestAuthToken();
  });

  test('creates order with valid data', async () => {
    const orderData = {
      items: [{ productId: 'prod-1', quantity: 2 }],
    };

    const response = await request(app)
      .post('/api/orders')
      .set('Authorization', `Bearer ${authToken}`)
      .send(orderData)
      .expect(201);

    expect(response.body.id).toBeDefined();
    expect(response.body.status).toBe('pending');
  });

  test('returns 401 without authentication', async () => {
    await request(app)
      .post('/api/orders')
      .send({})
      .expect(401);
  });

  test('returns 400 with invalid data', async () => {
    const response = await request(app)
      .post('/api/orders')
      .set('Authorization', `Bearer ${authToken}`)
      .send({ items: [] })
      .expect(400);

    expect(response.body.error).toContain('items');
  });
});
```

### External Service Testing

```javascript
// PATTERN: Use test containers for real dependencies
const { GenericContainer } = require('testcontainers');

describe('RedisCache', () => {
  let container;
  let cache;

  beforeAll(async () => {
    container = await new GenericContainer('redis:7')
      .withExposedPorts(6379)
      .start();

    const port = container.getMappedPort(6379);
    cache = new RedisCache({ host: 'localhost', port });
  });

  afterAll(async () => {
    await container.stop();
  });

  test('stores and retrieves values', async () => {
    await cache.set('key', 'value', 60);
    const result = await cache.get('key');
    expect(result).toBe('value');
  });
});
```

---

## Mocking Strategies

### When to Mock

```
MOCK:
- External services (APIs, databases in unit tests)
- Non-deterministic behavior (time, random)
- Slow operations (file I/O, network)
- Error conditions that are hard to trigger

DON'T MOCK:
- The unit under test
- Simple value objects
- Standard library functions
- Things that are fast and deterministic
```

### Mock Patterns

```javascript
// PATTERN: Dependency injection for testability
class OrderService {
  constructor(orderRepo, paymentGateway, emailService) {
    this.orderRepo = orderRepo;
    this.paymentGateway = paymentGateway;
    this.emailService = emailService;
  }

  async placeOrder(order) {
    const savedOrder = await this.orderRepo.save(order);
    await this.paymentGateway.charge(order.total);
    await this.emailService.sendConfirmation(order);
    return savedOrder;
  }
}

// Test with mocks
test('placeOrder charges payment and sends email', async () => {
  const mockRepo = { save: jest.fn().mockResolvedValue({ id: '123' }) };
  const mockPayment = { charge: jest.fn().mockResolvedValue(true) };
  const mockEmail = { sendConfirmation: jest.fn().mockResolvedValue(true) };

  const service = new OrderService(mockRepo, mockPayment, mockEmail);
  await service.placeOrder({ total: 100 });

  expect(mockPayment.charge).toHaveBeenCalledWith(100);
  expect(mockEmail.sendConfirmation).toHaveBeenCalled();
});
```

### Stub vs Mock vs Spy

```javascript
// STUB: Returns canned responses
const stubRepo = {
  findById: () => ({ id: '123', name: 'Test' }),
};

// MOCK: Verifies interactions
const mockRepo = {
  save: jest.fn(),
};
// Later: expect(mockRepo.save).toHaveBeenCalledWith(expectedData);

// SPY: Wraps real implementation
const realRepo = new UserRepository();
const spy = jest.spyOn(realRepo, 'findById');
// Real method executes, but calls are tracked
```

---

## Test Data Management

### Builder Pattern

```javascript
class UserBuilder {
  constructor() {
    this.user = {
      id: 'default-id',
      email: 'default@test.com',
      name: 'Default User',
      role: 'user',
      verified: false,
    };
  }

  withId(id) {
    this.user.id = id;
    return this;
  }

  withEmail(email) {
    this.user.email = email;
    return this;
  }

  asAdmin() {
    this.user.role = 'admin';
    return this;
  }

  verified() {
    this.user.verified = true;
    return this;
  }

  build() {
    return { ...this.user };
  }
}

// Usage
const admin = new UserBuilder().asAdmin().verified().build();
const unverified = new UserBuilder().withEmail('new@test.com').build();
```

### Faker for Random Data

```javascript
const { faker } = require('@faker-js/faker');

const createRandomUser = () => ({
  id: faker.string.uuid(),
  email: faker.internet.email(),
  name: faker.person.fullName(),
  phone: faker.phone.number(),
  address: {
    street: faker.location.streetAddress(),
    city: faker.location.city(),
    country: faker.location.country(),
  },
});
```

---

## Testing Anti-Patterns

### Anti-Pattern: Testing Implementation Details

```javascript
// BAD: Tests internal state
test('adds item to internal array', () => {
  const cart = new ShoppingCart();
  cart.addItem({ id: '1', price: 10 });
  expect(cart._items.length).toBe(1); // Accessing private field
});

// GOOD: Tests behavior
test('addItem increases item count', () => {
  const cart = new ShoppingCart();
  cart.addItem({ id: '1', price: 10 });
  expect(cart.getItemCount()).toBe(1);
});
```

### Anti-Pattern: Flaky Tests

```javascript
// BAD: Time-dependent, may fail randomly
test('token expires', async () => {
  const token = createToken();
  await sleep(1000);
  expect(token.isExpired()).toBe(true);
});

// GOOD: Control time explicitly
test('token expires after TTL', () => {
  jest.useFakeTimers();
  const token = createToken({ ttl: 1000 });

  jest.advanceTimersByTime(999);
  expect(token.isExpired()).toBe(false);

  jest.advanceTimersByTime(1);
  expect(token.isExpired()).toBe(true);
});
```

### Anti-Pattern: Test Interdependence

```javascript
// BAD: Tests depend on execution order
let sharedUser;

test('creates user', async () => {
  sharedUser = await createUser();
  expect(sharedUser.id).toBeDefined();
});

test('updates user', async () => {
  // Fails if previous test didn't run
  await updateUser(sharedUser.id, { name: 'New Name' });
});

// GOOD: Each test is independent
test('updates user name', async () => {
  const user = await createUser();
  await updateUser(user.id, { name: 'New Name' });
  const updated = await getUser(user.id);
  expect(updated.name).toBe('New Name');
});
```

### Anti-Pattern: Giant Test Methods

```javascript
// BAD: One test doing too much
test('user registration flow', async () => {
  // 50 lines of setup, actions, and assertions
  // Testing registration, email, verification, login, profile...
});

// GOOD: Focused tests
describe('User Registration', () => {
  test('creates user with valid data', async () => { /* ... */ });
  test('sends verification email', async () => { /* ... */ });
  test('rejects duplicate email', async () => { /* ... */ });
});
```
