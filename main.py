#!/usr/bin/env python3
"""Write one office joke as a single line to /output/entry.txt.

The joke is a leaving card that takes so long to go round the office
that the person it is for comes back from a new job to sign it.
Standard library only; no network access; the output is fixed, so
running the program twice leaves the same bytes both times.
"""

import os

JOKE = (
    "The leaving card for Dave went round the office for so long "
    "that he came back from his new job to sign it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise ValueError("written bytes do not match the entry")
    if len(written) != len(text):
        raise ValueError("written length does not match the entry")


if __name__ == "__main__":
    main()
