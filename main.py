"""Midnight Fridge Roast — make.fun bounty entry.

Writes one line of text roasting a smart fridge that refuses to open
after midnight to $MAKEFUN_OUTPUT_DIR/entry.txt (default: current dir).

Standard library only; deterministic; no network, no input.
"""

import os

ROAST = (
    "My smart fridge locks itself at midnight — apparently my leftovers "
    "have a curfew now, and the fridge is the bouncer who enforces it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ROAST + "\n")


if __name__ == "__main__":
    main()
