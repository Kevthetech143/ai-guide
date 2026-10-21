REVISE
Reviewer: Fable 5.1 (independent, fresh context). Date 2026-10-21. Read + verify only; no site file edited besides this one.
Why REVISE: every price, free_tier and link change in data/providers-018p.json matches the provider's own page (all re-opened today). Two watch_out sentences go past their cited source and need a wording fix (chatgpt, character-ai). Nothing else blocks. sora skipped per lead (card is being removed).

How I checked: curl for the 19 open pages; real Chrome (playwright-cli session ag018pr, profile ~/.config/pw-aiguide-recheck, closed when done) for the Cloudflare/JS pages: chatgpt.com, canva.com (incl. the Monthly billing switch), support.character.ai x2, character.ai, x.ai/pricing, grok.com/plans, flow.google.com/about (incl. collapsed "View plan features"), kling.ai, docs.midjourney.com, perplexity.ai/pro, suno.com. Page texts saved under /tmp/ag018p/. Progress log /tmp/ag018p/review-progress.log.

## Per-card lines (id | verdict | quote + URL)

canva-ai | OK | Yearly view: Pro "US$ 144 /year for one person"; Monthly switch: Pro "US$ 18 /month for one person"; Free "Up to 20 Standard or Premium AI uses^" (footnote: "actual usage may be lower"). https://www.canva.com/pricing/ (curl 403, renders in Chrome). price_from "$12/month (billed annually; $18 monthly)" and watch_out both match.

character-ai | FIX: watch_out -> "The free plan shows ads and has some limits; the cheapest paid plan (lite) starts at $4.99 a month, and the price changes by country." | The dropped sentence "The characters sometimes make things up." is not on either cited page (carried over from the old card; the home page is a sign-up wall, so I could not find it on an official page either). Rest verified: "(c.ai) lite starts at $4.99/mo. Pricing varies by region" https://support.character.ai/hc/en-us/articles/55388952900379--c-ai-lite-FAQ ; compare table "Ads Full / Less / None", "Feature limits Limited / Limited / Unlimited", "In the US, lite is $4.99 USD a month or $2.49 USD a week" https://support.character.ai/hc/en-us/articles/56173313531675-About-c-ai-lite (both curl 403, render in Chrome). price_from $4.99/month OK.

chatgpt | FIX: watch_out -> "The free plan gives unlimited plain chats but limits uploads, pictures and voice chats; the cheapest paid plan (Go) costs $8 a month and may include ads." | Page says Free "Unlimited text chats with GPT-6", "Limited messages with uploads", "Limited image creation", "Limited voice chats"; Go "$8 / month", "This plan may include ads." The patch text "has limits on messages" clashes with the page's "Unlimited text chats". Free plan does NOT say ads (worker right to move that to Go). https://chatgpt.com/pricing (curl 403, renders in Chrome). price_from $8/month OK.

grok | OK | "Free $0/month" "Limited" "Limited Chat requests"; "Plus $8/month"; "Premium $30/month"; "Super $100/month". No "SuperGrok" or X-account wording on the page. https://x.ai/pricing (curl 403, renders in Chrome). grok.com/plans (200) shows the same Plus $8 / Premium $30. price_from $8/month and watch_out match.

perplexity | OK | Free "$0 /month Good for limited daily usage"; Pro "$17 /month when billed annually". No $20 monthly figure on https://www.perplexity.ai/hub/pricing (200) nor on the card link https://www.perplexity.ai/pro (rendered in Chrome: only "$17 /month when billed annually"). Reverting the $20 is correct.

llama | OK | https://dev.meta.ai/llama/ (200): "Llama 4", "Running Meta Llama on Mac", "Running Meta Llama on Windows", "Running Meta Llama on Linux", "Getting the Models". llama.com now 301s to dev.meta.ai. Link move and watch_out_source fine; watch_out unchanged and fits the page (you run it yourself or via a partner).

mistral | OK | https://mistral.ai/pricing/ (200): Free "Limited messages and web searches."; Pro "$14.99 /mo Excluding taxes". Old link /products/vibe/ had no prices. Link, watch_out, watch_out_source match.

qwen | OK | unchanged card, date bump only; no watch_out_source added (right call, hardware claim not on an official page). https://qwen.ai/ 200. Content not re-read by me.

midjourney | OK | https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans (curl 403, renders in Chrome): "Basic Plan Monthly Price $10"; "Stealth Mode ... is only available on the Pro and Mega Plans." Linked Free Trials article: "No free trial is currently available in Discord or the midjourney.com website." free_tier false and "no free plan" hold.

stable-diffusion | OK | unchanged card, date bump only. Link 200. Content not re-read by me.

flux | OK | unchanged card, date bump only. https://bfl.ai 200. Content not re-read by me.

elevenlabs | OK | https://elevenlabs.io/pricing (200): "Starter $6 per month"; FAQ "Starter $6 (30,000 credits)"; "The equivalent monthly price on an annual plan is $5 for Starter". price_from "$5/month (billed annually; $6 monthly)" matches. watch_out (small free plan, monthly limit): Free "$0 (10,000 credits)", credits reset monthly. OK.

suno | OK | https://suno.com/pricing (200): annual view Pro "$8 /month Saves $24 by billing yearly!"; page's own plan data: Pro "monthly_price_usd":10,"annual_price_usd":96; Free "No commercial rights". price_from "$8/month (billed annually; $10 monthly)" and watch_out match.

runway | OK | https://runway.com/pricing (200): Standard "$15 $12 /month" "Billed annually"; Free "125 one-time credits"; "Gen-4.5 uses 12 credits per second of generated video" backs the watch_out. Unchanged card + source fine.

cursor | OK | https://cursor.com/pricing (200): "Free $0 /month Limited AI usage"; "Plus $8 /month" with "*Only Grok models are available on this plan"; "Premium $30 /month" with "*3rd party models are available in Cursor, billed separately by usage"; "Third Party model usage in Cursor is not included in the monthly prices shown and must be purchased separately." The $20 Pro plan is gone. Footer still "© 2026 Anysphere, Inc." so company field stands. price_from $8/month and watch_out match.

whisper | OK | https://github.com/openai/whisper 200. Unchanged card + source fine.

sora | SKIPPED per lead (card to be removed, like playht). Not reviewed.

veo | OK | https://flow.google.com/about (200, collapsed panels read from page HTML): "Try Google Flow free of charge"; Free plan "Included Features: 50 daily Google Flow credits ... Veo 3.1"; "Google AI Plus $4.99/mo*"; "Google AI Pro $19.99/mo*"; "* Prices may vary by market"; FAQ "Costs vary across image, video and model selection." free_tier true, price_from "$4.99/month (Google AI Plus)", link, watch_out all match. Old "pay per second" rightly dropped.

pika | OK | https://pika.art/pricing (200): Free "0 credits / month · packs only"; table "Price / mo $0 $10 $35"; "Price / mo (annual, –20%) $0 $8 $28"; "Monthly credits 0 · packs only"; Free and Starter "Included: No watermark". free_tier false is the honest read (free plan gives nothing to use without buying a pack); price_from and watch_out match; old watermark claim was wrong.

kling | OK (note) | https://kling.ai/app/membership/membership-plan (200, JS; rendered in Chrome): comparison "Basic $0 Free"; Basic column "-" for "Brand watermark removal" and "Generated content is for commercial use"; "Daily Free Credits for Subscribers -" for Basic; Standard "$10". Note only: the page is running a timed promo (countdown shown) with Standard "$6.99 / 1st mo ... Then $8.8/month"; $10 is the list price, so "start at $10 a month" is fine to keep. Link move OK; old "free daily credits" claim rightly dropped.

## watch_out_source URL check
All 17 added sources are official domains. curl 200: perplexity, llama, mistral, elevenlabs, suno, runway, cursor, whisper, flow.google.com, pika, kling. curl 403 but render in real Chrome: canva, character.ai support (x2), chatgpt, x.ai, docs.midjourney. None dead.

## Ship list
Ship as patched: canva-ai, grok, perplexity, llama, mistral, qwen, midjourney, stable-diffusion, flux, elevenlabs, suno, runway, cursor, whisper, veo, pika, kling.
Apply the two FIX watch_out strings above: chatgpt, character-ai.
sora: remove per lead.
