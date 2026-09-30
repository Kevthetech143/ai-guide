# Review — breadth batch 7 (016g)

Reviewer: independent reviewer agent, 2026-09-30 (ET).
Method: I fetched every stored URL with curl, a Chrome User-Agent and `-L` (status and final URL). Every home, pricing, terms,
privacy and about page was rendered in headless Chromium (Python Playwright) and its visible text read. I did not rely on meta
tags. I clicked the Monthly/Annual toggles where they exist (Ecrett, Komo), expanded FAQ answers from the static HTML
(OpenHands), and tested sign-up screens (Ecrett, Onyx, Komo). I read Onyx's GitHub README and API data. I scanned every site
for sunset, shut-down, acquired or waitlist wording.
Nothing was edited except this file. data/providers-016g.json and data/providers.json are untouched.

## Verdict: REVISE

0 keep, 6 fix, 1 cut. After fixes and the cut, 6 cards ship.

## Links
All 7 stored URLs returned HTTP 200, and each final URL equals the stored URL. None redirected.
- brain.fm/pricing, onyx.app/pricing, cline.bot/pricing, openhands.dev/pricing and komo.ai/pricing are 200.
- ecrettmusic.com/pricing and fadr.com/pricing are 404, but both plan tables are on the home page (the stored link), so this is fine.

## Major defects the worker notes missed
- **Brain.fm is not an AI product by its own page (rule 12).** brain.fm/science says: "Music made purely by AI is often cold and
  boring … Brain.fm gives you the best of both worlds by adding a layer of science to human-composed music." The home, pricing,
  about and science pages never call it AI. The card's "AI-generated functional music" contradicts the vendor.
- **Four wrong company names (rule 15), all shown on the vendor's own terms or privacy page:** Ecrett (SOUNDRAW Inc.),
  Fadr (Pebble LLC), Onyx (DanswerAI, Inc.) and OpenHands (All Hands AI). The worker wrote "no separate legal company name
  shown" for Fadr and Komo. That claim is false for Fadr, whose terms name Pebble LLC.
- **Komo's paid prices are not JS-only-unverifiable.** A headless render shows them. With Monthly clicked, Komo Pro is $20/month
  and Komo Max is $200/month; Annual is $17 and $170. The price can now be stated.
- **Wrong "no free tier" / "paid cloud" claims.** Onyx has a free MIT-licensed Community Edition you run yourself, so
  `free_tier` is wrong. OpenHands' Cloud *Individual* plan is itself "Free", so "paid cloud … price not listed" is wrong. Cline
  sells a **ClinePass subscription at $9.99/month**, so "No subscription" is wrong.
- **watch_out fields hold reviewer notes, not warnings for users.** Examples: "the price quoted is the standing list price, not a
  promo" and "no separate legal company name shown on the footer". These mean nothing to a beginner and must go.

## Verdicts

| id | verdict | evidence |
|---|---|---|
| brainfm | CUT | Rule 12. brain.fm/pricing: "MONTHLY PLAN $14.99 /month $14.99 billed monthly", "YEARLY PLAN $99.99 /year". Footer "© 2026 Brain.FM, Inc."; terms "provided by Brain.FM, Inc.". Price and company are correct. But brain.fm/science ("How is Brain.fm music made?") says the product adds science to **human-composed music** and calls music made purely by AI "cold and boring". No page calls the product AI. It is alive and takes users ("TRY FOR FREE"). |
| ecrett-music | FIX | Home page plan table opens on **Annual** ("INDIVIDUAL $4.99 /month billed annually", Business $14.99). With **Monthly** clicked: INDIVIDUAL "$7.99 /month", BUSINESS "$24.99 /month", FREE "$0.00 Download preview music for free". So $7.99 is correct. Footer "SOUNDRAW Inc."; terms: "'ecrett music' (the 'Service') operated by SOUNDRAW Inc." It is AI by its own page ("combinations of music created by AI", "ecrett AI will create music"). Terms Art. 3: free use is limited and "any music that is downloaded for free is prohibited from publishing and/or commercial use". Alive: the /play music maker loads and works; the footer copyright is "©ecrett music 2018" (old, but the app works). Not a duplicate: the `soundraw` card already exists, and Ecrett is SOUNDRAW Inc.'s separate, cheaper product ("Like Ecrett? Try its big brother SOUNDRAW!"). |
| fadr | FIX | Home page plan table: "Fadr Basic Free", "Fadr Plus $10/mo or $100/yr". FAQ: "Fadr Plus costs $10 USD per month or $100 USD per year". The "50% Off Fadr Plus" banner is a promo and was correctly ignored. Terms: agreement with "Pebble LLC, doing business as Fadr"; footer "Made with 💛 by Pebble". So the company is wrong, and the watch_out claim that no legal name is shown is false. AI by its own page (fadr.com/plus: "The finest AI stem separation on the planet"). Free plan: "Basic Stems", "MP3 Downloads". Plus adds "WAV Downloads", "Individual Drum Stems", "Stems Plugin". "Remix any song without prior experience." |
| onyx | FIX | Plan table: "Business For teams of any size. $20 per user / month Annual Billing". There is no monthly toggle, so "(billed annually)" is right. There is no seat minimum ("teams of any size"; README: "from individual users to the largest global enterprises"). Enterprise is "Contact us". Company: Cloud Terms (onyx.app/legal/cloud) say "DanswerAI, Inc., a Delaware corporation"; the privacy policy says "Danswer"; the footer only shows "© 2026 Onyx". GitHub onyx-dot-app/onyx is not archived (pushed 2026-09-30, 32k stars). README: "Onyx Community Edition (CE) is available freely under the MIT license". It deploys with Docker, and a "Lite" mode needs "under 1GB memory". So a free version exists and `free_tier` should be true (same rule-9 pattern as upscayl/vane). cloud.onyx.app sign-in shows "New to Onyx? Create an Account". The home page names connectors (Slack, Confluence, Drive, "50+ Connectors") but never email, so I removed "email". **Audience:** this is a workplace tool sold to companies ("Book a Demo", "enterprise knowledge"). One person can still buy one seat, so I kept it at skill "medium". Lead may cut on fit. |
| cline | FIX | Pricing: "OPEN SOURCE Free For individual developers … Pay only for AI inference on a usage basis"; Enterprise "Custom". But cline.bot/cline-pass: "ClinePass: Best Subscription for Open Weight Models … Get ClinePass for $9.99 *Standard rate $9.99 per month after promotion period" and "ClinePass costs $9.99/month". The card's "No subscription" is false, and rule 9 requires naming the paid part. Company "Cline Bot Inc." is verified (footer and TOS). It also now ships as a CLI and a desktop app ("Cline for Desktop (Beta) … No editor required"), not only in VS Code. |
| openhands | FIX | Pricing table: "Local Open Source Free"; "SaaS Individual Free — Bring your own key or use our providers at-cost … Get started free" ("Max Daily Conversations … 10", "Users 1"); "Enterprise Custom pricing". FAQ: open source is "MIT licensed … can run locally on your machine with your own LLM key". Cloud has "a free Individual tier, as well as commercial tiers for organizations". Its AI provider is "at cost, with no markup on a pay-as-you-go basis". So the only paid plan without a price is Enterprise, which is for organizations; the card's "paid cloud price not listed" is wrong. Company: the privacy policy says "All Hands AI ('All Hands AI', 'we,' or 'us')" at 24 Oak Street, Cambridge, MA; the footer says "© 2026 OpenHands". app.all-hands.dev returns 200. |
| komo | FIX | komo.ai/pricing, rendered, opens on **Annual** ("Komo Pro $17 /month when billed annually"). With **Monthly** clicked: "Free $0 forever 25 credits every day, Komo Fast + budget models"; "Komo Pro $20 /month, 2,000 monthly credits, Every premium model — GPT-5.6, Claude, Gemini, Grok, Deep research, People search"; "Komo Max $200 /month". Home: "Deep research requires a paid plan"; footer "© 2026 Komo AI · Answers with sources". /terms and /privacy are 404, and no terms link exists on the site or the login page, so the footer name "Komo AI" is the best evidence (rule 15: footer). Sign-up is open (komo.ai/auth/login: "Sign up", Google, Microsoft). Note: the site's "About" link goes to beta.komo.ai, a waitlist page for a different product ("The Self-Driving Business … Join Waitlist"). The search product itself is live and takes sign-ups, so this is not a rule-11 drop, but the lead should re-check it in the next batch. |

## Exact corrected field values (only changed fields)

```json
{
  "ecrett-music": {
    "company": "SOUNDRAW Inc.",
    "price_from": "$7.99/month (Individual), or $4.99/month billed annually",
    "good_for": "Making simple background music for videos, games and podcasts: pick a scene, mood and style, and its AI makes a new tune you can use without paying extra each time",
    "watch_out": "The free plan only downloads preview music, which you may not publish or use to make money. To use tracks in your videos you need Individual ($7.99/month). The music is meant to go inside videos, games or podcasts, not to be sold or shared as songs on their own"
  },
  "fadr": {
    "company": "Pebble LLC",
    "price_from": "$10/month (Fadr Plus), or $100/year",
    "good_for": "Using AI to pull a song apart into separate tracks (vocals, drums, bass, melody) and remix it, even with no music experience",
    "watch_out": "The free plan splits songs into the main parts and gives MP3 downloads only. Finer splits (like single drums), higher-quality WAV files and the add-ons for music software need Fadr Plus"
  },
  "onyx": {
    "company": "DanswerAI, Inc.",
    "free_tier": true,
    "price_from": "Free to run yourself (Onyx cloud $20 per user/month, billed annually)",
    "good_for": "AI chat and search across a team's work files and apps (like Slack, Google Drive and Confluence), in Onyx's cloud or installed on your own server",
    "watch_out": "Made for teams at work. The $20 per person price is only offered with yearly billing. The free version means installing it yourself on a computer or server you manage, which takes technical skill"
  },
  "cline": {
    "price_from": "Free app (you pay for the AI as you use it, or ClinePass $9.99/month)",
    "good_for": "An AI helper that plans, writes and changes code for you, inside the VS Code code editor, in a command window, or in a new desktop app (still in testing)",
    "watch_out": "The app is free, but the AI it uses is not: you buy AI credits as you go, connect your own paid account from a company like OpenAI or Anthropic, or subscribe to ClinePass ($9.99/month). Made for people who write code"
  },
  "openhands": {
    "company": "All Hands AI",
    "price_from": "Free (you pay for the AI at cost or use your own key; Enterprise plan for companies is custom-priced)",
    "good_for": "Open-source AI helpers that write and fix software for you, either installed free on your own computer or used on the OpenHands website",
    "watch_out": "Built for software developers. The free website plan allows 1 user and 10 conversations a day. Either way you pay for the AI itself, at cost through OpenHands or with your own paid account from an AI company"
  },
  "komo": {
    "company": "Komo AI",
    "price_from": "Free (Komo Pro $20/month, or $17/month billed annually)",
    "good_for": "Asking questions and getting AI answers with links to the sources; paid plans add deep research and top AI models",
    "watch_out": "The free plan gives 25 credits a day and only Komo's fast and budget AI models. Deep research, people search and top models like GPT, Claude and Gemini need Komo Pro ($20/month for 2,000 credits)"
  }
}
```

If the lead overrides the Brain.fm cut (for example, to treat "science-backed music" as in scope), these fields must change
because the current good_for is false by the vendor's own page:
`{"brainfm": {"good_for": "Music made to help you focus, relax or sleep; the company says it is written by people and shaped using brain science", "watch_out": "It is not free: after the free trial it costs $14.99/month, or $99.99/year. The company says its music is human-composed, not made by AI"}}`

## Booleans
- open_weights false on all 7 is correct. None of the pages offer downloadable model weights; open-source code alone doesn't count.
- runs_on_your_computer: true for onyx, cline and openhands is correct (each can be installed and run by you). False for fadr, komo, ecrett and brainfm is correct (all are websites or apps using the vendor's servers).
- free_tier: onyx false -> **true** (MIT Community Edition). The others are correct: ecrett $0.00 plan, fadr Basic "Free for life", cline free app, openhands Local and Individual "Free", komo "$0 forever", brainfm trial only.

## Not changed, for the lead to know
- Onyx, Cline and OpenHands are tools for developers or company teams. None of them is a pay-per-request API (so no rule-16
  problem), and each has a sign-up app or installer. But a very non-technical reader will struggle with all three. Their skill
  levels (medium, medium, hard) are fair.
- Cline's ClinePass page says "after promotion period", so there may be a lower first-period price at checkout. I used the stated
  standard rate of $9.99/month (rule 10). I did not go through checkout.
- OpenHands has also published its own models on Hugging Face in the past. The OpenHands site pages I read do not offer weights,
  so open_weights stays false.
- Batch count after this review: 6 cards (7 minus 1 cut).
