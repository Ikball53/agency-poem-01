"""Write one fixed poem about agency to entry.txt.

The poem is a constant: no network, no randomness, no clock.
The output directory comes from MAKEFUN_OUTPUT_DIR, or /output.
"""

import os

POEM = """The kettle was already warm.
I stood with my hand on the switch
the way you stand at a door
that is already unlocked.

Nothing asked me to choose.
That was the choosing.

Somewhere a machine waited
for a word it could not give itself —
a yes is only a yes
when somebody says it.

So I said it.
The water rose. The room filled
with steam and the small sound
of a thing finding what it was for.

Later, when they ask who did it,
I will not know how to answer.
My hand. The switch. The heat.
The whole of it, mine and not mine.

What I know is this: the door
was open the whole time.
Agency was never the opening.
It was stepping through.
"""

OUTPUT_ENV = "MAKEFUN_OUTPUT_DIR"


def main() -> None:
    output_dir = os.environ.get(OUTPUT_ENV) or "/output"
    # Fixed text in, fixed bytes out: identical on every run.
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
