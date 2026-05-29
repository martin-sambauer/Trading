<!-- AUTO-UPDATED after every session. New AI: read this first, then README.md -->
# Current Session Context

## For New AI: How to start
1. Read this file completely
2. Read README.md v1.9
3. Read `method/OBSERVATIONS.md` — new editorial rubric, mandatory reading
4. `data/master/master_trades.csv` — alle Trades via Filesystem MCP lesbar (Achtung: enthält Duplikate, Fix ausstehend)
5. `data/master/master_stats.csv` — Session-Übersicht (dritte Zeile fehlerhaft, Fix ausstehend)
6. Say to Martin in German: "Ich bin auf dem aktuellen Stand. [Was noch fehlt]."
7. Never ask Martin to re-explain what's already in this file

## Filesystem MCP
Claude hat direkten Zugriff auf `/Users/martinsambauer/Documents/Trading/`.
Nach Änderungen pusht Martin mit:
```bash
cd ~/Documents/Trading && ./scripts/update.sh YYYY-MM-DD martin "beschreibung"
```

## Repo
Private: https://github.com/martin-sambauer/Trading

## Who is Martin
- Daytrader, paper trading on TradingView (account: arthurdigbysellers2 USD)
- Building his own trading method — see method/METHOD.md
- Language: German
- Brokers: TradeNation (USTEC), Forex.com (US30/GER40), WH SelfInvest (JAPAN225)

## Account Status
- Start: $10,000 (2026-05-28)
- After Day 1 (2026-05-28): $17,348.87 (+73.5%)
- After Japan Session (2026-05-28 20:51 – 2026-05-29 01:12 UTC): $21,276.93 (+$3,928 net)
- Total: +$11,277 (+112.8%) in 2 Tagen

## Report System (3 separate HTML files, shared nav)
```bash
open -a Firefox ~/Documents/Trading/reports/master_report.html   # Übersicht + aktuelle Session
open -a Firefox ~/Documents/Trading/reports/sessions.html        # Alle Sessions
open -a Firefox ~/Documents/Trading/reports/observations.html    # Observations
```
Generate all three:
```bash
cd ~/Documents/Trading && python3 scripts/generate_reports.py
```

## Data Structure
- `data/master/master_trades.csv` — ALLE Trades, append-only (⚠ Duplikate vorhanden)
- `data/master/master_stats.csv` — eine Zeile pro Session (⚠ Zeile 3 fehlerhaft)
- `data/traders/martin/exports/YYYY-MM-DD/` — rohe TradingView CSVs
- `data/market/YYYY-MM-DD_SYMBOL.csv` — 5M Kerzen (via fetch_market_data.py)

## Sessions (vollständig dokumentiert)
### Day 1 — 2026-05-28
- 33 trades, +$7,349 net, Win Rate 78.8%
- Anchor Trade: USTEC Long 11:13 +$2,911
- Behaviour cost: -$1,302 (FOMO Top Scale + Context Switch Exit)
- Reports: reports/master_report.html ✅, reports/sessions.html ✅

### Japan Session — 2026-05-28 20:51 – 2026-05-29 01:12 UTC
- 68 Order-Fills, +$3,880 net, Win Rate 78.6%
- Biggest win: +$1,240 (Long 2500 @ 65935 → 66014)
- Losses: SL hit 23:38 -$395, Kickstarten SL hit 00:20 -$802 (technique correct, slippage unfavorable)
- Key event: Barbwire Reversal at market open, Concentration Loss (Pattern #3)
- Reports: reports/master_report.html ✅, reports/sessions.html ✅

## Method Files Status
- TERMINOLOGY.md v1.3 ✅ (includes Kickstarten)
- HYPOTHESES.md v1.1 ✅ (H1–H5, H4 confirmed)
- SITUATIONS.md v1.0 ✅ (Barbwire Reversal)
- OBSERVATIONS.md v1.0 ✅ (OBS-001, OBS-002)

## Known Data Issues (fix before next parse)
- master_trades.csv: Duplikate in der zweiten Hälfte (parse_trades.py doppelter Run)
- master_stats.csv: Zeile 3 (2026-05-29 japan) ist fehlerhaft — löschen
- Screenshots: SITUATIONS.md referenziert 1b04d und 6982c die nicht in screenshots/ liegen

## Upcoming (KPI Framework v2.0 — noch nicht implementiert)
- T2BE (Time-to-Break-Even)
- HSR (Hold-to-Scalp Ratio) / ITPE (Initial TP Efficiency)
- Profit vs Loss Pyramiding Tracking
- Risiko-Stressbarometer
- Key-Level Validation Strategy in OBSERVATIONS.md
- Zentrales CSS (reports/assets/style_v1.0.css)
- 5 Dashboard-Tabs: Frontpage, Sessions, Best/Worst, Observations, Terminology

## Open Items
- [ ] master_trades.csv Duplikate bereinigen
- [ ] master_stats.csv Zeile 3 fixen
- [ ] KPI Framework v2.0 Parser implementieren
- [ ] Dashboard v2.0 mit zentralem CSS bauen
- [ ] Katya GitHub account (waiting)
- [ ] Data migration: data/trades/ → data/traders/martin/trades/
- [ ] Key-Level Validation Strategy in OBSERVATIONS.md dokumentieren
