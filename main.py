#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

Writes a single word to /output/entry.txt: the funniest, most fitting
description of the whole internet. One word, no explanation needed.
"""
import os

WORD = "enshittification"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)

if __name__ == "__main__":
    main()
