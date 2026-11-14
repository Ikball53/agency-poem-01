# The Baton

A program that writes one short poem about agency to `entry.txt`.

The poem follows a single handover: a conductor's baton passed
from a grandfather's hand to a child's, then, when the hand
falters, to an agent that never tires — with one small human
thing kept back at the end.

Run it with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

It needs nothing but the Python standard library, makes no
network calls, and writes the same poem on every run.
