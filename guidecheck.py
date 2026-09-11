#!/usr/bin/env python3
"""Guidelines final-pass checks on the built dist/. Stdlib only."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")

issues = []

# A: no outline:none without replacement
css = open(os.path.join(ROOT, "static", "style.css"), encoding="utf-8").read()
if re.search(r"outline\s*:\s*none", css):
    issues.append("A: outline:none found in CSS")
# B: no transition:all
if re.search(r"transition\s*:\s*all", css):
    issues.append("B: transition:all found in CSS")
# C: literal ... in visible copy (guidelines: use ellipsis char)
for dp, _, fs in os.walk(DIST):
    for f in fs:
        if f.endswith(".html"):
            p = os.path.join(dp, f)
            src = open(p, encoding="utf-8").read()
            # strip tags, look for ... in text
            text = re.sub(r"<[^>]+>", " ", src)
            if "..." in text:
                issues.append("C: literal ... in %s" % os.path.relpath(p, DIST))
# D: duplicate ids per page
for dp, _, fs in os.walk(DIST):
    for f in fs:
        if f.endswith(".html"):
            p = os.path.join(dp, f)
            src = open(p, encoding="utf-8").read()
            ids = re.findall(r'id="([^"]+)"', src)
            dup = sorted({i for i in ids if ids.count(i) > 1})
            if dup:
                issues.append("D: duplicate ids %s in %s" % (dup, os.path.relpath(p, DIST)))
# E: heading order
for dp, _, fs in os.walk(DIST):
    for f in fs:
        if f.endswith(".html"):
            p = os.path.join(dp, f)
            src = open(p, encoding="utf-8").read()
            hs = [int(m) for m in re.findall(r"<h([1-6])[\s>]", src)]
            if not hs or hs[0] != 1:
                issues.append("E: no h1 first in %s %s" % (os.path.relpath(p, DIST), hs[:4]))
            if any(b - a > 1 for a, b in zip(hs, hs[1:])):
                issues.append("E: heading skip in %s %s" % (os.path.relpath(p, DIST), hs[:6]))

print("guideline issues: %d" % len(issues))
for i in issues[:30]:
    print(i)
sys.exit(1 if issues else 0)
