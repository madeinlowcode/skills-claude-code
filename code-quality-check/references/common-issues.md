# Common Code Quality Issues and Solutions

## Table of Contents
- [Prettier Issues](#prettier-issues)
- [ESLint Issues](#eslint-issues)
- [TypeScript Issues](#typescript-issues)
- [Test Issues](#test-issues)

---

## Prettier Issues

### "Prettier not found"
```bash
npm install --save-dev prettier
```

### Conflicting with ESLint
Install eslint-config-prettier to disable ESLint rules that conflict:
```bash
npm install --save-dev eslint-config-prettier
```

Add to ESLint config (flat config):
```javascript
import eslintConfigPrettier from "eslint-config-prettier";
export default [
  // ... other configs
  eslintConfigPrettier,
];
```

### Ignoring files
Create `.prettierignore`:
```
dist/
build/
node_modules/
coverage/
*.min.js
```

### Line ending issues (Windows/Unix)
Add to `.prettierrc`:
```json
{
  "endOfLine": "auto"
}
```

---

## ESLint Issues

### "ESLint configuration file not found"
Create `eslint.config.js` (flat config - recommended for ESLint 9+):
```javascript
import js from "@eslint/js";
export default [
  js.configs.recommended,
  {
    rules: {
      "no-unused-vars": "warn"
    }
  }
];
```

### "Parsing error: Unexpected token"
For TypeScript projects, install and configure:
```bash
npm install --save-dev typescript-eslint
```

```javascript
// eslint.config.js
import tseslint from "typescript-eslint";
export default tseslint.config(
  ...tseslint.configs.recommended
);
```

### "Module not found" in ESLint config
Ensure all plugins are installed:
```bash
npm install --save-dev @eslint/js typescript-eslint
```

### Legacy config migration
If using `.eslintrc.*`, migrate to flat config:
```bash
npx @eslint/migrate-config .eslintrc.json
```

### Too many errors to fix manually
Use `--fix` for auto-fixable issues:
```bash
npx eslint . --fix
```

For specific rule categories:
```bash
npx eslint . --fix --fix-type suggestion
npx eslint . --fix --fix-type problem
npx eslint . --fix --fix-type layout
```

---

## TypeScript Issues

### "Cannot find module" errors
1. Check `tsconfig.json` paths:
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

2. Ensure types are installed:
```bash
npm install --save-dev @types/node @types/react
```

### "Implicit any" errors
Either add explicit types or disable the rule (not recommended):
```json
{
  "compilerOptions": {
    "noImplicitAny": false
  }
}
```

### "Object is possibly undefined"
Use optional chaining or null checks:
```typescript
// Before
const value = obj.prop.nested;

// After
const value = obj?.prop?.nested;
// or
if (obj && obj.prop) {
  const value = obj.prop.nested;
}
```

### "Type X is not assignable to type Y"
Common solutions:
1. Use type assertion (when certain):
   ```typescript
   const value = data as ExpectedType;
   ```

2. Use type guards:
   ```typescript
   function isString(value: unknown): value is string {
     return typeof value === "string";
   }
   ```

3. Narrow the type properly:
   ```typescript
   if (typeof value === "string") {
     // TypeScript knows value is string here
   }
   ```

### Project references not working
For monorepos, ensure `tsconfig.json` has:
```json
{
  "references": [
    { "path": "./packages/shared" }
  ],
  "compilerOptions": {
    "composite": true
  }
}
```

Run with:
```bash
npx tsc --build --noEmit
```

---

## Test Issues

### Tests not found
Check test file patterns in config:

**Jest** (`jest.config.js`):
```javascript
module.exports = {
  testMatch: ["**/__tests__/**/*.[jt]s?(x)", "**/?(*.)+(spec|test).[jt]s?(x)"]
};
```

**Vitest** (`vitest.config.ts`):
```typescript
export default defineConfig({
  test: {
    include: ["**/*.{test,spec}.{js,ts,jsx,tsx}"]
  }
});
```

### Import errors in tests
For ESM projects, ensure Jest is configured:
```javascript
// jest.config.js
module.exports = {
  transform: {
    "^.+\\.(ts|tsx)$": "ts-jest"
  },
  moduleNameMapper: {
    "^@/(.*)$": "<rootDir>/src/$1"
  }
};
```

### Timeout errors
Increase timeout for async tests:
```typescript
// Jest
jest.setTimeout(30000);

// Vitest
test("slow test", async () => {
  // ...
}, { timeout: 30000 });
```

### Coverage below threshold
Run with coverage to identify gaps:
```bash
npx jest --coverage
npx vitest run --coverage
```

---

## Quick Reference Commands

| Task | Command |
|------|---------|
| Check formatting | `npx prettier --check .` |
| Fix formatting | `npx prettier --write .` |
| Lint check | `npx eslint .` |
| Lint fix | `npx eslint . --fix` |
| Type check | `npx tsc --noEmit` |
| Type check (watch) | `npx tsc --noEmit --watch` |
| Run tests | `npm test` |
| Tests with coverage | `npx jest --coverage` |
