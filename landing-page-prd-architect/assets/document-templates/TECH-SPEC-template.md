# Tech Spec: [Nome do Projeto]

## Stack Tecnológico

### Core
| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| [Framework] | [X.X] | Core framework |
| [Language] | [X.X] | Linguagem |
| [Styling] | [X.X] | Estilização |

### Dependências Principais
```json
{
  "dependencies": {
    "[pacote]": "^X.X.X",
    "[pacote]": "^X.X.X",
    "[pacote]": "^X.X.X"
  },
  "devDependencies": {
    "[pacote]": "^X.X.X"
  }
}
```

---

## Estrutura de Pastas

```
/
├── src/
│   ├── app/
│   │   ├── layout.tsx          # Root layout
│   │   ├── page.tsx            # Home page
│   │   └── globals.css         # Global styles
│   │
│   ├── components/
│   │   ├── ui/                 # Base UI components
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── input.tsx
│   │   │   └── ...
│   │   │
│   │   ├── sections/           # Page sections
│   │   │   ├── hero.tsx
│   │   │   ├── features.tsx
│   │   │   ├── testimonials.tsx
│   │   │   ├── pricing.tsx
│   │   │   ├── faq.tsx
│   │   │   ├── cta.tsx
│   │   │   └── ...
│   │   │
│   │   └── shared/             # Shared components
│   │       ├── header.tsx
│   │       ├── footer.tsx
│   │       ├── mobile-menu.tsx
│   │       └── ...
│   │
│   ├── lib/
│   │   ├── utils.ts            # Utility functions
│   │   └── constants.ts        # Constants
│   │
│   ├── hooks/
│   │   └── use-[hook].ts       # Custom hooks
│   │
│   └── types/
│       └── index.ts            # TypeScript types
│
├── public/
│   ├── images/                 # Static images
│   ├── fonts/                  # Custom fonts (if self-hosted)
│   └── favicon.ico
│
├── tailwind.config.ts
├── next.config.js
├── tsconfig.json
└── package.json
```

---

## Configurações

### Tailwind Config
```typescript
// tailwind.config.ts
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '[HEX]',
          foreground: '[HEX]',
        },
        secondary: {
          DEFAULT: '[HEX]',
          foreground: '[HEX]',
        },
        // ... demais cores da identidade visual
      },
      fontFamily: {
        sans: ['[Fonte Body]', 'sans-serif'],
        display: ['[Fonte Display]', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out',
        'fade-in-up': 'fadeInUp 0.5s ease-out',
        'slide-in': 'slideIn 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        fadeInUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideIn: {
          '0%': { transform: 'translateX(-100%)' },
          '100%': { transform: 'translateX(0)' },
        },
      },
    },
  },
  plugins: [],
}

export default config
```

### Next Config
```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    formats: ['image/avif', 'image/webp'],
    remotePatterns: [
      // Se usar imagens externas
    ],
  },
}

module.exports = nextConfig
```

---

## Componentes Base

### Button
```typescript
// Variants: primary, secondary, ghost, outline
// Sizes: sm, md, lg
// Props: asChild, loading, disabled
```

### Card
```typescript
// Parts: Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter
```

### Input
```typescript
// Variants: default, error
// Props: label, error, helperText
```

---

## SEO Configuration

```typescript
// src/app/layout.tsx
export const metadata: Metadata = {
  title: '[Título] | [Empresa]',
  description: '[Meta description - max 160 chars]',
  keywords: ['[keyword1]', '[keyword2]', '[keyword3]'],
  authors: [{ name: '[Empresa]' }],
  openGraph: {
    title: '[Título]',
    description: '[Descrição]',
    url: '[URL]',
    siteName: '[Nome do Site]',
    images: [
      {
        url: '/og-image.png',
        width: 1200,
        height: 630,
        alt: '[Alt text]',
      },
    ],
    locale: 'pt_BR',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: '[Título]',
    description: '[Descrição]',
    images: ['/og-image.png'],
  },
  robots: {
    index: true,
    follow: true,
  },
}
```

---

## Performance Targets

| Metric | Target | Tool |
|--------|--------|------|
| Performance | > 90 | Lighthouse |
| Accessibility | > 90 | Lighthouse |
| Best Practices | > 90 | Lighthouse |
| SEO | > 90 | Lighthouse |
| LCP | < 2.5s | Web Vitals |
| FID | < 100ms | Web Vitals |
| CLS | < 0.1 | Web Vitals |

### Otimizações Obrigatórias
- [ ] Images: next/image com lazy loading
- [ ] Fonts: next/font com display swap
- [ ] CSS: Purge unused (Tailwind automático)
- [ ] JS: Code splitting por rota
- [ ] Above-fold: Critical CSS inline

---

## Integrações

### Analytics
```typescript
// Implementar: [Google Analytics 4 / Vercel Analytics / Plausible]
```

### Formulários
```typescript
// Backend: [Formspree / API Route / Serverless Function]
// Validação: [Zod schema]
// Feedback: [Toast notifications]
```

### Email (se aplicável)
```typescript
// Provider: [Resend / SendGrid]
// Templates: [Lista de templates necessários]
```

---

## Deploy

### Plataforma
[Vercel / Netlify / Cloudflare Pages]

### Environment Variables
```env
# .env.local
NEXT_PUBLIC_[VAR_NAME]=value
[SECRET_VAR]=value
```

### Build Command
```bash
npm run build
```

### Output Directory
```
.next
```

---

## Checklist de Setup

### Inicial
- [ ] Criar projeto com create-next-app
- [ ] Configurar Tailwind com tema customizado
- [ ] Instalar dependências (framer-motion, lucide-react, etc.)
- [ ] Configurar estrutura de pastas
- [ ] Adicionar fontes via next/font

### Componentes
- [ ] Criar componentes base (Button, Card, Input)
- [ ] Criar Header com mobile menu
- [ ] Criar Footer
- [ ] Criar seções conforme PRD

### Conteúdo
- [ ] Adicionar imagens otimizadas
- [ ] Implementar textos do PRD
- [ ] Configurar SEO metadata

### Qualidade
- [ ] Testar responsividade
- [ ] Verificar acessibilidade
- [ ] Rodar Lighthouse
- [ ] Testar em múltiplos browsers

### Deploy
- [ ] Configurar environment variables
- [ ] Deploy para preview
- [ ] Testes finais
- [ ] Deploy para produção
