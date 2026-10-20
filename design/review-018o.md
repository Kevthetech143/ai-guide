REVISE
Reviewer: Fable 5.1 (independent, fresh context). Date 2026-10-20. Read + verify only; no site file edited.
Why REVISE: (a) 4 unverified cards carry a placeholder watch_out_source that must come off; (b) adobe-firefly CAN be verified (US page readable via the remote fetcher) and its watch_out is stale; (c) playht is a dead service and should be removed. The 5 worker-verified cards are all OK.

## Per-card verdicts

### gemini — OK
Source https://gemini.google/subscriptions/ (curl 200). Quotes: Free "$0/ month with a Google Account"; "Google AI Plus" "$4.99/ month"; "Google AI Pro" "$19.99/ month"; free limits "compute-based usage limits". Link move, price_from $4.99/month, watch_out and watch_out_source all match the page. Keep as patched.

### kimi — OK (the $19 is now verified)
Source https://www.kimi.com/membership/pricing (curl 200; page is JS-rendered, read with headless Chrome). Quote, annual toggle: "Plus Efficiency upgrade $ 15 / month $19 Billed annually $180"; free tier "Adagio $0"; toggle "Monthly Annually Save up to $480" (Ultra "$ 159 / month $199" -> 12 x $40 = $480, which confirms the second figure on each plan is the monthly-billed price). So "$15/month (billed annually; $19 monthly)" is correct and matches the claude card's style. Open weights: https://huggingface.co/moonshotai/Kimi-K3 (200) "We release the full Kimi K3 model weights under the Kimi K3 License." Keep as patched.

### capcut-ai — OK
Source https://www.capcut.com/pricing (curl 200). Quotes: "Free USD 0"; "Pro USD 19.99 /month"; yearly "Pro USD 179.99 /year"; no plan named Standard on the page. Note only: Teams is "USD 12.49 /month per seat (2 seats)" (cheaper per seat but 2 seats minimum, so Pro is the cheapest single plan — fine). Page also says prices are "for reference only" until sign-in; optional to mention, not required. Keep as patched.

### claude — OK
Source https://claude.com/pricing (curl 200; anthropic.com/pricing redirects there, 200). Quotes: Free "$0"; Pro "$17" with "$200 billed up front", "$20 if billed monthly"; Max "From $100". Keep as patched.

### claude-code — OK
Same page. Comparison table: Claude Code on Free "No", on Pro "Yes" (listed under "Everything in Free, plus:"). free_tier false, price same as Pro, watch_out "There is no free access" all match. Keep as patched.

### chatgpt — unverified; strip placeholder
No page read (Cloudflare 403 per worker; not re-tried, out of my scope). watch_out_source must be removed. Card otherwise = current providers.json card.

### canva-ai — unverified; strip placeholder
Same ruling as chatgpt.

### character-ai — unverified; strip placeholder
Same ruling as chatgpt.

### adobe-firefly — NOW VERIFIED; card changes
This Mac's IP is blocked by Adobe (curl AND headless Chrome both get "Access Denied" on plans.html and firefly.html). The remote WebFetch reader got the US page at https://www.adobe.com/products/firefly.html with content (so 200 from a normal network). Quotes: "Firefly Standard" "US$9.99/mo" "2,000 monthly generative credits"; "Firefly Pro" "US$19.99/mo"; Free plan: "Limited free daily generations across both standard and premium features", "Get free daily generations to quickly create video, audio, and images."; FAQ: "Adobe has a free plan that provides users with free daily generations to try Adobe Firefly."; credits: "monthly allocation of credits that reset each billing cycle." The string "25 credits" does not appear anywhere on the page. plans.html (the old link) only renders the Japan locale for the remote reader (yen prices) and is blocked here, so move link to firefly.html.
Result: free_tier true (unchanged), price_from $9.99/month (unchanged, verified), watch_out rewritten (old "25 credits a month" is stale), link moved, last_checked 2026-10-20, watch_out_source set.
Label: verified via remote fetch of Adobe's own page; not reproducible from this Mac's IP.

### playht — remove the card
Evidence:
- DNS: `dig play.ht A` -> no record; `dig play.ai A` -> no record; www.play.ht is a CNAME to play.ht (no A). curl -> 000. docs.play.ai -> Vercel "DEPLOYMENT_NOT_FOUND" 404 with an expired certificate. api.play.ai -> no response. whois play.ht still ACTIVE (domain owned, site gone).
- Official text (search-engine index of PlayAI's own pages play.ai/ and play.ht/, not live-readable because DNS is gone): "We have shut down the service. Thank you for being part of our journey." No Meta/PlayAI press release found on about.fb.com or ai.meta.com; the shutdown banner gives no reason.
- Acquisition: Bloomberg 2025-07-11 "Meta Acquires Voice AI Startup PlayAI" — Meta confirmed the acquisition per Bloomberg; the 2025-12-31 end date comes only from third-party sites (unverified).
Recommendation: REMOVE. An honesty-first guide cannot list a tool whose site does not load, with price "Check site". Both question pages that list it keep 3+ other providers, so nothing goes empty.
Question pages that reference id "playht" (data/questions.json):
- slug "ai-that-copies-a-voice" (title "Can AI copy a voice?") — filter.ids ["fish-audio","playht","hume-ai","ace-studio","orpheus-tts","f5-tts"] -> drop "playht"
- slug "ai-voices-in-many-languages" (title "Can AI speak in other languages?") — filter.ids ["playht","narakeet","fish-audio","synthesia"] -> drop "playht"
Fallback if the lead prefers to keep it (not recommended): use the JSON below with the honest watch_out and NO watch_out_source.

## Ruling on watch_out_source placeholders
Keep watch_out_source ONLY on: gemini, kimi, capcut-ai, claude, claude-code, adobe-firefly (now verified).
Remove it from: chatgpt, canva-ai, character-ai, playht.

## Exact final JSON for every card that changes from the patch

```json
{
  "categories": [
    "image"
  ],
  "company": "Adobe",
  "free_tier": true,
  "good_for": "Great for business-ready pictures that are safe to use commercially, since it is trained on licensed content.",
  "id": "adobe-firefly",
  "last_checked": "2026-10-20",
  "link": "https://www.adobe.com/products/firefly.html",
  "name": "Adobe Firefly",
  "open_weights": false,
  "price_from": "$9.99/month",
  "runs_on_your_computer": false,
  "skill_level": "easy",
  "watch_out": "The free plan only gives you a small number of free generations each day; the cheapest paid plan (Standard) costs $9.99 a month for 2,000 credits, and credits reset every month.",
  "watch_out_source": "https://www.adobe.com/products/firefly.html"
}
```

```json
{
  "id": "chatgpt",
  "name": "ChatGPT",
  "company": "OpenAI",
  "categories": [
    "chat",
    "agents"
  ],
  "open_weights": false,
  "free_tier": true,
  "price_from": "$8/month",
  "skill_level": "easy",
  "runs_on_your_computer": false,
  "good_for": "Great for chatting, writing, homework help, planning trips, and turning word descriptions into pictures.",
  "watch_out": "The free plan is limited and can show ads; the cheapest paid plan (Go) costs $8 a month.",
  "link": "https://chatgpt.com/pricing",
  "last_checked": "2026-09-14"
}
```

```json
{
  "categories": [
    "image"
  ],
  "company": "Canva",
  "free_tier": true,
  "good_for": "Great for making social media posts, flyers, and presentations with AI help, right inside an easy drag-and-drop design tool.",
  "id": "canva-ai",
  "last_checked": "2026-09-14",
  "link": "https://www.canva.com/pricing/",
  "name": "Canva AI (Magic Studio)",
  "open_weights": false,
  "price_from": "$15/month",
  "runs_on_your_computer": false,
  "skill_level": "easy",
  "watch_out": "The free plan only gives a small number of AI uses each month, and Canva prices change by country, so check the pricing page for your own price."
}
```

```json
{
  "id": "character-ai",
  "name": "Character AI",
  "company": "Character AI",
  "categories": [
    "chat"
  ],
  "open_weights": false,
  "free_tier": true,
  "price_from": "$9.99/month",
  "skill_level": "easy",
  "runs_on_your_computer": false,
  "good_for": "Great for chatting and roleplaying with fun characters you pick or create yourself - story heroes, historical figures, and helpful personas.",
  "watch_out": "The free plan has daily limits, and the characters sometimes make things up; the paid plan costs $9.99 a month.",
  "link": "https://character.ai",
  "last_checked": "2026-09-14"
}
```

playht — recommended: delete the card from providers.json and drop "playht" from the two filter.ids lists above. Fallback only if kept:

```json
{
  "categories": [
    "voice"
  ],
  "company": "PlayAI",
  "free_tier": false,
  "good_for": "It turned written text into spoken audio with hundreds of voices in many languages.",
  "id": "playht",
  "last_checked": "2026-10-20",
  "link": "https://play.ht",
  "name": "PlayAI (formerly PlayHT)",
  "open_weights": false,
  "price_from": "No longer sold",
  "runs_on_your_computer": false,
  "skill_level": "easy",
  "watch_out": "This service has shut down. Its website no longer loads, and the company posted that it closed the service. Pick another voice tool from this list."
}
```

## Unchanged from patch (ship as-is)
gemini, kimi, capcut-ai, claude, claude-code.

## Evidence trail
Progress log: /tmp/ag018o/review-progress.log. Rendered pages: /tmp/ag018o/kimi-dom.html, /tmp/ag018o/adobe-*.html (Access Denied), /tmp/ag018o/docs.html.
