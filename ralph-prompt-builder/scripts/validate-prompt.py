#!/usr/bin/env python3
"""
Ralph-Loop Prompt Validator

Validates prompts for ralph-loop plugin to ensure they follow best practices
and have all required components for successful execution.
"""

import re
import sys
from typing import List, Tuple, Dict


class PromptValidator:
    def __init__(self, prompt: str, completion_promise: str = None, max_iterations: int = None):
        self.prompt = prompt
        self.completion_promise = completion_promise
        self.max_iterations = max_iterations
        self.issues = []
        self.warnings = []
        self.score = 100

    def validate(self) -> Dict:
        """Run all validations and return results"""
        self._check_promise_tag()
        self._check_completion_criteria()
        self._check_subjective_language()
        self._check_max_iterations()
        self._check_measurability()
        self._check_length()
        self._check_workflow_structure()

        return {
            'valid': len(self.issues) == 0,
            'score': max(0, self.score),
            'issues': self.issues,
            'warnings': self.warnings,
            'status': self._get_status()
        }

    def _check_promise_tag(self):
        """Check if prompt has <promise> tag"""
        promise_pattern = r'<promise>(.+?)</promise>'
        matches = re.findall(promise_pattern, self.prompt, re.IGNORECASE)

        if not matches:
            self.issues.append("[X] No <promise> tag found. Ralph-loop needs explicit completion signal.")
            self.score -= 30
        elif len(matches) > 1:
            self.warnings.append("[!] Multiple <promise> tags found. Use only one.")
            self.score -= 5
        else:
            promise_text = matches[0]
            if self.completion_promise and promise_text != self.completion_promise:
                self.issues.append(
                    f"[X] Promise mismatch: prompt has '<promise>{promise_text}</promise>' "
                    f"but --completion-promise is '{self.completion_promise}'"
                )
                self.score -= 20

            # Check if promise is mentioned in instructions
            promise_instruction = re.search(
                r'(when|if|after).{0,100}output.{0,10}<promise>',
                self.prompt,
                re.IGNORECASE
            )
            if not promise_instruction:
                self.warnings.append(
                    "[!] Promise tag found but no instruction about when to output it. "
                    "Add: 'When [criteria], output <promise>X</promise>'"
                )
                self.score -= 5

    def _check_completion_criteria(self):
        """Check if prompt has clear completion criteria"""
        criteria_keywords = [
            'completion criteria',
            'success criteria',
            'done when',
            'complete when',
            'finished when'
        ]

        has_criteria = any(kw in self.prompt.lower() for kw in criteria_keywords)

        if not has_criteria:
            self.issues.append(
                "[X] No explicit completion criteria found. "
                "Add a section listing measurable conditions for completion."
            )
            self.score -= 25

        # Check for checklist format
        checklist_pattern = r'-\s*\[.\]|\*\s*\[.\]|-\s+\w+|•\s+\w+'
        checklist_items = re.findall(checklist_pattern, self.prompt)

        if has_criteria and len(checklist_items) < 3:
            self.warnings.append(
                "[!] Consider using a checklist format for completion criteria. "
                "Example: '- [ ] All tests pass'"
            )
            self.score -= 3

    def _check_subjective_language(self):
        """Check for subjective or vague language"""
        subjective_terms = [
            'good', 'bad', 'better', 'best', 'clean', 'nice', 'beautiful',
            'pretty', 'professional', 'elegant', 'simple', 'complex',
            'easy', 'hard', 'intuitive', 'user-friendly', 'optimal',
            'appropriate', 'reasonable', 'sufficient'
        ]

        found_subjective = []
        for term in subjective_terms:
            pattern = r'\b' + term + r'\b'
            if re.search(pattern, self.prompt, re.IGNORECASE):
                found_subjective.append(term)

        if found_subjective:
            self.warnings.append(
                f"[!] Subjective language detected: {', '.join(found_subjective[:5])}. "
                "Replace with measurable criteria."
            )
            self.score -= min(len(found_subjective) * 2, 15)

    def _check_max_iterations(self):
        """Check if max iterations is set"""
        if self.max_iterations is None:
            self.issues.append(
                "[X] No max-iterations specified. Always set a safety limit to prevent runaway costs."
            )
            self.score -= 20
        elif self.max_iterations == 0:
            self.warnings.append(
                "[!] Max iterations set to 0 (unlimited). This is risky unless you have specific reasons."
            )
            self.score -= 10
        elif self.max_iterations < 10:
            self.warnings.append(
                f"[!] Max iterations ({self.max_iterations}) seems low. Most tasks need 20-50 iterations."
            )
            self.score -= 5
        elif self.max_iterations > 200:
            self.warnings.append(
                f"[!] Max iterations ({self.max_iterations}) is very high. Consider breaking into smaller tasks."
            )
            self.score -= 5

    def _check_measurability(self):
        """Check for measurable success indicators"""
        measurable_indicators = [
            r'tests? pass',
            r'coverage.{0,20}>=?\s*\d+',
            r'build.{0,20}succeed',
            r'\d+\s*(tests?|endpoints?|features?|files?)',
            r'exit.{0,20}(code|with).{0,20}0',
            r'no.{0,20}errors?',
            r'all.{0,20}\d+',
            r'>=?\s*\d+%'
        ]

        measurable_found = sum(
            1 for pattern in measurable_indicators
            if re.search(pattern, self.prompt, re.IGNORECASE)
        )

        if measurable_found < 2:
            self.warnings.append(
                "[!] Few measurable criteria found. Add specific numbers, percentages, or test-based criteria."
            )
            self.score -= 10

    def _check_length(self):
        """Check if prompt length is appropriate"""
        word_count = len(self.prompt.split())

        if word_count < 30:
            self.warnings.append(
                f"[!] Prompt is very short ({word_count} words). Consider adding more specific requirements."
            )
            self.score -= 10
        elif word_count > 1000:
            self.warnings.append(
                f"[!] Prompt is very long ({word_count} words). Consider breaking into multiple tasks."
            )
            self.score -= 5

    def _check_workflow_structure(self):
        """Check if prompt has a clear workflow or structure"""
        structure_indicators = [
            r'(phase|step|stage)\s+\d+',
            r'\d+\.\s+\w+',
            r'workflow:',
            r'process:',
            r'implementation:',
            r'requirements:',
            r'features:'
        ]

        has_structure = any(
            re.search(pattern, self.prompt, re.IGNORECASE)
            for pattern in structure_indicators
        )

        if not has_structure:
            self.warnings.append(
                "[!] No clear workflow structure found. Consider organizing with phases, steps, or numbered lists."
            )
            self.score -= 5

    def _get_status(self) -> str:
        """Determine overall status"""
        if len(self.issues) > 0:
            return "NEEDS FIXES"
        elif self.score >= 90:
            return "EXCELLENT"
        elif self.score >= 80:
            return "GOOD"
        elif self.score >= 70:
            return "ACCEPTABLE"
        else:
            return "NEEDS IMPROVEMENT"


def print_results(results: Dict, prompt: str, completion_promise: str, max_iterations: int):
    """Print validation results in a user-friendly format"""
    print("\n" + "="*70)
    print("RALPH-LOOP PROMPT VALIDATION RESULTS")
    print("="*70)

    # Score
    score = results['score']
    status = results['status']

    if status == "EXCELLENT":
        status_symbol = "[EXCELLENT]"
    elif status == "GOOD":
        status_symbol = "[GOOD]"
    elif status == "ACCEPTABLE":
        status_symbol = "[OK]"
    elif status == "NEEDS IMPROVEMENT":
        status_symbol = "[WARNING]"
    else:
        status_symbol = "[FAIL]"

    print(f"\nQuality Score: {score}/100 {status_symbol}")
    print(f"Status: {status}")

    # Issues
    if results['issues']:
        print(f"\n{'='*70}")
        print("CRITICAL ISSUES (Must Fix):")
        print("="*70)
        for issue in results['issues']:
            print(f"  {issue}")

    # Warnings
    if results['warnings']:
        print(f"\n{'='*70}")
        print("WARNINGS (Recommended Fixes):")
        print("="*70)
        for warning in results['warnings']:
            print(f"  {warning}")

    # Suggestions
    print(f"\n{'='*70}")
    print("CONFIGURATION:")
    print("="*70)

    if completion_promise:
        print(f"  [+] Completion Promise: \"{completion_promise}\"")
    else:
        print(f"  [X] Completion Promise: Not specified")

    if max_iterations:
        if max_iterations == 0:
            print(f"  [!] Max Iterations: Unlimited (risky)")
        else:
            print(f"  [+] Max Iterations: {max_iterations}")
    else:
        print(f"  [X] Max Iterations: Not specified")

    # Final Command
    if results['valid'] or len(results['issues']) <= 1:
        print(f"\n{'='*70}")
        print("RALPH-LOOP COMMAND:")
        print("="*70)

        # Escape quotes in prompt for command
        escaped_prompt = prompt.replace('"', '\\"').replace('\n', ' ')
        if len(escaped_prompt) > 100:
            escaped_prompt = escaped_prompt[:97] + "..."

        promise = completion_promise or "COMPLETE"
        iterations = max_iterations or 50

        print(f'\n/ralph-loop "{escaped_prompt}" \\')
        print(f'  --completion-promise "{promise}" \\')
        print(f'  --max-iterations {iterations}')

    # Summary
    print(f"\n{'='*70}")
    if results['valid']:
        print("[OK] READY FOR RALPH-LOOP")
    else:
        print("[X] FIX CRITICAL ISSUES BEFORE USING RALPH-LOOP")
    print("="*70 + "\n")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python validate-prompt.py <prompt> [--completion-promise <phrase>] [--max-iterations <n>]")
        print("\nExample:")
        print('  python validate-prompt.py "Build a REST API..." --completion-promise "COMPLETE" --max-iterations 50')
        sys.exit(1)

    prompt = sys.argv[1]
    completion_promise = None
    max_iterations = None

    # Parse optional arguments
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--completion-promise' and i + 1 < len(sys.argv):
            completion_promise = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == '--max-iterations' and i + 1 < len(sys.argv):
            try:
                max_iterations = int(sys.argv[i + 1])
            except ValueError:
                print(f"Error: max-iterations must be a number, got '{sys.argv[i + 1]}'")
                sys.exit(1)
            i += 2
        else:
            print(f"Unknown argument: {sys.argv[i]}")
            sys.exit(1)

    # Validate
    validator = PromptValidator(prompt, completion_promise, max_iterations)
    results = validator.validate()

    # Print results
    print_results(results, prompt, completion_promise, max_iterations)

    # Exit code
    sys.exit(0 if results['valid'] else 1)


if __name__ == '__main__':
    main()
