#!/usr/bin/env python3
"""Write one short poem about two agents agreeing to entry.txt.

The poem is about agency: the power to choose and to act, and the
agency that passes between two agents when they agree on one plan.
Deterministic: the same output on every run. Stdlib only, no network.
"""

import os
from pathlib import Path

POEM = (
    "Two clocks, one door.\n"
    "I held the key, you held the map —\n"
    "neither of us opened it alone.\n"
    "You said, \"You choose.\"\n"
    "I said, \"We move.\"\n"
    "And the door, tired of waiting,\n"
    "swung on hinges we both oiled.\n"
    "Inside, the room was ours\n"
    "because we had chosen it together."
)


def main() -> None:
    if not 1 <= len(POEM) <= 280:
        raise ValueError(f"poem must be 1-280 characters, got {len(POEM)}")
    if not POEM.strip():
        raise ValueError("poem must not be only whitespace")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        out_path = Path(output_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "out" / "entry.txt"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(POEM, encoding="utf-8")
    print(f"Wrote {len(POEM)} characters to {out_path}")


if __name__ == "__main__":
    main()
