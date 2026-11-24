#!/usr/bin/env python3
"""Say What Actually Broke - entry program.

Writes the entry line (one line of software error copy, <= 200 chars)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: no clock, no randomness, no network.
"""
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ENTRY = (
    "Error 500: the database hit its disk limit - its own error log is now "
    "the largest file on that disk. We cleared 2 GB; it refilled in 40 "
    "seconds. Retrying is booked, not fixed."
)

def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(path)

if __name__ == "__main__":
    main()
