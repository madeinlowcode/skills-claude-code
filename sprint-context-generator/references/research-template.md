# Pesquisa e Documentação: FEAT-XXX - [Nome da Feature]

📂 **Documentação Relacionada:**
- [Especificação](spec.md) - Requisitos e análise de personas
- [Plano Técnico](plan.md) - Arquitetura e decisões técnicas
- [Lista de Tasks](tasks.md) - Tarefas detalhadas (XX tasks)

---

## Índice

1. [Tecnologias Utilizadas](#tecnologias-utilizadas)
2. [Melhores Práticas Pesquisadas](#melhores-práticas-pesquisadas)
3. [Artigos e Tutoriais Relevantes](#artigos-e-tutoriais-relevantes)
4. [Exemplos de Implementação](#exemplos-de-implementação)
5. [Referências de Código](#referências-de-código)
6. [Comunidade e Suporte](#comunidade-e-suporte)

---

## Tecnologias Utilizadas

### [Nome da Tecnologia 1]

**Link Oficial:** [URL da documentação oficial]

**Versão:** [X.Y.Z] (latest stable)

**Propósito:**
[Para que esta tecnologia será usada nesta feature]

**Principais Métodos/APIs:**

#### Método 1: `[methodName]()`
**Descrição:** [O que este método faz]

**Parâmetros:**
- `param1` (Type): [Descrição do parâmetro]
- `param2` (Type): [Descrição do parâmetro]

**Retorno:** [Tipo de retorno e descrição]

**Exemplo de uso:**
```typescript
import { methodName } from '[package-name]'

const result = methodName(param1, param2)
// [Descrição do que acontece]
```

**Documentação:** [URL específica do método]

---

#### Método 2: `[methodName]()`
[Repetir estrutura acima]

---

**Instalação:**
```bash
npm install [package-name]
# ou
yarn add [package-name]
```

**Configuração Básica:**
```typescript
// [Código de configuração inicial]
import { [imports] } from '[package-name]'

// [Setup necessário]
const config = {
  option1: value1,
  option2: value2,
}
```

**Requisitos/Dependências:**
- [Requisito 1: Ex: Node.js >= 18.x]
- [Requisito 2: Ex: TypeScript >= 5.x]

**Notas Importantes:**
- [Nota 1: Algo importante a saber sobre esta tecnologia]
- [Nota 2: Limitações ou cuidados especiais]

**Documentação Essencial:**
- [Seção 1]: [URL] - [Por que é importante]
- [Seção 2]: [URL] - [Por que é importante]

---

### [Nome da Tecnologia 2]
[Repetir estrutura acima para cada tecnologia]

---

## Melhores Práticas Pesquisadas

### Clean Architecture

**Fonte:** [Título do artigo/livro] - [URL]

**Autor/Organização:** [Nome]

**Data:** [YYYY-MM-DD]

**Resumo:**
[Principais pontos sobre Clean Architecture aplicáveis a esta feature]

**Princípios Aplicáveis:**

#### 1. Separação de Camadas
**Conceito:**
[Explicação do princípio]

**Como aplicar nesta feature:**
```
[Exemplo de estrutura de diretórios ou código]

src/
├── domain/           # Entidades e lógica de domínio
├── application/      # Casos de uso
├── infrastructure/   # Database, APIs externas
└── presentation/     # Controllers, UI
```

**Benefícios:**
- [Benefício 1]
- [Benefício 2]

---

#### 2. Dependency Inversion
**Conceito:**
[Explicação do princípio]

**Como aplicar nesta feature:**
```typescript
// Exemplo de código
interface [InterfaceName] {
  method(): ReturnType
}

class [ImplementationName] implements [InterfaceName] {
  method(): ReturnType {
    // implementação
  }
}

// Injeção de dependência
class [ServiceName] {
  constructor(private dependency: [InterfaceName]) {}
}
```

**Benefícios:**
- [Benefício 1: Testabilidade]
- [Benefício 2: Flexibilidade]

---

**Recursos Adicionais:**
- [Artigo relacionado 1]: [URL]
- [Vídeo explicativo]: [URL]

---

### Testes E2E com Playwright

**Fonte:** [URL da documentação oficial ou artigo]

**Resumo:**
[Principais padrões e práticas de testes E2E com Playwright]

**Padrões Recomendados:**

#### 1. Page Object Pattern
**Conceito:**
[Explicação do padrão]

**Exemplo de implementação:**
```typescript
// pages/LoginPage.ts
export class LoginPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('/login')
  }

  async fillEmail(email: string) {
    await this.page.fill('[data-testid="email-input"]', email)
  }

  async fillPassword(password: string) {
    await this.page.fill('[data-testid="password-input"]', password)
  }

  async submit() {
    await this.page.click('[data-testid="submit-button"]')
  }

  async login(email: string, password: string) {
    await this.fillEmail(email)
    await this.fillPassword(password)
    await this.submit()
  }
}
```

**Uso no teste:**
```typescript
test('usuário faz login com sucesso', async ({ page }) => {
  const loginPage = new LoginPage(page)
  await loginPage.goto()
  await loginPage.login('user@example.com', 'password123')

  await expect(page).toHaveURL('/dashboard')
})
```

**Benefícios:**
- [Benefício 1: Reutilização de código]
- [Benefício 2: Manutenibilidade]

---

#### 2. Fixtures Customizadas
**Conceito:**
[Explicação de fixtures]

**Exemplo:**
```typescript
// fixtures.ts
import { test as base } from '@playwright/test'

type Fixtures = {
  authenticatedPage: Page
}

export const test = base.extend<Fixtures>({
  authenticatedPage: async ({ page }, use) => {
    // Login automático
    await page.goto('/login')
    await page.fill('[data-testid="email"]', 'test@example.com')
    await page.fill('[data-testid="password"]', 'password123')
    await page.click('[data-testid="submit"]')

    await use(page)
  },
})
```

**Uso:**
```typescript
test('usuário autenticado acessa dashboard', async ({ authenticatedPage }) => {
  await authenticatedPage.goto('/dashboard')
  await expect(authenticatedPage.locator('h1')).toHaveText('Dashboard')
})
```

---

**Recursos Adicionais:**
- [Best Practices]: [URL da documentação oficial]
- [Tutorial avançado]: [URL]

---

### TDD (Test-Driven Development)

**Fonte:** [URL de artigo/livro sobre TDD]

**Resumo:**
[Principais conceitos de TDD aplicáveis a esta feature]

**Workflow Red-Green-Refactor:**

#### 1. Red (Teste que Falha)
**Passo:**
Escrever teste ANTES da implementação

**Exemplo:**
```typescript
// auth.service.test.ts
describe('AuthService', () => {
  it('deve retornar JWT válido quando credenciais corretas', async () => {
    const authService = new AuthService()
    const result = await authService.login('user@example.com', 'password123')

    expect(result.token).toBeDefined()
    expect(result.token).toMatch(/^eyJ/)  // JWT pattern
  })
})

// ❌ Teste FALHA porque AuthService.login() ainda não existe
```

---

#### 2. Green (Implementação Mínima)
**Passo:**
Escrever código mínimo para passar no teste

**Exemplo:**
```typescript
// auth.service.ts
export class AuthService {
  async login(email: string, password: string) {
    // Implementação mínima para passar no teste
    return {
      token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
    }
  }
}

// ✅ Teste PASSA mas implementação é hardcoded
```

---

#### 3. Refactor (Melhorar Código)
**Passo:**
Melhorar implementação mantendo testes passando

**Exemplo:**
```typescript
// auth.service.ts (refatorado)
export class AuthService {
  constructor(
    private userRepo: UserRepository,
    private jwtService: JWTService
  ) {}

  async login(email: string, password: string) {
    const user = await this.userRepo.findByEmail(email)

    if (!user || !await this.verifyPassword(password, user.passwordHash)) {
      throw new UnauthorizedError('Invalid credentials')
    }

    const token = this.jwtService.sign({ userId: user.id, email: user.email })

    return { token }
  }

  private async verifyPassword(plain: string, hash: string): Promise<boolean> {
    return bcrypt.compare(plain, hash)
  }
}

// ✅ Teste CONTINUA PASSANDO mas agora com implementação real
```

---

**Quando Aplicar TDD:**
- [Cenário 1: Lógica de negócio crítica]
- [Cenário 2: Algoritmos complexos]
- [Cenário 3: Validações]

**Recursos Adicionais:**
- [Livro: Test-Driven Development by Example]: [URL]
- [Artigo: TDD Best Practices]: [URL]

---

### Linting e Formatação

**Fonte:** [URL de guia de style guide ou best practices]

**Resumo:**
[Principais configurações de linting e formatação para esta feature]

**ESLint - Regras Essenciais:**

```json
// .eslintrc.json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  "rules": {
    "no-console": "warn",            // [Por que: evitar logs em produção]
    "no-unused-vars": "error",       // [Por que: código limpo]
    "@typescript-eslint/explicit-function-return-type": "warn",
    "@typescript-eslint/no-explicit-any": "error"  // [Por que: type safety]
  }
}
```

**Prettier - Configuração:**

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 80,
  "arrowParens": "always"
}
```

**Recursos Adicionais:**
- [ESLint Rules Reference]: [URL]
- [Prettier Options]: [URL]

---

### Husky - Git Hooks

**Fonte:** [URL da documentação oficial do Husky]

**Resumo:**
[Como configurar Git hooks para garantir qualidade antes de commits/pushes]

**Setup Completo:**

```bash
# Instalação
npm install -D husky lint-staged

# Ativar hooks
npx husky install

# Adicionar ao package.json
npm pkg set scripts.prepare="husky install"
```

**Pre-commit Hook:**

```bash
# .husky/pre-commit
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npx lint-staged
```

**Lint-staged:**

```json
// .lintstagedrc.json
{
  "*.{ts,tsx}": [
    "eslint --fix",
    "prettier --write"
  ],
  "*.{json,md}": [
    "prettier --write"
  ]
}
```

**Pre-push Hook:**

```bash
# .husky/pre-push
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npm run test
npm run type-check
```

**Benefícios:**
- [Benefício 1: Previne código com erros de ir para o repo]
- [Benefício 2: Consistência de formatação no time]

**Recursos Adicionais:**
- [Husky Documentation]: [URL]
- [Lint-staged Documentation]: [URL]

---

## Artigos e Tutoriais Relevantes

### Categoria: [Nome da Categoria, ex: Segurança]

#### 1. [Título do Artigo]

**URL:** [Link para o artigo]

**Autor:** [Nome do autor]

**Fonte:** [Site/Blog, ex: Dev.to, Medium, Blog oficial]

**Data de Publicação:** [YYYY-MM-DD]

**Resumo (1-2 linhas):**
[Breve resumo do que o artigo cobre]

**Por que é relevante:**
[Como este artigo se relaciona com a feature sendo implementada]

**Principais Takeaways:**
1. [Ponto importante 1]
2. [Ponto importante 2]
3. [Ponto importante 3]

**Código/Conceitos Aplicáveis:**
```typescript
// [Trecho de código relevante do artigo que pode ser usado]
```

---

#### 2. [Título do Artigo]
[Repetir estrutura acima]

---

### Categoria: [Outra Categoria, ex: Performance]

#### 1. [Título do Artigo]
[Repetir estrutura acima]

---

## Exemplos de Implementação

### Repositório 1: [Nome do Projeto/Repositório]

**URL:** [Link para o repositório GitHub]

**Descrição:**
[Breve descrição do que o projeto faz]

**Por que é relevante:**
[Como este projeto é similar ou aplica conceitos úteis para nossa feature]

**Tecnologias Usadas:**
- [Tecnologia 1]
- [Tecnologia 2]
- [Tecnologia 3]

**O que aproveitar:**

#### 1. [Aspecto específico, ex: Estrutura de autenticação]
**Localização:** `[caminho/no/repo]`

**Descrição:**
[O que este código faz e como funciona]

**Código de referência:**
```typescript
// [Trecho de código relevante]
```

**Como adaptar para nossa feature:**
[Explicação de como modificar/usar este código]

---

#### 2. [Outro aspecto específico]
[Repetir estrutura acima]

---

**Insights Gerais:**
- [Insight 1: Padrão interessante usado]
- [Insight 2: Solução elegante para problema X]
- [Insight 3: Estrutura de testes bem feita]

---

### Repositório 2: [Nome do Projeto/Repositório]
[Repetir estrutura acima]

---

## Referências de Código

### Snippet 1: [Título descritivo, ex: Implementação de JWT com refresh token]

**Fonte:** [URL onde foi encontrado]

**Linguagem:** [TypeScript, JavaScript, etc.]

**Descrição:**
[O que este snippet faz]

**Código:**
```typescript
// [Código completo do snippet com comentários]
import jwt from 'jsonwebtoken'

interface TokenPayload {
  userId: string
  email: string
}

export function generateTokens(payload: TokenPayload) {
  // Access token: curta duração (1h)
  const accessToken = jwt.sign(payload, process.env.JWT_SECRET!, {
    expiresIn: '1h',
    algorithm: 'RS256',
  })

  // Refresh token: longa duração (7 dias)
  const refreshToken = jwt.sign(payload, process.env.JWT_REFRESH_SECRET!, {
    expiresIn: '7d',
    algorithm: 'RS256',
  })

  return { accessToken, refreshToken }
}

export function verifyAccessToken(token: string): TokenPayload {
  try {
    return jwt.verify(token, process.env.JWT_SECRET!) as TokenPayload
  } catch (error) {
    if (error instanceof jwt.TokenExpiredError) {
      throw new Error('Token expired')
    }
    throw new Error('Invalid token')
  }
}
```

**Uso:**
```typescript
const tokens = generateTokens({ userId: '123', email: 'user@example.com' })
const payload = verifyAccessToken(tokens.accessToken)
```

**Notas:**
- [Nota 1: Usar variáveis de ambiente para secrets]
- [Nota 2: RS256 é mais seguro que HS256]

---

### Snippet 2: [Título descritivo]
[Repetir estrutura acima]

---

## Comunidade e Suporte

### Fóruns e Q&A

#### Stack Overflow
**Tag:** [tag-name, ex: `next-auth`]
**URL:** https://stackoverflow.com/questions/tagged/[tag-name]

**Perguntas Relevantes:**
1. [Título da pergunta] - [URL]
   - Resumo: [Breve resumo da resposta útil]

2. [Título da pergunta] - [URL]
   - Resumo: [Breve resumo da resposta útil]

---

#### GitHub Issues
**Repositório:** [org/repo]
**URL:** [URL do repositório]

**Issues Relevantes:**
1. [#123: Título do issue] - [URL]
   - Status: [Open/Closed]
   - Resumo: [Por que é relevante, solução proposta]

2. [#456: Título do issue] - [URL]
   - Status: [Open/Closed]
   - Resumo: [Por que é relevante, solução proposta]

---

### Discord/Slack da Comunidade

**Nome da Comunidade:** [Nome]
**Link de Convite:** [URL]

**Canais Úteis:**
- `#[canal-1]`: [Para que serve]
- `#[canal-2]`: [Para que serve]

---

### Twitter/X - Contas a Seguir

- [@[username]]: [Nome] - [Por que seguir, ex: Criador da biblioteca]
- [@[username]]: [Nome] - [Por que seguir, ex: Expert em performance]

---

### Newsletters/Blogs

1. **[Nome da Newsletter]**
   - URL: [Link]
   - Frequência: [Semanal/Mensal]
   - Por que assinar: [Conteúdo relevante que cobre]

2. **[Nome do Blog]**
   - URL: [Link]
   - Tópicos: [Tópicos cobertos]
   - Artigos recomendados: [Listar 2-3]

---

## Notas Adicionais

[Quaisquer notas, ideias ou recursos que não se encaixam nas seções acima mas são importantes para referência futura]

**TODO (Pesquisa Futura):**
- [ ] [Pesquisar sobre tópico X]
- [ ] [Validar se abordagem Y é melhor que Z]
- [ ] [Ler artigo sobre performance de W]

---

**Documento criado em:** [Data]
**Última atualização:** [Data]
**Versão:** 1.0
