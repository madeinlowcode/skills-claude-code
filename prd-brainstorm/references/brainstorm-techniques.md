# Técnicas de Brainstorming para Product Discovery

Este documento detalha as 3 técnicas principais usadas na Fase 2 do workflow.

---

## 1. Opportunity Solution Tree (OST)

### O que é?
Framework criado por Teresa Torres para conectar outcomes de negócio a oportunidades de usuário e soluções testáveis.

### Estrutura

```
                         ┌─────────────────────┐
                         │   OUTCOME DESEJADO  │
                         │  (Métrica de negócio)│
                         └──────────┬──────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            │                       │                       │
   ┌────────┴────────┐    ┌────────┴────────┐    ┌────────┴────────┐
   │  OPORTUNIDADE 1 │    │  OPORTUNIDADE 2 │    │  OPORTUNIDADE 3 │
   │ (Dor do usuário)│    │ (Dor do usuário)│    │ (Dor do usuário)│
   └────────┬────────┘    └────────┬────────┘    └────────┬────────┘
            │                       │                       │
      ┌─────┴─────┐           ┌─────┴─────┐           ┌─────┴─────┐
      │           │           │           │           │           │
   ┌──┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐
   │Sol A│     │Sol B│     │Sol C│     │Sol D│     │Sol E│     │Sol F│
   └─────┘     └─────┘     └─────┘     └─────┘     └─────┘     └─────┘
```

### Como Facilitar

#### Passo 1: Definir o Outcome
```
Pergunte:
"Qual resultado de negócio você quer alcançar com este produto?"

Exemplos de bons outcomes:
- "Aumentar retenção de usuários em 20% nos próximos 6 meses"
- "Reduzir tempo de onboarding de 15min para 5min"
- "Aumentar NPS de 30 para 50"
- "Reduzir churn mensal de 5% para 2%"

Características de um bom outcome:
✓ Mensurável (número específico)
✓ Temporal (prazo definido)
✓ Alinhado com estratégia do negócio
✓ Impactado pelo comportamento do usuário
```

#### Passo 2: Mapear Oportunidades
```
Pergunte:
"Quais problemas ou necessidades dos usuários, se resolvidos,
levariam a esse resultado?"

Técnica: Para cada oportunidade, pergunte "Por quê?"
- Por que o usuário abandona? → Não encontra o que procura
- Por que não encontra? → Busca não funciona bem
- Por que busca não funciona? → Resultados irrelevantes

Objetivo: Encontrar 3-5 oportunidades raiz
```

#### Passo 3: Gerar Soluções
```
Para cada oportunidade, pergunte:
"Que soluções podemos testar para resolver isso?"

Regras:
- Gere 2-3 soluções por oportunidade
- Soluções devem ser testáveis rapidamente
- Evite grandes apostas; prefira experimentos pequenos
```

### Exemplo Completo

```
OUTCOME: Aumentar conversão de trial para pago de 10% para 20%

OPORTUNIDADES:
├── 1. Usuários não entendem o valor durante trial
│   ├── Sol A: Onboarding guiado com casos de uso
│   ├── Sol B: Email sequence com dicas diárias
│   └── Sol C: Dashboard de "valor gerado"
│
├── 2. Trial muito curto para projetos complexos
│   ├── Sol A: Extensão de trial condicional
│   └── Sol B: Trial baseado em uso, não tempo
│
└── 3. Preço não é claro
    ├── Sol A: Calculadora de ROI
    └── Sol B: Comparativo com concorrentes
```

---

## 2. Jobs To Be Done (JTBD)

### O que é?
Framework que foca no "trabalho" que o usuário quer realizar, não no produto em si.

### A Frase JTBD

```
"Quando [SITUAÇÃO/CONTEXTO],
 eu quero [AÇÃO/MOTIVAÇÃO],
 para que [RESULTADO ESPERADO]."
```

### Os 3 Tipos de Jobs

#### Jobs Funcionais
O que o usuário quer **realizar** praticamente.

```
Exemplos:
- "Quando estou no trânsito, quero saber o tempo de chegada,
   para planejar meu dia."

- "Quando recebo uma fatura, quero registrá-la rapidamente,
   para manter controle financeiro."

- "Quando preciso compartilhar um arquivo grande, quero enviá-lo
   sem limite de tamanho, para não depender de email."
```

#### Jobs Emocionais
Como o usuário quer **se sentir**.

```
Exemplos:
- "Quando uso a ferramenta, quero me sentir no controle,
   para reduzir minha ansiedade sobre o projeto."

- "Quando compartilho relatórios, quero parecer profissional,
   para ganhar respeito da equipe."

- "Quando aprendo algo novo, quero sentir que estou progredindo,
   para manter motivação."
```

#### Jobs Sociais
Como o usuário quer **ser percebido**.

```
Exemplos:
- "Quando apresento para clientes, quero usar ferramentas modernas,
   para ser visto como inovador."

- "Quando colaboro com a equipe, quero contribuir visivelmente,
   para ser reconhecido pelo meu trabalho."

- "Quando escolho ferramentas, quero recomendar as melhores,
   para ser visto como referência técnica."
```

### Como Facilitar

#### Técnica de Entrevista
```
1. Identifique um momento específico de uso
   "Me conta sobre a última vez que você precisou [fazer X]..."

2. Explore o contexto
   "O que estava acontecendo nesse momento?"
   "O que você estava tentando alcançar?"

3. Capture a emoção
   "Como você se sentiu quando [situação]?"
   "O que seria ideal nesse momento?"

4. Entenda as alternativas
   "O que você fez para resolver?"
   "Por que escolheu essa abordagem?"
```

#### Template de Documentação
```
JOB #1: [Nome descritivo]
├── Situação: [Quando acontece]
├── Motivação: [O que quer fazer]
├── Resultado: [O que espera alcançar]
├── Tipo: Funcional / Emocional / Social
└── Frequência: Diária / Semanal / Mensal / Eventual
```

### Exemplo Completo

```
PROJETO: App de gestão de tarefas para freelancers

JOBS FUNCIONAIS:
1. "Quando recebo um novo projeto, quero quebrar em tarefas menores,
    para ter clareza do escopo."

2. "Quando estou trabalhando, quero registrar tempo automaticamente,
    para faturar corretamente."

JOBS EMOCIONAIS:
1. "Quando tenho múltiplos clientes, quero visualizar tudo em um lugar,
    para me sentir organizado e no controle."

2. "Quando entrego um projeto, quero ver métricas de produtividade,
    para sentir que fui eficiente."

JOBS SOCIAIS:
1. "Quando apresento progresso para clientes, quero mostrar relatórios
    profissionais, para ser visto como organizado."

2. "Quando indico ferramentas para outros freelancers, quero recomendar
    algo moderno, para ser visto como atualizado."
```

---

## 3. Assumption Mapping

### O que é?
Técnica para identificar e priorizar suposições que fundamentam o produto.

### Categorias de Suposições

```
┌─────────────────────────────────────────────────────────────────┐
│                      SUPOSIÇÕES DE VALOR                        │
│  "Os usuários querem isso?"                                     │
│  - O problema existe e é relevante                              │
│  - Os usuários pagariam por uma solução                         │
│  - A solução resolve o problema de forma satisfatória           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    SUPOSIÇÕES DE USABILIDADE                    │
│  "Os usuários conseguem usar?"                                  │
│  - Os usuários entendem a interface                             │
│  - Os usuários completam as tarefas principais                  │
│  - A curva de aprendizado é aceitável                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    SUPOSIÇÕES DE VIABILIDADE                    │
│  "Conseguimos construir?"                                       │
│  - A tecnologia existe e é acessível                            │
│  - Temos (ou podemos adquirir) as competências                  │
│  - O custo é viável dentro do orçamento                         │
│  - O prazo é realista                                           │
└─────────────────────────────────────────────────────────────────┘
```

### Matriz de Priorização

```
                         ALTO IMPACTO
                              │
                              │
    ┌─────────────────────────┼─────────────────────────┐
    │                         │                         │
    │    TESTAR DEPOIS        │    TESTAR PRIMEIRO      │
    │                         │                         │
    │  • Baixa incerteza      │  • Alta incerteza       │
    │  • Alto impacto         │  • Alto impacto         │
    │  • Risco moderado       │  • MAIOR RISCO          │
    │                         │                         │
────┼─────────────────────────┼─────────────────────────┼────
    │                         │                         │
BAIXA                         │                         ALTA
INCERTEZA                     │                      INCERTEZA
    │                         │                         │
    │    ASSUMIR COMO OK      │    MONITORAR            │
    │                         │                         │
    │  • Baixa incerteza      │  • Alta incerteza       │
    │  • Baixo impacto        │  • Baixo impacto        │
    │  • Pode prosseguir      │  • Ficar de olho        │
    │                         │                         │
    └─────────────────────────┼─────────────────────────┘
                              │
                              │
                         BAIXO IMPACTO
```

### Como Facilitar

#### Passo 1: Coletar Suposições
```
Para cada categoria, pergunte:
"O que precisa ser verdade para este produto ter sucesso?"

Técnica: Complete as frases
- "Acreditamos que os usuários querem..."
- "Assumimos que os usuários conseguem..."
- "Supomos que tecnicamente podemos..."
```

#### Passo 2: Classificar
```
Para cada suposição, pergunte:

IMPACTO:
"Se essa suposição estiver errada, qual o impacto no produto?"
- Alto: Produto não funciona / não tem valor
- Médio: Produto funciona parcialmente
- Baixo: Impacto mínimo

INCERTEZA:
"Quão confiantes estamos de que essa suposição é verdadeira?"
- Alta incerteza: Não temos dados, é um palpite
- Média incerteza: Temos alguns indícios
- Baixa incerteza: Temos evidências fortes
```

#### Passo 3: Planejar Validação
```
Para suposições no quadrante "TESTAR PRIMEIRO":

MÉTODOS DE VALIDAÇÃO:
- Entrevistas com usuários (qualitativo)
- Pesquisa/survey (quantitativo)
- Protótipo/mockup (usabilidade)
- Spike técnico (viabilidade)
- Análise de concorrentes (mercado)
- Teste A/B (comportamento)
```

### Template de Documentação

```markdown
## Assumption Map

### Alta Prioridade (Testar Primeiro)
| ID | Suposição | Tipo | Impacto | Incerteza | Validação |
|----|-----------|------|---------|-----------|-----------|
| A1 | Usuários querem X | Valor | Alto | Alta | Entrevistas |
| A2 | É possível integrar com Y | Viabilidade | Alto | Alta | Spike técnico |

### Média Prioridade (Testar Depois)
| ID | Suposição | Tipo | Impacto | Incerteza | Validação |
|----|-----------|------|---------|-----------|-----------|
| A3 | Usuários preferem mobile | Usabilidade | Alto | Média | Analytics |

### Baixa Prioridade (Monitorar)
| ID | Suposição | Tipo | Impacto | Incerteza | Validação |
|----|-----------|------|---------|-----------|-----------|
| A4 | Mercado vai crescer | Valor | Médio | Alta | Pesquisa |

### Assumir como OK
| ID | Suposição | Tipo | Justificativa |
|----|-----------|------|---------------|
| A5 | Usuários têm internet | Viabilidade | Público-alvo urbano |
```

### Exemplo Completo

```
PROJETO: Plataforma de mentoria online

SUPOSIÇÕES DE VALOR:
1. "Profissionais juniores querem mentoria estruturada"
   └── Impacto: Alto | Incerteza: Média | Validar: Pesquisa

2. "Mentores seniores têm tempo disponível para mentorar"
   └── Impacto: Alto | Incerteza: Alta | Validar: Entrevistas

SUPOSIÇÕES DE USABILIDADE:
1. "Usuários conseguem agendar sessões sem suporte"
   └── Impacto: Médio | Incerteza: Baixa | Validar: Teste de usabilidade

2. "Videoconferência integrada é preferida vs. links externos"
   └── Impacto: Médio | Incerteza: Alta | Validar: A/B test

SUPOSIÇÕES DE VIABILIDADE:
1. "Podemos integrar pagamentos recorrentes"
   └── Impacto: Alto | Incerteza: Baixa | Validar: Pesquisa de APIs

2. "Custo de infra de vídeo é viável"
   └── Impacto: Alto | Incerteza: Alta | Validar: Spike técnico

PRIORIZAÇÃO:
TESTAR PRIMEIRO:
- [A2] Mentores têm tempo disponível
- [V2] Custo de infra de vídeo

TESTAR DEPOIS:
- [A1] Juniores querem mentoria estruturada
- [U2] Vídeo integrado vs. externo

MONITORAR:
- [U1] Agendamento sem suporte

ASSUMIR OK:
- [V1] Integração de pagamentos (APIs maduras disponíveis)
```

---

## Combinando as Técnicas

### Fluxo Recomendado

```
1. JTBD → Entender o "porquê" do usuário
   ↓
2. OST → Conectar jobs a outcomes e soluções
   ↓
3. Assumption Mapping → Validar o que precisa ser verdade
```

### Matriz de Integração

```
┌─────────────────┬──────────────────┬───────────────────────┐
│     JTBD        │       OST        │   Assumption Map      │
├─────────────────┼──────────────────┼───────────────────────┤
│ Jobs Funcionais │ → Oportunidades  │ → Suposições de Valor │
│ Jobs Emocionais │ → Outcomes       │ → Suposições de Uso   │
│ Jobs Sociais    │ → Soluções       │ → Suposições Técnicas │
└─────────────────┴──────────────────┴───────────────────────┘
```

---

## Recursos Adicionais

### Livros
- "Continuous Discovery Habits" - Teresa Torres (OST)
- "Jobs to Be Done" - Anthony Ulwick
- "The Lean Startup" - Eric Ries (Validação de suposições)

### Ferramentas
- Miro/FigJam - Para árvores visuais
- Notion - Para documentação estruturada
- ProductBoard - Para gestão de insights

### Templates Online
- [OST Template - Miro](https://miro.com/templates/opportunity-solution-tree/)
- [JTBD Canvas - Strategyzer](https://www.strategyzer.com/)
