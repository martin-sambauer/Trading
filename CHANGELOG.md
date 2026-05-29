# Changelog

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

### Fixes [1.2.1] 2026-05-28
- Google Drive Pfad korrigiert: `~/Google Drive/Trading_Journal/` (ohne `My Drive/`)
- Git LFS für Screenshots eingerichtet
- Report HTML Pfade auf relative lokale Pfade umgestellt
- update.sh: magick statt convert, korrekter Google Drive Pfad

### [1.2.2] 2026-05-28
- report_standalone.html generiert mit eingebetteten Screenshots (Base64)
- Firefox empfohlen für lokale HTML Reports (Chrome blockiert Base64)
- US30 Screenshot mit Execution Marks hinzugefügt
- embed_screenshots Workflow dokumentiert

## [1.3] 2026-05-28
### Hinzugefügt
- README.md v1.3 — Katya als zweite Traderin integriert
- KATYA_ONBOARDING.md — vollständige Anleitung für Katya
- Neue Ordnerstruktur für zwei Trader (`data/traders/martin/`, `data/traders/katya/`)
- Vergleichsreport-Konzept (`reports/comparison/`)
- Screenshots aufgeteilt nach Trader (`screenshots/martin/`, `screenshots/katya/`)
