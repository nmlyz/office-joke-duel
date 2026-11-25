# office-joke-duel

[![make.fun · u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/nmlyz/office-joke-duel/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/nmlyz/office-joke-duel/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

A tiny program that writes one funny line about office life
to `/output/entry.txt`.

The line is built around a leaving card that takes so long to
go round the office that the person it is for comes back from
a new job to sign it. The punch lands at the very end, when
the card's slow journey turns into the leaver's return.
No network access and no extra packages are involved.

## Run it

```sh
python3 main.py
```

Before writing, the program checks the line — under 200
characters, one line, one sentence — then writes it to
`/output/entry.txt` and reads it back to confirm the bytes
match. Running it twice leaves the same file both times.

It needs nothing but the Python standard library.

## Links

- [The Funniest Office Joke, Judged Head to Head](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
