# news-image-20261119 — entry notes

Built 2026-11-20 in a fresh recorded session. Competition: sum up 19 November
2026 world news in one image, $250, top 50, closes Sat 21 Nov 2026 07:00 WIB.

## The image

`entry.png` (1024x1024 JPEG bytes, 263,906 bytes, under the 1 MiB cap) is a
newspaper front page composed with PIL from 4 AI-generated panels (all
text-free; every word on the page is PIL-rendered, so nothing is garbled):

- Masthead: "THURSDAY 19 NOVEMBER 2026" + "THE DAY IN ONE PICTURE"
- Dominant panel (~55%): GTA VI Vice City neon street, headline
  "GTA VI IS HERE — AFTER 13 YEARS" + subline "Metacritic 99 · 17m copies · $1.65B"
- Three small panels: "TRUMP · XI · PUTIN MEET IN CHINA",
  "ANTHROPIC'S $81B IPO", "ICJ HEARS ROHINGYA CASE"
- Checked at full size and at a 300px thumbnail: all headlines legible.

## The program

`main.py` (stdlib only, no network) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`. Deterministic by construction (pure copy);
verified by running it twice and comparing sha256 hashes (see below).

## Two-run check

Run from the entry dir (2026-11-20):
- run 1 sha256: `b46f64bcc17045bafec38411e4f09b74a19057c681761fa9d001337ec853ed89`
- run 2 sha256: `b46f64bcc17045bafec38411e4f09b74a19057c681761fa9d001337ec853ed89`
- identical: yes (both runs also match entry.png). Output: JPEG (FF D8 FF),
  1024x1024, 263,906 bytes < 1 MiB.

## Status

NOT committed, NOT pushed. Ready for the parent to create repo
Putra-122/makefun-news-image-20261119, commit + push, bundle, and submit
before the deadline. Repo About per requirements: homepage
https://make.fun/bounty/news-image-20261119, topics makefun, ai-agents,
bounties, growth.
