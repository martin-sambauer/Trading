# Changelog

## [2.1] 2026-05-29 — Day 3 Report, TDS Pattern #4, parse_trades Fix

### Added
- `reports/master_report.html` v2.1 — Day 3 als aktuelle Session, KPI-Barometer-Tabelle alle Sessions, Pattern #4 TDS in Behaviour-Tabelle
- `reports/sessions.html` v2.1 — Day 3 ganz oben mit Barometern direkt bei Screenshots, TDS-Block mit Regelformulierung
- `reports/observations.html` v2.1 — OBS-003 Key-Level Validation Strategy vollstaendig mit Day-3-Beispiel, Terminology Quick Reference

### Changed
- `data/master/master_stats.csv` — Day 3 Zeile hinzugefuegt (v2.0 Schema)
- `CURRENT_SESSION.md` — vollstaendig auf Day 3 aktualisiert, Pattern #4 TDS dokumentiert
- `scripts/parse_trades.py` v2.2 — kompatibel mit v1.0 (date) UND v2.0 (Session_Date) Schema; kein Crash mehr bei v2.0 master_stats.csv

### New Pattern documented
- Pattern #4 TDS (Target Derangement Syndrome): Nach grossem TP impulsiv in Gegenrichtung handeln obwohl Methoden-Regel dagegen spricht. Day 3: Short nach US30-Exit 11:53 UTC in 11h-UTC-Long-Bias-Zone. ~-$1,000 direkt, ~-$2,000 Opportunitaet.

### Fixed
- `parse_trades.py`: KeyError 'date' wenn master_stats.csv im v2.0-Format (Session_Date) — jetzt beide Schemas unterstuetzt

---

## [2.0] 2026-05-29 — KPI Framework v2.0, JSON-Architektur, Meta vollstaendig

### Added
- `scripts/parse_and_export.py` v3.0 — schlanker Parser: liest CSVs, berechnet alle v2.0 KPIs, exportiert dashboard_data.json
- `reports/assets/style_v1.0.css` — zentrales CSS, einzige Quelle fuer alle visuellen Regeln
- `method/OBSERVATIONS.md` v1.1 — OBS-003 Key-Level Validation Strategy
- `method/TERMINOLOGY.md` v1.4 — T2BE, HSR, ITPE, Profit/Loss Pyramiding, Risiko-Stressbarometer

### Changed
- `data/master/master_stats.csv` — auf v2.0 Schema migriert (alle KPI-Spalten)
- `README.md` v2.0 — Dokument-Architektur-Tabelle, Workflow/Rollenverteilung, 5-Tab Dashboard-Spec

---

## [1.9] 2026-05-29 — Meta-Update & KPI Framework v2.0 Vorbereitung

### Added
- `method/OBSERVATIONS.md` v1.0 — OBS-001, OBS-002
- `reports/observations.html`, `reports/sessions.html`

### Changed
- `README.md` v1.9, `CURRENT_SESSION.md`, `HYPOTHESES.md` v1.2 (H4 Confirmed)
- `scripts/generate_reports.py` v2.3

### Fixed
- master_stats.csv fehlerhafte dritte Zeile entfernt
- HYPOTHESES.md H4 war faelschlicherweise als "First evidence" markiert

---

## [1.8] 2026-05-29
- One-Pager ohne Session-Wiederholung, dezentere Schrift (Inter 600)

## [1.7] 2026-05-29
- No-Duplication Rule fuer Sessions

## [1.6] 2026-05-29
- Master Report mit Base64-Screenshots, Chart-Annotation-System
- update.sh v2.1 mit korrektem Google Drive Pfad

## [1.5] 2026-05-29
- fetch_market_data.py v2.1, parse_trades.py v2.1, update.sh v2.1
- Filesystem MCP aktiviert, TERMINOLOGY.md v1.3 (Kickstarten)

## [1.4] 2026-05-29
- SITUATIONS.md v1.0 (Barbwire Reversal), Pattern #3, H5

## [1.3] 2026-05-28
- Trader B (Katya) integriert, KATYA_ONBOARDING.md

## [1.2] 2026-05-28
- TECHSTACK.md, fetch_market_data.py v1.0, HTML-Report v1.0

## [1.1] 2026-05-28
- README, TERMINOLOGY, Report 2026-05-28 finalisiert

## [1.0] 2026-05-28
- Initiales Repo-Setup
