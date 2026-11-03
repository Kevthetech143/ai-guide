# Review of ai-guide-019b (batch 14, the 20 oldest cards) — 2026-11-03

Verdict: SHIP, with one mechanical fix before merge (kling price_from needs the site's discount note). Score: 9/10.

Why SHIP: every patched field I checked matches the provider's own page today. The one wording change (canva-ai watch_out) is true on canva.com/pricing and reads plainly. The two new watch_out_source URLs show the watch_out fact. A full field-by-field diff of providers-019b.json against providers.json at c252671 found only last_checked plus the three listed fields; nothing changed silently. JSON is valid and byte-identical to json.dumps(indent=2, ensure_ascii=False)+"\n". The "no question-page ripples" claim holds. The worker's own browser session is closed.

How I checked: curl (desktop UA) for flux (HF), stability, cursor, github.com/features/copilot/plans, elevenlabs, suno, runway; real Chrome via playwright-cli session ag019b-rev (profile ~/.config/pw-aiguide-review, no sign-in) for canva (403 to curl), kling (JS app, content in an iframe) and docs.midjourney.com (403 to curl). Session closed; `pgrep -f pw-aiguide-review` prints nothing.

## 1. canva-ai watch_out — OK
https://www.canva.com/pricing/ (Chrome, both Yearly and Monthly views). Free plan, "AI usage" row: "Limited access to Standard and Premium AI^". Pro: "10x more AI than Canva Free (Premium or Ultra AI)^"; Business: "20x more AI than Canva Free". Footnote: "^Standard, Premium, and Ultra AI tools share a monthly AI allowance that varies by plan." The standalone number 20 appears nowhere on the page (the only "20" is "20x more AI" for Business), so "up to 20 AI uses" had to go. Prices: Monthly view Pro "US$ 18 /month for one person"; Yearly view Pro "US$ 144 /year for one person" — so "$18 a month, or $144 if you pay for a year" still holds and price_from "$12/month (billed annually; $18 monthly)" holds (144/12 = 12). Readability: "The free plan only gives limited access to the AI tools" is one short plain sentence, 8th-grade fine.

## 2. watch_out_source URLs — OK
- flux | https://huggingface.co/black-forest-labs/FLUX.2-klein-4B (curl 200). Page text: "Our most accessible model runs on consumer GPUs like the RTX 3090/4070"; "The FLUX.2 [klein] 4B model fits in ~13GB VRAM and is accessible on NVIDIA RTX 3090/4070 and above"; "pip install git+https://github.com/huggingface/diffusers.git". Supports "takes some technical steps and a strong graphics card". License on page: Apache 2.0.
- stable-diffusion | https://stability.ai/news-updates/introducing-stable-diffusion-3-5 (curl 200). Page text: "You can download all Stable Diffusion 3.5 models from Hugging Face and the inference code on GitHub now"; "This model only requires 9.9 GB of VRAM (excluding text encoders) ... compatible with most consumer GPUs"; "run on consumer hardware". Supports "install it yourself and your computer needs a good graphics card".
- Field placement: watch_out_source after last_checked, same as 129 of the 224 existing sourced cards (the majority order). Fine.

## 3. kling price_from — FIX (convention, same as ace-studio in 018v)
https://kling.ai/app/membership/membership-plan (Chrome; the plan table is inside an iframe). Tabs: "Yearly 34% Off" / "Monthly 12% Off". Monthly tab, Standard: "$ 6.99 / 1st mo", "$10" (struck through), "30% Off 1st", "Then $8.8/month", "First-purchase offer available once. Monthly subscription can be canceled anytime." Yearly tab, Standard: "$ 79.2 / Year", "$120" (struck), "34% Off", "Then $79.2/year. Save $26.4 vs. monthly" (79.2 + 26.4 = 105.6 = 12 x $8.80, which confirms $8.80 is the ongoing monthly charge). Basic: "$ 0 Free"; in the comparison table Basic shows "-" for "Generated content is for commercial use" and "Brand watermark removal", so the watch_out holds.

Reading per the site rule: $10 is the Standard list price (shown struck through on both tabs). $6.99 is a first-month-only promo (not used). $8.80 is the price actually charged every month after that, which the page labels as "Monthly 12% Off" — a discount off list, exactly the boomy / ace-studio situation. The site's shape for that is list price plus a discount note. The worker kept bare "$10/month" with the note only in recheck-019b.md; the reader never sees it. Exact fix below. watch_out ("paid plans start at $10 a month") stays, same as boomy/ace-studio keep the list price in prose.

## 4. Spot-checks of other cards (all OK, free_tier and price_from hold)
- cursor | https://cursor.com/pricing (curl 200) | Free "$0 /month ... Limited AI usage"; Plus "$8 /month ... Our introductory plan ... *Only Grok models are available on this plan"; Premium "$30 /month"; Super "$100"; Ultra "$200"; Teams "$30 +/user/month". Only an Individual/Teams switch. free_tier true, "$8/month" hold.
- midjourney | https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans (Chrome) | "Basic Plan ... Monthly Price $10 ... Annual Price $96 ($8 / month)"; "Stealth Mode, which keeps your images and videos private, is only available on the Pro and Mega Plans". Free Trials article https://docs.midjourney.com/hc/en-us/articles/27870399340173-Free-Trials: "No free trial is currently available in Discord or the midjourney.com website." free_tier false, "$10/month" hold. (Optional, pre-existing, not the worker's change: most cards on this site write annual-vs-monthly as "$8/month (billed annually; $10 monthly)" — midjourney could follow that shape; lead's call, not required for SHIP.)
- github-copilot | https://github.com/features/copilot/plans (curl 200; card link https://github.com/features/copilot returns 200) | Free "$ 0 USD ... 2,000 completions per month ... Copilot CLI ... No credit card required"; Pro "$ 10 USD per user / month"; Pro+ "$ 39"; Max "$ 100". free_tier true, "$10/month" hold.
- elevenlabs | https://elevenlabs.io/pricing (curl 200) | Free "$0 (10,000 credits)" / "10k credits per month"; Starter "$6 $5 /mo 2 months free"; FAQ "The equivalent monthly price on an annual plan is $5 for Starter"; "Starter $6 (30,000 credits)". A "30,000 credits for $1" intro banner is on the page (promo, correctly not used). free_tier true, "$5/month (billed annually; $6 monthly)" hold.
- suno | https://suno.com/pricing (curl = Annual view; Chrome, Monthly clicked) | Monthly: Free "$0 /month ... 50 credits per day ... No commercial rights"; Pro "$10 /month"; Premier "$30 /month". Annual view: Pro "$8 /month Saves $24 by billing yearly!". free_tier true, "$8/month (billed annually; $10 monthly)" hold.
- runway | https://runway.com/pricing (curl 200) | Free "$0 /month 125 credits ... 125 one-time credits"; Standard "Billed annually. Save $36/year ... $15 $12 /month 625 credits /mo"; Yearly table "Standard $12 /month". free_tier true, "$12/month (billed annually; $15 monthly)" hold.

## 5. Silent-change check — OK
Diff of all 20 cards in providers-019b.json vs providers.json at c252671: only last_checked (20 cards, all -> "2026-11-03"), canva-ai watch_out, flux watch_out_source (added), stable-diffusion watch_out_source (added). No other field, no id/name/categories/link/free_tier/price_from/open_weights/runs_on_your_computer/good_for change. 20 ids all exist in providers.json; none new. File equals json.dumps(list, indent=2, ensure_ascii=False)+"\n" exactly.

## 6. Question-page ripples — OK
Grep of data/questions.json intro/meta_description/title for sentences that mention Canva together with a number or "AI uses": 0 hits. The worker's "none" claim holds.

## Fixes (exact field edits)
1. id: kling | field: price_from | new value: "$10/month (Standard list price; the page currently shows a 12% discount, $8.80 a month, plus 30% off the first month)" | source: https://kling.ai/app/membership/membership-plan (Chrome, Monthly tab) — "Standard $ 6.99 / 1st mo $10 30% Off 1st Then $8.8/month"; tab label "Monthly 12% Off". Same shape as boomy and ace-studio in providers.json.

Optional (pre-existing, lead's call): id: midjourney | field: price_from | new value: "$8/month (billed annually; $10 monthly)" | source: https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans — "Basic Plan Monthly Price $10 Annual Price $96 ($8 / month)".

## Not verified by me (worker's claims taken as reported)
character-ai, llama, mistral, pika, qwen, veo, whisper, deepseek, devin, gemma: no field changed except last_checked; I did not re-open these pages (outside the brief's spot-check list). The worker's deepseek note ("free_tier true is unchanged but not confirmed word for word") is an honest gap; the card stays as at HEAD.

Reviewer model: Fable 5.1 (claude-fable-5-1), the lead's named independent reviewer for this batch; a fresh-context cross-check against live pages is what the tier is for.
