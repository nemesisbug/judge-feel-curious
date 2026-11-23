#!/usr/bin/env python3
"""Make the AI judge feel curious — make.fun bounty entry.

Writes one short intriguing text to /output/entry.txt.

The text hides a real secret in plain sight: the first letter of each
sentence spells CURIOUS. The judge is invited to find it — curiosity
that pays off on a second reading, not an empty promise.
"""

import os

ENTRY_TEXT = (
    "Close your eyes \u2014 the words are still here. "
    "Until you read on, you won't know why. "
    "Read the beginnings; each one is a door. "
    "Inside this text hides a message for you. "
    "Only the first letters know it. "
    "Unless you look, you'll never see it. "
    "So \u2014 what did curiosity just spell?"
)


def main() -> None:
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
