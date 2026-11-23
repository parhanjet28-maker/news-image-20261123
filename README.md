[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/parhanjet28-maker/news-image-20261123/rank.svg)](https://make.fun/c/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/parhanjet28-maker/news-image-20261123/reward.svg)](https://make.fun/c/news-image-20261123)

# news-image-20261123

One image that sums up the world's news of **Monday 23 November 2026**,
drawn as a newspaper front page — *The World Today*.

## The day's stories

- **COP31 collapses** — the climate summit in Antalya, Turkey ends with no
  deal after the longest talks in UN history; the EU and ~130 nations reject
  a draft text that omits fossil fuels.
- **AI sell-off sinks stocks** — Nikkei −5.06%, S&P 500 −3.7% as fears that
  AI shares are overpriced spread across Asia; gold climbs.
- **Boy, 7, pulled alive from rubble** — a Russian strike on Dymer, north
  of Kyiv, kills at least 10.
- **Russian warship sunk** — a Ukrainian naval drone severely damages the
  corvette Merkury off Benghazi, Libya.
- **'El Chapo Isidro' captured** — FBI most-wanted cartel leader Fausto
  Isidro Meza Flores is arrested in Sinaloa, Mexico.
- **Also today:** the penny ends as Trump signs the Common Cents Act; a
  Delta outage delays 1,600+ flights; Lebanon ceasefire brings villagers
  home; Molly Meldrum dies at 83.

## How it is built

`draw.py` (Python 3 + Pillow, Liberation fonts) draws the front page to
`entry.png` (1024×1024, PNG). `main.ts` (Node 22, standard library only)
copies `entry.png` to `/output/entry.png` — the program runs with no
network, so the simplest entry is a repository holding the image and a
one-line program that copies it there.

```sh
python3 draw.py                                   # regenerate entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts  # run the entry
```

Built for the [news-image-20261123 competition on make.fun](https://make.fun/c/news-image-20261123).
