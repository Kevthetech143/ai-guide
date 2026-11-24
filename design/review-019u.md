# Review 019u (2026-11-24) — reviewer ag019u-review (Opus 5.5)

## Verdict: FIX 7.5/10 (patch is accurate on 19 cards; jammable publishes a first-month promo, and the UVR flag needs a reword). Apply the 4 edits below, then it ships.

The patch matches HEAD bdc1f9f except last_checked (old dates 2026-11-10 / 2026-11-11). I checked this with a field-by-field diff of providers-019u.json against data/providers.json. No hidden edits. All 20 cards are in the patch.

## 1. Paid web apps (all checked on the providers' own pages)
- jammable — FIX. https://www.jammable.com/pricing (200): "Basic For making covers $1.99 $8.99 first month, then $8.99 a month Start for $1.99"; headline "Your first month from $1.99"; FAQ "What can I do without a plan? You can browse and listen to every voice on Jammable. Making covers, downloading them, text to speech and duets all need a plan." So the list price is $8.99 and price_from is right. But the $1.99 is a first-month promo, and the card's watch_out publishes it ("with the first month at $1.99"). It came in on 10-29 (batch 018x) and the worker carried it forward without flagging it. It must come out.
  Second problem: the other watch_out sentence ("Many voices imitate real singers and characters...") is not on the cited pricing page. It is on https://www.jammable.com/terms (200): "These Custom Voice Models may bear certain resemblances to the vocal characteristics of identifiable public figures or fictional characters" and "We do not claim any ownership, affiliation, or representation of these public figures or fictional characters". The homepage trending list also shows "Michael Jackson", "ROSÉ (ALL-ROUNDER) BLACKPINK", "Eric Cartman (South Park)". The "no free plan / $8.99" fact is already in price_from, so (like onyx in 019t) the price drops out of watch_out and the source moves to /terms. No Black Friday banner seen.
- wispr-flow — OK. Real Chrome, https://wisprflow.ai/pricing: Annual tab (default) "Pro FOR INDIVIDUALS AND TEAMS $12/user/mo"; Monthly tab "$15/user/mo"; Free "Limited words per week", Pro "Unlimited dictations". The cited source https://wisprflow.ai/ says "Flow's is free, with no trial countdown or credit card required, for 2,000 words per week." No Black Friday text (checked in the browser: false). The only discount text is the standing student/educator offer, not published. OK.
- liner — OK. https://liner.com/pricing: Free "1 file upload/day (up to 25MB/file) Answers with ads"; "Pro $17.99 $14.99 /month, billed annually"; FAQ "a free account offers limited credits which may run out quickly with just a few tasks". "Get 17% off" is the yearly discount, not a sale. OK.
- undermind — OK. Real Chrome, https://www.undermind.ai/#pricing, all four views: Academic monthly "Pro $20 per month", Academic annual "$16 per month, billed annually"; Industry monthly "$75 per month", Industry annual "$60". Team is cheaper per head (Academic "$18.7 per person per month") but is sold as "5 seats at $18.7", so the cheapest thing one person can buy is Pro at $20/month. price_from says that. Free: "Standard rate limits on chats and searches"; Pro: "10x higher usage limits". OK.
- pixelcut — OK. Real Chrome, https://www.pixelcut.ai/pricing: Monthly "Pro $10 per month ... 600 AI Credits Monthly"; Yearly "$10 $8 per month, billed yearly". Free "Limited Background Removal Limited Upscale". FAQ: "Credits are a special resource used whenever you create or edit images with certain advanced AI models". The $10 strikethrough in the yearly view is the monthly price, not a sale. OK.
- draw-things — OK. https://drawthings.ai/: "FREE ACCOUNT Community ... offload tasks like image generation to Draw Things' managed servers"; "$8.99/mo Draw Things+ Enjoy higher compute limits and access premium cloud features, including custom LoRA uploads"; "For iPhone, iPad, and Mac". OK.
- krita-ai-diffusion paid part — OK. https://interstice.cloud/service: "One-time payment 10 € 5 000 tokens One-time payment 28 € 15 000 tokens"; "Start exploring with a limited number of free tokens". The README links interstice.cloud as the maker's site. OK.

## 2. Open-source / local cards: 13 of 13 checked (GitHub API + README, Hugging Face page)
None archived. All watch_out sentences found on the cited page unless noted.
- ultimate-vocal-remover: MIT, v5.6 (2023-09-26), pushed 2026-10-06. See section 3.
- diffrhythm-2: Apache-2.0, no releases, last push 2025-11-09 — going quiet (over 12 months), as the worker flagged. README links the Hugging Face Space and uses "pip install -r requirements.txt". Card stays.
- kokoro-tts: https://huggingface.co/hexgrad/Kokoro-82M (200): "With Apache-licensed weights"; usage is "!pip install -q kokoro"; "For more languages and details, see Advanced Usage"; "VOICES.md". OK.
- f5-tts: MIT, 1.1.22 (2026-07-23). "Our code is released under MIT License. The pre-trained models are licensed under the CC-BY-NC license". OK.
- dia2: Apache-2.0, no releases, last push 2025-11-29 (near going quiet). "The model only supports up to 2 minutes of generation in English"; "voices vary per generation ... Use with prefix"; "use CUDA 12.8+ drivers". OK.
- buzz: MIT, v1.4.5 (2026-08-23). "Buzz now requires Apple silicon. The last version to support Intel Macs is 1.4.5"; "App is not signed, you will get a warning when you install it". OK.
- handy: MIT, v0.10.2 (2026-11-24). https://handy.computer/: "the free and open source app for speech to text"; "One tool, one job. Transcribe what you say and put it into a text box"; "donate". No price anywhere. OK.
- spleeter: MIT, v2.3.0 (2021-09), pushed 2026-10-28. OK.
- stemroller: 3.1.1 (2026-06-30). README "You'll need to wait several minutes for splitting to complete"; site "totally free and open-source", "Donations are always appreciated". OK.
- piper-tts: GPL-3.0, v1.8.0 (2026-09-04). "pip install piper-tts"; "The Open Home Foundation is looking for maintainers for Piper!". OK.
- vibe: MIT, v3.3.8 (2026-11-21). "summaries using the Claude API"; "Ollama support". OK. ("speed depends on your computer" is a fair reading of "Optimized for GPU", not word for word; left, as in earlier batches.)
- swarmui: MIT, 0.9.8-Beta (2026-02-06), pushed 2026-11-22. "note that any models used have their own licenses". OK.
- krita-ai-diffusion: GPL-3.0, v1.53.0 (2026-08-22). "at least 6 GB VRAM (NVIDIA) is recommended. Otherwise generating images will take very long"; "Cloud generation is also available to get started quickly without heavy investment". OK.
- easy-diffusion: v3.0.16 (2026-03-31). README "Minimum 8 GB of system RAM", "Atleast 25 GB of space", NVIDIA/AMD/M1-M4 "or run on your CPU". The license sentence is in the repo's LICENSE file, not the README: "agrees not to use the Software: In any way that violates any applicable ... law ... To generate or disseminate ... content with the purpose of harming others". Same repo, so I left it (non-blocking).
- open_weights / runs_on_your_computer / free_tier: all unchanged and consistent with the pages above.

## 3. ultimate-vocal-remover — reword (worker's flag was right)
https://github.com/Anjok07/ultimatevocalremovergui README has no sentence about downloading models (searched: no "Download Center", no "slow", no "CPU"). What it does say: "Conversion times will significantly depend on your hardware. These models are computationally intensive."; "Nvidia GTX 1060 6GB is the minimum requirement for GPU conversions. Nvidia GPUs with at least 8GBs of V-RAM are recommended." The model "Download Center" text on https://ultimatevocalremover.com/ is about UVR6, which is not out yet, so pointing the source there would be wrong. Reword to the README facts; source stays GitHub.

UVR6 date: https://ultimatevocalremover.com/ says "UVR6 comes to Windows on December 11, 2026. Mac follows shortly after, then Linux. Until then, download UVR5." It is the maker's own plan, but it is a future date, and the card describes the app you can get today. Do not add it. Re-check after 12-11; if UVR6 has shipped, update the card then.

## 4. Question-page ripple
Searched questions.json (title, intro, meta_description) for Jammable and Ultimate Vocal Remover.
- ai-that-sings-in-another-voice intro: "Jammable and ACE Studio have no free plan, and many of Jammable's voices imitate real singers, so check you are allowed to share what you make." Still true (pricing FAQ + /terms + homepage). No $1.99 anywhere. No change.
- UVR appears in 4 intros/meta (ai-music-generator-on-my-computer, ai-that-takes-vocals-out-of-a-song x2, ai-that-splits-a-song-into-instruments). None mention model downloads or graphics cards. No change.
No ripple.

## Edit list for the lead (apply on top of providers-019u.json)
1. jammable | watch_out | Many voices imitate real singers and characters, so check you are allowed to share what you make.
2. jammable | watch_out_source | https://www.jammable.com/terms
3. ultimate-vocal-remover | watch_out | Splitting runs on your own computer, so how long it takes depends on your hardware. To use a graphics card it needs at least an NVIDIA GTX 1060 with 6 GB, and 8 GB of graphics memory is recommended.
4. (no field change) Do not add the UVR6 release date; re-check ultimate-vocal-remover after 2026-12-11.
Everything else in providers-019u.json ships as written. questions.json: no edits.

## Housekeeping
- Browser: my own session ag019u-review (profile ~/.config/pw-aiguide-recheck). After `close`, `pgrep -fl pw-aiguide-recheck` printed nothing (exit 1).
- Read-only apart from this file. I did not touch providers*.json, questions.json, any page, or /tmp/ai-wrapper/. No downloads. Scratch pages are in /tmp/ag019u-review/.
- Rung: Opus 5.5. An independent final review of published facts fits the Opus tier.
