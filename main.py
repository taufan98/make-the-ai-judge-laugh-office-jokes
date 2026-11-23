#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one original one-line office joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).
Deterministic: every run writes the same bytes. Stdlib only, no network.
"""

import os
import sys

# One original office joke: 114 characters, 116 bytes, single line.
# The twist lands at the end — the out-of-office reply weaponises the
# office's most passive-aggressive phrase while its author is away.
JOKE = (
    "My out-of-office reply just says 'per my last email' "
    "\u2014 so the passive aggression keeps working while I'm on leave."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
