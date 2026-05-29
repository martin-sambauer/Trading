<!-- Version: 1.1 | Letzte Änderung: 2026-05-28 -->
# Techstack & Setup-Dokumentation
*Komplettes technisches Setup. Nach einem Totalausfall in 30 Minuten wiederhergestellt.*

---

## Voraussetzungen

| Tool | Zweck | Install |
|------|-------|---------|
| macOS 15+ | Betriebssystem | — |
| Git | Versionierung | `xcode-select --install` |
| Node.js 11.16+ | Claude Code | `brew install node` |
| Python3 | Marktdaten-Scripts | vorinstalliert auf macOS |
| pip3 | Python Packages | mit Python3 dabei |
| imagemagick | Screenshot-Komprimierung | `brew install imagemagick` |
| Google Drive App | Screenshot-Sync | drive.google.com/drive/download |

---

## Schritt-für-Schritt Wiederherstellung

### 1. Repo klonen
```bash
cd ~/Documents
git clone https://github.com/trader-journal/Trading.git
cd Trading
```

### 2. Python-Abhängigkeiten installieren
```bash
pip3 install --break-system-packages git+https://github.com/rongardF/tvdatafeed.git pandas
```

### 3. imagemagick installieren
```bash
brew install imagemagick
```

### 4. Git-Zugangsdaten konfigurieren
```bash
git config --global user.name "Trader A"
git config --global user.email "deine@email.com"
git remote set-url origin https://trader-journal:GITHUB_TOKEN@github.com/trader-journal/Trading.git
```
GitHub Personal Access Token: `github.com → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)` → Scope: `repo`

### 5. Google Drive Desktop App installieren
- Download: drive.google.com/drive/download
- Einloggen → Ordner liegt unter `~/Google Drive/`
- Screenshots-Ordner: `~/Google Drive/My Drive/Trading_Journal/Screenshots/`

### 6. Scripts ausführbar machen
```bash
chmod +x ~/Documents/Trading/scripts/update.sh
```

---

## Scripts

### `scripts/update.sh` — Tägliches Push-Script
**Zweck:** Screenshots komprimieren + Google Drive sync + GitHub push — alles in einem Befehl.
```bash
cd ~/Documents/Trading && ./scripts/update.sh "2026-05-29 session close"
```
**Was es tut:**
1. Neue Screenshots aus Google Drive komprimieren (~150KB) und nach `screenshots/` kopieren
2. `rsync` von lokalem Repo nach Google Drive (ohne Screenshots-Ordner)
3. `git add -A` → `git commit` → `git push`

### `scripts/fetch_market_data.py` — Marktdaten-Downloader
**Zweck:** 5M-Kerzen (OHLCV) für alle Instrumente aus TradingView laden.
```bash
python3 ~/Documents/Trading/scripts/fetch_market_data.py --date 2026-05-28
```
**Output:** `data/market/YYYY-MM-DD_SYMBOL.csv`

**Symbole (ohne Login, Fallback-System):**
| Name | Primär | Fallback |
|------|--------|---------|
| USTEC | OANDA:NAS100USD | PEPPERSTONE:USTECH100CFD |
| US30 | PEPPERSTONE:US30 | OANDA:US30 |
| GER40 | PEPPERSTONE:GER40 | OANDA:DE40EUR |
| SPX | OANDA:SPX500USD | PEPPERSTONE:SPX500 |
| JAPAN225 | OANDA:JP225USD | PEPPERSTONE:JAPAN225CFD |
| OILGAS | OANDA:BCOUSD | PEPPERSTONE:USOIL |

### Täglicher Einzel-Befehl (alles zusammen)
```bash
cd ~/Documents/Trading && python3 scripts/fetch_market_data.py && ./scripts/update.sh "$(date +%Y-%m-%d) session close"
```

---

## Screenshot-Workflow

1. In TradingView: **Chart-Einstellungen (Zahnrad) → Tab "Trading" → "Executions" aktivieren**
2. Paper Trading Panel: richtigen Broker verbinden (TradeNation für USTEC, Forex.com für US30/GER40)
3. Kamera-Symbol klicken → Screenshot landet automatisch in `~/Downloads/` mit Name `SYMBOL_DATUM_UHRZEIT_HASH.png`
4. Screenshot nach Google Drive verschieben: `~/Google Drive/My Drive/Trading_Journal/Screenshots/`
5. Beim nächsten `update.sh`: wird automatisch komprimiert und ins Repo gepusht
6. GitHub URL: `https://raw.githubusercontent.com/trader-journal/Trading/main/screenshots/DATEINAME.png`

**Google Drive Screenshots-Ordner (öffentlich lesbar):**
https://drive.google.com/drive/folders/19HLdugzMQdtrNNCW7LL4hU_QvdZnxzp0

---

## Externe Dienste

| Dienst | Zweck | URL | Zugang |
|--------|-------|-----|--------|
| GitHub | Versionierung, Backup, Screenshot-Hosting | github.com/trader-journal/Trading | Personal Access Token |
| Google Drive | Screenshots Original (full-res) | drive.google.com | Google Account |
| TradingView | Charts, Marktdaten, Paper Trading | tradingview.com | Google SSO |

---

## TradingView Broker-Mapping

| Instrument | Broker im Paper Trading Panel |
|------------|------------------------------|
| USTEC | TradeNation |
| US30 | Forex.com |
| GER40 | Forex.com |
| SPX | TVC (kein Broker nötig) |

---

## Bekannte Probleme & Lösungen

| Problem | Lösung |
|---------|--------|
| `git push` fragt nach Passwort | `git remote set-url origin https://USER:TOKEN@github.com/...` |
| Execution Marks nicht sichtbar | Paper Trading Panel → richtigen Broker verbinden |
| tvDatafeed Timeout | Script nochmal ausführen, Fallback-Exchange wird versucht |
| Screenshots nicht im Report | Nach `git push` nochmal laden — GitHub braucht ~30 Sekunden |

---

## Git LFS (Large File Storage)
Screenshots werden via Git LFS gespeichert (installiert mit `brew install git-lfs`).

### Bei Wiederherstellung
```bash
git lfs install
git lfs pull
```

### Korrekte Google Drive Pfade
```
~/Google Drive/Trading_Journal/           ← Hauptordner
~/Google Drive/Trading_Journal/Screenshots/  ← Screenshots
```

### Report lokal öffnen
```bash
open ~/Documents/Trading/reports/YYYY-MM-DD/report.html
```

## Report öffnen
```bash
# Standalone Report (mit eingebetteten Screenshots) generieren:
cd ~/Documents/Trading
python3 << 'EOF'
import base64, re, os
with open('reports/YYYY-MM-DD/report.html', 'r') as f:
    html = f.read()
for f in os.listdir('screenshots'):
    if f.endswith('.png'):
        with open(f'screenshots/{f}', 'rb') as img:
            data = base64.b64encode(img.read()).decode()
        html = html.replace(f'../../screenshots/{f}', f'data:image/png;base64,{data}')
html = re.sub(r' onerror="[^"]*"', '', html)
with open('reports/YYYY-MM-DD/report_standalone.html', 'w') as f:
    f.write(html)
EOF

# In Firefox öffnen (Chrome blockiert Base64 bei lokalen Dateien)
open -a Firefox reports/YYYY-MM-DD/report_standalone.html
```
