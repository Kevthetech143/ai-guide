# review 019p (batch 28), 2026-11-18, Opus reviewer

VERDICT: SHIP the 19-card patch as written. 1 FIX for the lead on wellsaid-labs (that card is not in the patch).

Every changed field was re-checked on the provider's own page (curl, plus real Chrome for toggles). All match.

1. wellsaid-labs | FIX (lead edit, keep the card; the service is live). The card's link https://www.wellsaid.io/ai-voice-pricing now 301-redirects to "/", and so does /pricing. The homepage has only "Get a demo" buttons, no prices, and no free signup or trial (I searched the page text for "free", "trial" and "sign up": nothing). Quote: "Plans are scoped with our team based on how much voiceover you produce and where it needs to go." Replace:
   - link: "https://www.wellsaid.io/"
   - free_tier: false
   - price_from: "Custom price (ask sales)"
   - watch_out: "Plans are set up with WellSaid's team based on how much voiceover you make, so you have to ask for a demo to get a price."
   - watch_out_source: "https://www.wellsaid.io/"
   - last_checked: "2026-11-18"
   Ripple: ai-voiceover-for-my-videos names WellSaid but makes no price or free claim about it, so nothing changes there.
2. pictory | price_from "$29/month ($25/month billed annually)" OK. https://pictory.ai/pricing body: "Starter Black Friday Offer $12.50 Was $29 $14.50 Was $29 per month, billed annually / per month, billed monthly". The page title and meta description: "Pictory pricing starts at $25 per month" (dateModified 2026-11-16). $25 = 2 x $12.50 under "50% Off ALL Plans", so it fits. The annual card's "Was $29" is the monthly price shown as the anchor. The watch_out ("14-day trial", "720p", "$29 instead of $25") is all on the page.
3. mubert | price_from "$14/month" OK. Clicking Monthly on https://mubert.com/render/pricing in Chrome shows "Creator Non-commercial $14 / month". The annual price shows only as the Black Friday "$8.17 /mo ... Billed $98 for the first year", and the page has no regular annual price, so dropping the $11.69 bracket is correct. Restore the bracket after Black Friday.
4. scite | price_from "$20/month ($12/month billed yearly)" OK. On https://scite.ai/pricing in Chrome, unchecking "Billed yearly" shows "Basic ... $20 / month". This matches "Save $96" ($20x12 - $12x12 = $96).
5. photoshop-generative-fill | watch_out rewrite OK. Every sentence is on https://www.adobe.com/products/photoshop.html (Chrome): "US$22.99/mo Annual, billed monthly", "Generative credits for AI features in Photoshop", "Creative Cloud Pro ... Regularly at US$69.99/mo", "20+ creative apps and AI tools". The "25 credits" and "unlimited Generative Fill" claims are gone from the page, so cutting them was right. The $29.99 first-year promo (ends Nov 27) is correctly left out.
6. lindy | price_from "$29.99/user/month" KEEP, with a caveat: https://www.lindy.ai/pricing is running a live A/B test. My real Chrome and 1 of 5 curls got "Team ... $ 49.99 /mo 5,000 credits". The other 4 curls got "$ 29.99 /mo 3,000 credits ... paid usage starts at $29.99 per user per month". The Wayback copy from 11-17 shows $49.99. $29.99 is the cheapest plan the official page offers, so keep it. If the $49.99 page becomes the only one, change both price_from and watch_out to $49.99.
7. perplexity-comet | annual-only OK. https://www.perplexity.ai/pro shows only "$17 /month when billed annually", with no monthly toggle (checked the Chrome snapshot). The help center plan table says "Browser Agent (Comet Assistant) Queries: No" for Free. Not changed, and no monthly price was guessed.
8. lovable OK: in Chrome, clicking Yearly on https://lovable.dev/pricing shows "$25 Originally $25 per month $21 / month, billed annually". The watch_out's "5 build credits (up to 30 a month)" is on the page.
9. otter OK: https://otter.ai/pricing shows "Pro ... $16.99 /user/month" and "Pro $8.33 user/month". The watch_out's "300 monthly transcription minutes" and "3 lifetime audio/video file imports" are on the page.
10. playground-ai OK: https://playgroundai.com/design/pricing shows "Annual -20% $ 15 $ 12 /mo $ 144 will be charged in total annually" and "5 images every 3 hours ... 6 monthly credits".
11. synthesia OK: https://www.synthesia.io/pricing shows "$19 $14 /month $168 billed yearly". The "$9 first month" promo is correctly left out.
12. Unchanged spot-checks, all still true: speechify ("Premium ... $29 /Month", "10 robotic sounding voices"), opus-clip ("Starter ... $15 USD /mo Starter plan only available in monthly ... 150 credits per month"), typebot ("Starter $39 /month", "200 chats /months").

Browser: session ag019p-rev is closed. `pgrep -f pw-aiguide-review` printed nothing (exit 1).
