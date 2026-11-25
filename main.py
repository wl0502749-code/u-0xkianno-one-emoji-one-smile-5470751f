#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt: a bright sun with a
smiling face. Warm at first glance, readable by any stranger of any
age, no irony, no intimacy — just sunshine offered to someone unknown.
"""

import os

EMOJI = "\U0001F31E"  # 🌞 sun with face

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
