# Color Psychology & Palettes

## Cores por Emoção/Objetivo

### Confiança & Segurança
```
Azuis: #0066FF, #1E40AF, #3B82F6
Verdes escuros: #065F46, #047857
Uso: Fintechs, Bancos, Saúde, Seguros
```

### Inovação & Tecnologia
```
Roxos: #7C3AED, #8B5CF6
Azul elétrico: #0EA5E9, #06B6D4
Gradientes: Purple → Blue, Cyan → Blue
Uso: Tech, AI, SaaS, Startups
```

### Energia & Urgência
```
Laranjas: #F97316, #EA580C
Vermelhos: #DC2626, #EF4444
Amarelos: #EAB308, #FBBF24
Uso: E-commerce, Promoções, CTAs
```

### Luxo & Exclusividade
```
Preto: #0A0A0A, #171717
Dourado: #D4AF37, #B8860B
Roxo escuro: #581C87
Uso: Moda, Joias, Premium
```

### Natureza & Sustentabilidade
```
Verdes: #22C55E, #16A34A, #15803D
Terrosos: #A16207, #78716C
Uso: Eco, Orgânicos, Wellness
```

### Criatividade & Diversão
```
Rosa: #EC4899, #F472B6
Gradientes vibrantes: Pink → Orange, Purple → Pink
Uso: Creative, Gaming, Lifestyle
```

### Profissional & Corporativo
```
Azul navy: #1E3A5F, #0F172A
Cinzas: #475569, #64748B
Uso: Consultoria, B2B, Enterprise
```

## Estrutura de Paleta

### Mínimo necessário:
```
Primary: Cor principal (CTAs, links, destaques)
Background: Fundo principal (#FFFFFF ou #0A0A0A)
Foreground: Texto principal (#171717 ou #FAFAFA)
Muted: Backgrounds secundários
Muted-foreground: Textos secundários
Border: Bordas e divisores
```

### Completa:
```
Primary: #HEX
Primary-foreground: #HEX (texto sobre primary)
Secondary: #HEX
Secondary-foreground: #HEX
Accent: #HEX
Accent-foreground: #HEX
Background: #HEX
Foreground: #HEX
Card: #HEX
Card-foreground: #HEX
Muted: #HEX
Muted-foreground: #HEX
Border: #HEX
Input: #HEX
Ring: #HEX (focus state)
```

### Semânticas:
```
Success: #22C55E
Success-foreground: #FFFFFF
Warning: #EAB308
Warning-foreground: #000000
Error: #EF4444
Error-foreground: #FFFFFF
Info: #3B82F6
Info-foreground: #FFFFFF
```

## Gradientes Populares

### Tech/SaaS
```css
/* Purple to Blue */
background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%);

/* Cyan to Blue */
background: linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%);

/* Indigo to Purple */
background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
```

### Sunset/Warm
```css
/* Orange to Pink */
background: linear-gradient(135deg, #F97316 0%, #EC4899 100%);

/* Yellow to Orange */
background: linear-gradient(135deg, #FBBF24 0%, #F97316 100%);
```

### Nature
```css
/* Green gradient */
background: linear-gradient(135deg, #22C55E 0%, #16A34A 100%);

/* Teal */
background: linear-gradient(135deg, #14B8A6 0%, #0D9488 100%);
```

### Dark/Premium
```css
/* Dark with accent */
background: linear-gradient(135deg, #1E1E1E 0%, #0A0A0A 100%);

/* Subtle purple dark */
background: linear-gradient(135deg, #1E1B4B 0%, #0F0F1A 100%);
```

## Contraste e Acessibilidade

**Ratio mínimo WCAG:**
```
Texto normal: 4.5:1
Texto grande (18px+): 3:1
UI components: 3:1
```

**Ferramentas:**
- Contrast Checker: https://webaim.org/resources/contrastchecker/
- Coolors Contrast: https://coolors.co/contrast-checker

## Exemplo de Paleta Completa

### Tech Startup (Light Mode)
```json
{
  "primary": "#6366F1",
  "primary-foreground": "#FFFFFF",
  "secondary": "#F1F5F9",
  "secondary-foreground": "#1E293B",
  "accent": "#8B5CF6",
  "accent-foreground": "#FFFFFF",
  "background": "#FFFFFF",
  "foreground": "#0F172A",
  "card": "#FFFFFF",
  "card-foreground": "#0F172A",
  "muted": "#F1F5F9",
  "muted-foreground": "#64748B",
  "border": "#E2E8F0",
  "input": "#E2E8F0",
  "ring": "#6366F1"
}
```

### Tech Startup (Dark Mode)
```json
{
  "primary": "#818CF8",
  "primary-foreground": "#0F0F1A",
  "secondary": "#1E1E2E",
  "secondary-foreground": "#F1F5F9",
  "accent": "#A78BFA",
  "accent-foreground": "#0F0F1A",
  "background": "#0A0A0F",
  "foreground": "#F8FAFC",
  "card": "#16161F",
  "card-foreground": "#F8FAFC",
  "muted": "#1E1E2E",
  "muted-foreground": "#94A3B8",
  "border": "#2E2E3E",
  "input": "#2E2E3E",
  "ring": "#818CF8"
}
```

## Ferramentas de Referência

- Coolors: https://coolors.co/
- Color Hunt: https://colorhunt.co/
- Adobe Color: https://color.adobe.com/
- Realtime Colors: https://realtimecolors.com/
- Happy Hues: https://www.happyhues.co/
