# WORLD DEPARTURES — 27 November 2026

[![make.fun](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/crisdion3006/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/crisdion3006/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127)

A make.fun entry: one image summing up the world's news of Friday
27 November 2026, drawn entirely in code.

## The image

A split-flap airport departure board — the day's news as departing
flights, each row a story:

1. **Kuwait** — a drone strike kills 2 Italians; Iran denies
   responsibility.
2. **Gaza** — the latest from the war.
3. **Thanksgiving storm** — the storm grounds flights and the Macy's
   parade is postponed.
4. **Mali** — 300+ Russians killed backing the junta.
5. **France** — the presidential vote debacle.
6. **Ibiza** — a diesel tanker capsizes.
7. **UK** — net migration falls to its lowest since 1997.

## How it is built

`build_image.py` (Python, PIL only) draws the poster deterministically
and writes `entry.png`. `main.ts` (Node 22, stdlib only) copies that
exact image to `/output/entry.png`, byte for byte.
