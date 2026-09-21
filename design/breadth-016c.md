# ai-guide-016c — breadth notes (batch 3, data only)

**Verified and shipped: 12 of 30.** All prices read from the provider's own plan
table with a real Chrome User-Agent on 2026-09-21; links are the final URLs the
requests actually ended on. Fewer than 30 surviving is a PASS when the drops
are named — padding a 30 is a FAIL.

## What verified (12)

| id | category | price_from |
|---|---|---|
| soundraw | music | $16.99/month ($11.04/month billed annually) |
| lalal-ai | music | $7.50/month (billed annually) |
| flow-music | music | $6/month |
| musicfy | music | $8/month (billed annually) |
| musicgen | music | Free |
| exa | search | $7 per 1,000 searches (API) |
| tabby | code | $19/month per seat (Team; Community free) |
| gpt4all | chat | Free |
| jan | chat | Free |
| anythingllm | chat, agents | Free |
| comfyui | image | Free |
| diffusionbee | image | Free |

Coverage hits the thinnest categories: music (5), search (1), and run-on-your-own-computer open-weights tools (7).

## Dropped candidates with reasons (14)

- **beatoven-ai** — homepage live (200), but /pricing is a 404 and the plan
  table is JavaScript-rendered. Price unverifiable (rule 4).
- **boomy** — homepage and /pricing require JavaScript ("doesn't work properly
  without JavaScript enabled"). Price unverifiable (rule 4).
- **loudly** — /pricing is a 404; the real pricing page (/music/pricing) is a
  JS app whose static HTML carries no figures. Price unverifiable (rule 4).
- **moises-ai** — pricing is hidden behind login ("Log in to see our full
  pricing and features table"). Unverifiable without an account.
- **komo-ai** — pricing page is a JS app; only the Free $0 tier is visible in
  static text, paid amounts are not. Price unverifiable (rule 4).
- **consensus** — pricing page is a JS app ("Pricing Monthly Annual"
  headings but no figures). Price unverifiable (rule 4).
- **brave-search** — account.brave.com/plans/ is a JS app; no figures in
  static text. Price unverifiable (rule 4).
- **phind** — HTTP 403 even with a real Chrome User-Agent (curl TLS-fingerprint
  block, not a 403-from-meta-description case). Cannot verify (rule 1 tried).
- **andi (andisearch.com)** — JS app; essentially no static content.
  Unverifiable.
- **marginalia.nu** — live site, but it is a link directory with no AI
  product and no pricing structure. Not a fit for the guide.
- **mureka.ai** — homepage live but carries no price figures or pricing link
  in static text; pricing page 404. Price unverifiable (rule 4).
- **stableaudio.com** — homepage and /pricing are JS-rendered; no figures in
  static text. Price unverifiable (rule 4).
- **continue.dev** — live page announces Continue was acquired by Cursor; the
  product now exists only as an open-source codebase. Cursor is already in
  the guide, so no card added.
- **udio.com** — already in data/providers.json as `udio`; not re-added
  (id collision).

## Unclear pricing pages

- **Soundraw**: two prices are shown side by side ($16.99/mo monthly,
  $11.04/mo annual). The card says so plainly per the rules.
- **LALAL.AI**: Lite is shown as "$7.5 /mo $90 billed annually" — rendered
  as "$7.50/month (billed annually)".
- **Flow Music (flowmusic.app)**: riffusion.com now redirects here and the
  site brands itself "Google Flow Music" (Lyria 3.5); no "Riffusion" text
  remains on the page, so the card uses the current branding and makes no
  claim about the site's history or ownership beyond what the page shows.
- **Tabby**: Team is "$19/mo per seat" with no seat minimum stated, so one
  person can genuinely buy one seat — no hidden-minimum adjustment needed
  (rule 7 checked).

## Method notes

- Mac Python's SSL verification is broken ("unable to get local issue"), so
  all fetches used `curl -L` with a real Chrome User-Agent (macOS keychain
  CAs), which follows redirects and reports the final URL.
- HTML comments were stripped before reading text (rule 5); prices were read
  only from visible plan tables, never from meta descriptions (rule 4);
  watch_out limits were paired with the plan actually priced (rule 6).

## Lead review + REVISE applied (2026-09-21, before merge)
Muse shipped 12 and dropped 14 — the strictest batch yet, and the right direction: the eight
rules did their job upstream. An independent Opus 5 reviewer then fetched all 12 with a Chrome
UA. **Links were perfect this time: all 12 returned HTTP 200 and all 12 stored URLs matched the
final post-redirect URL** — the first batch with zero link defects. **12 landed, 11 merged.**

CUT (1):
- **musicfy** — the $8/month was a "SUMMER SALE 60% OFF, limited time only" price against a
  $190/year list. A sale price on a public guide is a wrong price waiting to happen.

FIXED in place (5):
- **flow-music** "$6/month" → **"$6/month (billed annually)"**. The pricing page ships with the
  Yearly toggle already on (`data-state="on"`) and three "Save 25%" badges, so $6 was the annual
  rate presented as a flat monthly price. Lead re-verified the badges independently.
- **soundraw** — watch_out said WAV and stems "need one of the Artist plans". Artist **Starter**
  is MP3-only too; only **Artist Pro** unlocks WAV and stems. Corrected.
- **comfyui** "Free" → **"Free to run yourself (cloud from $16/month billed annually)"**. Lead
  verified comfy.org/pricing carries a real paid table ($16/$192, Comfy Cloud confirmed).
- **anythingllm** "Free" → **"Free to run yourself (team cloud from $50/month)"**. Lead verified
  /pricing redirects to /cloud with $50 and $99 tiers.
- **exa** — added the free start to watch_out: $20 credits at sign-up plus $10 monthly, no card
  required. The card read pricier than reality.

CONFIRMED HONEST (reviewer checked each, no change needed): musicgen (MIT code / CC-BY-NC-4.0
weights, non-commercial, and the card already says so), jan (no pricing page at all, /pricing
404s), gpt4all (nomic.ai sells a *different* product; the GPT4All page is download-only),
diffusionbee (no paid tier), lalal-ai (every number and plan attribution correct),
tabby ($19/seat Team, free Community, no seat minimum).

## OPEN STRUCTURAL ISSUE — do NOT patch ad hoc, needs one deliberate pass
`open_weights` has no written definition and the EXISTING data is already inconsistent:
ollama=true and lm-studio=true (they are apps that load other people's weights), but
aider=false (also an open-source app). This batch's true values on gpt4all/jan/anythingllm/
comfyui/diffusionbee follow the ollama precedent, so they were left ALONE for consistency
rather than flipped in isolation.
NEXT TASK should: (1) write one definition — proposal: `open_weights` means THIS product's own
model weights are openly published, which makes every runner/app false; (2) normalise all 115
cards in a single pass; (3) if runners matter to readers, add a separate honest flag for
"works with open models" instead of overloading this one.
