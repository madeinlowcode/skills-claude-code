# Tech Stack Guide

## Frameworks

### Next.js (Recomendado)
**Quando usar:**
- Projetos React que precisam de SSR/SSG
- SEO é importante
- Precisa de API routes
- Quer deploy fácil na Vercel

**Setup:**
```bash
npx create-next-app@latest [nome] --typescript --tailwind --eslint --app
```

### Astro
**Quando usar:**
- Sites estáticos/content-focused
- Performance é prioridade máxima
- Pouca interatividade JS
- Blog, portfolio, landing page simples

**Setup:**
```bash
npm create astro@latest
```

### React + Vite
**Quando usar:**
- SPA simples
- Não precisa de SSR
- Protótipos rápidos
- Bundle size importa

**Setup:**
```bash
npm create vite@latest [nome] -- --template react-ts
```

### HTML/CSS/JS Puro
**Quando usar:**
- Página única muito simples
- Sem interatividade complexa
- Cliente quer editar diretamente

## Styling

### Tailwind CSS (Recomendado)
**Por que usar:**
- Desenvolvimento rápido
- Design system built-in
- Purge automático de CSS não usado
- Fácil customização

**Configuração base:**
```js
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#6366F1',
        // ...
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Space Grotesk', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
```

### CSS Modules
**Quando usar:**
- Projeto já existente sem Tailwind
- Preferência por CSS tradicional
- Escopo automático de estilos

### Styled Components
**Quando usar:**
- Projetos React que preferem CSS-in-JS
- Temas dinâmicos
- Props-based styling

## Animações

### Framer Motion (React)
```bash
npm install framer-motion
```
**Uso:**
```jsx
import { motion } from 'framer-motion'

<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5 }}
>
```

### GSAP (Qualquer)
```bash
npm install gsap
```
**Uso:**
```js
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)
```

### AOS (Simples)
```bash
npm install aos
```
**Uso:**
```html
<div data-aos="fade-up" data-aos-delay="100">
```

## Componentes UI

### shadcn/ui (Recomendado para Next.js)
```bash
npx shadcn@latest init
npx shadcn@latest add button card input
```

### Radix UI (Primitivos)
```bash
npm install @radix-ui/react-dialog @radix-ui/react-dropdown-menu
```

### Headless UI (Tailwind)
```bash
npm install @headlessui/react
```

## Formulários

### React Hook Form
```bash
npm install react-hook-form
```

### Zod (Validação)
```bash
npm install zod @hookform/resolvers
```

## Integrações

### Analytics
- **Vercel Analytics:** Built-in para Vercel
- **Google Analytics 4:** Universal
- **Plausible:** Privacy-focused

### Email
- **Resend:** Modern, developer-friendly
- **SendGrid:** Enterprise
- **Mailchimp:** Marketing

### Pagamentos
- **Stripe:** Padrão do mercado
- **LemonSqueezy:** Simpler para digital products

### CRM/Forms
- **HubSpot:** Full-featured
- **Formspree:** Simple forms
- **ConvertKit:** Creators

## Deploy

### Vercel (Recomendado para Next.js)
- Deploy automático via Git
- Edge functions
- Analytics built-in
- Preview deployments

### Netlify
- Bom para Astro/static
- Forms built-in
- Functions serverless

### Cloudflare Pages
- CDN global
- Workers
- Gratuito generoso

## Stack Recomendada por Tipo

### Landing Page Tech/SaaS
```
Framework: Next.js 14 (App Router)
Styling: Tailwind CSS
UI: shadcn/ui
Animations: Framer Motion
Icons: Lucide React
Forms: React Hook Form + Zod
Analytics: Vercel Analytics
Deploy: Vercel
```

### Landing Page Simples/Rápida
```
Framework: Astro
Styling: Tailwind CSS
Animations: AOS
Icons: Lucide (via CDN)
Forms: Formspree
Deploy: Netlify
```

### Landing Page E-commerce
```
Framework: Next.js 14
Styling: Tailwind CSS
UI: shadcn/ui
Animations: GSAP
Icons: Lucide React
Payment: Stripe
Analytics: GA4
Deploy: Vercel
```

## Estrutura de Pastas (Next.js)

```
/src
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
├── components/
│   ├── ui/           # shadcn components
│   ├── sections/     # Hero, Features, etc.
│   └── shared/       # Header, Footer, etc.
├── lib/
│   └── utils.ts
├── hooks/
├── types/
└── assets/
    ├── images/
    └── fonts/
```

## Performance Checklist

- [ ] Images otimizadas (WebP, next/image)
- [ ] Fonts preloaded
- [ ] Critical CSS inline
- [ ] Lazy loading abaixo do fold
- [ ] Code splitting
- [ ] Lighthouse score > 90
