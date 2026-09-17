# trust-014 — wiring the locked trust page into the site

Task ai-guide-014b: wire the already-written trust text
(data/how-we-review.md, lead-corrected, do-not-rewrite) into the site build.

## What was wired

1. **New page `about/how-we-review/`** (dist/about/how-we-review/index.html),
   generated in build.py via `page()` + `write()` like every other page —
   no hand-written HTML in dist/.
   - Source: data/how-we-review.md, read at build time and converted by a
     tiny stdlib `md_trust()` (added to build.py): `# ` -> `<h1>`,
     `## ` -> `<h2>`, blank-line separated paragraphs (wrapped source lines
     joined with a space), and the GitHub issues URL ->
     `<a href="https://github.com/Kevthetech143/ai-guide/issues">`.
     All other text goes through the existing `esc()`.
   - title: "How we review - AI Guide"
   - meta: "How this plain-language AI guide is kept current: weekly
     checks, no ads, no paid listings, and how to report a mistake."
   - canonical: BASE_URL + "about/how-we-review/"
   - The existing `/about/` "How this guide works" page is untouched —
     this is a sibling, not a replacement.

2. **Footer, every page**: the `about_link` logic in `page()` now emits
   both links: "How this guide works" `&middot;` "How we review".
   - New param `is_review_page`: on the new page the "How we review"
     footer text is omitted entirely (no self-link), mirroring the
     round-2 cut that keeps "How this guide works" unlinked on /about/.
   - The new page's footer still links "How this guide works"
     (../../about/index.html) — it is a sibling, not itself.
   - templates/base.html was NOT edited: the footer already carries
     `$about_link`, so the whole change lives in one code path instead
     of a new template variable.

3. **Home**: one plain-English line right after the hero section in
   templates/home.html:
   "Nobody pays to be listed. Read how we review."
   (href="about/how-we-review/", relative from dist/index.html).

4. **Sitemap**: canonical appended to `start_urls`, so dist/sitemap.xml
   includes `about/how-we-review/` with a `<lastmod>`. BUILD_DATE set to
   2026-09-17. `UPDATED` (footer "Updated ..." stamp) left as
   `date.today()` — it already reads the real build day.

## Relative-path choices

- Page is two levels down (dist/about/how-we-review/index.html), so
  `style_prefix="../.."` and `home_href="../../index.html"` — one level
  deeper than /about/ (which uses `".."` / `"../index.html"`).
- Footer review link is computed as
  `home_href.replace("index.html", "about/how-we-review/index.html")`,
  the same pattern as `about_href`/`start_href`, so it stays correct no
  matter which page's footer renders it (e.g. ../../about/how-we-review/
  index.html on the new page itself — unused there, but computed anyway).
- Home link is "about/how-we-review/" (trailing slash); linkcheck.py
  resolves directories to index.html, so it validates cleanly.

## Left out because it was not true

- No JSON-LD at all on the new page: no ratings, no reviews, no author
  were invented. page() got no `json_ld` argument.
- No "review score" / "rating" / "we tested" / "our team" claims anywhere
  on the page — the source text only says what is actually done
  (weekly checks, no ads, no affiliate links, no paid placement) and
  what happens when a price cannot be confirmed.
- No names: "Devin", "Kelvin", and "Muse" appear on no page; the footer
  and body only say what the site does.
- The new page does not link "How we review" to itself in the footer —
  not even as plain text — because the acceptance reads "appears on all
  HTML pages except the new page", and omitting it is the strictest
  reading of that rule.
