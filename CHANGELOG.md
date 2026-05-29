# Changelog

## [1.9] 2026-05-29 — Meta-Update & KPI Framework v2.0 Vorbereitung

### Added
- `method/OBSERVATIONS.md` v1.0 — neue redaktionelle Rubrik für Marktbeobachtungen (OBS-001, OBS-002)
- `reports/observations.html` — dedizierte Seite für Observations mit eingebetteten Screenshots
- `reports/sessions.html` — dedizierte Seite für alle Sessions (chronologisch, neuste zuerst)
- Key-Level Validation Strategy — dokumentiert in OBSERVATIONS.md (ausstehend) und TERMINOLOGY.md (ausstehend)

### Changed
- `README.md` v1.9 — Report Structure Rule auf 3 separate HTML-Files umgestellt, Observations-Reiter als Pflicht, Dokument-Architektur ergänzt
- `CURRENT_SESSION.md` — vollständig aktualisiert, Known Issues dokumentiert, KPI v2.0 Roadmap
- `HYPOTHESES.md` v1.2 — H4 auf "Confirmed" gesetzt, alle Pattern-Status aktualisiert
- `reports/master_report.html` — Overview + aktuelle Session (kein Repetition mehr)
- `scripts/generate_reports.py` v2.3 — generiert jetzt 3 separate Dateien mit gemeinsamer Nav
- `data/master/master_stats.csv` — fehlerhafte dritte Zeile entfernt

### Fixed
- master_stats.csv: fehlerhafte Zeile (2026-05-29 japan mit falschen Werten) entfernt
- HYPOTHESES.md: H4 fälschlicherweise als "First evidence" markiert → jetzt "Confirmed"
- CHANGELOG: fehlende Einträge für v1.6–v1.8 nachgetragen (siehe unten)

### Known Issues (ausstehend)
- master_trades.csv: Duplikate in zweiter Hälfte (parse_trades.py doppelter Run) → Fix vor nächstem Parse
- SITUATIONS.md: referenziert Screenshots 1b04d und 6982c die nicht in screenshots/ liegen

---

## [1.8] 2026-05-29

### Added
- `reports/master_report.html` — One-Pager, kein Wiederholen von Sessions
- Typography Rule in README: min 15px Body, min 12px Labels, kein 800/900-weight für Headers
- No-Duplication Rule: jede Session erscheint genau einmal pro Datei

### Changed
- `scripts/generate_reports.py` v2.2 — dezentere Schrift (Inter 600 statt Syne 800), One-Pager-Logik
- `README.md` v1.8 — Report Structure Rule auf 3-Teile-Layout präzisiert

---

## [1.7] 2026-05-29

### Changed
- Report-Struktur: Japan Session nicht mehr wiederholt (Part 2 + Part 3 waren identisch)
- `README.md` v1.7 — No-Duplication Rule explizit dokumentiert

---

## [1.6] 2026-05-29

### Added
- `reports/master_report.html` — Master Report mit allen Sessions, Charts mit 3-Spalten-Annotation
- Chart-Annotation-System: Was passiert ist · Highlights · Fehler/Schwächen direkt unter jedem Screenshot
- `scripts/generate_reports.py` v2.0 — standalone HTML mit Base64-eingebetteten Screenshots
- Git Remote URL bereinigt (Token entfernt)
- `scripts/img_to_base64.py` — Hilfsskript für Screenshot-Komprimierung

### Changed
- `README.md` v1.6 — Report Structure Rule (3 Teile), Screenshot Rule, Typography Rule
- `scripts/update.sh` v2.1 — korrekter Google Drive Pfad (arthurdigbysellers2@googlemail.com)
- `CURRENT_SESSION.md` — Kickstarten korrekt als Technik dokumentiert (kein Pattern)

### Fixed
- Google Drive Pfad in update.sh: GoogleDrive-arthurdigbysellers2@googlemail.com
- Git user.name/user.email Warnung (manuell zu setzen)

---

## [1.5] 2026-05-29

### Added
- `scripts/fetch_market_data.py` v2.1 — holt 5M Kerzen via yfinance, ^GDAXI Fix, breites Zeitfenster
- `scripts/parse_trades.py` v2.1 — parst TradingView Export-CSVs, kein Datumsfilter mehr
- `scripts/update.sh` v2.1 — ein Befehl: Marktdaten + Trades + Screenshots + Git Push
- `data/master/master_trades.csv` — zentrale Trades-Datei, alle Trades aller Sessions
- Filesystem MCP aktiviert — Claude liest/schreibt direkt ins Repo

### Changed
- `TERMINOLOGY.md` v1.3 — Kickstarten hinzugefügt

### Fixed
- update.sh und fetch_market_data.py waren vertauscht
- GER40 Ticker: GDAXI → ^GDAXI
- parse_trades.py: Datumsfilter entfernt (Japan-Trades haben Vortags-Timestamps)

---

## [1.4] 2026-05-29

### Added
- `method/SITUATIONS.md` v1.0 — Barbwire Reversal als erste Situation
- `KATYA_ONBOARDING.md` v1.1
- Pattern #3: Concentration Loss
- H5: Barbwire Reversal Hypothesis

### Changed
- `TERMINOLOGY.md` v1.2 → v1.3 (Barbwire, Barbwire Reversal)
- `HYPOTHESES.md` v1.0 → v1.1 (H5 hinzugefügt)
- `README.md` v1.4

---

## [1.3] 2026-05-28

### Added
- README.md v1.3 — Trader B (Katya) integriert
- KATYA_ONBOARDING.md v1.0
- Ordnerstruktur für zwei Trader

---

## [1.2] 2026-05-28

### Added
- TECHSTACK.md v1.1
- `scripts/fetch_market_data.py` v1.0
- `data/market/` — 5M Kerzen für alle 6 Symbole
- HTML-Report v1.0
- Screenshot-Infrastruktur: Google Drive → komprimiert → GitHub → HTML

### Changed
- `README.md` v1.2
- `TERMINOLOGY.md` v1.2 — TDS, Account Fuse, Spike Catcher, Mental Stop

### Fixed [1.2.1–1.2.2]
- Google Drive Pfad
- Git LFS für Screenshots
- report_standalone.html mit Base64-Screenshots

---

## [1.1] 2026-05-28

### Changed
- README.md überarbeitet
- TERMINOLOGY.md erweitert
- Report 2026-05-28 finalisiert

---

## [1.0] 2026-05-28

### Added
- Initiales Repo-Setup
- README.md v1.0, METHOD.md v0.1, TERMINOLOGY.md v0.1, HYPOTHESES.md v0.1
- data/trades/2026-05-28.csv
- data/master/master_stats.csv
- reports/2026-05-28/report.md
- scripts/update.sh v1.0
