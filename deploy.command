#!/bin/bash
# Roots Dental Care — one-click deploy.
# Refreshes the site from the latest zip Claude dropped, then pushes live.
cd "$(dirname "$0")/.." || exit 1
if [ -f rdc-latest.zip ]; then
  echo "Refreshing site files from rdc-latest.zip ..."
  unzip -oq rdc-latest.zip
fi
cd roots-dental-care || exit 1
git add -A
git commit -m "site update $(date '+%Y-%m-%d %H:%M')" 2>/dev/null || echo "(no changes to commit)"
git push
echo ""
echo "Pushed. Hostinger will redeploy in about a minute."
echo "You can close this window."
