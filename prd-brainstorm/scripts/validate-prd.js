#!/usr/bin/env node

/**
 * PRD Validator Script
 * Validates that a PRD file contains all required sections and follows the template structure.
 *
 * Usage: node validate-prd.js <path-to-prd.md>
 */

const fs = require('fs');
const path = require('path');

// Required sections in a valid PRD
const REQUIRED_SECTIONS = [
  { name: 'Metadata', patterns: ['## Metadata', '| Projeto', '| Versão', '| Data', '| Status'] },
  { name: 'Overview', patterns: ['## 1. Overview', '### 1.1 Problema', '### 1.2 Solução'] },
  { name: 'Contexto', patterns: ['## 2. Contexto', '### 2.1 Background', '### 2.2 Usuários'] },
  { name: 'Assumptions', patterns: ['## 3. Assumptions'] },
  { name: 'Scope', patterns: ['## 4. Scope', '### 4.1 In Scope', '### 4.2 Out of Scope'] },
  { name: 'User Stories', patterns: ['## 5. User Stories', '**Como**', '**Quero**', '**Para**'] },
  { name: 'Technical Stack', patterns: ['## 6. Technical Stack', '### 6.1 Stack Escolhida'] },
  { name: 'Success Metrics', patterns: ['## 7. Success Metrics'] },
  { name: 'Dependencies', patterns: ['## 8. Dependencies'] },
  { name: 'Timeline', patterns: ['## 9. Timeline'] },
  { name: 'Próximos Passos', patterns: ['## 10. Próximos Passos', 'sprint-context-generator'] }
];

// Validation rules for content quality
const QUALITY_RULES = [
  {
    name: 'User Story Format',
    check: (content) => {
      const hasUserStoryFormat = /\*\*Como\*\*.*\*\*Quero\*\*.*\*\*Para\*\*/s.test(content);
      return hasUserStoryFormat;
    },
    message: 'User Stories devem seguir o formato "Como X, Quero Y, Para Z"'
  },
  {
    name: 'Acceptance Criteria',
    check: (content) => {
      const hasAcceptanceCriteria = /Critérios de Aceitação:/i.test(content);
      return hasAcceptanceCriteria;
    },
    message: 'User Stories devem ter Critérios de Aceitação'
  },
  {
    name: 'Measurable Metrics',
    check: (content) => {
      // Check for numbers in the metrics section
      const metricsSection = content.match(/## 7\. Success Metrics[\s\S]*?(?=## 8\.)/);
      if (!metricsSection) return false;
      return /\d+%|\d+ dias|\d+ semanas|\d+ meses|\d+ usuários/i.test(metricsSection[0]);
    },
    message: 'Métricas de sucesso devem ser mensuráveis (incluir números específicos)'
  },
  {
    name: 'Tech Stack Justification',
    check: (content) => {
      const techSection = content.match(/## 6\. Technical Stack[\s\S]*?(?=## 7\.)/);
      if (!techSection) return false;
      return /Justificativa/i.test(techSection[0]) || /Por que/i.test(techSection[0]);
    },
    message: 'Tech Stack deve incluir justificativas para as escolhas'
  },
  {
    name: 'Sprint Context Integration',
    check: (content) => {
      return /sprint-context-generator/i.test(content);
    },
    message: 'PRD deve mencionar integração com sprint-context-generator'
  }
];

// Colors for terminal output
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  cyan: '\x1b[36m',
  bold: '\x1b[1m'
};

function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

function validatePRD(filePath) {
  // Check if file exists
  if (!fs.existsSync(filePath)) {
    log(`\n❌ Arquivo não encontrado: ${filePath}`, 'red');
    return { valid: false, errors: ['Arquivo não encontrado'], warnings: [] };
  }

  const content = fs.readFileSync(filePath, 'utf-8');
  const errors = [];
  const warnings = [];
  const passed = [];

  log(`\n${colors.bold}🔍 Validando PRD: ${path.basename(filePath)}${colors.reset}\n`);

  // Check required sections
  log('📋 Verificando seções obrigatórias...', 'cyan');
  for (const section of REQUIRED_SECTIONS) {
    const foundPatterns = section.patterns.filter(p => content.includes(p));
    const coverage = (foundPatterns.length / section.patterns.length) * 100;

    if (foundPatterns.length === section.patterns.length) {
      passed.push(section.name);
      log(`  ✓ ${section.name}`, 'green');
    } else if (foundPatterns.length > 0) {
      warnings.push(`${section.name}: incompleto (${coverage.toFixed(0)}% dos padrões encontrados)`);
      log(`  ⚠ ${section.name} (${coverage.toFixed(0)}% completo)`, 'yellow');
    } else {
      errors.push(`Seção ausente: ${section.name}`);
      log(`  ✗ ${section.name}`, 'red');
    }
  }

  // Check quality rules
  log('\n📊 Verificando qualidade do conteúdo...', 'cyan');
  for (const rule of QUALITY_RULES) {
    if (rule.check(content)) {
      passed.push(rule.name);
      log(`  ✓ ${rule.name}`, 'green');
    } else {
      warnings.push(rule.message);
      log(`  ⚠ ${rule.name}`, 'yellow');
    }
  }

  // Check file size (too short might indicate incomplete PRD)
  const lineCount = content.split('\n').length;
  log('\n📏 Verificando tamanho do documento...', 'cyan');
  if (lineCount < 50) {
    warnings.push('PRD muito curto (menos de 50 linhas). Pode estar incompleto.');
    log(`  ⚠ ${lineCount} linhas (recomendado: > 100)`, 'yellow');
  } else if (lineCount < 100) {
    log(`  ⚠ ${lineCount} linhas (mínimo aceitável)`, 'yellow');
  } else {
    log(`  ✓ ${lineCount} linhas`, 'green');
  }

  // Count user stories
  const userStoryCount = (content.match(/#### US-\d+/g) || []).length;
  log('\n📝 Verificando User Stories...', 'cyan');
  if (userStoryCount < 3) {
    warnings.push(`Apenas ${userStoryCount} User Stories. Recomendado: pelo menos 3.`);
    log(`  ⚠ ${userStoryCount} User Stories (recomendado: >= 3)`, 'yellow');
  } else {
    log(`  ✓ ${userStoryCount} User Stories`, 'green');
  }

  // Summary
  const isValid = errors.length === 0;

  log('\n' + '═'.repeat(50));
  log(`${colors.bold}📊 RESULTADO DA VALIDAÇÃO${colors.reset}`);
  log('═'.repeat(50));

  log(`\nSeções OK: ${passed.length}/${REQUIRED_SECTIONS.length + QUALITY_RULES.length}`, passed.length === REQUIRED_SECTIONS.length + QUALITY_RULES.length ? 'green' : 'yellow');

  if (errors.length > 0) {
    log(`\n❌ ERROS (${errors.length}):`, 'red');
    errors.forEach(e => log(`   • ${e}`, 'red'));
  }

  if (warnings.length > 0) {
    log(`\n⚠️  AVISOS (${warnings.length}):`, 'yellow');
    warnings.forEach(w => log(`   • ${w}`, 'yellow'));
  }

  log('\n' + '═'.repeat(50));
  if (isValid && warnings.length === 0) {
    log('✅ PRD VÁLIDO E COMPLETO', 'green');
  } else if (isValid) {
    log('✅ PRD VÁLIDO (com avisos)', 'yellow');
  } else {
    log('❌ PRD INVÁLIDO', 'red');
  }
  log('═'.repeat(50) + '\n');

  return { valid: isValid, errors, warnings, passed };
}

// CLI handling
const args = process.argv.slice(2);

if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
  console.log(`
${colors.bold}PRD Validator${colors.reset}
Valida a estrutura e qualidade de arquivos PRD.

${colors.cyan}Uso:${colors.reset}
  node validate-prd.js <caminho-do-prd.md>
  node validate-prd.js --help

${colors.cyan}Exemplos:${colors.reset}
  node validate-prd.js ./prd.md
  node validate-prd.js ./docs/prd.md

${colors.cyan}Seções verificadas:${colors.reset}
  • Metadata (projeto, versão, data, status)
  • Overview (problema, solução, objetivo)
  • Contexto (background, usuários, métricas)
  • Assumptions (valor, usabilidade, viabilidade)
  • Scope (in scope, out of scope, futuro)
  • User Stories (formato padrão + critérios)
  • Technical Stack (escolhas + justificativas)
  • Success Metrics (KPIs mensuráveis)
  • Dependencies & Blockers
  • Timeline
  • Próximos Passos (integração sprint-context-generator)

${colors.cyan}Regras de qualidade:${colors.reset}
  • User Stories no formato "Como X, Quero Y, Para Z"
  • Critérios de aceitação para cada story
  • Métricas mensuráveis (números específicos)
  • Justificativas para escolhas de tech stack
  • Referência à integração com sprint-context-generator
`);
  process.exit(0);
}

const filePath = path.resolve(args[0]);
const result = validatePRD(filePath);

// Exit code based on validation result
process.exit(result.valid ? 0 : 1);
