# Identidade Visual: [Nome do Projeto]

## Paleta de Cores

### Cores Principais
| Nome | HEX | Uso |
|------|-----|-----|
| Primary | #[HEX] | CTAs, links, destaques principais |
| Primary Foreground | #[HEX] | Texto sobre primary |
| Secondary | #[HEX] | Elementos complementares |
| Secondary Foreground | #[HEX] | Texto sobre secondary |
| Accent | #[HEX] | Destaques especiais, badges |
| Accent Foreground | #[HEX] | Texto sobre accent |

### Cores de Background
| Nome | HEX | Uso |
|------|-----|-----|
| Background | #[HEX] | Fundo principal |
| Foreground | #[HEX] | Texto principal |
| Card | #[HEX] | Fundo de cards |
| Card Foreground | #[HEX] | Texto em cards |
| Muted | #[HEX] | Backgrounds secundários |
| Muted Foreground | #[HEX] | Textos secundários |

### Cores de UI
| Nome | HEX | Uso |
|------|-----|-----|
| Border | #[HEX] | Bordas e divisores |
| Input | #[HEX] | Background de inputs |
| Ring | #[HEX] | Focus state |

### Cores Semânticas
| Nome | HEX | Uso |
|------|-----|-----|
| Success | #22C55E | Confirmações, sucesso |
| Warning | #EAB308 | Alertas, atenção |
| Error | #EF4444 | Erros, problemas |
| Info | #3B82F6 | Informações |

### Gradientes
```css
/* Primary Gradient */
--gradient-primary: linear-gradient(135deg, #[HEX1] 0%, #[HEX2] 100%);

/* Background Gradient */
--gradient-bg: linear-gradient(180deg, #[HEX1] 0%, #[HEX2] 100%);

/* Accent Gradient */
--gradient-accent: linear-gradient(90deg, #[HEX1] 0%, #[HEX2] 100%);
```

---

## Tipografia

### Fontes
| Uso | Fonte | Fallback |
|-----|-------|----------|
| Display/Headlines | [Fonte] | sans-serif |
| Body | [Fonte] | sans-serif |
| Monospace | [Fonte] | monospace |

### Google Fonts Import
```html
<link href="https://fonts.googleapis.com/css2?family=[Fonte1]:wght@[weights]&family=[Fonte2]:wght@[weights]&display=swap" rel="stylesheet">
```

### Hierarquia Desktop
| Elemento | Size | Weight | Line Height | Letter Spacing |
|----------|------|--------|-------------|----------------|
| H1 | 64px | 700 | 1.1 | -0.02em |
| H2 | 48px | 700 | 1.2 | -0.02em |
| H3 | 32px | 600 | 1.3 | -0.01em |
| H4 | 24px | 600 | 1.4 | 0 |
| Body Large | 18px | 400 | 1.6 | 0 |
| Body | 16px | 400 | 1.6 | 0 |
| Small | 14px | 400 | 1.5 | 0 |
| Caption | 12px | 500 | 1.4 | 0.02em |

### Hierarquia Mobile
| Elemento | Size | Weight |
|----------|------|--------|
| H1 | 40px | 700 |
| H2 | 32px | 700 |
| H3 | 24px | 600 |
| H4 | 20px | 600 |
| Body | 16px | 400 |

---

## Ícones

### Biblioteca
- **Nome:** [Lucide/Phosphor/Heroicons]
- **Estilo:** [Outline/Solid/Duotone]
- **Stroke Width:** [1.5/2]

### Tamanhos
| Nome | Size | Uso |
|------|------|-----|
| XS | 14px | Inline com texto pequeno |
| SM | 16px | Buttons small, badges |
| MD | 20px | UI geral, buttons |
| LG | 24px | Cards, features |
| XL | 32px | Destaques |
| 2XL | 48px | Hero, ilustrações |

### Cores
- **Default:** currentColor (herda do texto)
- **Primary:** var(--primary)
- **Muted:** var(--muted-foreground)
- **Success/Error/Warning:** cores semânticas

---

## Espaçamento

### Sistema Base (4px)
```
--space-1: 4px
--space-2: 8px
--space-3: 12px
--space-4: 16px
--space-5: 20px
--space-6: 24px
--space-8: 32px
--space-10: 40px
--space-12: 48px
--space-16: 64px
--space-20: 80px
--space-24: 96px
```

### Seções
- Padding vertical: 80px (desktop) / 48px (mobile)
- Container max-width: 1280px
- Container padding: 24px (desktop) / 16px (mobile)

### Componentes
- Card padding: 24px
- Button padding: 12px 24px (md)
- Input padding: 12px 16px
- Gap entre cards: 24px

---

## Componentes

### Buttons

#### Primary
```
Background: var(--primary)
Text: var(--primary-foreground)
Hover: opacity 90%, translateY(-2px)
Active: scale(0.98)
Border-radius: 8px
```

#### Secondary
```
Background: var(--secondary)
Text: var(--secondary-foreground)
Border: 1px solid var(--border)
```

#### Ghost
```
Background: transparent
Text: var(--foreground)
Hover: var(--muted)
```

#### Sizes
| Size | Padding | Font Size | Height |
|------|---------|-----------|--------|
| SM | 8px 16px | 14px | 36px |
| MD | 12px 24px | 16px | 44px |
| LG | 16px 32px | 18px | 52px |

### Cards
```
Background: var(--card)
Border: 1px solid var(--border)
Border-radius: 12px
Shadow: 0 1px 3px rgba(0,0,0,0.1)
Hover shadow: 0 4px 12px rgba(0,0,0,0.15)
```

### Inputs
```
Background: var(--input)
Border: 1px solid var(--border)
Border-radius: 8px
Focus: ring 2px var(--ring)
Placeholder: var(--muted-foreground)
```

### Badges
```
Background: var(--accent)
Text: var(--accent-foreground)
Padding: 4px 12px
Border-radius: 9999px
Font-size: 12px
Font-weight: 500
```

---

## Efeitos

### Sombras
```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);
```

### Border Radius
```css
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 16px;
--radius-full: 9999px;
```

### Transições
```css
--transition-fast: 150ms ease;
--transition-base: 200ms ease;
--transition-slow: 300ms ease;
--transition-spring: 500ms cubic-bezier(0.16, 1, 0.3, 1);
```

---

## Referências Visuais

### Inspiração 1
- **URL:** [Link]
- **O que usar:** [Descrição]

### Inspiração 2
- **URL:** [Link]
- **O que usar:** [Descrição]

### Inspiração 3
- **URL:** [Link]
- **O que usar:** [Descrição]
