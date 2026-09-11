# ROUND 3 (FINAL) — adversarial user + edge cases + would the best practitioner sign it (2026-09-11)
Reviewer: brutal design critic (senior product designer, consumer, phone-first).
Method: read static/style.css and built dist/ on the Mac; every claim checked against built HTML. No browser rendering. Round 1 scored 5/10, round 2 scored 6/10.

## SCORE: 7/10
Why 7 and not 8: the round-2 lies are gone — one name on all five surfaces ("Task helpers" in title, h1, home tile, and "Good for" rows, verified in devin.html), /all/ is a real 60-card page so 109 crumbs and both escape hatches resolve, the legend and freshness line are on every list page, the quiz metadata is fixed, the footer self-link on /about/ is now plain text, and the home crumbwrap is gone. That is competent, honest work. But the round-2 price fix was only half-applied: the placeholder "Check site" still sits bare in 20 card facts rows and 3 detail pages, and the legend header promises "Badges, in plain words" while defining only 2 of 5 badge types. 7 = competent junior who shipped the truth and missed a template branch; 8 needs zero placeholders and zero over-promised microcopy.

## TOP 5 FAILURES

**1. "Check site" is still bare English in 20 card facts + 3 detail pages (round-2 failure #2, half-fixed).**
`dist/p/veo.html:32`: `<li><span class="k">Price</span><span>Check site</span></li>` — and the same card sits at `dist/all/index.html:253` as `<div><span class="k">Price:</span> Check site</div>`. The free-tier-unknown branch was fixed (microsoft-copilot); the paid-only-unknown branch was not. Fix — detail page: `<li><span class="k">Price</span><span>No monthly price &mdash; check the provider's site; you pay per use</span></li>`; card: `<div><span class="k">Price:</span> No monthly price &mdash; check the provider's site</div>`. Veo's own watch line ("you pay per second of video") already says this — the fact row contradicts the card's own copy.

**2. The legend header over-promises.** Every list page: `<p class="legend">Badges, in plain words:` defines only Open source / Company-made. Cards also wear Free, Paid, Easy/Medium/Hard, and "Runs on your computer" — undefined. Fix: append ` <strong>Runs on your computer</strong> &mdash; it runs on your own device, nothing sent to the cloud.` and ` <strong>Easy / Medium / Hard</strong> &mdash; how tricky it is to set up and use.` — or cut the heading to "Some words, explained:".

**3. "Task helpers" hint has a subject-verb error.** Home tile and /start/ picker: `<span class="tile-hint">does multi-step jobs alone</span>`. Helpers *do*. Fix: `do multi-step jobs for you` — warmer than "alone", which reads lonely, not capable.

**4. /start/ step 1 heading mislabels two categories.** `<h2>1. What do you want to make?</h2>` — Chat and Search are not "making". Fix: `<h2>1. What do you want to do?</h2>`, matching the subtitle's own verb. Same page: the picker reads "Chat AIs … Search AIs, Task helpers" — round 2's broken-parallel-rhythm warning stands; and "Paid ones / needs a subscription" has the same verb slip ("ones needs" &rarr; "need").

**5. /all/ is a 60-card, 54KB page with zero in-page navigation.** No category anchors, no jump list, no back-to-top; cards are alphabetized, not grouped, so she cannot even skip to "Video". Fix: group cards under `<h2 id="video">Video</h2>`-style headings, add a compact jump list under the subtitle (`<nav aria-label="Jump to a category">`), plus a "Back to top" link after the last card.

## ADVERSARIAL WALKTHROUGH (68, 390px phone, taps everything)
- She picks "No preference — show everything", lands on /all/ — which now exists — then scrolls a 60-card wall with no way to jump or find her place; no way back up without the full scroll. She abandons.
- On Veo she reads "Price: Check site" beside a "Paid" badge, taps "Visit the official site" expecting a price, and lands on deepmind.google — a research-lab homepage, not pricing. The site outsourced the answer and called it a fact row.
- On /start/ she taps "Paid ones" ("needs a subscription" — ones *need*) and reaches a list where several cards still say "Price: Check site". She has been told to check the site twice in one journey. Trust erodes per tap.

## MISSING
- **In-page navigation on /all/.** 60 cards, no anchors; a category jump list plus back-to-top turns the wall into a list. (Fix in failure #5.)
- **Unknown-price template branch, both shapes.** Free-tier-unknown is fixed; paid-only-unknown still emits bare "Check site" on cards and detail pages. One branch in build.py, two replacement strings. (Fix in failure #1.)
- **Complete badge definitions or an honest legend heading.** Define all five badge types, or cut "Badges, in plain words:" to "Some words, explained:". (Fix in failure #2.)

## CUT LIST
- Unused `.count` rule in static/style.css — dead CSS, no markup references it.
- The `<p>` wrappers around standalone biglinks on start/chat/ (and siblings) — a paragraph containing a single block link adds nothing; the biglink already carries margin.
- The "Good for" fact value that is just a category name (`<li><span class="k">Good for</span><span>Video</span></li>` on veo.html) — the card lede already says what it is good for; a bare category adds a filler row.

## ONE-LINE VERDICT
The site stopped lying about where links go and what things are called; it still outsources the one fact this audience cares about most — price — to a two-word shrug, and it built a 60-card page with no way to navigate it.

FINAL SCORE: 7/10
