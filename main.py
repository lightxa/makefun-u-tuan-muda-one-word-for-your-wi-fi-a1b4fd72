"""One Word for Your Wi-Fi.

Writes a single word describing home Wi-Fi to /output/entry.txt.

The word: peekaboo.

Home Wi-Fi plays peekaboo. It is there, full bars, the video is
playing, and then it is simply gone, at the exact second the call
matters, the file is nearly downloaded, the show reaches its climax.
A moment later it is back, pretending nothing happened, until the
next round of the game. One word, one concrete image, no explanation
needed: everyone who has lived with home Wi-Fi has played this game
and lost it.
"""

import os

# The entry word: 8 characters, one word, inside the 1-20 gate.
WORD = "peekaboo"

OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Check the word against the gate: 1-20 chars, not only whitespace."""
    if not word or len(word) > 20:
        raise ValueError("entry word must be 1 to 20 characters")
    if not word.strip():
        raise ValueError("entry word must not be only whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word")


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
