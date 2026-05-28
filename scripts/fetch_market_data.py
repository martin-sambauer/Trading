#!/bin/bash
# Trading Journal Update Script v1.2
# Verwendung: cd ~/Documents/Trading && ./scripts/update.sh "Kommentar"

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
GDRIVE_SCREENSHOTS="$HOME/Google Drive/My Drive/Trading_Journal/Screenshots"
REPO_SCREENSHOTS="$REPO_DIR/screenshots"
GDRIVE_DIR="$HOME/Google Drive/My Drive/Trading_Journal"
COMMENT=${1:-"Daily update $(date +%Y-%m-%d)"}

echo "Trading Journal Update..."

# 1. Screenshots komprimieren und ins Repo kopieren
echo "Screenshots komprimieren..."
if command -v convert &> /dev/null; then
    for f in "$GDRIVE_SCREENSHOTS"/*.png; do
        [ -f "$f" ] || continue
        filename=$(basename "$f")
        target="$REPO_SCREENSHOTS/$filename"
        if [ ! -f "$target" ]; then
            convert "$f" -resize 1400x -quality 75 "$target"
            echo "  Komprimiert: $filename"
        fi
    done
else
    echo "  imagemagick nicht installiert — Screenshots werden direkt kopiert"
    cp "$GDRIVE_SCREENSHOTS"/*.png "$REPO_SCREENSHOTS/" 2>/dev/null
fi

# 2. Google Drive sync
echo "Sync zu Google Drive..."
rsync -av --exclude='.git' --exclude='screenshots/' "$REPO_DIR/" "$GDRIVE_DIR/" 2>/dev/null

# 3. GitHub push
echo "Push zu GitHub..."
cd "$REPO_DIR"
git add -A
git commit -m "$COMMENT"
git push origin main

echo "Fertig! GitHub + Google Drive aktualisiert."