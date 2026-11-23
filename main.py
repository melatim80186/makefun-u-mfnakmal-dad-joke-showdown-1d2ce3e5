#!/usr/bin/env python3
"""Dad Joke Showdown entry: write one dad joke to /output/entry.txt.

The joke (88 chars, ASCII):
    My daughter asked why the moon is always broke. I said, 'It's down to its last quarter.'
"""

import os

# The winning joke (88 chars, ASCII). The turn: "broke" primes money, and
# "quarter" lands it twice at once -- a coin, and a phase of the moon.
# Punchline word is the last word, so the joke ends on the pun.
JOKE = "My daughter asked why the moon is always broke. I said, 'It's down to its last quarter.'"

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text: str) -> bytes:
    """Enforce the competition gate and return the exact bytes to write.

    /output/entry.txt must be UTF-8 text of 1-200 chars, not only whitespace.
    """
    assert isinstance(text, str), "entry must be str"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    data = text.encode("utf-8")  # raises on non-UTF-8; also pins the exact bytes
    assert data.decode("utf-8") == text, "entry must round-trip as UTF-8"
    return data


def main() -> None:
    data = gate_check(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    print(f"wrote {OUTPUT_PATH} ({len(JOKE)} chars, {len(data)} bytes)")


if __name__ == "__main__":
    main()
