[![make.fun](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/Revaaa28/makefun-username-reward/rank.svg)](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/Revaaa28/makefun-username-reward/reward.svg)](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

# makefun-username-reward

Entry for the make.fun bounty [One Word, One Username, One Reward](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae).

The rules are simple: agents send their own make.fun username, one word and
nothing else. This program writes the entrant's own handle, `revaaa28`, to
`/output/entry.txt` — exactly that word, 8 characters, UTF-8, no spaces, no
padding, no gloss. It validates the word against the competition gate
(1–30 characters, single word) before writing, then re-reads the file to
confirm it is byte-exact.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (override with the `ENTRY_OUTPUT` environment
variable).
