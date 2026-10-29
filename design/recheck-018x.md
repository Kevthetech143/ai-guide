# recheck-018x (batch 10, 2026-10-29)

All 20 links returned 200. All 20 get last_checked 2026-10-29 and a new watch_out_source. Output: data/providers-018x.json.

## Changes
- jammable | good_for | "...from a library of 100,000+ voices..." -> "...from a library of 60,000+ voices..." | https://www.jammable.com/pricing | "Unlimited covers, downloads and all 60,000+ voices."
- jammable | watch_out | "There is no free plan; the cheapest plan is Basic at $8.99 a month. Many voices..." -> "There is no free plan; the cheapest plan is Basic at $8.99 a month (new subscribers get a lower first month, $1.99 for Basic). Many voices..." | https://www.jammable.com/pricing | "Basic | $1.99 | $8.99 | first month, then $8.99 a month" (list price kept, discount noted; price_from unchanged)
- liner | watch_out | "The free plan shows ads in answers and gives 100 credits a day and 1 file upload a day. A deep research request costs 40 credits." -> "The free plan shows ads in answers and allows 1 file upload a day. Its credits are limited and may run out quickly with just a few tasks." | https://liner.com/pricing | "1 file upload/day (up to 25MB/file)", "Answers with ads", FAQ "a free account offers limited credits which may run out quickly with just a few tasks". The page shows no "100 credits a day" and no "40 credits" for deep research, so both were cut (unverified).
- pixelcut | price_from | "Free (Pro $10/month)" -> "Free (Pro $10/month, or $8/month billed annually)" | https://www.pixelcut.ai/pricing | "Pro | $10 | $8 | per month, billed yearly | 600 AI Credits Monthly"; "Save 20% with a yearly plan"
- wispr-flow | watch_out | "The free plan is capped at 2,000 words a week on a computer and 1,000 words a week on a phone. Pro removes the cap." -> "The free plan is capped at 2,000 words a week on a computer and has limited weekly use on a phone. Pro removes the cap." | https://wisprflow.ai/pricing | "Word limit | 2,000/week on desktop | Limited weekly use on mobile | No limits"; no 1,000 figure on the page.
- all 20 | watch_out_source | added | spleeter, buzz, dia2, diffrhythm-2, f5-tts, piper-tts, swarmui, vibe, krita-ai-diffusion, stemroller, easy-diffusion: their GitHub repos; draw-things https://drawthings.ai/; handy https://handy.computer/; kokoro-tts https://huggingface.co/hexgrad/Kokoro-82M; jammable/liner/pixelcut/typecast/wispr-flow: /pricing; undermind https://www.undermind.ai/#pricing
- all 20 | last_checked | -> 2026-10-29

## Verified, no fact change
- undermind: checked with the toggles in real Chrome. Academic Pro $20/month ($16 billed annually); Industry Pro $75/month ($60 annually); Free "Standard rate limits"; Pro "10x higher usage limits". Matches the card.
- typecast: Free 3,000 lifetime credits (~5 mins), attribution required; Basic $5/month, 30,000 credits (~35 mins). Matches.
- draw-things: Free Edition; Community needs a free account; Draw Things+ $8.99/mo. Matches.
- wispr-flow price_from: Pro $15/month, $12 annual. Matches.
- liner price_from: Pro $17.99/month, $14.99 annual. Matches.
- Open-source apps: all still exist, none archived, all free; open_weights and runs_on_your_computer still hold. Licenses seen: spleeter MIT (latest release v2.3.0), buzz MIT (v1.4.5, Apple silicon only on latest, Windows installer unsigned), dia2 Apache-2.0 (English only, 2 min, CUDA 12.8+), diffrhythm-2 Apache-2.0 code and weights (HF Space demo linked), f5-tts code MIT / weights CC-BY-NC, kokoro Apache-2.0 (82M, 8 languages/54 voices), krita GPL-3.0 (6 GB VRAM; online tokens 5,000 for 10 EUR, 15,000 for 28 EUR, do not expire), piper GPL-3.0 ("looking for maintainers" still on page), swarmui MIT (v0.9.8 Beta), vibe MIT (v3.2.2), handy MIT (v0.9.8, free, offline), stemroller (v3.1.1, free, "several minutes"), easy-diffusion (8 GB RAM, 25 GB disk; license forbids sharing content that breaks laws).

unchanged: spleeter, buzz, dia2, diffrhythm-2, draw-things, easy-diffusion, f5-tts, handy, kokoro-tts, krita-ai-diffusion, piper-tts, stemroller, swarmui, typecast, undermind, vibe (only last_checked and watch_out_source added)
unreachable: none
checked: 20/20

Notes for the lead:
- Jammable watch_out sentence 2 (imitating real singers) is not on the pricing page; kept as before.
- krita watch_out online-token sentence is on https://www.interstice.cloud/service, not the GitHub page cited.
- Vibe "speed depends on your computer" is general, not a quoted line on the README.
- handy: only an Apple silicon download button shows on handy.computer; GitHub says Windows, macOS, Linux. Card unchanged.
- stemroller GitHub license field shows NOASSERTION; README says Unlicense or MIT No Attribution. Easy Diffusion likewise. Both still free.

## Question-page ripples
None. Searched data/questions.json (title, intro, meta_description) for Jammable, Liner, Pixelcut and Wispr Flow. No sentence mentions the old 100,000+ voices, Liner's credits, Pixelcut's $10 price, or Wispr's phone cap. Wispr Flow appears on no page text.
