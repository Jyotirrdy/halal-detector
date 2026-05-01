#!/usr/bin/env python3
"""Simple halal ingredient detector CLI.

This tool classifies a product's ingredient list as:
- HALAL LIKELY
- HARAM LIKELY
- CHECK MANUALLY

It is educational and should not replace formal certification.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from typing import Iterable


HARAM_KEYWORDS = {
    "pork",
    "ham",
    "bacon",
    "lard",
    "gelatin (porcine)",
    "porcine",
    "blood",
    "wine",
    "beer",
    "rum",
    "brandy",
    "alcohol",
    "ethanol",
    "cochineal",
    "carmine",
}

CHECK_KEYWORDS = {
    "gelatin",
    "emulsifier",
    "mono and diglycerides",
    "diglycerides",
    "rennet",
    "enzyme",
    "natural flavor",
    "flavoring",
    "shortening",
    "glycerin",
    "e471",
    "e472",
    "e120",
}

HALAL_HINTS = {
    "halal certified",
    "suitable for vegetarians",
    "vegan",
    "plant based",
}


@dataclass
class DetectionResult:
    verdict: str
    found_haram: list[str]
    found_check: list[str]
    found_halal_hints: list[str]


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def find_keywords(text: str, keywords: Iterable[str]) -> list[str]:
    found = []
    for keyword in keywords:
        if keyword in text:
            found.append(keyword)
    return sorted(set(found))


def detect_halal_status(ingredients: str) -> DetectionResult:
    text = normalize(ingredients)
    haram = find_keywords(text, HARAM_KEYWORDS)
    check = find_keywords(text, CHECK_KEYWORDS)
    halal_hints = find_keywords(text, HALAL_HINTS)

    if haram:
        verdict = "HARAM LIKELY"
    elif check:
        verdict = "CHECK MANUALLY"
    else:
        verdict = "HALAL LIKELY"

    return DetectionResult(verdict, haram, check, halal_hints)


def format_result(result: DetectionResult) -> str:
    lines = [f"Verdict: {result.verdict}"]
    if result.found_haram:
        lines.append(f"Haram indicators: {', '.join(result.found_haram)}")
    if result.found_check:
        lines.append(f"Needs verification: {', '.join(result.found_check)}")
    if result.found_halal_hints:
        lines.append(f"Positive hints: {', '.join(result.found_halal_hints)}")

    lines.append(
        "Note: Always verify with trusted halal certification and scholars for final decisions."
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Check ingredient text for halal risk")
    parser.add_argument(
        "ingredients",
        nargs="*",
        help="Ingredient list text. If omitted, you will be prompted.",
    )
    args = parser.parse_args()

    if args.ingredients:
        ingredients = " ".join(args.ingredients)
    else:
        ingredients = input("Paste ingredients: ").strip()

    if not ingredients:
        raise SystemExit("No ingredients provided.")

    result = detect_halal_status(ingredients)
    print(format_result(result))


if __name__ == "__main__":
    main()
