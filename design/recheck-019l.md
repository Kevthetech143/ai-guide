# recheck-019l (batch 24, 20 oldest cards, checked 2026-11-13/13)

## Changes
- taskade | price_from | "Free (Starter $6/month, billed yearly only; Pro $20/month, or $10/month billed yearly)" -> "Free (Starter $6/month, billed yearly; Pro $10/month, billed yearly)" | https://www.taskade.com/pricing | "Pro $10 /mo Yearly $120 billed yearly"; the page now shows only yearly rates, no monthly Pro price anywhere, so the old "$20/month" monthly Pro price could not be verified and was dropped (never guessed)
- taskade | watch_out | "...unlimited agents and automations need the Pro plan at $20/month on monthly billing." -> "The free plan covers 2 people, 3 live apps and 1 AI agent. Starter ($6/month, billed yearly at $72) gives unlimited apps and 3 agents; unlimited agents and automations need the Pro plan at $10/month, billed yearly at $120." | https://www.taskade.com/pricing | compare table: Free 3 live apps, 1 agent, 2 people; "Starter $72 billed yearly", "Pro Unlimited AI agents / Unlimited automations ... $120 billed yearly"
- wangp | good_for | "...Wan 2.2, LTX-2, Qwen Image, Flux and ACE-Step..." -> "...Wan 2.2, LTX 2.5, Qwen Image, Flux 3 Klein and ACE-Step..." | https://wangp.ai/ | model list: "LTX 2.5, Wan 2.1 / 2.2, Qwen Image / 2.1, Flux 3 Klein, ACE-Step"
- adobe-firefly | watch_out_source | https://www.adobe.com/products/firefly.html -> https://www.adobe.com/products/firefly/plans.html | the plans page is where the $9.99 Standard / 2,000 credits fact is shown
- all 20 | last_checked | -> 2026-11-13

## Verified, no change (key facts seen on the official page)
- mage-space: Basic $10/mo, 500 gems; Pro $30 adds unlimited video + ControlNet (mage.space/membership)
- magenta-realtime: MRT2 open weights, Apple Silicon, Base needs M3 Pro/M2 Max, Small any, ~2.5GB/450MB (magenta.withgoogle.com/mrt2)
- researchrabbit: Free 50 seed articles; RR+ $12.5 monthly, $10 annual, 300 seed articles (researchrabbit.ai/pricing)
- scenario: Free 50 credits/day no card; Starter $15 1,500 credits private generations; Pro $45 train custom models + unlimited relaxed (scenario.com/pricing)
- screenpipe: monthly toggle clicked in the browser: Basic "$25 / month, or $250/yr annually"; Free "search recent work" (screenpipe.com/pricing)
- sd-next: Apache-2.0, last push 2026-11-13, not archived, README lists Nvidia/AMD/Intel Arc/Apple M1/M2/CPU. No GitHub "releases" are published (API says none), so no version name to report.
- stockimg-ai: Starter $12/mo 300 credits; Premium $24; Ultra $48 unlimited credits (stockimg.ai/pricing)
- viggle: Free (1 at a time, 7-day storage), Pro list $9.99/mo (page default shows yearly $7.99, "Was $9.99"), 80 credits, no watermark; Live $19.99 all models (viggle.ai/pricing). Unverified: the "5 videos a day" in good_for (page only says 5 daily free credits).
- wan-2-2: Apache-2.0, last push 2026-09-21, not archived, README "80GB VRAM" for main commands and "24GB (e.g. RTX 4090)" for 5B; hosted create.wan.video Pro $10/mo billed monthly ($5 billed yearly)
- wangp: "Free to run locally under its Community License", paid hosting/SaaS needs permission, "select models start at 6 GB of VRAM" (wangp.ai)
- adobe-firefly: Standard $9.99/mo 2,000 credits; free daily generations. Black Friday promo on Pro/Pro Plus (ends Dec 6): list prices kept ($19.99 / $49.99); cheapest paid plan unaffected.
- anara: Plus $10 ($8 yearly), Max 5x $100 with Deep Search, free 20MB/120 pages (anara.com/pricing)
- brave-search: help page confirms ads + Premium ad-free + Brave browser only; price is not on that page, so I read the official checkout page account.brave.com/?intent=checkout&product=search: "$3.00 /month", annual "$2.50 /month, $29.99 /year" (no sign-in)
- capcut-ai: Pro $19.99/month, 1,200 credits, 1 TB. Note: the page also lists a team plan at about $12/seat/month; kept Pro as the individual paid plan.
- chatgpt: Free $0, Go $8/month "may include ads", Plus $20, Pro from $100 (chatgpt.com/pricing)
- claude: Free; Pro "$17 per month with annual ... $20 if billed monthly" (claude.com/pricing)
- claude-code: Free plan row says Claude Code "No"; Pro $20/$17 (claude.com/pricing)
- ecosia: Free $0, Starter $7.99, Pro $14.99, daily limits (ecosia.org/pricing, browser). Flag for lead: the watch_out sentence "You can try AI Chat without signing in" is not on the pricing page (it shows "Create an account"); left unchanged since I could not disprove it.
- fellou: Free 1000 sparks/2 scheduled tasks; Plus $19, $16 yearly, 2000 sparks (fellou.ai/pricing)

unchanged: mage-space, magenta-realtime, researchrabbit, scenario, screenpipe, sd-next, stockimg-ai, viggle, wan-2-2, anara, brave-search, capcut-ai, chatgpt, claude, claude-code, ecosia, fellou (date only; adobe-firefly source URL only)
unreachable: none (adobe and ecosia block curl with 403 but render in real Chrome)
shut down: none
checked: 20/20

## Question-page ripples
None. Searched data/questions.json for Taskade, WanGP, Adobe Firefly: no sentence states Taskade's price or free limits (slugs with Taskade only name it as an automation/agent tool), WanGP's model list, or Firefly's price. Nothing to fix.

Browser: session ag019l closed; `pgrep -f pw-aiguide-recheck` printed nothing.
Watch items seen: Adobe Black Friday promo (above). Others not seen.


LEAD NOTE 2026-11-13: taskade changes above were REVERTED by Fable (monthly Pro $20 exists behind the Yearly toggle); taskade is date-only. All dates corrected to 2026-11-13. See review-019l.md.
