# Recommended Configuration Examples

## Table of Contents
- [Prettier Configuration](#prettier-configuration)
- [ESLint Flat Config](#eslint-flat-config)
- [TypeScript Configuration](#typescript-configuration)
- [Combined Setup Script](#combined-setup-script)

---

## Prettier Configuration

### .prettierrc (recommended)
```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 100,
  "endOfLine": "auto",
  "bracketSpacing": true,
  "arrowParens": "avoid"
}
```

### .prettierignore
```
node_modules/
dist/
build/
coverage/
.next/
.nuxt/
*.min.js
*.min.css
package-lock.json
yarn.lock
pnpm-lock.yaml
```

---

## ESLint Flat Config

### Basic JavaScript (eslint.config.js)
```javascript
import js from "@eslint/js";

export default [
  js.configs.recommended,
  {
    ignores: ["dist/", "node_modules/", "coverage/"]
  },
  {
    rules: {
      "no-unused-vars": "warn",
      "no-console": "warn"
    }
  }
];
```

### TypeScript Project (eslint.config.js)
```javascript
import js from "@eslint/js";
import tseslint from "typescript-eslint";

export default tseslint.config(
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    ignores: ["dist/", "node_modules/", "coverage/"]
  },
  {
    languageOptions: {
      parserOptions: {
        project: true
      }
    },
    rules: {
      "@typescript-eslint/no-unused-vars": "warn",
      "@typescript-eslint/explicit-function-return-type": "off",
      "@typescript-eslint/no-explicit-any": "warn"
    }
  }
);
```

### React + TypeScript (eslint.config.js)
```javascript
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import reactPlugin from "eslint-plugin-react";
import reactHooksPlugin from "eslint-plugin-react-hooks";

export default tseslint.config(
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    ignores: ["dist/", "node_modules/", "coverage/", ".next/"]
  },
  {
    files: ["**/*.{ts,tsx}"],
    plugins: {
      react: reactPlugin,
      "react-hooks": reactHooksPlugin
    },
    languageOptions: {
      parserOptions: {
        ecmaFeatures: { jsx: true }
      }
    },
    settings: {
      react: { version: "detect" }
    },
    rules: {
      "react/react-in-jsx-scope": "off",
      "react-hooks/rules-of-hooks": "error",
      "react-hooks/exhaustive-deps": "warn"
    }
  }
);
```

### With Prettier Integration
```javascript
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import eslintConfigPrettier from "eslint-config-prettier";

export default tseslint.config(
  js.configs.recommended,
  ...tseslint.configs.recommended,
  eslintConfigPrettier, // Must be last to override other configs
  {
    ignores: ["dist/", "node_modules/"]
  }
);
```

---

## TypeScript Configuration

### Standard Web Project (tsconfig.json)
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "allowImportingTsExtensions": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### React Project (tsconfig.json)
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "allowImportingTsExtensions": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src"],
  "exclude": ["node_modules"]
}
```

### Node.js Project (tsconfig.json)
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022"],
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

---

## Combined Setup Script

### package.json scripts
```json
{
  "scripts": {
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "quality": "npm run format:check && npm run lint && npm run typecheck",
    "quality:fix": "npm run format && npm run lint:fix && npm run typecheck",
    "precommit": "npm run quality",
    "prepush": "npm run quality && npm run test"
  }
}
```

### Required Dependencies
```bash
# Prettier
npm install --save-dev prettier

# ESLint (with TypeScript)
npm install --save-dev eslint @eslint/js typescript-eslint

# ESLint + Prettier integration
npm install --save-dev eslint-config-prettier

# TypeScript
npm install --save-dev typescript

# React ESLint plugins (if React project)
npm install --save-dev eslint-plugin-react eslint-plugin-react-hooks

# Test runner (choose one)
npm install --save-dev vitest
# or
npm install --save-dev jest ts-jest @types/jest
```

---

## Pre-commit Hook Setup (Husky + lint-staged)

### Installation
```bash
npm install --save-dev husky lint-staged
npx husky init
```

### .husky/pre-commit
```bash
npx lint-staged
```

### package.json (lint-staged config)
```json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ],
    "*.{json,css,scss,md}": [
      "prettier --write"
    ]
  }
}
```
