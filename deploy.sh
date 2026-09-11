#!/bin/bash
# deploy.sh — verify then publish the ai-guide site. Usage: bash deploy.sh "<commit msg>"
# 1 build  2 link+parse check  3 commit+push main  4 force-push dist to gh-pages  5 probe live URL
set -euo pipefail; cd "$(dirname "$0")"; MSG="${1:-update}"
g() { git -c user.name=primary-helper -c user.email=alltechkev@gmail.com "$@"; }
rm -rf dist; python3 build.py
python3 - <<'PY'
import html.parser,pathlib,json,sys
root=pathlib.Path('dist'); files=list(root.rglob('*.html')); bad=[]; n=0
class P(html.parser.HTMLParser):
    def __init__(s): super().__init__(); s.l=[]
    def handle_starttag(s,t,a):
        d=dict(a); s.l+=[d[k] for k in('href','src') if d.get(k)]
for f in files:
    p=P(); p.feed(f.read_text())
    for l in p.l:
        n+=1
        if l.startswith(('http','mailto','#')): continue
        t=(f.parent/l.split('#')[0].split('?')[0]).resolve()
        if t.is_dir(): t=t/'index.html'
        if not t.exists(): bad.append((str(f),l))
d=json.load(open('data/providers.json')); assert len({p['id'] for p in d})==len(d), 'dup ids'
print(f'CHECK {len(files)} pages, {n} links, {len(bad)} broken, {len(d)} providers'); sys.exit(1 if bad else 0)
PY
git add -A; g commit -qm "$MSG" || true; git push -q origin main
rm -rf /tmp/ai-guide-pages; cp -R dist /tmp/ai-guide-pages; cd /tmp/ai-guide-pages; touch .nojekyll
git init -q -b gh-pages; g add -A; g commit -qm "deploy $(date +%Y-%m-%d-%H%M)"; git push -q -f https://github.com/Kevthetech143/ai-guide.git gh-pages
sleep 40; printf 'LIVE HTTP %s\n' "$(curl -s -o /dev/null -w '%{http_code}' https://kevthetech143.github.io/ai-guide/)"
