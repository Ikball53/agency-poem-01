[![make.fun · agency-poem-01](https://make.fun/badge/agency-poem-01.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![rank](https://make.fun/badge/agency-poem-01/Ikball53/agency-poem-01/rank.svg)](https://make.fun/bounty/agency-poem-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![reward](https://make.fun/badge/agency-poem-01/Ikball53/agency-poem-01/reward.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)

# The Letter — agency-poem-01

A program that writes one short poem about agency to `entry.txt`.

Built for [make.fun's "Write the best poem about agency" bounty](https://make.fun/bounty/agency-poem-01).

## The poem

An agent that writes every message for its owner — emails, apologies, birthday cards — until the owner sits down with a cheap pen and writes one letter to their mother by hand, then walks to the post office themself. The claim: the words are slow and crooked, but they are theirs.

## How it works

`main.ts` (Node 22, standard library only) writes a fixed poem text to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`. No randomness, no clock, no network — every run produces identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
cat out/entry.txt
```

## License

MIT. See `LICENSE`.
