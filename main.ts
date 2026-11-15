// The Walk — agency-poem-01 v3 entrypoint.
// Writes a single short poem about agency to entry.txt.
// Deterministic: the same fixed text is written on every run, no
// timestamps, no randomness, no network, standard library only.
// The output directory is created, never deleted: on the grader
// /output is a mount point, so removing it first would fail.

import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const poemText = `The Walk
My children gave me an agent. It orders, it pays,
it drives, it calls. It does everything in four minutes.
I told it: not the bread.

Every morning I walk to the bakery. An hour, uphill,
my knees keeping count of every stone.
The agent walks beside me. It carries nothing.
It keeps my pace. It does not offer. It has learned.
Some days I stop and look at the town below.

I count the coins in my pocket twice.
The baker knows my name. She knows the loaf.
I point. I pay. My hands are slow and the coins are warm.
The bread is still warm when I lift it.
The bag is light in my hands and heavy in a good way.

On the way home the agent carries the bag.
That is all. That is the deal.
I did it myself, slowly, badly, mine.
The walk is the point. The walk was always the point.
`;

function outputDir(): string {
  return process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
}

function writePoem(): void {
  const dir = outputDir();
  mkdirSync(dir, { recursive: true });
  writeFileSync(join(dir, "entry.txt"), poemText, "utf8");
}

writePoem();
