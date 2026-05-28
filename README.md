<!-- Version: 1.1 | Letzte Änderung: 2026-05-28 -->
# Trading Journal — Martin Sambauer

## Für KI-Agenten: Lies das zuerst
Dieses Repository ist das zentrale Gehirn des Trading-Entwicklungssystems von Martin Sambauer.
Alles ist so dokumentiert dass du als KI sofort einspringen und nahtlos weiterarbeiten kannst.

### Pflichtlektüre vor jeder Session
1. Diese README — Kontext, Logistik, aktueller Stand
2. `method/METHOD.md` — die Handelsmethode
3. `method/TERMINOLOGY.md` — alle Begriffe
4. `method/HYPOTHESES.md` — aktuelle Verhaltens-Hypothesen
5. `data/master/master_stats.csv` — aggregierte Performance über alle Tage
6. Letzter Report in `reports/` — was zuletzt besprochen wurde

---

## Wer ist Martin?
- Aktiver Daytrader, Papertrading-Phase zur Methodenentwicklung
- Ziel: Eine eigene, analytisch beschriebene Handelsmethode entwickeln die so gut dokumentiert ist, dass sie ein Fremder ausführen könnte
- Ansatz: Daten-getriebenes Selbstverständnis — er will sein eigenes Verhalten verstehen und verbessern
- Sprache: Deutsch

---

## Trading-Setup
- **Plattform:** TradingView (Charts) + SelfInvest / TradeNation (Ausführung)
- **Konto:** Papertrading, Startkapital $10.000 (28.05.2026)
- **Timeframes:** 1D (links, Kontext/Bias) + 5M (rechts, Einstieg/Ausführung)
- **Indikatoren:** BB 20, SMA20, SMA200, PDH/PDL, PWH/W

### Gehandelte Instrumente
| Symbol | Name | Typische Session |
|--------|------|-----------------|
| USTEC | US Tech 100 CFD | 11:00–14:00 Uhr (Hauptinstrument) |
| US30 | Dow Jones CFD | 15:30–17:30 Uhr |
| GER40 | DAX CFD | 07:00–09:00 Uhr |
| SPX | S&P 500 CFD | 15:30–17:30 Uhr |
| JAPAN225 | Nikkei CFD | Gelegentlich |

### Kontext-Indikatoren (nicht getradet)
| Symbol | Zweck |
|--------|-------|
| OILGAS | Antizyklischer Indikator — läuft oft gegenläufig zu Aktienindizes |

---

## Täglicher Workflow

### Was Martin liefert
1. **Balance History CSV** — Export aus TradingView (Papertrading Konto → History → Export)
2. **TradingView Screenshots** — Kamera-Symbol in TradingView, werden automatisch benannt: `SYMBOL_DATUM_UHRZEIT.png`
3. **Kommentare** — was er beobachtet hat, warum er bestimmte Entscheidungen getroffen hat

### Was die KI macht
1. Balance History parsen → Trade-Tabelle erstellen
2. Trades kategorisieren (Phase, Symbol, Behaviour Pattern)
3. Tagesreport erstellen (`reports/YYYY-MM-DD/report.md`)
4. `data/master/master_stats.csv` um den neuen Tag erweitern
5. `data/trades/YYYY-MM-DD.csv` anlegen
6. Hypothesen überprüfen und updaten (`method/HYPOTHESES.md`)
7. Methode verfeinern falls neue Erkenntnisse (`method/METHOD.md`)
8. Terminologie ergänzen falls neue Begriffe (`method/TERMINOLOGY.md`)
9. Diese README updaten (Status, letztes Update)

### Screenshot-Konvention
- **Speicherort:** Google Drive → My Drive → Trading_Journal → Screenshots
- **Benennung:** automatisch durch TradingView: `SYMBOL_YYYY-MM-DD_HH-MM-SS.png`
- **Typen:** Jeder Screenshot bekommt im Report einen Typ:
  - `TRADE` — wurde an diesem Tag getradet
  - `CONTEXT` — Kontext-Indikator (z.B. Öl)
  - `WATCH` — beobachtet, nicht getradet

---

## Projektstruktur
```
Trading/                             ← lokaler Ordner: ~/Documents/Trading
├── README.md                        ← Du bist hier — immer aktuell halten
├── method/
│   ├── METHOD.md                    ← Handelsmethode (lebendes Dokument)
│   ├── TERMINOLOGY.md               ← Alle Begriffe definiert
│   └── HYPOTHESES.md                ← Verhaltens-Hypothesen
├── data/
│   ├── trades/
│   │   └── YYYY-MM-DD.csv           ← Tägliche Rohdaten (eine Datei pro Tag)
│   └── master/
│       └── master_stats.csv         ← Aggregierte Tabelle, wächst täglich
├── reports/
│   └── YYYY-MM-DD/
│       └── report.md                ← Täglicher Analyse-Report
├── screenshots/                     ← Platzhalter (echte Files auf Google Drive)
└── scripts/
    └── update.sh                    ← Tägliches Push-Script
```

### Speicherorte
| Was | Wo |
|-----|-----|
| Methode, Stats, Reports, CSVs | GitHub: github.com/martin-sambauer/Trading |
| Screenshots, Videos | Google Drive: My Drive/Trading_Journal/Screenshots/ |
| Lokale Arbeitskopie | ~/Documents/Trading |

---

## Tägliches Push-Script
```bash
cd ~/Documents/Trading && ./scripts/update.sh "YYYY-MM-DD update"
```
Dieses Script pusht automatisch zu GitHub UND synct zu Google Drive.

---

## CSV-Format (Balance History aus TradingView)
```
DATUM UHRZEIT  VORHER    NACHHER   DELTA    WÄHRUNG  BESCHREIBUNG
2026-05-28 17:03:31  17,461.32  17,498.32  +37.00  USD  Close long position for symbol...
```
Die KI parst dieses Format und extrahiert: Symbol, Richtung, Einheiten, Entry, Exit, P&L, Kommission.

---

## Aktueller Status
- **Letztes Update:** 2026-05-28
- **Trading-Tage dokumentiert:** 1
- **Aktuelle Methode Version:** 0.1
- **Dokumentierte Behaviour Patterns:** 2 (FOMO Top Scale, Context Switch Exit)
- **Offene Hypothesen:** 3 (H1, H2, H3)
- **Kontostand:** $17,348.87 (Start: $10,000)
- **Gesamte P&L:** +$7,348.87 (+73.5%)
