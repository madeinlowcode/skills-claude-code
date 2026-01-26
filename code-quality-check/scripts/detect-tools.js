#!/usr/bin/env node
/**
 * detect-tools.js
 * Detects which code quality tools are configured in a Node.js project.
 * Checks for Prettier, ESLint, TypeScript, and test runners.
 */

const fs = require('fs');
const path = require('path');

const projectRoot = process.argv[2] || process.cwd();

function fileExists(filePath) {
  return fs.existsSync(path.join(projectRoot, filePath));
}

function readJson(filePath) {
  try {
    const fullPath = path.join(projectRoot, filePath);
    if (fs.existsSync(fullPath)) {
      return JSON.parse(fs.readFileSync(fullPath, 'utf8'));
    }
  } catch (e) {}
  return null;
}

function detectPrettier() {
  const configFiles = [
    '.prettierrc',
    '.prettierrc.json',
    '.prettierrc.yml',
    '.prettierrc.yaml',
    '.prettierrc.js',
    '.prettierrc.cjs',
    '.prettierrc.mjs',
    'prettier.config.js',
    'prettier.config.cjs',
    'prettier.config.mjs'
  ];

  const pkg = readJson('package.json');
  const hasPrettierConfig = configFiles.some(fileExists);
  const hasPrettierInPkg = pkg?.prettier !== undefined;
  const hasPrettierDep = pkg?.devDependencies?.prettier || pkg?.dependencies?.prettier;

  return {
    installed: !!hasPrettierDep,
    configured: hasPrettierConfig || hasPrettierInPkg,
    configFile: configFiles.find(fileExists) || (hasPrettierInPkg ? 'package.json' : null),
    version: hasPrettierDep || null
  };
}

function detectEslint() {
  const flatConfigFiles = [
    'eslint.config.js',
    'eslint.config.mjs',
    'eslint.config.cjs',
    'eslint.config.ts',
    'eslint.config.mts',
    'eslint.config.cts'
  ];

  const legacyConfigFiles = [
    '.eslintrc',
    '.eslintrc.js',
    '.eslintrc.cjs',
    '.eslintrc.json',
    '.eslintrc.yml',
    '.eslintrc.yaml'
  ];

  const pkg = readJson('package.json');
  const flatConfig = flatConfigFiles.find(fileExists);
  const legacyConfig = legacyConfigFiles.find(fileExists);
  const hasEslintInPkg = pkg?.eslintConfig !== undefined;
  const hasEslintDep = pkg?.devDependencies?.eslint || pkg?.dependencies?.eslint;

  return {
    installed: !!hasEslintDep,
    configured: !!flatConfig || !!legacyConfig || hasEslintInPkg,
    configFile: flatConfig || legacyConfig || (hasEslintInPkg ? 'package.json' : null),
    configType: flatConfig ? 'flat' : (legacyConfig || hasEslintInPkg ? 'legacy' : null),
    version: hasEslintDep || null
  };
}

function detectTypescript() {
  const configFiles = [
    'tsconfig.json',
    'tsconfig.build.json',
    'tsconfig.app.json'
  ];

  const pkg = readJson('package.json');
  const hasConfig = configFiles.some(fileExists);
  const hasTsDep = pkg?.devDependencies?.typescript || pkg?.dependencies?.typescript;

  let tsConfig = null;
  if (fileExists('tsconfig.json')) {
    tsConfig = readJson('tsconfig.json');
  }

  return {
    installed: !!hasTsDep,
    configured: hasConfig,
    configFile: configFiles.find(fileExists) || null,
    version: hasTsDep || null,
    strict: tsConfig?.compilerOptions?.strict || false
  };
}

function detectTestRunner() {
  const pkg = readJson('package.json');
  const deps = { ...pkg?.devDependencies, ...pkg?.dependencies };

  const runners = [];

  if (deps?.jest || fileExists('jest.config.js') || fileExists('jest.config.ts')) {
    runners.push({ name: 'jest', version: deps?.jest || 'configured' });
  }

  if (deps?.vitest || fileExists('vitest.config.js') || fileExists('vitest.config.ts')) {
    runners.push({ name: 'vitest', version: deps?.vitest || 'configured' });
  }

  if (deps?.mocha || fileExists('.mocharc.json') || fileExists('.mocharc.js')) {
    runners.push({ name: 'mocha', version: deps?.mocha || 'configured' });
  }

  if (deps?.['@playwright/test'] || fileExists('playwright.config.ts')) {
    runners.push({ name: 'playwright', version: deps?.['@playwright/test'] || 'configured' });
  }

  if (deps?.cypress || fileExists('cypress.config.js') || fileExists('cypress.config.ts')) {
    runners.push({ name: 'cypress', version: deps?.cypress || 'configured' });
  }

  return {
    detected: runners.length > 0,
    runners: runners
  };
}

function detectScripts() {
  const pkg = readJson('package.json');
  const scripts = pkg?.scripts || {};

  return {
    lint: scripts.lint || null,
    format: scripts.format || scripts.prettier || null,
    typecheck: scripts.typecheck || scripts['type-check'] || scripts.tsc || null,
    test: scripts.test || null,
    build: scripts.build || null
  };
}

// Run detection
const results = {
  projectRoot: projectRoot,
  packageJson: fileExists('package.json'),
  prettier: detectPrettier(),
  eslint: detectEslint(),
  typescript: detectTypescript(),
  testRunner: detectTestRunner(),
  scripts: detectScripts()
};

console.log(JSON.stringify(results, null, 2));
