# Changelog

## [2.0] 2026-05-29 — KPI Framework v2.0, JSON-Architektur, Meta vollstaendig

### Added
- `scripts/parse_and_export.py` v3.0 — neuer schlanker Parser: liest CSVs, berechnet alle v2.0 KPIs, exportiert `dashboard_data.json`. Kein HTML mehr im Script.
- `data/master/dashboard_data.json` — zentrales Daten-Interface fuer alle HTML-Reports
- `reports/assets/style_v1.0.css` — zentrales CSS, einzige Quelle der Wahrheit fuer alle visuellen Regeln
- `method/OBSERVATIONS.md` v1.1 — OBS-003 Key-Level Validation Strategy (taktisches LP am Support)
- `method/TERMINOLOGY.md` v1.4 — T2BE, HSR, ITPE, Profit/Loss Pyramiding, Risiko-Stressbarometer vollstaendig definiert

### Changed
- `data/master/master_stats.csv` — auf v2.0 Schema migriert: alle neuen KPI-Spalten (T2BE, PP/LP, Stress-Sentiments)
- `README.md` v2.0 — Dokument-Architektur-Tabelle, Workflow/Rollenverteilung, 5-Tab Dashboard-Spec, Paper/Live Trading Switch vorbereitet
- `CURRENT_SESSION.md` — v2.0 Roadmap und Known Issues aktualisiert

### Architecture Decision
- `generate_reports.py` wird umgebaut: liest `dashboard_data.json` via fetch(), kein HTML-Code im Python-Script
- Dashboard wird statisches HTML das JSON via JavaScript laedt — reduziert Script-Groesse um ~80%
- CSS-Quelle: `reports/assets/style_v1.0.css` wird von generate_reports.py eingelesen und inline eingebettet

### Known Issues
- `{data` directory im Repo-Root ist ein kaputtes Artefakt — manuell loeschen via `rm -rf ~/Documents/Trading/\{data`
- `master_trades.csv` enthaelt Duplikate — vor naechstem Parse bereinigen
- `generate_reports.py` noch im alten Format (v2.3) — wird mit naechster Session auf v3.0 (JSON-basiert) umgebaut

---

## [1.9] 2026-05-29 — Meta-Update & KPI Framework v2.0 Vorbereitung

### Added
- `method/OBSERVATIONS.md` v1.0 — neue redaktionelle Rubrik fuer Marktbeobachtungen (OBS-001, OBS-002)
- `reports/observations.html` — dedizierte Seite fuer Observations mit eingebetteten Screenshots
- `reports/sessions.html` — dedizierte Seite fuer alle Sessions (chronologisch, neuste zuerst)

### Changed
- `README.md` v1.9 — Report Structure Rule auf 3 separate HTML-Files umgestellt
- `CURRENT_SESSION.md` — vollstaendig aktualisiert, Known Issues, KPI v2.0 Roadmap
- `HYPOTHESES.md` v1.2 — H4 auf Confirmed gesetzt, alle Pattern-Status aktualisiert
- `scripts/generate_reports.py` v2.3 — 3 separate Dateien mit gemeinsamer Nav

### Fixed
- master_stats.csv: fehlerhafte dritte Zeile entfernt
- HYPOTHESES.md: H4 war faelschlicherweise als First evidence markiert

---

## [1.8] 2026-05-29

### Added
- Typography Rule: min 15px Body, min 12px Labels, kein 800/900-weight
- No-Duplication Rule: jede Session erscheint genau einmal

### Changed
- `scripts/generate_reports.py` v2.2 — dezentere Schrift, One-Pager-Logik
- `README.md` v1.8

---

## [1.7] 2026-05-29

### Changed
- Japan Session nicht mehr wiederholt im Report
- `README.md` v1.7 — No-Duplication Rule

---

## [1.6] 2026-05-29

### Added
- Master Report mit Screenshots, 3-Spalten-Chart-Annotation
- `scripts/generate_reports.py` v2.0 — standalone HTML mit Base64-Screenshots
- Git Remote URL bereinigt

### Changed
- `README.md` v1.6 — Report Structure Rule, Screenshot Rule, Typography Rule
- `scripts/update.sh` v2.1 — korrekter Google Drive Pfad

---

## [1.5] 2026-05-29

### Added
- `scripts/fetch_market_data.py` v2.1
- `scripts/parse_trades.py` v2.1
- `scripts/update.sh` v2.1
- `data/master/master_trades.csv`
- Filesystem MCP aktiviert

### Changed
- `TERMINOLOGY.md` v1.3 — Kickstarten hinzugefuegt

---

## [1.4] 2026-05-29

### Added
- `method/SITUATIONS.md` v1.0 — Barbwire Reversal
- Pattern #3: Concentration Loss
- H5: Barbwire Reversal Hypothesis

---

## [1.3] 2026-05-28

### Added
- Trader B (Katya) integriert
- KATYA_ONBOARDING.md v1.0

---

## [1.2] 2026-05-28

### Added
- TECHSTACK.md v1.1
- fetch_market_data.py v1.0
- HTML-Report v1.0
- Screenshot-Infrastruktur

---

## [1.1] 2026-05-28

### Changed
- README, TERMINOLOGY, Report 2026-05-28 finalisiert

---

## [1.0] 2026-05-28

### Added
- Initiales Repo-Setup
- README v1.0, METHOD v0.1, TERMINOLOGY v0.1, HYPOTHESES v0.1
- update.sh v1.0
