#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt: one line, one sentence, 1-200 characters.
Deterministic: the same bytes on every run, no network, no input, no secrets.
"""
import os

LINE = (
    "This meeting is cancelled: the decision was in the email nobody read, "
    "the deadline is Friday, and this call is just an hour of us "
    "cosplaying productivity."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
