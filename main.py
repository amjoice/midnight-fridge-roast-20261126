#!/usr/bin/env python3
"""Midnight Fridge Roast - one line roasting a fridge that locks at midnight.

Pure stdlib, deterministic, no network, no secrets. Writes a single line
under 200 characters to /output/entry.txt.
"""
import os

ENTRY = "At 11:59 you're my fridge. At midnight you won't open — you're a bouncer now, and somehow I'm never on your list."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as out:
        out.write(ENTRY)


if __name__ == "__main__":
    main()
