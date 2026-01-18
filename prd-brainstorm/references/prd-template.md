# PRD Template

Este é o template estruturado para geração do Product Requirements Document.

---

## Estrutura do Arquivo PRD

```markdown
# PRD: [Nome do Projeto]

## Metadata
| Campo         | Valor                    |
|---------------|--------------------------|
| Projeto       | [Nome]                   |
| Versão        | 1.0.0                    |
| Data          | [YYYY-MM-DD]             |
| Status        | Draft / Review / Approved|
| Autor         | [Nome]                   |
| Stakeholders  | [Lista]                  |

---

## 1. Overview

### 1.1 Problema
[Descrição clara e concisa do problema que este produto resolve]

- **Dor principal:** [Uma frase]
- **Impacto:** [Quantificado se possível]
- **Frequência:** [Com que frequência o problema ocorre]

### 1.2 Solução Proposta
[Descrição da solução em alto nível]

### 1.3 Objetivo
[O que o produto deve alcançar - objetivo SMART]

---

## 2. Contexto

### 2.1 Background
[Por que estamos construindo isso agora? Qual o contexto de negócio?]

### 2.2 Usuários Alvo

#### Persona Principal
| Atributo        | Descrição                |
|-----------------|--------------------------|
| Nome            | [Nome fictício]          |
| Idade           | [Faixa etária]           |
| Ocupação        | [Profissão]              |
| Nível técnico   | Baixo / Médio / Alto     |
| Objetivos       | [Lista]                  |
| Frustrações     | [Lista]                  |
| Ferramentas     | [O que usa hoje]         |

#### Personas Secundárias
[Se aplicável]

### 2.3 Métricas de Sucesso
| Métrica              | Meta              | Como medir           |
|----------------------|-------------------|----------------------|
| [Métrica 1]          | [Valor target]    | [Método]             |
| [Métrica 2]          | [Valor target]    | [Método]             |
| [Métrica 3]          | [Valor target]    | [Método]             |

---

## 3. Assumptions

### 3.1 Suposições de Valor
| # | Suposição | Risco | Como validar |
|---|-----------|-------|--------------|
| 1 | [Texto]   | Alto/Médio/Baixo | [Método] |
| 2 | [Texto]   | Alto/Médio/Baixo | [Método] |

### 3.2 Suposições de Usabilidade
| # | Suposição | Risco | Como validar |
|---|-----------|-------|--------------|
| 1 | [Texto]   | Alto/Médio/Baixo | [Método] |

### 3.3 Suposições de Viabilidade
| # | Suposição | Risco | Como validar |
|---|-----------|-------|--------------|
| 1 | [Texto]   | Alto/Médio/Baixo | [Método] |

### 3.4 Riscos Identificados
| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| [Risco 1] | Alta/Média/Baixa | Alto/Médio/Baixo | [Ação] |

---

## 4. Scope

### 4.1 In Scope (MVP)
- [ ] [Feature 1] - [Breve descrição]
- [ ] [Feature 2] - [Breve descrição]
- [ ] [Feature 3] - [Breve descrição]

### 4.2 Out of Scope
- [Feature X] - Motivo: [Por que não agora]
- [Feature Y] - Motivo: [Por que não agora]

### 4.3 Future Considerations (v2+)
- [Feature futura 1]
- [Feature futura 2]

---

## 5. User Stories

### Épico 1: [Nome do Épico]

#### US-001: [Título da Story]
**Como** [tipo de usuário],
**Quero** [ação/capacidade],
**Para** [benefício/resultado].

**Critérios de Aceitação:**
- [ ] [Critério 1]
- [ ] [Critério 2]
- [ ] [Critério 3]

**Prioridade:** Must Have / Should Have / Could Have / Won't Have
**Estimativa:** [P/M/G ou Story Points]

---

#### US-002: [Título da Story]
**Como** [tipo de usuário],
**Quero** [ação/capacidade],
**Para** [benefício/resultado].

**Critérios de Aceitação:**
- [ ] [Critério 1]
- [ ] [Critério 2]

**Prioridade:** Must Have / Should Have / Could Have / Won't Have
**Estimativa:** [P/M/G ou Story Points]

---

### Épico 2: [Nome do Épico]
[Repetir estrutura de User Stories]

---

## 6. Technical Stack

### 6.1 Stack Escolhida
| Camada       | Tecnologia    | Versão   | Justificativa        |
|--------------|---------------|----------|----------------------|
| Frontend     | [Tech]        | [X.X.X]  | [Por que essa]       |
| Backend      | [Tech]        | [X.X.X]  | [Por que essa]       |
| Database     | [Tech]        | [X.X.X]  | [Por que essa]       |
| Infra/Deploy | [Tech]        | [X.X.X]  | [Por que essa]       |
| Outros       | [Tech]        | [X.X.X]  | [Por que essa]       |

### 6.2 Alternativas Consideradas
| Tecnologia    | Prós                | Contras              | Por que não |
|---------------|---------------------|----------------------|-------------|
| [Alt 1]       | [Lista]             | [Lista]              | [Motivo]    |
| [Alt 2]       | [Lista]             | [Lista]              | [Motivo]    |

### 6.3 Requisitos Técnicos
- **Performance:** [Requisitos de tempo de resposta, throughput]
- **Escalabilidade:** [Requisitos de carga, crescimento esperado]
- **Segurança:** [Requisitos de autenticação, autorização, compliance]
- **Disponibilidade:** [SLA esperado]

---

## 7. Success Metrics

### 7.1 KPIs Primários
| KPI | Baseline | Meta (30 dias) | Meta (90 dias) |
|-----|----------|----------------|----------------|
| [KPI 1] | [Atual] | [Target] | [Target] |
| [KPI 2] | [Atual] | [Target] | [Target] |

### 7.2 KPIs Secundários
| KPI | Descrição | Como medir |
|-----|-----------|------------|
| [KPI] | [Descrição] | [Método] |

### 7.3 Critérios de Sucesso do MVP
- [ ] [Critério 1]
- [ ] [Critério 2]
- [ ] [Critério 3]

---

## 8. Dependencies & Blockers

### 8.1 Dependências Internas
| Dependência | Owner | Status | Data esperada |
|-------------|-------|--------|---------------|
| [Dep 1]     | [Quem]| Pendente/Em andamento/Concluído | [Data] |

### 8.2 Dependências Externas
| Dependência | Fornecedor | Status | Risco |
|-------------|------------|--------|-------|
| [Dep 1]     | [Quem]     | [Status] | [Risco] |

### 8.3 Blockers Atuais
| Blocker | Impacto | Owner | Ação necessária |
|---------|---------|-------|-----------------|
| [Blocker] | [Impacto] | [Quem] | [Ação] |

---

## 9. Timeline

### 9.1 Milestones
| Milestone | Descrição | Data Target |
|-----------|-----------|-------------|
| M1: Kickoff | Início do desenvolvimento | [Data] |
| M2: Alpha | Features core funcionando | [Data] |
| M3: Beta | Versão testável | [Data] |
| M4: Release | Lançamento MVP | [Data] |

### 9.2 Fases
```
[Semana 1-2] Fase 1: Setup & Arquitetura
[Semana 3-4] Fase 2: Core Features
[Semana 5-6] Fase 3: Integração & Testes
[Semana 7]   Fase 4: Polish & Deploy
```

---

## 10. Próximos Passos

### Ações Imediatas
1. [ ] Revisar PRD com stakeholders
2. [ ] Executar `/sprint-context-generator` para contexto técnico
3. [ ] Criar tasks no backlog

### Integração com Sprint Context
Este PRD será usado como entrada para o `sprint-context-generator`, que irá:
- Importar problema, solução e user stories
- Definir arquitetura técnica detalhada
- Criar estrutura de tarefas do sprint

---

## Changelog

| Versão | Data | Autor | Mudanças |
|--------|------|-------|----------|
| 1.0.0  | [Data] | [Autor] | Versão inicial |

---

## Aprovações

| Role | Nome | Data | Status |
|------|------|------|--------|
| Product Owner | [Nome] | [Data] | Pendente / Aprovado |
| Tech Lead | [Nome] | [Data] | Pendente / Aprovado |
| Stakeholder | [Nome] | [Data] | Pendente / Aprovado |
```

---

## Notas de Uso

### Preenchimento Mínimo (MVP do PRD)
Para projetos pequenos ou provas de conceito, as seções obrigatórias são:
1. Overview (problema + solução)
2. Scope (in/out)
3. User Stories (pelo menos 3)
4. Technical Stack
5. Próximos Passos

### Preenchimento Completo
Para projetos maiores ou com múltiplos stakeholders, preencha todas as seções.

### Formatação
- Use Markdown válido
- Mantenha tabelas alinhadas
- Use checkboxes para itens acionáveis
- Inclua datas no formato YYYY-MM-DD
