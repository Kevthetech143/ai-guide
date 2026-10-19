REVISE

Review of ai-guide-018n (uncommitted on b32603f), 2026-10-19. Read-only; nothing edited outside this file.

## Verified by re-running (AI_GUIDE_BUILD_DATE=2026-10-19, normal dist)
- Data check (data/providers.json, 237 cards): 150 checked < 30 days, 87 >= 30 days, oldest 2026-09-11, newest 2026-10-10, 0 future dates, 15 distinct dates. Worker's 150/87/237 are correct.
- `python3 build.py` exit 0. `test_freshness.py` Ran 4 OK. `test_question_filter.py` Ran 4 OK.
- deploy.sh link check: CHECK 371 pages, 13277 links, 0 broken, 237 providers, exit 0.
- `guidecheck.py` exit 0, "F-freshness WARN: 87 of 237 cards are past 30 days". Same result with no env (default = today).
- Sitemap: 371 entries, 15 distinct real lastmod dates, 0 entries dated 2026-10-19.
- Negative copy (/tmp/ag018n/neg, "re-checked weekly" put back): guidecheck exit 1, "F-freshness: weekly-check claim 're-checked weekly'".
- Future-date case (AI_GUIDE_BUILD_DATE=2026-10-01 on the real data): guidecheck EXIT 1, lists each card dated after the build date. Worker had not read this exit code; it is correct.
- 87 provider pages carry "Needs a new check"; matches the data.
- "weekly" in dist: 23 files, all provider product facts (e.g. "weekly rate limits", "weekly meal plans"); none is a check-cadence claim. Confirmed with the narrower pattern below: 0 hits in dist, 1 hit in the negative copy.

## Required fixes

1. data/how-we-review.md:8 and templates/about.html:5 — the new promise is false on ship day.
   "We re-check every listing at least once every 30 days." is a plain statement of fact, but today 87 of 237 listings are past 30 days. This is the same failure class the task exists to fix. Keep the 30-day promise (overseer decision), state it as the aim:
   - how-we-review.md:8 -> `We aim to re-check every listing at least once every 30 days.`
   - about.html:5 -> `Every listing shows the date it was last checked, and we aim to re-check each one at least every 30 days.`
   - build.py:605 meta description -> `How this plain-language AI guide is kept current: a 30-day re-check goal, no ads, no paid listings, and how to report a mistake.`

2. Category pages show two near-identical lines back to back (dist/chat/index.html, rendered text):
   "150 of 237 listings checked in the last 30 days. Oldest check: September 11, 2026. Oldest check here: September 11, 2026."
   A non-technical reader cannot tell the two "oldest" lines apart. Smallest fix, build.py:122 `oldest_check_line`:
   `return "Oldest check on this page: %s." % nice_date(min(p["last_checked"] for p in ps))`
   and keep the global stamp as is. (Question pages use the same function, so they get the same clearer wording.)

3. guidecheck.py:77-80 — the weekly rule is too broad. It FAILS on provider facts such as
   "Weekly rate limits apply; check your usage page." / "Check the weekly rate limit before you buy." / "Updated weekly with new meal plans." (all tested: MATCH). A future provider fact would break deploy. Replace lines 77-80 with:
   ```python
   _SUBJ = r"(?:we|listing|listings|site|card|cards|page|pages|price|prices|provider|providers)"
   fresh_re = re.compile(
       r"\b%s\b[^.]{0,40}?\b(?:re-?check\w*|review\w*|updat\w*|check\w*)\b[^.]{0,20}?\b(?:weekly|every week|each week|next week)\b"
       r"|\b(?:weekly|every week|each week)\s+(?:(?:re-?)?checks?|reviews?|cadence)\b" % _SUBJ, re.I)
   ```
   Tested: still catches "Every listing is re-checked weekly", "We check prices every week", "Prices are checked weekly", "weekly checks", "weekly cadence", "we ... will check again next week"; does not match the four provider-fact sentences above; 0 hits on the real dist; 1 hit on the negative copy.

## Nits (not blocking)
- build.py:87-88 duplicates the MONTHS list already defined at build.py:25. Delete the second copy.
- Footer "Site rebuilt October 19, 2026." is true but "rebuilt" is a builder's word. Plainer: `This page was made on October 19, 2026.` Optional.
- Design note: the stamp on category and question pages is the site-wide count, not the page's own. Acceptable for 1a; a per-page count would be the better next step.

## Wording score (non-technical reader): 7/10
Home stamp "150 of 237 listings checked in the last 30 days. Oldest check: September 11, 2026." is plain, honest, not alarming: good. Trust page is short and clear, but sentence 2 claims a cadence that is not met today (fix 1), and category pages print two "oldest" lines in a row (fix 2). With fixes 1 and 2 applied: 9/10.

## No regressions found
Unrelated pages (about, start, all, provider cards) render; link check 0 broken; question filter tests pass; provider data untouched (`git status` shows no change to data/providers.json).
