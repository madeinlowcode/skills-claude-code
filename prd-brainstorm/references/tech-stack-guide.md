# Guia de Tech Stacks

Referência para escolha de tecnologias na Fase 3 do workflow.

---

## Matriz de Decisão

### Critérios de Avaliação

| Critério | MVP Simples | Stack Robusto |
|----------|-------------|---------------|
| Tempo até produção | 1-4 semanas | 4-12 semanas |
| Curva de aprendizado | Baixa | Média-Alta |
| Custo inicial | $ | $$-$$$ |
| Escalabilidade | Limitada | Alta |
| Manutenibilidade | Média | Alta |
| Comunidade/Docs | Importante | Crítico |

### Quando escolher cada abordagem

**MVP Simples:**
- Validação de hipótese
- Projeto pessoal/side project
- Prazo apertado (< 4 semanas)
- Equipe pequena (1-2 devs)
- Orçamento limitado
- Baixo tráfego esperado

**Stack Robusto:**
- Produto já validado
- Empresa/startup com funding
- Expectativa de escala
- Equipe maior (3+ devs)
- Requisitos de compliance
- Alto tráfego esperado

---

## Stacks por Tipo de Projeto

### 1. Web App (SaaS/Dashboard)

#### Opção A: MVP Simples
```
Frontend: Next.js + Tailwind CSS
Backend:  Next.js API Routes (serverless)
Database: Supabase (PostgreSQL + Auth)
Deploy:   Vercel
Extras:   Shadcn/ui para componentes

Pros:
✓ Full-stack em um framework
✓ Deploy automático
✓ Auth + DB grátis no tier free
✓ Excelente DX

Contras:
✗ Vendor lock-in Vercel
✗ Limites do serverless
✗ Menos controle de infra
```

#### Opção B: Stack Robusto
```
Frontend: React + TypeScript + Vite
Backend:  Node.js (Express/Fastify) ou Go
Database: PostgreSQL + Redis
Deploy:   AWS (ECS/EKS) ou GCP
Extras:   Docker, Terraform

Pros:
✓ Escalabilidade horizontal
✓ Controle total de infra
✓ Otimização fine-grained
✓ Multi-cloud possível

Contras:
✗ Mais complexidade operacional
✗ Maior custo inicial
✗ Requer DevOps skills
```

---

### 2. Mobile App

#### Opção A: MVP Simples
```
Framework: React Native + Expo
Backend:   Firebase ou Supabase
Database:  Firestore ou PostgreSQL
Deploy:    Expo EAS

Pros:
✓ Código único iOS/Android
✓ Hot reload rápido
✓ OTA updates
✓ Ecossistema Expo rico

Contras:
✗ Performance não-nativa
✗ Limitações de Expo
✗ Bundle size maior
```

#### Opção B: Stack Robusto
```
Framework: Flutter ou Swift/Kotlin nativos
Backend:   Node.js/Go + GraphQL
Database:  PostgreSQL + Redis
Deploy:    App Store / Play Store direto

Pros:
✓ Performance nativa (Flutter)
✓ Acesso completo a APIs nativas
✓ Melhor UX percebida
✓ Mais controle de releases

Contras:
✗ Mais tempo de desenvolvimento
✗ Requer conhecimento específico
✗ Dois codebases (se nativo puro)
```

---

### 3. API/Backend Service

#### Opção A: MVP Simples
```
Runtime:   Node.js (Fastify/Express)
Database:  Supabase ou PlanetScale
Auth:      Clerk ou Auth0
Deploy:    Railway ou Render
Docs:      Swagger auto-gerado

Pros:
✓ Setup rápido
✓ JavaScript familiar
✓ Deploys automáticos
✓ Managed databases

Contras:
✗ Performance limitada (Node single-thread)
✗ Menos tipagem (mesmo com TS)
✗ Custos escalam rápido
```

#### Opção B: Stack Robusto
```
Runtime:   Go ou Rust
Database:  PostgreSQL + Redis
Auth:      Custom JWT ou Keycloak
Deploy:    Kubernetes (EKS/GKE)
Docs:      OpenAPI spec

Pros:
✓ Alta performance
✓ Baixo consumo de recursos
✓ Tipagem forte
✓ Escalabilidade previsível

Contras:
✗ Curva de aprendizado
✗ Desenvolvimento mais lento
✗ Menos bibliotecas prontas
```

---

### 4. E-commerce

#### Opção A: MVP Simples
```
Plataforma: Shopify ou WooCommerce
Customização: Liquid/PHP + APIs
Pagamentos: Stripe (integrado)
Deploy:     Managed pela plataforma

Pros:
✓ Pronto para vender em dias
✓ Pagamentos configurados
✓ Temas prontos
✓ SEO built-in

Contras:
✗ Taxas por transação
✗ Customização limitada
✗ Vendor lock-in forte
```

#### Opção B: Stack Robusto
```
Frontend:   Next.js + Commerce.js ou Medusa
Backend:    Medusa.js ou custom
Database:   PostgreSQL
Pagamentos: Stripe SDK direto
Deploy:     Vercel + Railway

Pros:
✓ Controle total
✓ Sem taxas por transação
✓ Customização ilimitada
✓ Headless = flexibilidade

Contras:
✗ Mais desenvolvimento
✗ Responsabilidade de PCI compliance
✗ Manutenção contínua
```

---

### 5. Landing Page / Marketing Site

#### Opção A: MVP Simples
```
Framework: Astro ou Next.js (SSG)
CMS:       Contentful ou Sanity
Styling:   Tailwind CSS
Deploy:    Vercel ou Netlify
Analytics: Plausible ou GA4

Pros:
✓ Performance excelente (SSG)
✓ SEO otimizado
✓ CDN global grátis
✓ Edição por não-devs (CMS)

Contras:
✗ Limitado para features dinâmicas
✗ Rebuild necessário para conteúdo
```

#### Opção B: Stack Robusto
```
Framework: Next.js (ISR/SSR)
CMS:       Strapi self-hosted
Styling:   Tailwind + Design System
Deploy:    Vercel + CDN custom
A/B Test:  LaunchDarkly ou custom

Pros:
✓ Conteúdo dinâmico
✓ A/B testing avançado
✓ Personalização
✓ Multi-idioma robusto

Contras:
✗ Mais infra necessária
✗ Complexidade de cache
✗ Custo maior
```

---

### 6. CLI Tool / Developer Tool

#### Opção A: MVP Simples
```
Linguagem: Node.js (Commander.js) ou Python (Click)
Package:   npm ou PyPI
Docs:      README + --help

Pros:
✓ Desenvolvimento rápido
✓ Distribuição fácil (npm/pip)
✓ Familiar para maioria
✓ Cross-platform automático

Contras:
✗ Requer runtime instalado
✗ Startup mais lento
✗ Dependências pesadas
```

#### Opção B: Stack Robusto
```
Linguagem: Go ou Rust
Build:     Binary único
Distribute: GitHub Releases + Homebrew
Docs:      Man pages + website

Pros:
✓ Binary único (zero deps)
✓ Startup instantâneo
✓ Cross-compile fácil
✓ Performance excelente

Contras:
✗ Curva de aprendizado
✗ Mais código para features simples
✗ Compilação mais lenta
```

---

### 7. Data Pipeline / ETL

#### Opção A: MVP Simples
```
Orquestração: Prefect ou Dagster Cloud
Processing:   Python + Pandas
Storage:      S3 + DuckDB
Deploy:       Managed cloud

Pros:
✓ Python familiar
✓ Managed infra
✓ UI de monitoramento
✓ Fácil debug

Contras:
✗ Custo escala rápido
✗ Limites de processamento
✗ Vendor lock-in
```

#### Opção B: Stack Robusto
```
Orquestração: Apache Airflow ou Prefect self-hosted
Processing:   Spark ou Polars
Storage:      S3 + Delta Lake
Compute:      Databricks ou EMR

Pros:
✓ Escala para PBs
✓ Processamento distribuído
✓ Ecossistema maduro
✓ Replay/backfill robusto

Contras:
✗ Complexidade operacional
✗ Custo de infra alto
✗ Requer engenharia de dados
```

---

## Comparativo de Tecnologias

### Frontend Frameworks (2024-2025)

| Framework | Learning Curve | Performance | Ecosystem | Best For |
|-----------|---------------|-------------|-----------|----------|
| Next.js | Média | Alta | Excelente | Full-stack apps |
| React + Vite | Baixa | Alta | Excelente | SPAs, libs |
| Vue 3 | Baixa | Alta | Boa | Apps progressivas |
| Svelte | Baixa | Excelente | Crescendo | Apps leves |
| Astro | Baixa | Excelente | Boa | Sites estáticos |

### Backend Frameworks

| Framework | Language | Performance | Learning | Best For |
|-----------|----------|-------------|----------|----------|
| Next.js API | JS/TS | Média | Baixa | Full-stack |
| Express | JS/TS | Média | Baixa | APIs simples |
| Fastify | JS/TS | Alta | Média | APIs performáticas |
| Go (std lib) | Go | Excelente | Média | Microservices |
| Rust (Actix) | Rust | Excelente | Alta | High-perf |
| FastAPI | Python | Boa | Baixa | ML/Data APIs |

### Databases

| Database | Type | Scaling | Best For |
|----------|------|---------|----------|
| PostgreSQL | Relational | Vertical + Read replicas | Maioria dos casos |
| Supabase | PostgreSQL managed | Auto | MVPs |
| PlanetScale | MySQL managed | Horizontal | Scale sem ops |
| MongoDB | Document | Horizontal | Schemas flexíveis |
| Redis | Key-Value | Cluster | Cache, sessions |
| DynamoDB | Key-Value | Auto | Serverless |

### Deploy Platforms

| Platform | Complexity | Cost (start) | Best For |
|----------|------------|--------------|----------|
| Vercel | Baixa | Free | Next.js apps |
| Netlify | Baixa | Free | Static + Functions |
| Railway | Baixa | $5/mo | Full-stack |
| Render | Baixa | Free tier | Containers |
| Fly.io | Média | Pay-as-go | Edge deploy |
| AWS | Alta | Pay-as-go | Enterprise |

---

## Checklist de Decisão

### Antes de escolher, responda:

```markdown
## Contexto do Projeto
- [ ] Qual o prazo? ____
- [ ] Qual o orçamento? ____
- [ ] Quantos devs? ____
- [ ] Nível de experiência da equipe? ____

## Requisitos Técnicos
- [ ] Usuários esperados (pico): ____
- [ ] Requisitos de latência: ____
- [ ] Precisa de real-time? ____
- [ ] Precisa de offline? ____
- [ ] Compliance específico? ____

## Preferências
- [ ] Linguagem preferida: ____
- [ ] Cloud preferido: ____
- [ ] Já tem infra existente? ____
```

### Regra de Ouro

> "Use a tecnologia mais simples que atende aos requisitos atuais,
> não aos requisitos imaginários do futuro."

---

## Recursos para Pesquisa

### Onde pesquisar stacks atuais
- [StackShare](https://stackshare.io/) - Stacks de empresas reais
- [ThoughtWorks Radar](https://www.thoughtworks.com/radar) - Tendências
- [State of JS/CSS](https://stateofjs.com/) - Surveys anuais
- [GitHub Trends](https://github.com/trending) - Projetos em alta
- [HackerNews](https://news.ycombinator.com/) - Discussões técnicas

### Queries úteis para WebSearch
```
"[tipo de projeto] tech stack 2025"
"[tecnologia] vs [alternativa] comparison 2025"
"[tecnologia] production experience"
"[startup famosa] tech stack"
"best [categoria] framework 2025"
```
