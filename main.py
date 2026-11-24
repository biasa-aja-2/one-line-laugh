#!/usr/bin/env python3
"""The One-Line Laugh - writes one funny line to /output/entry.txt.

Pure standard library. Deterministic: every run writes the same line.

The line, per the judge's brief:
- Everyday truth everyone recognises: a smoke detector's low-battery
  chirp always seems to start in the middle of the night.
- Surprise at the very end: "and a grudge" reframes the beeping as
  deliberate, personal malice from a small plastic disc on the ceiling.
- Economical: one sentence, nothing there to explain the joke.
- Fresh angle vs the round-1 entry (a houseplant named Wi-Fi): this one
  personifies a household device instead of renaming one, and the twist
  lands on the last three words.
"""

import os

LINE = "My smoke detector only beeps at 3 a.m., which is how I know it has a sense of humor and a grudge."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Self-check against the gate: 1-200 chars, one line, not blank.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 chars, got %d" % len(text)
    assert "\n" not in text, "line must be a single line"
    assert text.endswith("."), "line must end with a period"
    assert "  " not in text, "line must not contain double spaces"
    assert len(text.split()) <= 40, "line must stay economical, got %d words" % len(text.split())
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d chars to %s" % (len(LINE), OUTPUT_PATH))


if __name__ == "__main__":
    main()
