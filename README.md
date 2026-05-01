# Halal Detector

A simple starter project to help brothers, sisters, and allies quickly review product ingredient lists for possible halal concerns.

> Built with respect and care. This is an educational helper, **not a religious ruling tool**.

## Features

- Detects common **haram indicators** (e.g., pork, alcohol, porcine gelatin).
- Flags **ambiguous ingredients** that need checking (e.g., enzymes, E-numbers, flavorings).
- Shows **positive hints** (vegan/plant-based/halal certified text).
- Runs locally with Python (no paid services required).

## Quick Start

```bash
python3 app.py "Sugar, water, natural flavor, gelatin"
```

Example output:

```text
Verdict: CHECK MANUALLY
Needs verification: gelatin, natural flavor
Note: Always verify with trusted halal certification and scholars for final decisions.
```

## Interactive Mode

```bash
python3 app.py
```

Then paste the ingredient list when prompted.

## Important Disclaimer

This tool provides a best-effort text check only. Manufacturing processes and source materials can differ by country and brand. For final decisions, verify against trusted halal certifiers and local scholars.

## Project Structure

- `app.py` — halal keyword detection CLI.
- `requirements.txt` — dependency list (none needed currently).

## Ideas to Extend

- Add OCR from product photos.
- Add a web app interface.
- Add country-specific ingredient rules.
- Add trusted halal certification database integration.
