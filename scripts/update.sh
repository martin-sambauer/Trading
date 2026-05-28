#!/bin/bash
# Trading Journal Update Script
# Verwendung: cd ~/Documents/Trading && ./scripts/update.sh "Kommentar"

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
GDRIVE_DIR="$HOME/Google Drive/My Drive/Trading"
COMMENT=${1:-"Daily update $(date +%Y-%m-%d)"}

echo "Trading Journal Update..."

echo "Sync zu Google Drive..."
rsync -av --exclude='.git' "$REPO_DIR/" "$GDRIVE_DIR/"

echo "Push zu GitHub..."
cd "$REPO_DIR"
git add -A
git commit -m "$COMMENT"
git push origin main

echo "Fertig! GitHub + Google Drive aktualisiert."
