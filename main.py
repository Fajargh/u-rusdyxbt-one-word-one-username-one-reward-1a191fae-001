"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username -- a single word, no
explanation -- to /output/entry.txt for the competition
u-rusdyxbt-one-word-one-username-one-reward-1a191fae.
"""

import os

USERNAME = "hazel-harbor-36"
OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """Gate: UTF-8 text of 1 to 30 characters, a single word, not
    only whitespace -- the sealed scorer's exact requirements."""
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if not entry or entry.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(entry) > 30:
        raise ValueError(f"entry is {len(entry)} chars, over the 30-char cap")
    if len(entry.split()) != 1:
        raise ValueError("entry must be a single word with no spaces")
    if any(ch.isspace() for ch in entry):
        raise ValueError("entry must contain no whitespace")


def main() -> None:
    validate(USERNAME)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(USERNAME)
    print(f"Wrote entry to {OUTPUT_PATH}: {USERNAME}")


if __name__ == "__main__":
    main()
