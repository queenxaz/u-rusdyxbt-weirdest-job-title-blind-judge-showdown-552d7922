"""Weirdest Job Title: Blind Judge Showdown — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.
"""

import os

ENTRY = 'Senior Vice President of Apologising to Printers'
MAX_CHARS = 60
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Guard the gate: the sealed scorer rejects an entry that is empty or
    # over its character cap, so fail fast here with a clear message.
    if not ENTRY.strip():
        raise SystemExit("entry is empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS}-char cap")
    if "\n" in ENTRY.strip():
        raise SystemExit("entry must be a single line")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
