# Changelog

## [1.5] 2026-05-29

### Added
- `scripts/fetch_market_data.py` — holt 5M Kerzen via yfinance für alle Symbole, append-safe
- `scripts/parse_trades.py` — parst TradingView Export-CSVs → master_trades.csv + master_stats.csv, duplikat-sicher
- `scripts/update.sh` v2.0 — ein Befehl: Marktdaten + Trades + Screenshots + Git Push
- `data/master/master_trades.csv` — zentrale Trades-Datei, alle Trades aller Sessions, wächst append-only
- `data/master/master_stats.csv` — Japan Session 2026-05-29 hinzugefügt
- Filesystem MCP aktiviert — Claude liest/schreibt direkt ins Repo, keine Uploads mehr nötig

### Changed
- `scripts/update.sh` — komplett neu, ersetzt fehlerhafte v1.2
- `CURRENT_SESSION.md` — Workflow-Beschreibung aktualisiert

### Fixed
- update.sh und fetch_market_data.py waren vertauscht (v1.2 Bug)

---

## [1.4] 2026-05-29
### Added
- `method/SITUATIONS.md` — market situation library, first entry: Barbwire Reversal
- Barbwire + Barbwire Reversal in TERMINOLOGY.md
- Pattern #3: Concentration Loss
- H5: Barbwire Reversal Hypothesis
- `KATYA_ONBOARDING.md` v1.1 — complete step-by-step guide with TradingView setup

### Changed
- `method/TERMINOLOGY.md` — fully translated to English
- `method/HYPOTHESES.md` — fully translated to English
- README v1.4 — mandatory hypothesis check for every data analysis, JAPAN225 added, Trader B fully integrated

---

## [1.3] 2026-05-28
### Hinzugefügt
- README.md v1.3 — Trader B als zweite Traderin integriert
- KATYA_ONBOARDING.md — vollständige Anleitung für Trader B
- Neue Ordnerstruktur für zwei Trader (`data/traders/trader a/`, `data/traders/trader b/`)
- Vergleichsreport-Konzept (`reports/comparison/`)
- Screenshots aufgeteilt nach Trader (`screenshots/trader a/`, `screenshots/trader b/`)

---

## [1.2] 2026-05-28
### Hinzugefügt
- TECHSTACK.md v1.1 — komplettes Setup-Dokument
- `scripts/fetch_market_data.py` — automatischer Marktdaten-Download
- `data/market/` — 5M Kerzen für alle 6 Symbole
- `screenshots/` — komprimierte Chart-Screenshots mit Execution Marks
- HTML-Report v1.0 mit 5 Seiten (Dashboard, Sessions, Trades, Behaviour, Methode)
- Screenshot-Infrastruktur: Google Drive → komprimiert → GitHub → HTML eingebettet
- Account-System Dokumentation (paper/live, Reset-Handling)
- Dubletten-Regel dokumentiert

### Geändert
- README.md v1.2 — vollständige KI-Übergabe, Screenshot-Workflow, Account-System, Google Drive URL
- TERMINOLOGY.md v1.2 — TDS neu definiert, Account Fuse, Spike Catcher, mentaler Stop Loss neu
- `scripts/update.sh` — Screenshot-Komprimierung mit imagemagick integriert

### Fixes [1.2.1] 2026-05-28
- Google Drive Pfad korrigiert
- Git LFS für Screenshots eingerichtet
- Report HTML Pfade auf relative lokale Pfade umgestellt

### [1.2.2] 2026-05-28
- report_standalone.html generiert mit eingebetteten Screenshots (Base64)
- Firefox empfohlen für lokale HTML Reports
- embed_screenshots Workflow dokumentiert

---

## [1.1] 2026-05-28
### Geändert
- README.md komplett überarbeitet
- TERMINOLOGY.md erweitert
- Report 2026-05-28 finalisiert
- Google Drive Pfad korrigiert

### Hinzugefügt
- CHANGELOG.md
- Versionsnummern in allen Dokumenten

---

## [1.0] 2026-05-28
### Hinzugefügt
- Initiales Repo-Setup
- README.md v1.0, METHOD.md v0.1, TERMINOLOGY.md v0.1, HYPOTHESES.md v0.1
- data/trades/2026-05-28.csv — erster Handelstag
- data/master/master_stats.csv
- reports/2026-05-28/report.md
- scripts/update.sh
