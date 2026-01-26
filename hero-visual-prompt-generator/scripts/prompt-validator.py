#!/usr/bin/env python3
"""
Prompt Validator for Hero Visual Prompts

Validates that image and video prompts contain all required elements
for premium hero section visuals.

Usage:
    python prompt-validator.py "prompt text" --type image
    python prompt-validator.py "prompt text" --type video
    python prompt-validator.py --file prompt.txt --type image
"""

import argparse
import re
import sys
from typing import List, Tuple

# Required elements for image prompts
IMAGE_REQUIRED_ELEMENTS = [
    ("Subject", ["subject:", "subject -"]),
    ("Composition", ["composition:", "composition -"]),
    ("Key Elements", ["key elements:", "elements:", "key elements -"]),
    ("Environment", ["environment:", "background:", "environment -"]),
    ("Lighting", ["lighting:", "light:", "lighting -"]),
    ("Style & Details", ["style:", "style & details:", "style and details:", "details:"]),
    ("Aspect Ratio", ["aspect ratio:", "ratio:", "aspect:"]),
]

# Required elements for video prompts
VIDEO_REQUIRED_ELEMENTS = [
    ("Sequence", ["sequence:", "sequence -"]),
    ("Visuals", ["visuals:", "visual:", "visuals -", "start:", "- start:"]),
    ("Lighting & Camera", ["lighting & camera:", "lighting and camera:", "camera:", "lighting:"]),
    ("Style", ["style:", "quality:"]),
    ("Duration", ["duration:", "length:", "time:"]),
    ("Aspect Ratio", ["aspect ratio:", "ratio:", "aspect:"]),
]

# Quality keywords that should be present
QUALITY_KEYWORDS = [
    "hyper-realistic",
    "hyperrealistic",
    "8k",
    "4k",
    "cinematic",
    "commercial",
    "professional",
    "ultra-sharp",
    "high quality",
    "high-end",
]

# Common aspect ratio patterns
ASPECT_RATIO_PATTERNS = [
    r"16:9",
    r"9:16",
    r"21:9",
    r"4:5",
    r"1:1",
    r"1920x1080",
    r"1080x1920",
    r"2560x1080",
    r"1080x1350",
]


def check_element_present(prompt: str, element_name: str, keywords: List[str]) -> bool:
    """Check if an element is present in the prompt."""
    prompt_lower = prompt.lower()
    return any(keyword.lower() in prompt_lower for keyword in keywords)


def check_quality_keywords(prompt: str) -> Tuple[bool, List[str]]:
    """Check for presence of quality keywords."""
    prompt_lower = prompt.lower()
    found = [kw for kw in QUALITY_KEYWORDS if kw.lower() in prompt_lower]
    return len(found) >= 2, found


def check_aspect_ratio(prompt: str) -> Tuple[bool, str]:
    """Check for valid aspect ratio specification."""
    for pattern in ASPECT_RATIO_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            return True, pattern
    return False, ""


def validate_image_prompt(prompt: str) -> Tuple[bool, List[str], List[str]]:
    """
    Validate an image prompt.

    Returns:
        Tuple of (is_valid, missing_elements, warnings)
    """
    missing = []
    warnings = []

    # Check required elements
    for element_name, keywords in IMAGE_REQUIRED_ELEMENTS:
        if not check_element_present(prompt, element_name, keywords):
            missing.append(element_name)

    # Check quality keywords
    has_quality, found_quality = check_quality_keywords(prompt)
    if not has_quality:
        warnings.append(f"Low quality keyword count. Found: {found_quality if found_quality else 'none'}")

    # Check aspect ratio format
    has_ratio, ratio_found = check_aspect_ratio(prompt)
    if not has_ratio and "Aspect Ratio" not in missing:
        warnings.append("Aspect ratio mentioned but format unclear")

    # Check for lighting detail
    if "Lighting" not in missing:
        lighting_keywords = ["backlight", "rim light", "golden hour", "soft light",
                          "dramatic", "volumetric", "ambient", "studio"]
        if not any(kw.lower() in prompt.lower() for kw in lighting_keywords):
            warnings.append("Lighting section lacks specific technique details")

    is_valid = len(missing) == 0
    return is_valid, missing, warnings


def validate_video_prompt(prompt: str) -> Tuple[bool, List[str], List[str]]:
    """
    Validate a video prompt.

    Returns:
        Tuple of (is_valid, missing_elements, warnings)
    """
    missing = []
    warnings = []

    # Check required elements
    for element_name, keywords in VIDEO_REQUIRED_ELEMENTS:
        if not check_element_present(prompt, element_name, keywords):
            missing.append(element_name)

    # Check for motion description
    motion_keywords = ["start", "middle", "end", "begin", "transition", "movement"]
    if not any(kw.lower() in prompt.lower() for kw in motion_keywords):
        warnings.append("Missing clear motion progression (start/middle/end)")

    # Check quality keywords
    has_quality, found_quality = check_quality_keywords(prompt)
    if not has_quality:
        warnings.append(f"Low quality keyword count. Found: {found_quality if found_quality else 'none'}")

    # Check aspect ratio format
    has_ratio, ratio_found = check_aspect_ratio(prompt)
    if not has_ratio and "Aspect Ratio" not in missing:
        warnings.append("Aspect ratio mentioned but format unclear")

    # Check duration format
    duration_pattern = r"\d+[-\s]?\d*\s*seconds?"
    if "Duration" not in missing and not re.search(duration_pattern, prompt, re.IGNORECASE):
        warnings.append("Duration mentioned but specific seconds not clear")

    # Check camera movement
    camera_keywords = ["push-in", "pull-out", "orbit", "track", "static", "pan",
                      "zoom", "dolly", "crane", "float"]
    if not any(kw.lower() in prompt.lower() for kw in camera_keywords):
        warnings.append("No specific camera movement described")

    is_valid = len(missing) == 0
    return is_valid, missing, warnings


def format_results(prompt_type: str, is_valid: bool, missing: List[str], warnings: List[str]) -> str:
    """Format validation results for display."""
    lines = []

    status = "VALID" if is_valid else "INVALID"
    lines.append(f"\n{'='*50}")
    lines.append(f"  {prompt_type.upper()} PROMPT VALIDATION: {status}")
    lines.append(f"{'='*50}")

    if missing:
        lines.append("\nMISSING REQUIRED ELEMENTS:")
        for element in missing:
            lines.append(f"  - {element}")

    if warnings:
        lines.append("\nWARNINGS:")
        for warning in warnings:
            lines.append(f"  - {warning}")

    if is_valid and not warnings:
        lines.append("\nAll required elements present.")
        lines.append("Prompt is ready for generation.")
    elif is_valid:
        lines.append("\nPrompt is valid but review warnings for better results.")
    else:
        lines.append("\nPlease add missing elements before generation.")

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Validate hero visual prompts for completeness"
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        help="The prompt text to validate"
    )
    parser.add_argument(
        "--file", "-f",
        help="Read prompt from file instead of argument"
    )
    parser.add_argument(
        "--type", "-t",
        choices=["image", "video"],
        required=True,
        help="Type of prompt to validate"
    )

    args = parser.parse_args()

    # Get prompt text
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                prompt = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}")
            sys.exit(1)
    elif args.prompt:
        prompt = args.prompt
    else:
        print("Error: Provide prompt text or --file argument")
        sys.exit(1)

    # Validate based on type
    if args.type == "image":
        is_valid, missing, warnings = validate_image_prompt(prompt)
    else:
        is_valid, missing, warnings = validate_video_prompt(prompt)

    # Output results
    print(format_results(args.type, is_valid, missing, warnings))

    # Exit code
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
