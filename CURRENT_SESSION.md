<!-- AUTO-UPDATED after every session. New AI: read this first, then README.md -->
# Current Session Context

## For New AI: How to start
1. Read this file completely
2. Read README.md
3. `data/master/master_trades.csv` — alle Trades direkt lesbar via Filesystem MCP
4. `data/master/master_stats.csv` — Session-Übersicht
5. Say to Martin in German: "Ich bin auf dem aktuellen Stand. [Was noch fehlt]."
6. Never ask Martin to re-explain what's already in this file

## Filesystem MCP
Claude hat direkten Zugriff auf `/Users/martinsambauer/Documents/Trading/` — kein Upload nötig.
Nach Änderungen pusht Martin mit:
```bash
cd ~/Documents/Trading && ./scripts/update.sh "DATUM beschreibung"
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

## Data Structure
- `data/master/master_trades.csv` — ALLE Trades, append-only, 101 Einträge
- `data/master/master_stats.csv` — eine Zeile pro Session
- `data/traders/martin/exports/YYYY-MM-DD/` — rohe TradingView CSVs
- `data/market/YYYY-MM-DD_SYMBOL.csv` — 5M Kerzen (via fetch_market_data.py)

## Scripts (einmal ausführen nach Session-Ende)
```bash
cd ~/Documents/Trading && ./scripts/update.sh [YYYY-MM-DD] [trader] [kommentar]
```
Macht automatisch: Marktdaten holen + Trades parsen + Screenshots + Git Push

## Day 1 — 2026-05-28 (COMPLETE)
- 33 trades, +$7,349 net, Win Rate 78.8%
- Anchor Trade: USTEC Long 11:13 +$2,911
- Behaviour cost: -$1,302 (FOMO Top Scale + Context Switch Exit)
- Report: reports/2026-05-28/report_standalone.html ✅

## Japan Session — 2026-05-28 20:51 – 2026-05-29 01:12 UTC (DATA COMPLETE)
- 68 Order-Fills, +$3,880 net, Win Rate 78.6%
- Biggest win: +$1,240 (Long 2500 @ 65935 → 66014)
- Losses: Stop Loss hit 23:38 -$395, Short Stop hit 00:20 -$802
- Key event: Barbwire Reversal at market open, Concentration Loss (Pattern #3)
- Report: FEHLT NOCH → `reports/martin/2026-05-28_japan/`

## Open Items
- [ ] Japan session report erstellen
- [ ] `update.sh` für 2026-05-29 ausführen (Marktdaten + Push)
- [ ] Katya GitHub account (waiting)
- [ ] Data migration: data/trades/ → data/traders/martin/trades/

## Key Method Insights
- Barbwire Reversal: SITUATIONS.md
- H5: Barbwire → high probability strong move
- Hypothesis check mandatory (H1–H5) bei jeder Analyse
