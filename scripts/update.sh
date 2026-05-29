#!/bin/bash
# Trading Journal Update Script v2.0
# Verwendung: cd ~/Documents/Trading && ./scripts/update.sh [YYYY-MM-DD] [trader] [kommentar]
# Defaults: heutiges Datum, martin, "Daily update DATUM"

set -e
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

DATE=${1:-$(date +%Y-%m-%d)}
TRADER=${2:-martin}
COMMENT=${3:-"Daily update $DATE"}

GDRIVE_SCREENSHOTS="$HOME/Google Drive/My Drive/Trading_Journal/Screenshots"
REPO_SCREENSHOTS="$REPO_DIR/screenshots"

echo "================================================"
echo "Trading Journal Update"
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

    for f in "$GDRIVE_SCREENSHOTS"/*.png "$GDRIVE_SCREENSHOTS"/*.jpg; do
        [ -f "$f" ] || continue
        filename=$(basename "$f")
        target="$REPO_SCREENSHOTS/$filename"
        if [ ! -f "$target" ]; then
            if [ -n "$CONVERT_CMD" ]; then
                $CONVERT_CMD "$f" -resize 1400x -quality 75 "$target"
                echo "  Komprimiert: $filename"
            else
                cp "$f" "$target"
                echo "  Kopiert (imagemagick fehlt): $filename"
            fi
        fi
    done
    echo "  Screenshots: fertig"
else
    echo "  Google Drive Screenshots Ordner nicht gefunden, übersprungen"
fi

# 4. Git push
echo ""
echo "[4/4] Git push..."
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
