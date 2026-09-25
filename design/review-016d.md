# Review 016d — breadth batch 4 (11 cards)

Reviewer: independent Opus 5.5, 2026-09-25. Every card fetched live with a Chrome
User-Agent, redirects followed, `<!-- -->` stripped. JS-rendered plan tables were
read in a real Chromium (Playwright) and, where prices are animated, screenshotted.
Data file NOT edited.

## Overall verdict: REVISE

4 CUT, 6 FIX, 1 KEEP. Merge the 7 survivors only after the FIX text below is applied.

Links: 10/11 returned 200 and matched the final URL. tavily.com redirects to
www.tavily.com (FIX). vocalremover.org returns 403 to curl (Cloudflare challenge,
`cf-mitigated: challenge`) but 200 in a real browser, so the lead's link check must
use a browser for it.

## Per card

### beatoven — CUT
The site can no longer be used or bought from.
- https://www.beatoven.ai/pricing (the site's own footer "Pricing" link): HTTP 404
  in curl AND in a real browser: "Page Not Found".
- https://www.beatoven.ai/blog/: HTTP 404.
- The homepage has no sign-up or create button. The API page's dashboard link
  https://sync.beatoven.ai/apiDashboard, and studio.beatoven.ai, fail with
  "Could not resolve host".
- The $0/$6/$10/$20/$3 prices exist only in JSON-LD structured data. That is machine
  metadata like a meta tag, not a visible plan table (rule 4).

### vocal-remover — FIX (fits the guide: the page says "Separate voice from music ... with powerful AI algorithms")
"Free" hides a paid membership (rule 9).
- https://vocalremover.org (browser): "New version with better algorithms — currently
  available for subscribers only."
- https://vocalremover.org/next/pricing (browser): "Get a membership ... Free 10 minutes
  8 minutes 100Mb — Month US$12.95 Buy 300 minutes 25 minutes 2Gb Yes Year US$99 Buy
  500 minutes" (columns: Total Audio Duration Per Day / File Duration / File Size / Priority).
- price_from: `Free (up to 10 minutes of audio a day); membership US$12.95/month or US$99/year`
- watch_out: `The newer, better version is for paying members; free use is capped at 10 minutes of audio a day and 8-minute files`

### mojeek — CUT (not an AI product; same reason wave-video and riverside-fm were cut in 016b)
- https://www.mojeek.com: "Mojeek is a growing independent search engine which does not
  track you." No AI feature anywhere on the home page, and the card describes none.
- The only AI link is the developer API (https://www.mojeek.com/services/search/web-search-api/:
  "Startup £2 * CPM"). That price is correct, but an API is not what the card sells.

### marginalia-search — CUT (the site says it is not AI)
- https://marginalia-search.com: "Open Source Custom index and crawler software Simple
  technology, no AI AGPL license".
- open_weights: true is also wrong. It has no model weights, only AGPL source code.

### tavily — FIX (link only; price verified)
- https://tavily.com → final https://www.tavily.com/ (and /pricing → www.tavily.com/pricing).
- Pricing screenshot (www.tavily.com/pricing, rendered): "Researcher Free / month ...
  1,000 API credits / month", "Pay As You Go $0.008 / credit", "Project $30 / month ...
  4,000 API credits / month". The $30 is an animated digit roller that is unreadable in
  the static HTML. The worker's figure is right.
- link: `https://www.tavily.com/`

### supermaven — CUT (sunset by its owner)
- https://supermaven.com/blog/sunsetting-supermaven (200): "Sunsetting Supermaven Nov 21,
  2025 ... Existing users will be fully refunded today ... We're sunsetting Supermaven
  after our acquisition one year ago ... we now recommend any existing VS Code users to
  migrate to Cursor ... We will no longer support agent conversations".
- The homepage still shows a stale "Pro $10 /month" table, but no one new can buy it.

### goose — FIX (price "Free" verified: Apache 2.0, nothing sold)
- https://goose-docs.ai (200, final URL matches): "goose is a general-purpose AI agent that
  runs on your machine. Not just for code — use it for research, writing, automation..."
  and "Use API keys or your existing Claude, ChatGPT, or Gemini subscriptions".
- The card's "automating dev work" understates it. The site-move sentence in watch_out
  means nothing to readers (and https://block.github.io/goose/ still returns 200).
- good_for: `A free, open-source AI assistant on your own computer (desktop app or command line) that does tasks for you - coding, research, writing and automation`
- watch_out: `You connect your own AI model (an API key or an existing Claude, ChatGPT or Gemini subscription), and that model's costs are separate`

### continue — CUT (product wound down)
- https://continue.dev (200, title "Continue (acquired by Cursor)"): "Continue has joined
  Cursor ... our open-source codebase remains freely available as a foundation for others."
- FAQ, opened in a browser: "What happened to my data? All user data has been deleted in
  accordance with the privacy notice". The Hub is gone, so there is nothing current to
  recommend. The "unclear Hub price" is moot.

### qodo — FIX (wrong allowance on the priced plan, rule 6)
- https://www.qodo.ai/pricing/ (browser, clicking each option): "~18 Reviews/Mo 2,500
  credits" → "Pro Team $30"; "~36 Reviews/Mo 5,000 credits" → "$60"; "~144" → "$240".
  Also "Monthly billing • no commitment", "Free 14 Day Trial NO CREDIT CARD", and in the
  nav "Open Source Free for open source projects".
- The card says ~36 reviews a month for $30. That is the $60 tier.
- watch_out: `$30/month buys 2,500 credits (about 18 reviews a month); about 36 reviews costs $60/month. 14-day free trial; free only for open-source projects`

### pieces — FIX (price verified; category and description are off)
- https://pieces.app/pricing: "$18.99 per user / month · billed monthly", "Is Pieces free
  to use? No.", "Starting the 7-day Pro trial takes a card on file."
- https://pieces.app: "The memory layer for everything you do ... Research, chats,
  emails, notes, meetings and more" and "Pieces forms memories every 2 seconds from the
  apps you already use. Captured by default What you see From the currently focused
  application". It is no longer a coding tool.
- categories: `["chat"]`
- good_for: `An app that quietly remembers what you work on across your computer so you can ask AI about it later - recaps, meeting prep, finding past work`
- watch_out: `No free plan (the 7-day trial needs a card); it captures what is on your screen every 2 seconds by default, so check its privacy settings`

### replicate — FIX (wrong price for the named model). Keep it at "hard": the guide already carries comfyui, aider and gemma at hard, and Replicate has a browser Playground
- https://replicate.com/pricing: "black-forest-labs/flux-1.1-pro ... $0.04 / output image",
  "black-forest-labs/flux-dev ... $0.025 / output image". The card pairs $0.04 with
  flux-dev. The page banner "Wan 3.0 is 30% off this week" is a promo and must not be used.
- https://replicate.com: "Run AI with an API ... All with one line of code", "Compare
  models in the Playground", "Generate images Generate speech Generate music ...".
- price_from: `Pay as you go per model - e.g. $0.025 per image (flux-dev), $0.04 per image (flux-1.1-pro)`
- good_for: `Trying thousands of AI models (images, video, speech, music, chat) from one account, in a browser playground or through code`
- watch_out: `Built for developers and billed per use - every run costs money, with no flat monthly plan`
