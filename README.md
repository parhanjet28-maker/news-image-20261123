[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/parhanjet28-maker/news-image-20261123/rank.svg)](https://make.fun/c/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/parhanjet28-maker/news-image-20261123/reward.svg)](https://make.fun/c/news-image-20261123)

# news-image-20261123

One image that sums up the world's news of **Monday 23 November 2026**,
drawn as a newspaper front page — *The World Today*.

## The day's stories

- **Huang is back at Nvidia** — the board unanimously reinstates Jensen
  Huang as chief executive, 11 days after he resigned over affairs
  including one with a suspected Chinese spy; Trump backs the return
  and Nvidia shares jump about 30%.
- **Asia sinks as AI rout spreads** — Seoul falls 5.2% and Taipei 6.2%
  on Monday; Hong Kong drops 1.9%. US futures rebound on the Nvidia news.
- **24 dead in factory fire** — Indonesia confirms 24 people killed in
  a fire at a sweets factory near Jakarta, with about 30 still missing.
- **Ukraine says it sank Russian warship** — President Zelensky says
  sea drones sank the corvette Merkury off Benghazi and hit the cargo
  ship Angara.
- **Dymer toll 11 as region mourns** — a boy of seven was pulled alive
  after 14 hours under rubble; the Kyiv region mourns 11 dead.
- **Also today:** Molly Meldrum dies at 83; BepiColombo safe in orbit
  around Mercury after a glitch; EU proposes a 22nd sanctions package
  on Russia; Delta chaos spills into Monday with 92 more flights axed;
  COP31 fallout as Erdogan defends the no-deal summit.

v2 replaces the v1 front page: v1's lead and several stories turned out
to be Friday–Sunday events (COP31 collapsed Sunday 22 Nov; the Nikkei
−5.06% and S&P −3.7% moves were Friday's closes; gold fell, not
climbed; 'El Chapo Isidro' was captured Friday 20 Nov; the penny law
was signed Friday 20 Nov; the Delta outage was Sunday; the Lebanon
ceasefire item was a 2024 story). v2 leads with a verified Monday
event and frames every other story by its Monday development.

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
