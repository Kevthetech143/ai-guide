# Freshness repair step 1a (task ai-guide-018n, 2026-10-19)

Promise is now "re-checked at least every 30 days, on a rolling basis". Code + wording only; data/providers.json untouched.

## Changes
- build.py: BUILD_DATE = today (local) or env AI_GUIDE_BUILD_DATE=YYYY-MM-DD; OVERDUE_DAYS = 30; UPDATED, freshness_line, LAST_FULL_REVIEW removed.
- Stamp (under h1 on home, category, start, all, question pages): "<N> of <total> listings checked in the last 30 days. Oldest check: <Month D, YYYY>."
- Sitemap lastmod: provider = its last_checked; category/question = newest last_checked of cards shown; all other pages = newest overall.
- Overclaims found in built dist/ and fixed:
  1. how-we-review.md "re-checked weekly" + "cadence began September 14" -> 30-day promise (also "check again next week" -> "check again"; intro "We keep" -> "We try to keep").
  2. build.py meta description of how-we-review: "weekly checks" -> "checks at least every 30 days".
  3. Category pages: "Prices and plans checked October 2026" (was today's month) -> "Oldest check here: <date>" from the cards on the page.
  4. Question pages: "Last checked <today>" -> "Oldest check here: <date>".
  5. Footer on every page: "Updated <today>" -> "Site rebuilt <build date>" (base.html).
  6. about.html: "Every page is stamped with the date it was last checked" -> "Every listing shows the date it was last checked, and we re-check each one at least every 30 days."
- Left alone on purpose: "weekly" still appears in 23 built files, all as product facts (provider watch_out "weekly rate limits"; one question meta "weekly meal plans"). Not about checking; provider facts are out of scope. So `grep -ril weekly dist` is 23, not 0.
- guidecheck.py F-freshness: FAIL if built text/meta says weekly/every week/each week/next week near check/review/update words, or any last_checked > BUILD_DATE; WARN with count of cards past 30 days.
- test_freshness.py: overdue at 30 not 29, stamp count/oldest, sitemap lastmod.

## Re-run
    cd /Users/admin/agents/ai-guide-brain/site
    python3 build.py && python3 guidecheck.py && python3 test_freshness.py
    AI_GUIDE_BUILD_DATE=2026-10-30 python3 build.py   # reproducible build

Backups: *.bak-20261019-018n (build.py, guidecheck.py, data/how-we-review.md, templates/base.html, templates/about.html).
