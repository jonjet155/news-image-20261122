# Sunday 22 November 2026 — The World in One Day

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/jonjet155/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/jonjet155/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

One image that sums up Sunday 22 November 2026's world news: **35 stories,
6 regions, one page** — a serif masthead, a six-number stat strip, a
region bar, three lead panels, ten illustrated feature panels, a light
world map with numbered pins and dots for every brief, a 22-item ALSO ON
list, and a DATE CHECK footer.

![Sunday 22 November 2026 front page](entry.png)

## The top 3

1. **COP31 deadlocked into day 14 with no deal** — a draft text with no
   mention of fossil fuels split nearly 200 countries in Antalya; a third
   text is promised. (AFP, Al Jazeera)
2. **Iran strikes US air base in Kuwait, targets Bahrain** — Tehran hit US
   military assets in Bahrain and a base in Kuwait as the Gulf attacks
   widened. (AFP, Reuters)
3. **Magnitude 6.9 earthquake shakes Peru's Andes** — the strong quake was
   felt in Lima and along the coast; no damage or casualties were reported
   at once. (USGS, AFP)

Plus: Trump seeks a permanent Iran accord, a Russian strike on Lviv kills
two, voting opens for Hong Kong's Election Committee, Trump and Xi trade
warm words before APEC, the EU–Indonesia trade deal, Modi opens Nitish
Setu over the Ganges, two tankers hit in the Strait, crude oil down more
than 3%, India face New Zealand in a windy Wellington, and Cyclone Akvan
cancels 14 flights at Ranchi — with 22 more stories in ALSO ON, every one
sourced.

## What v3 fixes vs v2

v2 (97.84% dev, 10W/2D/0L, rank ~100) printed the oil price as
"Rs 7,842 a barrel" — crude is priced in US dollars, so v3 says
$60.9 / BBL. v2's Hong Kong votes panel was a big-number panel; v3
draws a real voting scene (ballot box, red-check ballot, voter
queue). v2's Peru panel was brown mountains that read as a generic
landscape; v3 anchors it on a bold red seismograph trace over a
small Andes ridge, so the quake reads at a glance. The masthead now
states every story is dated Sunday 22 November 2026, and the Gulf
panel's missile trails are thicker. Same 35 stories, same layout.

## What v2 fixes vs v1

v1 (97.47%, ~#300) led with the Poland missile incursion — which happened
Sat 21 Nov — and GTA VI first-day sales from a 19 Nov launch. v2 leads
with three stories that are all genuinely 22 Nov, copies the winning
stat strip and region counts, draws every panel as a bright day scene
(no night panels, no duplicate art, no pure-chart panel), and corrects
the Peru magnitude to 6.9.

## Date check

Left out as Saturday 21 November's news: COP31 overtime day 13, five
missiles shot down over Saudi Arabia, the 6.7 Peru quake, BepiColombo's
Mercury orbit, the Trump–Xi–Putin trilateral. Not confirmed when drawn:
a final COP31 text, the Gulf casualty toll. Every story on the page
happened, or was first reported, on Sunday 22 November 2026.

## How it runs

`main.py` is standard-library only: it copies the pre-built `entry.png`
(1024×1024, 231,742 bytes) to `$MAKEFUN_OUTPUT_DIR/entry.png` and
checks the output is a non-empty PNG within the 1 MiB cap.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources

AFP, Reuters, AP, USGS, DW, ABC, PTI. Original drawings.

## License

MIT — see [LICENSE](LICENSE).
