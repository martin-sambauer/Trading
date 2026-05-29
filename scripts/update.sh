#!/bin/bash
# Trading Journal Update Script v2.2
# Verwendung: cd ~/Documents/Trading && ./scripts/update.sh [YYYY-MM-DD] [trader] [kommentar]

set -e
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

DATE=${1:-$(date +%Y-%m-%d)}
TRADER=${2:-martin}
COMMENT=${3:-"Daily update $DATE"}

GDRIVE_BASE="$HOME/Library/CloudStorage/GoogleDrive-arthurdigbysellers2@googlemail.com/My Drive"
GDRIVE_SCREENSHOTS="$GDRIVE_BASE/Trading_Journal/Screenshots"
REPO_SCREENSHOTS="$REPO_DIR/screenshots"

echo "================================================"
echo "Trading Journal Update v2.2"
echo "Datum:  $DATE"
echo "Trader: $TRADER"
echo "================================================"

# 1. Marktdaten holen
echo ""
echo "[1/4] Marktdaten holen..."
python3 scripts/fetch_market_data.py "$DATE"

# 2. Trades parsen (master_trades.csv nur)
echo ""
echo "[2/4] Trades parsen..."
python3 scripts/parse_trades.py "$DATE" "$TRADER"

# 3. Screenshots kopieren
echo ""
echo "[3/4] Screenshots..."
if [ -d "$GDRIVE_SCREENSHOTS" ]; then
    COUNT=0
    for f in "$GDRIVE_SCREENSHOTS"/*.png "$GDRIVE_SCREENSHOTS"/*.jpg; do
        [ -f "$f" ] || continue
        filename=$(basename "$f")
        target="$REPO_SCREENSHOTS/$filename"
        if [ ! -f "$target" ]; then
            cp "$f" "$target"
            echo "  -> $filename"
            COUNT=$((COUNT + 1))
        fi
    done
    echo "  $COUNT Screenshots verarbeitet"
else
    echo "  Google Drive nicht gefunden"
fi

# 4. Screenshots in bestehende HTML-Reports einbetten
# WICHTIG: Ueberschreibt NICHT den HTML-Inhalt — bettet nur Screenshots ein
echo ""
echo "[4/4] Reports + Git push..."
python3 scripts/embed_screenshots.py && echo "  Screenshots eingebettet" || echo "  embed_screenshots.py nicht gefunden, uebersprungen"

git add -A

if git diff --cached --quiet; then
    echo "  Nichts zu committen"
else
    git commit -m "$COMMENT"
    git push origin main
    echo "  Gepusht: $COMMENT"
fi

echo ""
echo "================================================"
echo "Fertig!"
echo "================================================"
