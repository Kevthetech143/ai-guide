# breadth-016m notes (worker: Sonnet 5.5; SEARCH-only batch; Haiku-tier fetch work done locally)

Date: 2026-10-10. Shipped: 5 verified cards in data/providers-016m.json (fewer than 18, no padding). Nothing was tested by us; every fact was read from the provider's own pages with a browser User-Agent and Playwright (toggles clicked where one existed). Legal entity was checked before prices, per rule 27.

## Shipped (5) and what was read
- anara: anara.com/pricing, Monthly clicked: Free $0, Plus $10, Pro $20, Max $100 (Yearly view shows Plus $8, Pro $16, Max $80). Entity "Anara Labs, Inc." from the Terms of Service intro and footer. Deep Search is listed only under Max. No seat minimum text on the page ("per seat", self-serve buttons). Home page says "Search the literature ... Cited answers".
- brave-search: search.brave.com / brave.com/search. Free. Paid option found: Search Premium at account.brave.com checkout (Monthly $3.00, Annual $2.50/mo = $29.99/yr), "available exclusively in the Brave browser" (help/premium). Entity "Brave Software, Inc." from brave.com/terms-of-use. Brave Search API (paid, developer) exists on the site but is not an app for beginners and is not priced on the card. Terms page is dated May 2023. Ask Brave page (search.brave.com/ask) loads.
- ecosia: ecosia.org/pricing: Free $0, Starter $7.99/month, Pro $14.99/month (AI Chat plans; no Monthly/Yearly toggle on the page). Entity "Ecosia GmbH" from the Privacy Policy and Imprint (the Terms of Service text does not name it). Search results page itself returned HTTP 403 to headless Chromium, but the AI Chat tab and results page chrome were visible.
- qwant: free; about.qwant.com says AI is "free and unlimited as soon as you create a Qwant account"; help.qwant.com explains Flash Answer is an AI answer, experimental. Entity "QWANT" (Société par actions simplifiée) from the legal notices page; the card uses the name exactly as printed there. UNCLEAR: the live search page returned "Qwant is temporarily unavailable (HTTP 403)" to headless Chromium twice, so we could not see a live AI answer; home page and help pages loaded fine. The about page still says "Many more features will arrive throughout 2025" (stale wording). Lead should open a real search in a normal browser before accepting.
- reddit-ai-search: reddit.com/answers and the Reddit Help article "Reddit's AI search". The help page says logged-out 10 questions a week, logged-in 50 a day, Premium 100 a day. Reddit Premium page: $5.99/Month, $49.99/Year. Entity "Reddit, Inc." from the User Agreement. UNCLEAR: no plan table says the word "Free"; free_tier=true rests on the help page limits for logged-out and logged-in users. Reddit's own pages call it "AI search"; the product name "Reddit Answers" appears only in the URL, so the card uses "Reddit AI search". The browser URL ends on /answers/ plus a transient js_challenge query string; the card stores the clean /answers/ URL.

## Dropped candidates and reasons
- Felo: prices carry "was $20.99 / $14.99" strike-through promo wording, list price unclear (rule 10); terms URL guess 404.
- Genspark: /pricing redirects to a login page; no price visible.
- Phind: failed in earlier batches and not retried successfully (404/403 history). OpenEvidence: HTTP 403. SciSpace: bot challenge page (HTTP 202 "confirm you are human"). Presearch: Cloudflare DNS error 1016. Stack Overflow AI Assist: HTTP 403 security check.
- MediSearch: medical AI search, but Terms and Privacy name no company (rule 18). EvidenceHunt: Pro is 20 EUR/month when the toggle is set to Monthly (16.5 billed yearly), free Basic plan exists, but Terms/Privacy name no legal entity.
- Humata: document Q&A, Free + Expert $9.99; Terms/Privacy name no legal entity ("Humata" only), and it is a PDF chat tool rather than search.
- Sourcely: Ultra $19 (yearly view) / Max $39, no free plan in the table, terms name no legal entity.
- SurfSense: site links to /sunset ("SurfSense is moving to a local app"); a product change that reads as a sunset of the earlier product (rule 11); terms name no legal entity.
- Khoj / Open Paper (Khoj Inc.): Khoj Cloud was reported sunset in batch 016l; Open Paper is a paper reader and workbench, not a search product (rule 27); login-gated home page.
- Dropbox Dash: team product ($15/user/month billed yearly or $19 monthly, Dash for Business $35), "Get 50% off" banner, no free plan, not for a beginner.
- Litmaps, Connected Papers: literature-mapping tools; their own pages do not claim AI (rule 12).
- Logically (afforai.com redirects there): writing and reference tool, not search.
- ThinkAny: pricing page lists gpt-4-turbo, claude-3-opus and llama3-70b (looks stale) and its terms page returns HTTP 500.
- Yahoo Scout: help.yahoo.com calls it "an AI-powered search discovery engine ... available in beta to all users" and Yahoo Inc. is the entity (terms), but no page states a price or says it is free; left out rather than guessed. Could be revisited.
- Ask.com: homepage says the search business is discontinued (rule 11). Silatus: site not found. Gigabrain: now sells trading agents.
- Farfalle, MindSearch, Open Notebook, Kotaemon: open-source search/notebook projects that need Docker or developer setup; Farfalle's README still lists llama3/gpt-4o-era models. Not carried through (not beginner apps).
- Startpage, Swisscows: search engines with no AI answer feature found on their pages. Wolfram Alpha, Iris.ai, Scholarcy, Opera AI, DeepWiki, Skywork, Flowith: skimmed, not search-first or not beginner products.

## Unclear pricing pages
- Qwant (live search blocked to headless, see above), Reddit AI search (no "Free" plan label), Ecosia (no Monthly/Yearly toggle; prices shown as "/ month"), Yahoo Scout (no price statement), Felo (promo vs list), EvidenceHunt (toggle needed a real click on the switch; Monthly = 20 EUR).
