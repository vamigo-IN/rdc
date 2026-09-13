#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build step: regenerate service pages, then stamp a fresh ?v=<version> on every
stylesheet/script link across ALL pages so browsers never serve a stale asset
after a deploy. Run this before zipping/deploying (instead of the generator alone)."""
import re, time, glob, subprocess, os

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

VERSION = str(int(time.time()))

# 1) regenerate the 5 service pages
subprocess.run(["python3", "_generate-service-pages.py"], check=True)

# 2) stamp ?v=VERSION on the css + js links in every html file (idempotent)
files = glob.glob("*.html") + glob.glob("*/index.html")
for f in files:
    s = open(f, encoding="utf-8").read()
    s = re.sub(r'/assets/css/styles\.css(\?v=\d+)?', f'/assets/css/styles.css?v={VERSION}', s)
    s = re.sub(r'/assets/js/main\.js(\?v=\d+)?', f'/assets/js/main.js?v={VERSION}', s)
    open(f, "w", encoding="utf-8").write(s)

print(f"built version {VERSION}, stamped {len(files)} html files")
