#!/usr/bin/env bash
# Publier le blog : .md + INDEX.md, puis ./deploy/publish.sh
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/gen.py
python3 tools/seal.py && python3 tools/seal.py
python3 tools/seal.py --verify
git add -A
git commit -q -m "publish $(date +%F-%H%M) [skip ci]" || echo "rien de nouveau"
git pull --rebase -q origin main 2>/dev/null || true
git push -u origin main
echo "publié → https://blog.noirebox.eu"
