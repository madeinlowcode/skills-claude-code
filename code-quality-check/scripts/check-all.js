#!/usr/bin/env node
/**
 * check-all.js
 * Runs all code quality checks: Prettier, ESLint, TypeScript, and Tests.
 * Supports --fix flag to auto-fix issues where possible.
 */

const { execSync, spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const shouldFix = args.includes('--fix');
const skipTests = args.includes('--skip-tests');
const projectRoot = args.find(a => !a.startsWith('--')) || process.cwd();

const results = {
  prettier: { status: 'skipped', issues: 0, fixed: 0 },
  eslint: { status: 'skipped', errors: 0, warnings: 0, fixed: 0 },
  typescript: { status: 'skipped', errors: 0 },
  tests: { status: 'skipped', passed: 0, failed: 0 }
};

function log(emoji, message) {
  console.log(`${emoji} ${message}`);
}

function runCommand(command, options = {}) {
  try {
    const result = spawnSync(command, {
      shell: true,
      cwd: projectRoot,
      encoding: 'utf8',
      ...options
    });
    return {
      success: result.status === 0,
      stdout: result.stdout || '',
      stderr: result.stderr || '',
      status: result.status
    };
  } catch (e) {
    return { success: false, stdout: '', stderr: e.message, status: 1 };
  }
}

function fileExists(filePath) {
  return fs.existsSync(path.join(projectRoot, filePath));
}

function hasNodeModules() {
  return fileExists('node_modules');
}

function detectPrettier() {
  const configFiles = ['.prettierrc', '.prettierrc.json', '.prettierrc.js', 'prettier.config.js'];
  return configFiles.some(f => fileExists(f)) || fileExists('package.json');
}

function detectEslint() {
  const flatConfigs = ['eslint.config.js', 'eslint.config.mjs', 'eslint.config.cjs'];
  const legacyConfigs = ['.eslintrc', '.eslintrc.js', '.eslintrc.json', '.eslintrc.yml'];
  return [...flatConfigs, ...legacyConfigs].some(f => fileExists(f));
}

function detectTypescript() {
  return fileExists('tsconfig.json');
}

// Check node_modules
if (!hasNodeModules()) {
  log('[!]', 'node_modules not found. Run npm install first.');
  process.exit(1);
}

console.log('');
log('[=]', 'CODE QUALITY CHECK');
log('[=]', '==================');
console.log(`Mode: ${shouldFix ? 'Fix' : 'Check only'}`);
console.log(`Path: ${projectRoot}`);
console.log('');

// 1. PRETTIER
log('[1]', 'PRETTIER - Code Formatting');
console.log('---');

if (detectPrettier()) {
  const prettierCmd = shouldFix
    ? 'npx prettier --write "**/*.{js,jsx,ts,tsx,json,css,scss,md}" --ignore-unknown'
    : 'npx prettier --check "**/*.{js,jsx,ts,tsx,json,css,scss,md}" --ignore-unknown';

  const prettierResult = runCommand(prettierCmd);

  if (prettierResult.success) {
    results.prettier.status = 'passed';
    log('[OK]', 'All files are formatted correctly');
  } else {
    if (shouldFix) {
      results.prettier.status = 'fixed';
      results.prettier.fixed = (prettierResult.stdout.match(/\n/g) || []).length;
      log('[OK]', `Fixed formatting in ${results.prettier.fixed} files`);
    } else {
      results.prettier.status = 'failed';
      const unformatted = prettierResult.stdout.split('\n').filter(l => l.trim());
      results.prettier.issues = unformatted.length;
      log('[X]', `${results.prettier.issues} files need formatting:`);
      unformatted.slice(0, 10).forEach(f => console.log(`   - ${f}`));
      if (unformatted.length > 10) console.log(`   ... and ${unformatted.length - 10} more`);
    }
  }
} else {
  log('[-]', 'Prettier not configured, skipping');
}

console.log('');

// 2. ESLINT
log('[2]', 'ESLINT - Static Analysis');
console.log('---');

if (detectEslint()) {
  const eslintCmd = shouldFix
    ? 'npx eslint . --fix --format stylish'
    : 'npx eslint . --format stylish';

  const eslintResult = runCommand(eslintCmd);

  // Parse ESLint output for counts
  const errorMatch = eslintResult.stdout.match(/(\d+) errors?/);
  const warningMatch = eslintResult.stdout.match(/(\d+) warnings?/);
  const fixedMatch = eslintResult.stdout.match(/(\d+) errors? and \d+ warnings? potentially fixable/);

  results.eslint.errors = errorMatch ? parseInt(errorMatch[1]) : 0;
  results.eslint.warnings = warningMatch ? parseInt(warningMatch[1]) : 0;

  if (eslintResult.success && results.eslint.errors === 0) {
    results.eslint.status = 'passed';
    if (results.eslint.warnings > 0) {
      log('[!]', `Passed with ${results.eslint.warnings} warnings`);
    } else {
      log('[OK]', 'No linting issues found');
    }
  } else {
    if (shouldFix) {
      results.eslint.status = results.eslint.errors > 0 ? 'partial' : 'fixed';
      log('[!]', `Fixed what was auto-fixable. Remaining: ${results.eslint.errors} errors, ${results.eslint.warnings} warnings`);
    } else {
      results.eslint.status = 'failed';
      log('[X]', `Found ${results.eslint.errors} errors and ${results.eslint.warnings} warnings`);
    }

    if (eslintResult.stdout) {
      console.log('\nDetails:');
      console.log(eslintResult.stdout.substring(0, 2000));
      if (eslintResult.stdout.length > 2000) console.log('... (output truncated)');
    }
  }
} else {
  log('[-]', 'ESLint not configured, skipping');
}

console.log('');

// 3. TYPESCRIPT
log('[3]', 'TYPESCRIPT - Type Checking');
console.log('---');

if (detectTypescript()) {
  const tscResult = runCommand('npx tsc --noEmit --pretty');

  if (tscResult.success) {
    results.typescript.status = 'passed';
    log('[OK]', 'No type errors found');
  } else {
    results.typescript.status = 'failed';
    // Count errors
    const errorLines = (tscResult.stdout + tscResult.stderr).match(/error TS\d+/g) || [];
    results.typescript.errors = errorLines.length;
    log('[X]', `Found ${results.typescript.errors} type errors`);

    const output = tscResult.stdout || tscResult.stderr;
    if (output) {
      console.log('\nDetails:');
      console.log(output.substring(0, 2000));
      if (output.length > 2000) console.log('... (output truncated)');
    }
  }
} else {
  log('[-]', 'TypeScript not configured, skipping');
}

console.log('');

// 4. TESTS
if (!skipTests) {
  log('[4]', 'TESTS - Test Suite');
  console.log('---');

  let testCmd = null;
  if (fileExists('vitest.config.js') || fileExists('vitest.config.ts')) {
    testCmd = 'npx vitest run';
  } else if (fileExists('jest.config.js') || fileExists('jest.config.ts')) {
    testCmd = 'npx jest';
  } else {
    // Check package.json for test script
    try {
      const pkg = JSON.parse(fs.readFileSync(path.join(projectRoot, 'package.json'), 'utf8'));
      if (pkg.scripts?.test && !pkg.scripts.test.includes('no test specified')) {
        testCmd = 'npm test';
      }
    } catch (e) {}
  }

  if (testCmd) {
    const testResult = runCommand(testCmd);

    if (testResult.success) {
      results.tests.status = 'passed';
      log('[OK]', 'All tests passed');
    } else {
      results.tests.status = 'failed';
      log('[X]', 'Some tests failed');
      const output = testResult.stdout || testResult.stderr;
      if (output) {
        console.log('\nDetails:');
        console.log(output.substring(0, 1500));
        if (output.length > 1500) console.log('... (output truncated)');
      }
    }
  } else {
    log('[-]', 'No test runner configured, skipping');
  }

  console.log('');
}

// SUMMARY
console.log('');
log('[=]', 'SUMMARY');
log('[=]', '=======');
console.log('');

const statusEmoji = {
  passed: '[OK]',
  fixed: '[OK]',
  partial: '[!]',
  failed: '[X]',
  skipped: '[-]'
};

console.log(`Prettier:   ${statusEmoji[results.prettier.status]} ${results.prettier.status.toUpperCase()}`);
console.log(`ESLint:     ${statusEmoji[results.eslint.status]} ${results.eslint.status.toUpperCase()} (${results.eslint.errors} errors, ${results.eslint.warnings} warnings)`);
console.log(`TypeScript: ${statusEmoji[results.typescript.status]} ${results.typescript.status.toUpperCase()} (${results.typescript.errors} errors)`);
if (!skipTests) {
  console.log(`Tests:      ${statusEmoji[results.tests.status]} ${results.tests.status.toUpperCase()}`);
}

console.log('');

// Exit code
const hasFailures = results.prettier.status === 'failed' ||
                    results.eslint.status === 'failed' ||
                    results.typescript.status === 'failed' ||
                    results.tests.status === 'failed';

if (hasFailures) {
  log('[X]', 'Code quality check FAILED - fix issues before deploy');
  process.exit(1);
} else {
  log('[OK]', 'Code quality check PASSED - ready for deploy');
  process.exit(0);
}
