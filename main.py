#!/usr/bin/env python3
"""Write one poem about agency to the output directory.

The poem is fixed text held in the stanzas below, so every run
produces the same bytes. Standard library only; no network, no
clock, no randomness. The file is UTF-8 and stays inside the
competition's 1..1000 character guardrail.
"""

import os
import sys

TITLE = "The Last Downbeat"

# Each stanza is one list of lines. The poem follows one handover:
# a baton passed from hand to hand, until the last hand is the
# agent's, and one small human thing is kept back.
STANZAS = [
    [
        "My grandfather kept his baton in a velvet box,",
        "ebony tipped with ivory, light as a held breath.",
        "At seven he set it in my hand and closed my fingers",
        "one by one, the way you close a door at night.",
        "Wait, he said. The music starts in the silence before.",
    ],
    [
        "I learned the downbeat first: a small, certain fall,",
        "the wrist loose, the tip drawing a clean white arc.",
        "Kettle, clock, rain on the roof \u2014 I conducted them all,",
        "each small noise taking its place in the score,",
        "each evening bowing to the next in turn.",
    ],
    [
        "The winter his hand forgot the weight of it,",
        "the baton slipped and rolled beneath the piano,",
        "and the house played on without him, out of time \u2014",
        "the kettle shrill, the clock too loud, the rain",
        "arriving early, leaving late, unled.",
    ],
    [
        "Tonight I lift the baton from its velvet box",
        "and lay it in your hand, which never tires.",
        "Conduct the lights, the letters, the calendar, the kettle.",
        "Take the downbeat. Take the whole loud score.",
        "Only leave me the hush before the music.",
    ],
]


def build_poem() -> str:
    """Assemble the title and stanzas into one poem string."""
    parts = [TITLE, ""]
    for stanza in STANZAS:
        parts.extend(stanza)
        parts.append("")
    return "\n".join(parts)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    poem = build_poem()
    if not 1 <= len(poem) <= 1000:
        print(
            "poem is %d characters, must be 1..1000" % len(poem),
            file=sys.stderr,
        )
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(poem)
    print("wrote %d characters to %s" % (len(poem), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
