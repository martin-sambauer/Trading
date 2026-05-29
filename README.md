<!-- Version: 1.3 | Letzte Änderung: 2026-05-28 -->
# Trading Journal — Martin & Katya Sambauer

## Technisches Setup & Wiederherstellung
Bei Computerausfall oder neuem Gerät: siehe `TECHSTACK.md` — komplette Schritt-für-Schritt Anleitung.

---

## Für KI-Agenten: Lies das zuerst
Dieses Repository ist das zentrale Gehirn des Trading-Entwicklungssystems von Martin und Katya Sambauer.
Alles ist so dokumentiert dass du als KI sofort einspringen und nahtlos weiterarbeiten kannst.

### Pflichtlektüre vor jeder Session
1. Diese README — Kontext, Logistik, aktueller Stand
2. `method/METHOD.md` — die Handelsmethode
3. `method/TERMINOLOGY.md` — alle Begriffe
4. `method/HYPOTHESES.md` — aktuelle Verhaltens-Hypothesen
5. `data/traders/martin/master_stats.csv` — Martins aggregierte Performance
6. `data/traders/katya/master_stats.csv` — Katyas aggregierte Performance (sobald vorhanden)
7. Letzter Report in `reports/martin/` oder `reports/katya/`

### KI-Anweisungen pro Session-Typ
- **Martin solo:** Lies `data/traders/martin/` und erstelle Report in `reports/martin/`
- **Katya solo:** Lies `data/traders/katya/` und erstelle Report in `reports/katya/`
- **Vergleich:** Lies beide Ordner und erstelle zusätzlich Report in `reports/comparison/`
- **Immer:** Nach jeder Session README, METHOD.md, TERMINOLOGY.md, HYPOTHESES.md updaten falls neue Erkenntnisse

---

## Die Trader

### Martin Sambauer
- Aktiver Daytrader, Papertrading zur Methodenentwicklung
- Ziel: Eigene analytisch beschriebene Methode entwickeln
- Hauptinstrument: USTEC, GER40 morning session
- Typische Handelszeiten: 07:00–09:00 (GER40), 11:00–14:00 (USTEC), 16:30–17:30 (US30/SPX)
- GitHub: martin-sambauer
- Lokales Repo: `~/Documents/Trading`
- Google Drive Screenshots: `~/Google Drive/Trading_Journal/Screenshots/`

### Katya Sambauer
- Aktive Traderin, eigenes Setup parallel zu Martin
- Ziel: Parallele Datenerfassung für Verhaltensvergleich
- Instrumente: wird dokumentiert sobald bekannt
- GitHub: wird als Collaborator hinzugefügt
- Lokales Repo: `~/Documents/Trading` (geklont vom selben Repo)
- Google Drive Screenshots: eigener Ordner (wird konfiguriert)

---

## Trading-Setup (beide Trader)
- **Plattform:** TradingView (Charts + Ausführung) + TradeNation / Forex.com (Broker)
- **Timeframes:** 1D (links, Kontext/Bias) + 5M (rechts, Einstieg/Ausführung)
- **Indikatoren:** BB 20, SMA20, SMA200, PDH/PDL, PWH/W

### Gehandelte Instrumente
| Symbol | TradingView | Broker | Typische Session |
|--------|-------------|--------|-----------------|
| USTEC | TRADENATION:USTEC | TradeNation | 11:00–14:00 Uhr |
| US30 | FOREXCOM:US30 | Forex.com | 16:30–17:30 Uhr |
| GER40 | FOREXCOM:GER40 | Forex.com | 07:00–09:00 Uhr |
| SPX | TVC:SPX | TradingView | 16:30–17:30 Uhr |
| JAPAN225 | — | — | Gelegentlich |

### Kontext-Indikatoren (nicht getradet)
| Symbol | Zweck |
|--------|-------|
| OILGAS | Antizyklischer Indikator |

---

## Projektstruktur
```
Trading/
├── README.md                          ← Du bist hier (v1.3)
├── CHANGELOG.md                       ← Alle Änderungen
├── TECHSTACK.md                       ← Komplettes technisches Setup
├── KATYA_ONBOARDING.md                ← Anleitung für Katya
├── method/
│   ├── METHOD.md                      ← Handelsmethode (lebendes Dokument)
│   ├── TERMINOLOGY.md                 ← Alle Begriffe
│   └── HYPOTHESES.md                  ← Verhaltens-Hypothesen
├── data/
│   ├── traders/
│   │   ├── martin/
│   │   │   ├── trades/YYYY-MM-DD.csv  ← Tägliche Trades
│   │   │   ├── market/YYYY-MM-DD_SYMBOL.csv ← 5M Kerzen
│   │   │   ├── exports/               ← Rohe TradingView Exports
│   │   │   └── master_stats.csv       ← Aggregierte Stats
│   │   └── katya/
│   │       ├── trades/YYYY-MM-DD.csv
│   │       ├── market/YYYY-MM-DD_SYMBOL.csv
│   │       ├── exports/
│   │       └── master_stats.csv
├── reports/
│   ├── martin/
│   │   └── YYYY-MM-DD/
│   │       ├── report.html            ← Täglicher Report
│   │       └── report_standalone.html ← Standalone mit eingebetteten Bildern
│   ├── katya/
│   │   └── YYYY-MM-DD/
│   │       ├── report.html
│   │       └── report_standalone.html
│   └── comparison/
│       └── YYYY-MM-DD/
│           └── report.html            ← Vergleichsreport beide Trader
├── screenshots/
│   ├── martin/                        ← Martins komprimierte Charts
│   └── katya/                         ← Katyas komprimierte Charts
└── scripts/
    ├── update.sh                      ← Tägliches Push-Script
    └── fetch_market_data.py           ← Marktdaten-Download
```

**Hinweis:** Übergangsweise liegen Martins Daten noch in `data/trades/`, `data/market/` und `reports/2026-05-28/` — werden beim nächsten Cleanup in die neue Struktur migriert.

---

## Account-System
| Account-Typ | Beschreibung |
|-------------|-------------|
| `paper` | Papertrading — kein echtes Geld |
| `live` | Live-Account — echtes Geld |

Jeder Trade hat eine `account_id` Spalte. P&L-Vergleiche nur innerhalb desselben Account-Typs.

---

## Dubletten-Regel
Jeder Trade ist eindeutig durch `Datum + Zeit + Symbol + Trader`.
Beim Einlesen neuer Daten werden bestehende Einträge nie überschrieben — nur ergänzt.

---

## Täglicher Workflow

### Was jeder Trader liefert
1. **Balance History CSV** — TradingView → Paper Trading → Balance History → Export
2. **Order History CSV** — TradingView → Paper Trading → Order History → Export
3. **Screenshots** — `Cmd+Shift+4` mit sichtbaren Execution Marks, in Google Drive ablegen
4. **Kommentare** — Beobachtungen, Entscheidungsgründe

### Was die KI macht
1. Daten parsen → Trade-Tabelle + master_stats.csv updaten
2. Tagesreport HTML erstellen (5 Seiten: Dashboard, Sessions, Trades, Behaviour, Methode)
3. Standalone Report mit eingebetteten Screenshots generieren
4. Falls beide Trader Daten geliefert haben → Vergleichsreport erstellen
5. Methode / Terminologie / Hypothesen updaten falls neue Erkenntnisse
6. CHANGELOG updaten
7. README Status updaten

### Screenshot-Konvention
- **Execution Marks aktivieren:** Chart-Einstellungen → Tab "Trading" → "Executions"
- **Broker verbinden:** TradeNation für USTEC, Forex.com für US30/GER40
- **Screenshot:** `Cmd+Shift+4` (zeigt Execution Marks, TradingView Kamera-Button nicht)
- **Benennung:** automatisch durch Mac `Screenshot YYYY-MM-DD at HH.MM.SS.png` oder TradingView `SYMBOL_DATUM.png`

### Report öffnen
```bash
open -a Firefox ~/Documents/Trading/reports/martin/YYYY-MM-DD/report_standalone.html
```
**Hinweis:** Firefox verwenden — Chrome blockiert Base64-Bilder bei lokalen Dateien.

---

## Vergleichsreport (Martin vs. Katya)
Wenn beide Trader an einem Tag gehandelt haben, erstellt die KI einen Vergleichsreport mit:
- P&L Vergleich side-by-side
- Win Rate Vergleich
- Behaviour Pattern Vergleich (wer macht welche Fehler häufiger?)
- Methoden-Abweichungen (gleicher Markt, gleiche Zeit — unterschiedliche Entscheidungen?)
- Live vs. Paper Vergleich (falls relevant)

---

## Täglicher Push (ein Befehl)
```bash
cd ~/Documents/Trading && python3 scripts/fetch_market_data.py && ./scripts/update.sh "$(date +%Y-%m-%d) session close"
```

---

## CSV-Formate

### Balance History
```
Time, Balance before, Balance after, Realized PnL (value), Realized PnL (currency), Action
```

### Order History (für Intentions-Analyse)
```
Symbol, Side, Type, Quantity, Limit price, Stop price, Fill price, Status, Commission, Placing time, Closing time, Order ID
```
Enthält auch gecancelte Orders → zeigt Spike Catcher und ursprüngliche Intention.

---

## Aktueller Status
- **Letztes Update:** 2026-05-28
- **Trading-Tage dokumentiert:** 1 (Martin), 0 (Katya)
- **Methode Version:** 0.1
- **README Version:** 1.3
- **Dokumentierte Behaviour Patterns:** 2
- **Offene Hypothesen:** 4 (H1–H4)
- **Martin Kontostand:** $17,348.87 (Start: $10,000 am 2026-05-28)
- **Katya Kontostand:** noch nicht gestartet
