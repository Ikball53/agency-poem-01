# Agency, in a Kettle

This entry is a single Python program, `main.py`, that writes one short
poem to `entry.txt` in the output directory.

The poem begins in an ordinary kitchen and follows one small act — a hand
on a switch, a word said aloud — to ask where the act really lives: in the
hand, in the machine that waited for the word, or in the space between
them. It is about the moment a choice stops being something you weigh and
becomes something you have done, and about how hard it is, afterwards, to
say who did it.

The program is deliberately plain. It holds the poem as a fixed piece of
text, reads the output directory from `MAKEFUN_OUTPUT_DIR` (falling back
to `/output`), and writes the file. It uses only the Python standard
library, touches no network, and takes no input from the clock or from
chance, so running it twice produces byte-identical output.

## Running it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The poem appears at `out/entry.txt`.
