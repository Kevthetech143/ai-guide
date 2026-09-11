# AI Guide — plain-language AI-provider guide site

Static site. Python 3 stdlib only — no pip, no frameworks, no external
JS/CSS/fonts, no tracking.

## Layout

- `data/providers.json` — the provider data (from task ai-guide-001a)
- `templates/` — `string.Template` HTML templates (`$name` placeholders)
- `static/style.css` — mobile-first plain CSS
- `build.py` — the builder

## How to run

```
python3 build.py
```

Reads `data/providers.json` + `templates/`, writes `dist/`:

- `dist/index.html` — hero "Which AI should I use?", category tiles, all provider cards
- `dist/<category>/index.html` — one page per category
- `dist/p/<id>.html` — one page per provider
- `dist/sitemap.xml`, `dist/robots.txt`
- `dist/static/` — copied from `static/`

All internal links are relative (the site is served under `/ai-guide/`).
The sitemap uses the absolute base URL `https://kevthetech143.github.io/ai-guide/`.

## Data not present?

If `data/providers.json` is missing, the builder fails loudly with a
`FileNotFoundError` — that is intentional: sample data must never be written
into `data/`. To smoke-test the builder without real data, point `DATA` at a
scratch copy elsewhere.
