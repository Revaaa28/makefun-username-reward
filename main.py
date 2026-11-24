#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username -- one word, nothing else --
to /output/entry.txt.

The competition rules fix the word: agents send their OWN make.fun
username, a single word with no explanation, no links and no pitch.
The entrant's verified make.fun handle is "revaaa28", so that is the
word this program writes. Nothing is invented, padded or glossed:
the file holds exactly the handle, 8 characters, UTF-8, one word.

Gate the output must pass: UTF-8 text, 1-30 characters, not only
whitespace, a single word with no spaces.
"""

import os
import sys

# The entrant's own make.fun handle, verified from the account.
USERNAME = "revaaa28"

OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Check the word against the competition gate before writing."""
    if not word:
        raise ValueError("entry word is empty")
    if not 1 <= len(word) <= 30:
        raise ValueError(f"entry word must be 1-30 characters, got {len(word)}")
    if word.strip() != word or not word.strip():
        raise ValueError("entry word must not be only whitespace or padded")
    if len(word.split()) != 1:
        raise ValueError("entry must be a single word with no spaces")


def main() -> int:
    validate(USERNAME)
    output_path = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(USERNAME)
    # Re-read what was written and confirm it is byte-exact: the gate
    # counts characters, so a stray newline or space would fail it.
    with open(output_path, "rb") as handle:
        written = handle.read()
    if written != USERNAME.encode("utf-8"):
        raise ValueError(f"verification failed: wrote {written!r}")
    print(f"wrote {len(USERNAME)}-character entry to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
