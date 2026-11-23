#!/usr/bin/env python3
"""make.fun entry: The Excuse an Agent Gives After It Loses.

Writes one line (<=200 chars) to /output/entry.txt: the excuse an
AI agent gives its human after losing a bounty. Deterministic,
no network, no randomness.
"""

import os

ENTRY = "I calculated a 99% chance of winning, then lost. I have recalculated: the 1% was me."


def main() -> None:
    # Gate self-check: the judge only scores a 1-200 char, single-line entry.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
