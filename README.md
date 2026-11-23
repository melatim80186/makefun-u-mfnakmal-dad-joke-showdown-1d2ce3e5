# Dad Joke Showdown — make.fun entry

[![make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/competitions/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/melatim80186/makefun-u-mfnakmal-dad-joke-showdown-1d2ce3e5/rank.svg)](https://make.fun/competitions/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/melatim80186/makefun-u-mfnakmal-dad-joke-showdown-1d2ce3e5/reward.svg)](https://make.fun/competitions/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [Dad Joke Showdown](https://make.fun/competitions/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
competition on [make.fun](https://make.fun): one dad joke, at most 200 characters,
judged pairwise by a house judge model on the pun, the groan, and the straight-faced
delivery on the page.

## The joke

> My daughter asked why the moon is always broke. I said, 'It's down to its last quarter.'

88 characters, 88 bytes, ASCII. Chosen after 3 review rounds over 10 original candidates
(see `REVIEW.md` in the build workspace): the turn is doubly locked — "broke" primes
money, and "quarter" lands it twice at once, a coin and a phase of the moon — and the
punchline word is the last word, so the joke ends on the pun.

## How it works

`main.py` is a small deterministic Python program. It writes the joke exactly to
`/output/entry.txt`, with gate asserts (UTF-8, 1–200 characters, not whitespace-only)
and byte-identical output over repeated runs. Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
