#!/bin/bash
# Trading Journal Update Script v2.1
# Verwendung: cd ~/Documents/Trading && ./scripts/update.sh [YYYY-MM-DD] [trader] [kommentar]

set -e
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

DATE=${1:-$(date +%Y-%m-%d)}
TRADER=${2:-martin}
COMMENT=${3:-"Daily update $DATE"}

# Google Drive — korrekter Pfad
GDRIVE_BASE="$HOME/Library/CloudStorage/GoogleDrive-arthurdigbysellers2@googlemail.com/My Drive"
GDRIVE_SCREENSHOTS="$GDRIVE_BASE/Trading_Journal/Screenshots"
REPO_SCREENSHOTS="$REPO_DIR/screenshots"

echo "================================================"
echo "Trading Journal Update v2.1"
echo "Datum:  $DATE"
echo "Trader: $TRADER"
echo "================================================"

# 1. Marktdaten holen
echo ""
echo "[1/4] Marktdaten holen..."
python3 scripts/fetch_market_data.py "$DATE"

# 2. Trades parsen → master_trades.csv + master_stats.csv
echo ""
echo "[2/4] Trades parsen..."
python3 scripts/parse_trades.py "$DATE" "$TRADER"

# 3. Screenshots komprimieren
echo ""
echo "[3/4] Screenshots..."
if [ -d "$GDRIVE_SCREENSHOTS" ]; then
    if command -v magick &> /dev/null; then
        CONVERT_CMD="magick"
    elif command -v convert &> /dev/null; then
        CONVERT_CMD="convert"
    else
        CONVERT_CMD=""
    fi

    COUNT=0
    for f in "$GDRIVE_SCREENSHOTS"/*.png "$GDRIVE_SCREENSHOTS"/*.jpg; do
        [ -f "$f" ] || continue
        filename=$(basename "$f")
        target="$REPO_SCREENSHOTS/$filename"
        if [ ! -f "$target" ]; then
            if [ -n "$CONVERT_CMD" ]; then
                $CONVERT_CMD "$f" -resize 1400x -quality 75 "$target"
            else
                cp "$f" "$target"
            fi
            echo "  → $filename"
            COUNT=$((COUNT + 1))
        fi
    done
    if [ $COUNT -eq 0 ]; then
        echo "  Keine neuen Screenshots"
    else
        echo "  $COUNT Screenshots verarbeitet"
    fi
else
    echo "  Google Drive nicht gefunden: $GDRIVE_SCREENSHOTS"
fi

# 4. Master Report neu generieren
echo ""
echo "[4/4] Reports + Git push..."
python3 scripts/generate_reports.py 2>/dev/null && echo "  Reports regeneriert" || echo "  Report-Generator nicht gefunden, übersprungen"

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
