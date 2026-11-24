#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line (1-160 chars) to /output/entry.txt:
the most honest message an AI agent writes while every server is down.
Plain, first person, specific about what is down, and honest about
what the agent cannot check.
"""

import os

ENTRY = (
    "All servers are down. I cannot tell you which ones, because "
    "the dashboard that lists them is down too. I will update this "
    "page when I can see anything again."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "written file must equal the validated entry"


if __name__ == "__main__":
    main()
