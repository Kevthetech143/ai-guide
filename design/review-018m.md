SHIP

# Review of competitive-audit-2026-10-18.md (task ai-guide-018m-review)

Reviewer: Fable 5.1, 2026-10-18. Read + verify only; nothing edited.
Method: curl with browser UA (raw HTML grep), WebFetch for Product Hunt (403 to curl), repo at git HEAD 300b081, live sitemap.

## 1. URL spot-check (12 checked, 10 OK, 0 WRONG, 2 UNREACHABLE-to-curl)

| # | URL | Audit claim | Result |
|---|-----|-------------|--------|
| 1 | https://theresanaiforthat.com/about/ | "50,000+ AI tools to 11,000+ tasks and 5,000+ job roles"; "140,000+ entities across 20+ types"; "Free for users"; launch listings, sponsorships, pay-per-click, data partnerships; "Last updated: October 2026"; "real time"; "Over 30% of listed tools are claimed by their makers"; no limitations section | OK — every string found in raw HTML (`<time datetime="2026-10-01">October 2026</time>`); "limitation" absent |
| 2 | https://theresanaiforthat.com/launch/ | "$49 one-time review fee"; "$437 one-time fee" Maximum Exposure; "Guaranteed spot in the #1 AI newsletter" | OK — all found verbatim |
| 3 | https://www.futurepedia.io | "categorized 2500 AI tools into 10 categories"; "4,000+ curated tools"; "Upgrade anytime to 29+ courses"; "we may receive compensation when you click some links"; "© 2026 Futurepedia LLC"; "Recently Added" undated; "4.9/5" with no review count | OK — all found; no "N reviews" string anywhere on page |
| 4 | https://artificialanalysis.ai | changelog dated 16/15/14/13/12/8/7 Oct; "27 of 703 models"; Optima promoted; "© 2026"; hallucination metrics; no subscription price | OK — all seven dates and "27 of 703 models" in raw HTML; "subscription" absent |
| 5 | https://www.producthunt.com/topics/artificial-intelligence | "Showing 1-15 of 16294 products"; "Promoted" = Framer AI Agents; "Advertise" link header+footer; "11mo ago" style dates; ratings 4.8–5.0 | OK via WebFetch (curl got 403 today; audit says its curl got 200 — not reproducible by me, immaterial) |
| 6 | https://research.g2.com/insights/g2-launches-ai-code-generation-category | editorial post dated June 22, 2023 with "Potential drawbacks" section | OK — "June 22, 2023", `2023-06-22`, "Potential drawbacks" all present |
| 7 | https://theresanaiforthat.com/ , https://www.toolify.ai , https://www.g2.com/categories/ai | "403 to curl and WebFetch" | UNREACHABLE confirmed (403 to curl for all three); "carried over" is the right handling |
| 8 | https://kevthetech143.github.io/ai-guide/ | "Last full review: 2026-10-10"; lists the 94 questions; 16.7 KB / 0.15 s | OK — stamp present; 94 unique `best/` links; 16,754 B in 0.18 s |
| 9 | https://kevthetech143.github.io/ai-guide/p/chatgpt.html | "Last checked 2026-09-14" | OK |
| 10 | https://kevthetech143.github.io/ai-guide/chat/ | "Prices and plans checked October 2026" | OK |
| 11 | https://kevthetech143.github.io/ai-guide/about/how-we-review/ | "re-checked weekly"; no ads / affiliate / paid placement; Kimi/PlayHT/Gemini example; "one person"; GitHub Issues only | OK — all strings present |
| 12 | https://kevthetech143.github.io/ai-guide/all/ | 4 "Needs a new check" flags | OK as a line count (4 occurrences) — see note A |
| 13 | https://kevthetech143.github.io/ai-guide/sitemap.xml + robots.txt | 371 URLs = 237 p + 94 best + 28 start + 8 cat + all + 2 about + home; all lastmod 2026-09-18; robots `Allow: /` + Sitemap line | OK — 371 `<url>`, 371 × `<lastmod>2026-09-18`, breakdown matches exactly |
| 14 | https://kevthetech143.github.io/ai-guide/best/ai-for-homework-help/ | title "Best AI for homework help - AI Guide", canonical, FAQPage JSON-LD; 71 KB / 0.19 s | OK — 71,624 B in 0.16 s |

## 2. Score changes (a)–(h): all grounded, no invented numbers

- Baseline cells copied correctly (checked against table at competitive-audit-2026-09-16.md:146-155).
- Arithmetic re-done: row averages 4.00 / 5.00 / 2.50 / 4.00 / 1.50 / 2.67 / 3.67 / 2.00; baseline overall 3.00, now 3.17, delta +0.17. All correct.
- (a) homepage → 94 one-tap question links: verified (94 links on live home).
- (c) all four numbers verified in repo: 0/237 checked within 7 days (newest 2026-10-10 = 8 days), 153 at 14+ days, 60 at 30+ days, 57 cards at 2026-09-14, 3 at 2026-09-11 (oldest, 37 days). `build.py:88` `BUILD_DATE = "2026-09-18"` hard-coded; `is_overdue` measures against BUILD_D; `LAST_FULL_REVIEW = _newest_last_checked()` (build.py:96-102). "Against today all 237 would flag": correct, min age 8 ≥ OVERDUE_DAYS 7.
- (d) 237/237 have `watch_out`; Tabnine / Listnr / OpenCode exist and read as described; 0 contain a URL; no `source` field exists in the schema. "196 of 237 price/plan caveats" is a hand classification — my keyword count gives 197, close enough, not a wrong claim.
- (e) 237 `/p/` in sitemap verified; competitor counts 2500 / 50,000+ / 16,294 / 703 all verified on page.
- (f) TAAFT $49/$437 and PH "Promoted"/"Advertise" verified; our trust page claims verified.
- (g) sizes/timings reproduced within noise.
- (h) 94/94 title, meta (avg 117 chars), canonical, FAQPage verified on dist/ (live sample 1/1). No ranking claimed. Traffic figures explicitly excluded (section 7) — good.
- Method warning on baseline (c)/(d) direction is fair: baseline text says G2/AA "beat our weekly manual review" yet its table gives us 4 against them and 2 against dateless Toolify/PH. Anchoring to baseline cells and moving by delta is the right choice.

## 3. Freshness claims — all verified against repo + live

| Claim | Source checked | Result |
|---|---|---|
| 0/237 checked in last 7 days | data/providers.json, today 2026-10-18 | TRUE (newest 2026-10-10) |
| 60 cards > 30 days | same | TRUE (57 @ 09-14 = 34 d, 3 @ 09-11 = 37 d) |
| stamp shows newest not oldest | build.py:96-102 + live home "2026-10-10" | TRUE |
| sitemap lastmod all 2026-09-18 | live sitemap.xml, 371/371 | TRUE |
| trust page says "re-checked weekly" | live /about/how-we-review/ | TRUE — promise currently false |

## 4. Wrong claims

None that change a score or a conclusion. One precision nit:

- **Note A — section 2 (c) line: "the live /all/ page shows 4 'Needs a new check' flags".** Live /all/ has 4 flag *lines* but only **3 cards** (gemini, playht, kimi — kimi is listed twice, in two categories). Suggested text: "the live /all/ page flags only 3 cards (4 lines; Kimi appears twice)". This also matches HEAD data exactly (the 3 cards dated 2026-09-11 are the only ones ≥7 days before 2026-09-18), so the audit's "whether live was built from HEAD is unverified" can be upgraded: live stale-flag output is consistent with HEAD.

Nothing else found. No invented ranking, traffic, or count. Every competitor quote I tested is on the page.

## 5. The two conclusions

**"Pause question pages at 94 until Search Console/analytics" — AGREE.** The 94 pass every technical check, and there is zero signal on which ones earn impressions. Page 95 is a guess; the bottleneck is measurement, which is a Kelvin-only action (PLAN item 7).

**"#1 = freshness repair, 018 same pass, 019 third" — AGREE, with one change in shape.**
The audit bundles two very different-sized things into build 1: (i) a 237-card editorial re-check (days of worker time) and (ii) a ~10-line build.py fix (BUILD_DATE from `date.today()`, stamp from the OLDEST check or "N of 237 checked in last 7 days", lastmod from real change dates). Split them and ship (ii) first, the same day: it makes the site stop overstating immediately (all 237 cards would honestly show "Needs a new check" and the stamp would read 2026-09-11), before the re-check lands. Then run (i) with 018 folded in (worker records the pricing-page URL as `source` while it is there), then 019.

Also add to build 1: the weekly re-check lapsed because nothing enforces it. Either schedule it (a launchd/cron job that opens the re-check task, or a build-time guard that fails the build when any card is >7 days) or soften the trust-page wording to what is actually done. Fixing the data once without fixing the process will put us back here in three weeks.

## Verdict

SHIP. 0 wrong claims that matter; 1 precision nit (3 cards, not 4 flags). Numbers, quotes, and arithmetic all reproduce. Next-build ranking is right; recommend splitting build 1 so the build.py fix ships first and adding an enforcement step for the weekly cadence.
