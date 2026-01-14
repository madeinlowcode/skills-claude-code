#!/usr/bin/env python3
"""
Script de Validação de Compatibilidade XML para long-running-agent

Valida se um arquivo features.xml está no formato correto para ser consumido
pela skill long-running-agent.

Uso:
    python validate-compatibility.py <caminho-para-features.xml>

Exemplo:
    python validate-compatibility.py docs/context-log-running/jwt-auth/features.xml

Verificações realizadas:
    1. XML bem formado (sintaxe correta)
    2. Atributos obrigatórios presentes (id, status, priority)
    3. ID no formato FEAT-XXX (3 dígitos)
    4. Status válido: pending | in-progress | complete | blocked
    5. Priority válido: high | medium | low
    6. Tag <steps> presente com pelo menos 1 <step>
    7. Tag <description> presente e não vazia
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Tuple
import re


class ValidationError:
    """Representa um erro de validação."""

    def __init__(self, feature_id: str, error_type: str, message: str, severity: str = "ERROR"):
        self.feature_id = feature_id
        self.error_type = error_type
        self.message = message
        self.severity = severity  # ERROR, WARNING, INFO

    def __str__(self):
        icon = "❌" if self.severity == "ERROR" else "⚠️" if self.severity == "WARNING" else "ℹ️"
        return f"{icon} [{self.severity}] {self.feature_id or 'GLOBAL'}: {self.message}"


class XMLValidator:
    """Validador de features.xml para compatibilidade com long-running-agent."""

    VALID_STATUSES = {"pending", "in-progress", "complete", "blocked"}
    VALID_PRIORITIES = {"high", "medium", "low"}
    FEATURE_ID_PATTERN = re.compile(r'^FEAT-\d{3}$')

    def __init__(self, xml_path: str):
        self.xml_path = Path(xml_path)
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []
        self.root = None

    def validate(self) -> Tuple[bool, List[ValidationError]]:
        """
        Executa todas as validações.

        Returns:
            Tuple[bool, List[ValidationError]]: (is_valid, errors_and_warnings)
        """
        # Verificar se arquivo existe
        if not self.xml_path.exists():
            self.errors.append(ValidationError(
                "",
                "FILE_NOT_FOUND",
                f"Arquivo não encontrado: {self.xml_path}"
            ))
            return False, self.errors + self.warnings

        # Validar XML bem formado
        if not self._validate_xml_syntax():
            return False, self.errors + self.warnings

        # Validar estrutura raiz
        if not self._validate_root_structure():
            return False, self.errors + self.warnings

        # Validar cada feature
        self._validate_features()

        # Validar IDs únicos
        self._validate_unique_ids()

        # Validar contadores
        self._validate_counters()

        is_valid = len(self.errors) == 0
        return is_valid, self.errors + self.warnings

    def _validate_xml_syntax(self) -> bool:
        """Valida se o XML está bem formado."""
        try:
            tree = ET.parse(self.xml_path)
            self.root = tree.getroot()
            return True
        except ET.ParseError as e:
            self.errors.append(ValidationError(
                "",
                "XML_SYNTAX_ERROR",
                f"XML malformado: {str(e)}"
            ))
            return False
        except Exception as e:
            self.errors.append(ValidationError(
                "",
                "PARSE_ERROR",
                f"Erro ao fazer parse do arquivo: {str(e)}"
            ))
            return False

    def _validate_root_structure(self) -> bool:
        """Valida a estrutura do elemento raiz <features>."""
        if self.root.tag != "features":
            self.errors.append(ValidationError(
                "",
                "INVALID_ROOT",
                f"Elemento raiz deve ser <features>, encontrado: <{self.root.tag}>"
            ))
            return False

        # Verificar atributos opcionais mas recomendados
        if not self.root.get("project"):
            self.warnings.append(ValidationError(
                "",
                "MISSING_PROJECT_ATTR",
                "Atributo 'project' não encontrado em <features>. Recomendado para organização.",
                "WARNING"
            ))

        if not self.root.get("total"):
            self.warnings.append(ValidationError(
                "",
                "MISSING_TOTAL_ATTR",
                "Atributo 'total' não encontrado em <features>. Útil para rastreamento.",
                "WARNING"
            ))

        if not self.root.get("completed"):
            self.warnings.append(ValidationError(
                "",
                "MISSING_COMPLETED_ATTR",
                "Atributo 'completed' não encontrado em <features>. Útil para rastreamento.",
                "WARNING"
            ))

        return True

    def _validate_features(self):
        """Valida todas as features encontradas."""
        categories = self.root.findall(".//category")

        if not categories:
            self.warnings.append(ValidationError(
                "",
                "NO_CATEGORIES",
                "Nenhuma <category> encontrada. Features devem estar organizadas em categorias.",
                "WARNING"
            ))

        for category in categories:
            category_name = category.get("name", "UNNAMED")

            if not category.get("name"):
                self.errors.append(ValidationError(
                    "",
                    "MISSING_CATEGORY_NAME",
                    "Tag <category> sem atributo 'name'"
                ))

            features = category.findall("feature")

            if not features:
                self.warnings.append(ValidationError(
                    "",
                    "EMPTY_CATEGORY",
                    f"Categoria '{category_name}' não contém nenhuma <feature>",
                    "WARNING"
                ))

            for feature in features:
                self._validate_single_feature(feature)

    def _validate_single_feature(self, feature: ET.Element):
        """Valida uma única feature."""
        feature_id = feature.get("id", "UNKNOWN")

        # 1. Validar atributo 'id'
        if not feature.get("id"):
            self.errors.append(ValidationError(
                feature_id,
                "MISSING_ID",
                "Feature sem atributo 'id'"
            ))
        elif not self.FEATURE_ID_PATTERN.match(feature_id):
            self.errors.append(ValidationError(
                feature_id,
                "INVALID_ID_FORMAT",
                f"ID '{feature_id}' inválido. Formato esperado: FEAT-XXX (3 dígitos, ex: FEAT-001)"
            ))

        # 2. Validar atributo 'status'
        status = feature.get("status")
        if not status:
            self.errors.append(ValidationError(
                feature_id,
                "MISSING_STATUS",
                "Feature sem atributo 'status'"
            ))
        elif status not in self.VALID_STATUSES:
            self.errors.append(ValidationError(
                feature_id,
                "INVALID_STATUS",
                f"Status '{status}' inválido. Valores aceitos: {', '.join(self.VALID_STATUSES)}"
            ))

        # 3. Validar atributo 'priority'
        priority = feature.get("priority")
        if not priority:
            self.errors.append(ValidationError(
                feature_id,
                "MISSING_PRIORITY",
                "Feature sem atributo 'priority'"
            ))
        elif priority not in self.VALID_PRIORITIES:
            self.errors.append(ValidationError(
                feature_id,
                "INVALID_PRIORITY",
                f"Priority '{priority}' inválida. Valores aceitos: {', '.join(self.VALID_PRIORITIES)}"
            ))

        # 4. Validar <description>
        description = feature.find("description")
        if description is None:
            self.errors.append(ValidationError(
                feature_id,
                "MISSING_DESCRIPTION",
                "Feature sem tag <description>"
            ))
        elif not description.text or not description.text.strip():
            self.errors.append(ValidationError(
                feature_id,
                "EMPTY_DESCRIPTION",
                "Tag <description> está vazia"
            ))

        # 5. Validar <steps>
        steps = feature.find("steps")
        if steps is None:
            self.errors.append(ValidationError(
                feature_id,
                "MISSING_STEPS",
                "Feature sem tag <steps>"
            ))
        else:
            step_elements = steps.findall("step")
            if not step_elements:
                self.errors.append(ValidationError(
                    feature_id,
                    "EMPTY_STEPS",
                    "Tag <steps> não contém nenhum <step>"
                ))

            # Validar cada step
            for i, step in enumerate(step_elements, 1):
                if not step.text or not step.text.strip():
                    self.errors.append(ValidationError(
                        feature_id,
                        "EMPTY_STEP",
                        f"Step #{i} está vazio"
                    ))

        # 6. Validar <notes> (opcional mas recomendado)
        notes = feature.find("notes")
        if notes is None:
            self.warnings.append(ValidationError(
                feature_id,
                "MISSING_NOTES",
                "Feature sem tag <notes>. Recomendado para referências e contexto adicional.",
                "WARNING"
            ))

        # 7. Validar features bloqueadas
        if status == "blocked":
            if notes is None or not notes.text or "Blocked:" not in notes.text:
                self.warnings.append(ValidationError(
                    feature_id,
                    "BLOCKED_WITHOUT_REASON",
                    "Feature marcada como 'blocked' mas sem razão explícita em <notes>",
                    "WARNING"
                ))

    def _validate_unique_ids(self):
        """Valida se todos os IDs de features são únicos."""
        ids = []
        for feature in self.root.findall(".//feature"):
            feature_id = feature.get("id")
            if feature_id:
                if feature_id in ids:
                    self.errors.append(ValidationError(
                        feature_id,
                        "DUPLICATE_ID",
                        f"ID duplicado: '{feature_id}' aparece mais de uma vez"
                    ))
                ids.append(feature_id)

    def _validate_counters(self):
        """Valida se os contadores 'total' e 'completed' estão corretos."""
        total_attr = self.root.get("total")
        completed_attr = self.root.get("completed")

        if total_attr is None or completed_attr is None:
            return  # Já foi avisado em _validate_root_structure

        try:
            total_expected = int(total_attr)
            completed_expected = int(completed_attr)
        except ValueError:
            self.errors.append(ValidationError(
                "",
                "INVALID_COUNTER",
                "Atributos 'total' e 'completed' devem ser números inteiros"
            ))
            return

        # Contar features reais
        all_features = self.root.findall(".//feature")
        total_actual = len(all_features)
        completed_actual = len([f for f in all_features if f.get("status") == "complete"])

        if total_actual != total_expected:
            self.warnings.append(ValidationError(
                "",
                "INCORRECT_TOTAL",
                f"Atributo 'total' está incorreto. Esperado: {total_actual}, Encontrado: {total_expected}",
                "WARNING"
            ))

        if completed_actual != completed_expected:
            self.warnings.append(ValidationError(
                "",
                "INCORRECT_COMPLETED",
                f"Atributo 'completed' está incorreto. Esperado: {completed_actual}, Encontrado: {completed_expected}",
                "WARNING"
            ))


def print_results(is_valid: bool, issues: List[ValidationError]):
    """Imprime os resultados da validação de forma formatada."""
    errors = [i for i in issues if i.severity == "ERROR"]
    warnings = [i for i in issues if i.severity == "WARNING"]

    print("\n" + "="*70)
    print("  RESULTADO DA VALIDAÇÃO XML")
    print("="*70)

    if is_valid and not warnings:
        print("\n✅ VALIDAÇÃO PASSOU! Arquivo XML está 100% compatível com long-running-agent.\n")
        return

    if errors:
        print(f"\n❌ VALIDAÇÃO FALHOU! Encontrados {len(errors)} erro(s):\n")
        for error in errors:
            print(f"  {error}")

    if warnings:
        print(f"\n⚠️  {len(warnings)} aviso(s) encontrado(s):\n")
        for warning in warnings:
            print(f"  {warning}")

    print("\n" + "="*70)

    if is_valid and warnings:
        print("✅ Validação passou (com avisos). XML é compatível mas pode ser melhorado.")
    elif errors:
        print("❌ Validação falhou. Corrija os erros acima antes de usar com long-running-agent.")

    print("="*70 + "\n")


def auto_fix_counters(xml_path: Path) -> bool:
    """
    Tenta corrigir automaticamente os contadores 'total' e 'completed'.

    Returns:
        bool: True se conseguiu corrigir, False caso contrário
    """
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        all_features = root.findall(".//feature")
        total_actual = len(all_features)
        completed_actual = len([f for f in all_features if f.get("status") == "complete"])

        root.set("total", str(total_actual))
        root.set("completed", str(completed_actual))

        # Salvar com indentação bonita
        indent_xml(root)
        tree.write(xml_path, encoding="UTF-8", xml_declaration=True)

        print(f"✅ Contadores corrigidos automaticamente:")
        print(f"   - total: {total_actual}")
        print(f"   - completed: {completed_actual}")

        return True
    except Exception as e:
        print(f"❌ Erro ao tentar corrigir contadores: {str(e)}")
        return False


def indent_xml(elem, level=0):
    """Adiciona indentação bonita ao XML."""
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for child in elem:
            indent_xml(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def main():
    """Função principal."""
    if len(sys.argv) < 2:
        print("Uso: python validate-compatibility.py <caminho-para-features.xml>")
        print("\nExemplo:")
        print("  python validate-compatibility.py docs/context-log-running/jwt-auth/features.xml")
        print("\nOpções:")
        print("  --auto-fix    Tenta corrigir automaticamente problemas simples (contadores)")
        sys.exit(1)

    xml_path = sys.argv[1]
    auto_fix = "--auto-fix" in sys.argv

    print(f"\n🔍 Validando: {xml_path}\n")

    validator = XMLValidator(xml_path)
    is_valid, issues = validator.validate()

    print_results(is_valid, issues)

    # Se houver apenas warnings de contadores e --auto-fix estiver habilitado
    if auto_fix and is_valid:
        errors = [i for i in issues if i.severity == "ERROR"]
        counter_warnings = [i for i in issues if i.error_type in ("INCORRECT_TOTAL", "INCORRECT_COMPLETED")]

        if not errors and counter_warnings:
            print("\n🔧 Tentando corrigir contadores automaticamente...\n")
            if auto_fix_counters(Path(xml_path)):
                print("\n✅ Arquivo corrigido! Execute a validação novamente para confirmar.\n")

    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
