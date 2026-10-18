# Competitive audit re-run — ai-guide vs the same 6 directories

Date: 2026-10-18 (task ai-guide-018m). Research only; no site, data, or build file was touched.
Baseline: `design/competitive-audit-2026-09-16.md` (average 3.0/5).
Our site today (live, opened): 237 providers, 94 question pages (`/best/`), 8 categories,
`/start/` picker, `/about/how-we-review/`, sitemap with 371 URLs.

## 1. Changes per competitor (only what changed since 2026-09-16)

Fetch methods: WebFetch and curl with a browser user-agent. Three sites returned HTTP 403 to both.

### TAAFT — https://theresanaiforthat.com
- Homepage: not reachable today (403 to curl and WebFetch). Homepage-based baseline claims **carried over**.
- Opened https://theresanaiforthat.com/about/ (WebFetch): count now stated. "50,000+ AI tools to 11,000+ tasks and 5,000+ job roles"; "140,000+ entities across 20+ types". Baseline said count not stated. Self-reported.
- Money, same page: "Free for users." Builders pay for "launch listings," sponsorships, and pay-per-click; also "data partnerships."
- Money, https://theresanaiforthat.com/launch/ (WebFetch): "$49 one-time review fee" basic listing; "$437 one-time fee" Maximum Exposure tier with a "Guaranteed spot in the #1 AI newsletter". The baseline had only "Ad" labels and an unverified premium plan, so paid listing is now confirmed and priced.
- Freshness, about page: "Last updated: October 2026"; "tracks each tool's version releases in real time"; dead tools retired by "automated and manual checks". Page-level dating exists now. Per-card dates still not seen (cards not reachable).
- Downsides: the about page has no limitations section. It says "Over 30% of listed tools are claimed by their makers", so some copy is vendor-written.

### Futurepedia — https://www.futurepedia.io
- Opened (WebFetch). Count: "We've categorized 2500 AI tools into 10 categories" (baseline 2503) and still "4,000+ curated tools". The fetch summary also reports category counts summing to about 4,647 (summary arithmetic, unverified). The numbers still conflict.
- Money: free course access, "Upgrade anytime to 29+ courses". New disclosure line: "To keep our site free, we may receive compensation when you click some links on our site." Sponsored listings: page does not say.
- Dating: only "© 2026 Futurepedia LLC". No per-tool dates. "Recently Added" has no dates.
- Downsides: none. Every blurb is positive. Ratings like "4.9/5" show with no review count.

### Toolify — https://www.toolify.ai
- Not reachable today (403 to curl and WebFetch; /about-us also 403). **Carried over** in full: sponsored Featured section, dateless cards, no downsides.

### Product Hunt, AI topic — https://www.producthunt.com/topics/artificial-intelligence
- Opened (WebFetch and raw curl, 661 KB). Baseline page was near-blank to my fetcher; this time it rendered.
- Count now measurable: "Showing 1-15 of 16294 products" (confirmed in raw HTML).
- Money: one item labeled "Promoted" (Framer AI Agents); "Advertise" link in header and footer.
- Dating: relative only ("11mo ago", "4mo ago"). No exact dates on cards.
- Downsides: almost none. Ratings 4.8–5.0 shown; the only skepticism is in forum threads.

### G2 AI — https://www.g2.com/categories/ai
- Not reachable today (403; /categories/ai-agents also 403). **Carried over**: Key Strengths / Potential Drawbacks from user reviews, no paid placement in ratings, quarterly dated reports.
- Only new G2 evidence: https://research.g2.com/insights/g2-launches-ai-code-generation-category (opened) is an editorial post dated June 22, 2023 with a "Potential drawbacks" section. Not a change.

### Artificial Analysis — https://artificialanalysis.ai
- Opened (WebFetch and raw curl, 1.48 MB). Changelog is dated to the day and current: 16 Oct, 15 Oct, 14 Oct, 13 Oct, 12 Oct, 8 Oct, 7 Oct (day and month only; footer "© 2026"). "16 Oct" confirmed in raw HTML.
- Count: "27 of 703 models" in the Intelligence section (703 confirmed in raw HTML). Baseline said "hundreds" (unverified).
- Money: no ads. Own products promoted (e.g. Optima, a custom benchmark builder). No subscription price found on the homepage.
- Downsides: unchanged; it publishes cost and hallucination metrics as data.

## 2. Score table, baseline vs now

Same 8 dimensions, same 1–5 scale, same per-competitor columns as the baseline. Each cell is our
standing against that competitor. Format: baseline → now. Competitors I could not re-open
(Toolify, G2) keep their baseline cell unless OUR site changed in a way that applies to them.

| Dim | TAAFT | Futurepedia | Toolify | ProdHunt | G2 | AA | baseline avg | now avg | delta |
|-----|-------|-------------|---------|----------|----|----|---|---|---|
| (a) 3-tap answer | 3→4 | 3→4 | 3→4 | 3→4 | 4→4 | 4→4 | 3.33 | 4.00 | +0.67 |
| (b) readability | 5→5 | 5→5 | 5→5 | 5→5 | 5→5 | 5→5 | 5.00 | 5.00 | 0 |
| (c) price current + dated | 3→2 | 3→3 | 2→2 | 2→2 | 4→3 | 4→3 | 3.00 | 2.50 | -0.50 |
| (d) honest downsides | 3→4 | 3→4 | 3→4 | 3→4 | 4→4 | 4→4 | 3.33 | 4.00 | +0.67 |
| (e) breadth | 1→1 | 2→2 | 1→1 | 1→1 | 2→2 | 1→2 | 1.33 | 1.50 | +0.17 |
| (f) trust signals | 2→3 | 3→3 | 3→3 | 2→3 | 2→2 | 2→2 | 2.33 | 2.67 | +0.33 |
| (g) speed, clutter | 4→4 | 4→4 | 4→4 | 4→4 | 3→3 | 3→3 | 3.67 | 3.67 | 0 |
| (h) findable | 2→2 | 2→2 | 2→2 | 2→2 | 2→2 | 2→2 | 2.00 | 2.00 | 0 |
| **Overall** | | | | | | | **3.00** | **3.17** | **+0.17** |

Method warning: the baseline's (c) and (d) cells read backwards (our site scored 4 against G2/AA,
who beat us, and 2 against dateless Toolify/PH, who we beat). I kept the baseline cells as the
anchor and moved each by what changed. Deltas are meaningful; absolute (c)/(d) values are not
comparable across rows.

One-line reasons, each tied to a page opened on our live site:

- (a) 3→4 on four: 94 question pages are each a one-tap answer from the homepage (https://kevthetech143.github.io/ai-guide/ lists the questions; https://kevthetech143.github.io/ai-guide/best/ai-for-homework-help/ answers in one short paragraph plus a ranked list). Picker at https://kevthetech143.github.io/ai-guide/start/. I did not tap-test with real users (unverified). G2/AA unchanged.
- (b) 5: https://kevthetech143.github.io/ai-guide/about/how-we-review/ and https://kevthetech143.github.io/ai-guide/p/chatgpt.html read in short plain sentences. Competitor copy unchanged or still jargon-heavy.
- (c) down. The weekly promise is not being met. `data/providers.json` today: the newest `last_checked` is 2026-10-10 (8 days ago), so 0 of 237 cards were checked in the last 7 days; 153 are 14+ days old; 60 are 30+ days old (57 cards still read 2026-09-14, e.g. https://kevthetech143.github.io/ai-guide/p/chatgpt.html shows "Last checked 2026-09-14"). Yet https://kevthetech143.github.io/ai-guide/chat/ says "Prices and plans checked October 2026" and https://kevthetech143.github.io/ai-guide/about/how-we-review/ says "re-checked weekly". The stale flag is effectively dead: `build.py:88` hard-codes `BUILD_DATE = "2026-09-18"`, so overdue is measured against that date (the live /all/ page flags only 3 cards, gemini, playht and kimi, on 4 lines since Kimi appears in two categories; against today's date all 237 would show it). TAAFT now publishes a dated "Last updated: October 2026" page; AA is dated daily through 16 Oct. Dated cards are still ahead of Futurepedia/Toolify/PH, which show none.
- (d) 3→4 on four: all 237 cards carry a specific `watch_out` (verified in data; sampled e.g. Tabnine, Listnr, OpenCode: caps, who it is not for), against Futurepedia ("No tool listing includes any limitations") and TAAFT/PH with none. Caveat: 196 of 237 are price/plan caveats, and 0 carry a source link, so the honesty is still unverifiable. G2/AA stay 4 (they have user data and benchmarks behind theirs).
- (e) +0.17: 60 → 237 providers (sitemap: 237 `/p/` pages), still about 10x below Futurepedia's own 2,500, about 200x below TAAFT's 50,000+, and 16,294 products on Product Hunt's topic page. Only AA moves (703 models is a different unit, about 3x). Four-fold growth moved the score a fraction because the gap is orders of magnitude.
- (f) 2→3 vs TAAFT and PH: the trust page (https://kevthetech143.github.io/ai-guide/about/how-we-review/) states no ads, no affiliate links, no paid placement, and gives a real held-back-price example (Kimi/PlayHT/Gemini). TAAFT sells $49/$437 listings and sponsorships; PH labels "Promoted" and sells ads; so "unbought" is now a true, stated difference. No lift vs G2/AA (verified reviews, methodology). Still no named person ("maintained by one person"), no reviews, and the weekly claim is currently false (see c).
- (g) unchanged: our home page was 16.7 KB in 0.15 s, a question page 71 KB in 0.19 s (raw HTML via curl). PH topic page was 661 KB and AA home 1.48 MB. Baseline cells hold.
- (h) unchanged: see section 4 evidence below. Technical readiness improved; visibility is not shown.

## 3. Where we still lose

Is the gap smaller? Mixed. Smaller on breadth and honesty; larger in one place that matters for trust.

- **Freshness is now a trust problem, not just a gap.** We publish "re-checked weekly" and a "Last full review: 2026-10-10" stamp. The stamp is the NEWEST card date (`build.py:96-102`), not the oldest, so it overstates. Real state: 0 cards checked in 7 days, 60 cards older than 30 days. A visitor who trusts the stamp is misled. Competitors lose less here: AA is dated daily, TAAFT dates its page October 2026. This is the single worst item and it is our own doing.
- **Breadth.** 237 vs 2,500 (Futurepedia's claim), 50,000+ (TAAFT's claim), 16,294 (Product Hunt topic page). Gap shrank from about 40x to about 10x against Futurepedia only. We lose to every competitor on coverage and will keep doing so; the strategy is curated honesty, not count.
- **Evidence.** Our downsides are asserted. G2 shows user-review data, AA shows measured numbers. We have 237 `watch_out` lines and 0 source links. Plan task 018 is still open.
- **Feedback loop.** Only a GitHub Issues link on the trust page. No per-card report link; non-technical visitors rarely have GitHub accounts. Plan task 019 is still open.
- **Findability, unmeasured.** Sitemap has 371 URLs and every one has `lastmod 2026-09-18` (hard-coded, also stale). I cannot show we rank for anything. No Search Console, no analytics, so we cannot tell whether any of the 94 question pages gets a single visit.
- **Trust signals.** One unnamed maintainer, no reviews, no methodology beyond the one page. G2/AA/Futurepedia still lead.
- **Where we still win:** readability (5.0), the unbought policy now stated and true while TAAFT/PH/Toolify/Futurepedia disclose paid placement or compensation, and a guided path. These only matter if people arrive.

## 4. Findability evidence (h)

No rankings are claimed. Evidence only:
- robots.txt (https://kevthetech143.github.io/ai-guide/robots.txt): `Allow: /` and `Sitemap:` line present.
- sitemap.xml (https://kevthetech143.github.io/ai-guide/sitemap.xml): 371 URLs: 237 providers, 94 question pages, 28 `/start/`, 8 categories, `/all/`, 2 `/about/`, home. Defect: all 371 `lastmod` values are 2026-09-18.
- All 94 question pages, fetched live: 94/94 have a unique `<title>`, 94/94 a meta description (average 117 characters), 94/94 a canonical link, 94/94 FAQPage JSON-LD (checked with a script; example https://kevthetech143.github.io/ai-guide/best/ai-for-homework-help/ title "Best AI for homework help - AI Guide").
- `site:kevthetech143.github.io/ai-guide` through the WebSearch tool: returned the homepage only, with a cached copy showing "Last full review: 2026-09-26" (an older crawl). No subpages returned. A second query surfaced the homepage and the GitHub repo. This tool is not Google; Google index status is **unverified**.
- **Search Console is not yet submitted** (needs Kelvin's Google login). No analytics account either, per PLAN item 7. Until that is done we cannot measure whether question pages earn impressions.

## 5. Do more question pages still pay?

**No, not yet.** The 94 are technically sound (4 of 4 checks above) but we have zero evidence any of them is indexed or visited. Page 95 costs editorial time and adds nothing we can measure. Pause at 94. Resume once Search Console and analytics show which kinds of questions get impressions, then write more of those. (This reverses the baseline's "expand to ~200" advice; the reason is that the bottleneck moved from page count to measurement.)

## 6. Next 3 builds, ranked by visitor value / effort

Not in PLAN-be-the-best.md, added because it is a defect: the trust page's promise is currently untrue.

1. **Freshness repair (new, before 018/019).** (i) Run the weekly re-check that lapsed: 237 cards, 60 of them over 30 days, batched across workers. (ii) Fix `build.py`: `BUILD_DATE` from today's date, "Last full review" shows the OLDEST check (or "N of 237 checked in the last 7 days"), sitemap `lastmod` from real change dates. Effort: small code change plus one re-check pass. Value: highest, because every price on the site depends on it and the trust page stakes the site's credibility on it.
2. **PLAN 018: evidence link per `watch_out`.** Do it in the same pass as build 1: the worker is already on the provider's official pricing page, so it records that URL as the source. Adds a `source` field and a "Source" link under the warning. Effort: medium editorial (237 cards), little code. Value: closes the one dimension (d) where G2/AA still beat us with evidence.
3. **PLAN 019: "Report a wrong price" on each card.** Smallest version: a per-card link to a prefilled GitHub issue (card id in the title), no form or server. Effort: small, `build.py` only. Value: moderate, held down because the audience mostly lacks GitHub accounts; an email option would do more but exposes an address (Kelvin's call). Corrections list can wait for real reports.

Outside the three (needs Kelvin, not a build, and larger value than any of them): submit the sitemap to Search Console and create the analytics account.

## 7. Evidence notes

- Opened today: theresanaiforthat.com/about/ and /launch/; futurepedia.io; producthunt.com topic page; artificialanalysis.ai; research.g2.com article. Text claims for these come from WebFetch summaries (a small model); PH "16294" and AA "703" and "16 Oct" were re-confirmed by grep in raw HTML.
- Not reachable today (403 to curl and WebFetch): theresanaiforthat.com homepage, toolify.ai (and /about-us), g2.com/categories/ai and /ai-agents. Marked carried over.
- Traffic figures that appeared in search snippets (TAAFT "5M+ monthly visitors", newsletter sizes) were not on a page I opened and are excluded. Unverified.
- Our site data came from live URLs (curl) plus `/Users/admin/agents/ai-guide-brain/site/data/providers.json` and `build.py` (git HEAD 300b081). Live pages and local source could differ; the stale-flag finding rests on `build.py:88-110` plus the live /all/ page (3 cards flagged, exactly what HEAD data predicts, so live is consistent with HEAD; Fable review 018m).
- The 8 scores are my judgement anchored to the baseline's cells; no user testing was done.
- Progress log: `/tmp/ag018m/progress.log`.
