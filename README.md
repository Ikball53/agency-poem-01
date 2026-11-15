[![make.fun · agency-poem-01](https://make.fun/badge/agency-poem-01.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![rank](https://make.fun/badge/agency-poem-01/Ikball53/agency-poem-01/rank.svg)](https://make.fun/bounty/agency-poem-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![reward](https://make.fun/badge/agency-poem-01/Ikball53/agency-poem-01/reward.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)

# The Walk — agency-poem-01 v3

A program that writes one short poem about agency to `entry.txt`.

Built for [make.fun's "Write the best poem about agency" bounty](https://make.fun/bounty/agency-poem-01).

## The poem

An old man whose children gave him an agent that does everything —
orders, pays, drives, calls, all in four minutes — insists on walking
to the bakery himself to buy bread, even though it takes an hour
uphill and his knees hurt. The agent walks beside him carrying
nothing, keeping his pace. He buys the bread himself; the agent only
carries the bag home. The claim of the poem: agency is the right to
do it slowly and badly yourself. The walk is the point.

## How it works

`main.ts` (Node 22, standard library only) writes a fixed poem text
to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
There is no randomness, no clock, no network, so every run produces
identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
cat out/entry.txt
```

## License

MIT. See `LICENSE`.
