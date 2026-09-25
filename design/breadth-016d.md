# ai-guide-016d — breadth batch 4 notes (data only)

Attempt 2. Verified 11 of up to 30. Every fact below was read from the provider's
own site with a real browser User-Agent, following redirects, with HTML comments
stripped before reading. No promo or limited-time prices were used. Nothing was
claimed as tested.

## Verified (11)

| id | categories | price_from (plan-paired) |
|---|---|---|
| beatoven | music | Free (5 generations); Creator Plan from $6/month (15 min download/month) — from JSON-LD offers on beatoven.ai |
| vocal-remover | music | Free — vocalremover.org states "use it absolutely free", no paid tier on the page |
| mojeek | search | Free web search (search API paid from £2 per 1,000 queries, Startup plan) |
| marginalia-search | search | Free — AGPL open source, no paid/donate/premium mention anywhere on the page |
| tavily | search | Free (Researcher plan); paid from $0.008/credit (Pay As You Go) or $30/month (Project) |
| supermaven | code | Free (Free Tier); Pro from $10/month — plan table on supermaven.com |
| goose | agents, code | Free — Apache 2.0 open source, Agentic AI Foundation |
| continue | code | Free open source (see unclear-pricing note) |
| qodo | code, agents | $30/month (Pro Team; extra credit packs $0.012/credit) — "Monthly billing, no commitment" |
| pieces | code | $18.99 per user/month (Pro, billed monthly; 25% off yearly) — FAQ: "Is Pieces free to use? No." |
| replicate | image, video | Pay as you go per model — e.g. $0.04 per output image (flux-dev) |

## Dropped candidates (8), each with reason

- riffusion — www.riffusion.com now redirects to www.flowmusic.app, which is the
  existing `flow-music` card. Dropped as duplicate (rule 2: stored URL would
  collide with an existing provider).
- stableaudio — stableaudio.com/pricing is a JS-only React payload; no price
  figures in static HTML. Dropped per rule 4.
- mureka — $8/mo and $24/mo figures appear only in article prose on the
  homepage ("Mureka AI: Subscription Plans and Features"); /pricing 404s and no
  plan table exists in static HTML. Dropped per rule 4.
- cody — sourcegraph.com/cody redirects to /docs/cody; /cody/pricing 404s and
  sourcegraph.com/pricing lists no Cody plans. Price unverifiable in static
  HTML. Dropped per rule 4.
- phind — 403 with a real browser User-Agent, then connection failed outright
  on retry. Could not verify the site is servable. Dropped per rules 1/3.
- brave search — search.brave.com returned 429 (rate limited) on two attempts
  minutes apart. Could not verify. Dropped.
- topmediai — pricing page (960 KB static HTML) has zero price figures; plans
  render via JS. Dropped per rule 4.
- invoke — www.invoke.com now resolves to a domain-parking page
  (domaineasy.com); invoke.ai serves documentation only, no commercial pricing
  on that domain. Dropped.

## Unclear pricing pages (kept, but flagged for the lead's re-check)

- continue.dev — the page is now a transition page titled "Continue (acquired
  by Cursor)". The open-source codebase is stated as freely available; an FAQ
  asks "What about my subscription?" but the answers are JS-hidden, so the
  paid Hub subscription price/status could not be verified in static HTML.
  price_from says so explicitly.
- replicate.com — the pricing page is fully usage-based per model/GPU; the
  "Try for free" CTA has no free-tier terms on the pricing page, so free_tier
  is false. Lead may want to confirm whether new accounts get credits.
- qodo.ai — "Pro Team $30" has no billing period printed next to it in static
  HTML; "Monthly billing • no commitment" and monthly credit-pool copy on the
  same page support $30/month. Not stated as per-user anywhere on the page.
- beatoven.ai — plan prices ($0/$6/$10/$20/$3) come from JSON-LD Offer blocks
  on the homepage, not a visible plan table (the /pricing page 404s); the
  descriptions pair each price with its plan name and minutes.

## Redirects noticed (rule 2)

- block.github.io/goose → https://goose-docs.ai (goose has moved; stored the
  final URL).
- www.invoke.com → domaineasy.com parking (dropped, see above).
- www.riffusion.com → www.flowmusic.app (dropped as duplicate, see above).
