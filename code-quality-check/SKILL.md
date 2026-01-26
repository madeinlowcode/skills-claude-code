---
name: code-quality-check
description: |
  Comprehensive code quality verification for Node.js/TypeScript projects before production deployment.
  Executes Prettier (formatting), ESLint (linting), TypeScript (type checking), and test runners.

  Use this skill when:
  - User asks to "verify code quality" or "check code quality"
  - User wants to "run linter", "run prettier", "run type check", or "check types"
  - User needs to "prepare code for production" or "pre-deploy check"
  - User requests "code review" or "automated code review"
  - User asks to "verify project standards" or "check coding standards"
  - User mentions "format code", "lint code", or "fix formatting"
  - Before deploying, merging, or releasing code
---

# Code Quality Check

Run comprehensive code quality verification: formatting, linting, type checking, and tests.

## Quick Start

### 1. Detect Project Tools
```bash
node scripts/detect-tools.js [project-path]
```
Returns JSON with detected tools (Prettier, ESLint, TypeScript, test runners) and their configurations.

### 2. Run All Checks
```bash
# Check only (no modifications)
node scripts/check-all.js [project-path]

# Check and auto-fix where possible
node scripts/check-all.js --fix [project-path]

# Skip tests
node scripts/check-all.js --skip-tests [project-path]
```

## Workflow

### Step 1: Detection
Run `detect-tools.js` to identify what's configured in the project. Check for:
- `package.json` existence
- Prettier config files (`.prettierrc`, `prettier.config.js`, etc.)
- ESLint config files (`eslint.config.js` for flat config, `.eslintrc.*` for legacy)
- TypeScript (`tsconfig.json`)
- Test runners (Jest, Vitest, Mocha, Playwright, Cypress)

### Step 2: Execution Order
Execute checks in this order (each step depends on previous):

1. **Prettier** - Fix formatting first
2. **ESLint** - Then fix linting (may depend on formatting)
3. **TypeScript** - Type check (requires valid syntax from steps 1-2)
4. **Tests** - Run test suite (requires all above passing)

### Step 3: Report Results

Format output as:
```
[OK] Prettier - All files formatted
[X] ESLint - 3 errors, 5 warnings
[OK] TypeScript - No type errors
[-] Tests - Skipped (no runner configured)

SUMMARY: 1 check failed - fix issues before deploy
```

## Manual Commands Reference

### Prettier
```bash
# Check formatting
npx prettier --check "**/*.{js,jsx,ts,tsx,json,css,md}"

# Fix formatting
npx prettier --write "**/*.{js,jsx,ts,tsx,json,css,md}"

# List unformatted files
npx prettier --list-different "**/*.{js,jsx,ts,tsx}"
```

### ESLint
```bash
# Check for issues
npx eslint .

# Auto-fix issues
npx eslint . --fix

# Check specific file types
npx eslint "**/*.{ts,tsx}"

# Inspect config (debug)
npx @eslint/config-inspector
```

### TypeScript
```bash
# Type check without emitting
npx tsc --noEmit

# Type check with pretty output
npx tsc --noEmit --pretty

# Watch mode
npx tsc --noEmit --watch

# Build mode (monorepos)
npx tsc --build --noEmit
```

### Tests
```bash
# Jest
npx jest
npx jest --coverage

# Vitest
npx vitest run
npx vitest run --coverage

# npm script
npm test
```

## Handling Issues

When issues are found:

1. **Auto-fixable issues**: Run with `--fix` flag
2. **Manual fixes needed**: Show specific errors and suggest fixes
3. **Missing tool**: Report as skipped, don't fail

For common issues and solutions, see [references/common-issues.md](references/common-issues.md).

For recommended configurations, see [references/config-examples.md](references/config-examples.md).

## Output Format

Use these status indicators:
- `[OK]` - Check passed
- `[X]` - Check failed (errors found)
- `[!]` - Check passed with warnings
- `[-]` - Check skipped (tool not configured)

## CI/CD Integration

Recommended npm scripts for `package.json`:
```json
{
  "scripts": {
    "quality": "prettier --check . && eslint . && tsc --noEmit",
    "quality:fix": "prettier --write . && eslint --fix . && tsc --noEmit"
  }
}
```

Exit codes:
- `0` - All checks passed
- `1` - One or more checks failed
