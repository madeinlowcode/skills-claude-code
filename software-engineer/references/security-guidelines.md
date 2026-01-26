# Security Guidelines

## Table of Contents
1. [OWASP Top 10](#owasp-top-10)
2. [Secure Coding Patterns](#secure-coding-patterns)
3. [Authentication & Authorization](#authentication--authorization)
4. [Data Protection](#data-protection)
5. [Infrastructure Security](#infrastructure-security)

---

## OWASP Top 10

### 1. Injection

```
RISK: Untrusted data sent to interpreter as command/query

SQL INJECTION:
// VULNERABLE
const query = `SELECT * FROM users WHERE id = ${userId}`;
db.query(query);

// SECURE
const query = 'SELECT * FROM users WHERE id = $1';
db.query(query, [userId]);

COMMAND INJECTION:
// VULNERABLE
exec(`convert ${inputFile} ${outputFile}`);

// SECURE
execFile('convert', [inputFile, outputFile]);

NOSQL INJECTION:
// VULNERABLE (MongoDB)
db.users.find({ username: req.body.username });
// Attack: { username: { $gt: "" } } returns all users

// SECURE
const username = String(req.body.username);
db.users.find({ username });
```

### 2. Broken Authentication

```
RISKS:
- Weak passwords allowed
- No brute force protection
- Session IDs in URLs
- Sessions not invalidated on logout

MITIGATIONS:
// Password requirements
const passwordSchema = z.string()
  .min(12, 'Password must be at least 12 characters')
  .regex(/[A-Z]/, 'Must contain uppercase')
  .regex(/[a-z]/, 'Must contain lowercase')
  .regex(/[0-9]/, 'Must contain number')
  .regex(/[^A-Za-z0-9]/, 'Must contain special character');

// Rate limiting
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts
  message: 'Too many login attempts, try again later',
});

// Session management
app.use(session({
  secret: process.env.SESSION_SECRET,
  name: 'sessionId', // Don't use default 'connect.sid'
  cookie: {
    secure: true,     // HTTPS only
    httpOnly: true,   // No JavaScript access
    sameSite: 'lax',  // CSRF protection
    maxAge: 3600000,  // 1 hour
  },
  resave: false,
  saveUninitialized: false,
}));
```

### 3. Sensitive Data Exposure

```
RISKS:
- Data transmitted in clear text
- Sensitive data stored unencrypted
- Weak cryptographic algorithms
- Keys exposed in code

MITIGATIONS:
// Always use HTTPS
app.use((req, res, next) => {
  if (!req.secure) {
    return res.redirect(`https://${req.headers.host}${req.url}`);
  }
  next();
});

// Encrypt sensitive data at rest
const encryptedSSN = crypto.encrypt(ssn, process.env.ENCRYPTION_KEY);

// Hash passwords properly
const hashedPassword = await bcrypt.hash(password, 12);

// Never log sensitive data
logger.info('User updated', {
  userId: user.id,
  // NOT: ssn, password, creditCard
});

// Use secure headers
app.use(helmet());
```

### 4. XML External Entities (XXE)

```
RISK: XML parser processes external entity references

// VULNERABLE
const parser = new XMLParser();
const result = parser.parse(xmlInput);

// SECURE
const parser = new XMLParser({
  allowBooleanAttributes: true,
  ignoreDeclaration: true,
  ignorePiTags: true,
  // Disable external entities
  parseTagValue: false,
  cdataPropName: '__cdata',
});

// Or use JSON instead of XML when possible
```

### 5. Broken Access Control

```
RISKS:
- IDOR (Insecure Direct Object References)
- Missing function-level access control
- CORS misconfiguration

// VULNERABLE - IDOR
app.get('/api/orders/:orderId', async (req, res) => {
  const order = await Order.findById(req.params.orderId);
  res.json(order); // Anyone can access any order!
});

// SECURE
app.get('/api/orders/:orderId', async (req, res) => {
  const order = await Order.findById(req.params.orderId);
  if (!order) {
    return res.status(404).json({ error: 'Order not found' });
  }
  if (order.userId !== req.user.id && req.user.role !== 'admin') {
    return res.status(403).json({ error: 'Forbidden' });
  }
  res.json(order);
});

// Role-based access
const requireRole = (...roles) => (req, res, next) => {
  if (!roles.includes(req.user.role)) {
    return res.status(403).json({ error: 'Insufficient permissions' });
  }
  next();
};

app.delete('/api/users/:id', requireRole('admin'), deleteUser);
```

### 6. Security Misconfiguration

```
CHECKLIST:
[ ] Remove default credentials
[ ] Disable directory listing
[ ] Remove unnecessary features/frameworks
[ ] Update dependencies regularly
[ ] Configure proper error messages
[ ] Disable debug mode in production

// Error handling - don't leak stack traces
app.use((err, req, res, next) => {
  logger.error('Unhandled error', { error: err });

  if (process.env.NODE_ENV === 'production') {
    res.status(500).json({ error: 'Internal server error' });
  } else {
    res.status(500).json({ error: err.message, stack: err.stack });
  }
});

// Security headers
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", 'data:', 'https:'],
    },
  },
  referrerPolicy: { policy: 'strict-origin-when-cross-origin' },
}));
```

### 7. Cross-Site Scripting (XSS)

```
TYPES:
- Reflected: Input immediately returned in response
- Stored: Input saved and shown to other users
- DOM-based: Client-side JavaScript manipulation

// VULNERABLE
app.get('/search', (req, res) => {
  res.send(`<h1>Results for: ${req.query.q}</h1>`);
  // Attack: /search?q=<script>stealCookies()</script>
});

// SECURE - Server-side
import { escape } from 'html-escaper';
app.get('/search', (req, res) => {
  res.send(`<h1>Results for: ${escape(req.query.q)}</h1>`);
});

// SECURE - React (automatic escaping)
function SearchResults({ query }) {
  return <h1>Results for: {query}</h1>; // Safe
}

// DANGEROUS in React
<div dangerouslySetInnerHTML={{ __html: userContent }} /> // AVOID

// CSP Header
Content-Security-Policy: default-src 'self'; script-src 'self'
```

### 8. Insecure Deserialization

```
RISK: Untrusted data deserialized without validation

// VULNERABLE - eval of JSON
const data = eval('(' + userInput + ')');

// VULNERABLE - YAML with arbitrary constructors
yaml.load(userInput);

// SECURE - JSON.parse (safe)
try {
  const data = JSON.parse(userInput);
} catch {
  throw new Error('Invalid JSON');
}

// SECURE - Schema validation after parse
const data = JSON.parse(userInput);
const validated = schema.parse(data);
```

### 9. Using Components with Known Vulnerabilities

```
MITIGATIONS:
# Regular dependency audits
npm audit
npm audit fix

# Automated scanning in CI
# .github/workflows/security.yml
- name: Security audit
  run: npm audit --production --audit-level=high

# Dependabot for automated updates
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"

# Pin versions in production
"dependencies": {
  "express": "4.18.2",  // Exact version
  // NOT: "express": "^4.18.2"
}
```

### 10. Insufficient Logging & Monitoring

```
WHAT TO LOG:
- Authentication events (login, logout, failed attempts)
- Authorization failures
- Input validation failures
- Application errors
- System events

// Security event logging
const securityLogger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  defaultMeta: { service: 'security' },
  transports: [
    new winston.transports.File({ filename: 'security.log' }),
  ],
});

// Log security events
securityLogger.warn('Failed login attempt', {
  ip: req.ip,
  email: req.body.email,
  timestamp: new Date().toISOString(),
  userAgent: req.headers['user-agent'],
});

// Set up alerts
if (failedLoginCount > 10) {
  alerting.send({
    severity: 'high',
    message: 'Possible brute force attack',
    details: { ip, email },
  });
}
```

---

## Secure Coding Patterns

### Input Validation

```javascript
// PATTERN: Validate early, validate everything
const userSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  age: z.number().int().min(0).max(150),
  role: z.enum(['user', 'admin']),
});

app.post('/api/users', (req, res) => {
  const result = userSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({
      error: 'Validation failed',
      details: result.error.issues,
    });
  }
  // Use result.data (validated and typed)
  createUser(result.data);
});
```

### Output Encoding

```javascript
// Context-specific encoding
function encodeForHTML(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;');
}

function encodeForURL(str) {
  return encodeURIComponent(str);
}

function encodeForJS(str) {
  return JSON.stringify(str);
}
```

### Secure Random Values

```javascript
// INSECURE
Math.random(); // Predictable

// SECURE
import crypto from 'crypto';

// Random token
const token = crypto.randomBytes(32).toString('hex');

// Random integer
const randomInt = crypto.randomInt(0, 100);

// UUID
import { randomUUID } from 'crypto';
const id = randomUUID();
```

---

## Authentication & Authorization

### JWT Best Practices

```javascript
// Token generation
const token = jwt.sign(
  {
    sub: user.id,
    role: user.role,
    // Don't include sensitive data
  },
  process.env.JWT_SECRET,
  {
    expiresIn: '15m',     // Short-lived access tokens
    algorithm: 'HS256',   // Or RS256 for asymmetric
    issuer: 'my-app',
    audience: 'my-app-users',
  }
);

// Token verification
const verifyToken = (token) => {
  try {
    return jwt.verify(token, process.env.JWT_SECRET, {
      algorithms: ['HS256'], // Prevent algorithm confusion
      issuer: 'my-app',
      audience: 'my-app-users',
    });
  } catch (error) {
    throw new AuthenticationError('Invalid token');
  }
};

// Refresh token rotation
const refreshToken = crypto.randomBytes(64).toString('hex');
await storeRefreshToken(user.id, refreshToken);
// On refresh: invalidate old token, issue new pair
```

### Password Storage

```javascript
import bcrypt from 'bcrypt';

// Hashing
const SALT_ROUNDS = 12; // Adjust based on performance
const hashedPassword = await bcrypt.hash(password, SALT_ROUNDS);

// Verification
const isValid = await bcrypt.compare(inputPassword, hashedPassword);

// Migration from weak hashing
async function verifyAndMigrate(email, password) {
  const user = await findUser(email);

  if (user.hashAlgorithm === 'md5') {
    // Old algorithm
    if (md5(password) === user.passwordHash) {
      // Migrate to bcrypt
      user.passwordHash = await bcrypt.hash(password, SALT_ROUNDS);
      user.hashAlgorithm = 'bcrypt';
      await user.save();
      return true;
    }
  } else {
    // Modern algorithm
    return await bcrypt.compare(password, user.passwordHash);
  }
  return false;
}
```

---

## Data Protection

### Encryption at Rest

```javascript
import crypto from 'crypto';

const ALGORITHM = 'aes-256-gcm';

function encrypt(text, key) {
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv(ALGORITHM, key, iv);

  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');

  const authTag = cipher.getAuthTag();

  return {
    iv: iv.toString('hex'),
    encrypted,
    authTag: authTag.toString('hex'),
  };
}

function decrypt(encryptedData, key) {
  const decipher = crypto.createDecipheriv(
    ALGORITHM,
    key,
    Buffer.from(encryptedData.iv, 'hex')
  );

  decipher.setAuthTag(Buffer.from(encryptedData.authTag, 'hex'));

  let decrypted = decipher.update(encryptedData.encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');

  return decrypted;
}
```

### Secrets Management

```javascript
// NEVER hardcode secrets
const apiKey = 'sk_live_abc123'; // WRONG

// Use environment variables
const apiKey = process.env.API_KEY;

// Use secrets manager in production
import { SecretsManager } from 'aws-sdk';

async function getSecret(secretName) {
  const client = new SecretsManager();
  const data = await client.getSecretValue({ SecretId: secretName }).promise();
  return JSON.parse(data.SecretString);
}

// Rotate secrets regularly
// Never log secrets
logger.info('Config loaded', {
  database: config.database,
  // NOT: apiKey, password
});
```

---

## Infrastructure Security

### CORS Configuration

```javascript
// INSECURE - allows everything
app.use(cors());

// SECURE - explicit whitelist
const corsOptions = {
  origin: (origin, callback) => {
    const whitelist = [
      'https://myapp.com',
      'https://admin.myapp.com',
    ];
    if (!origin || whitelist.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  maxAge: 86400, // 24 hours
};

app.use(cors(corsOptions));
```

### Rate Limiting

```javascript
import rateLimit from 'express-rate-limit';

// General rate limit
const generalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  standardHeaders: true,
  legacyHeaders: false,
});

// Strict limit for auth endpoints
const authLimiter = rateLimit({
  windowMs: 60 * 60 * 1000, // 1 hour
  max: 5, // 5 attempts
  message: 'Too many attempts, please try again later',
  skipSuccessfulRequests: true,
});

app.use('/api/', generalLimiter);
app.use('/api/auth/', authLimiter);
```

### Security Headers Checklist

```
HEADER                          PURPOSE
──────────────────────────────────────────────────────
Strict-Transport-Security       Force HTTPS
Content-Security-Policy         Prevent XSS
X-Content-Type-Options          Prevent MIME sniffing
X-Frame-Options                 Prevent clickjacking
X-XSS-Protection                XSS filter (legacy)
Referrer-Policy                 Control referrer info
Permissions-Policy              Control browser features
```
