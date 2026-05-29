<!-- AUTO-UPDATED after every session. New AI: read this first, then README.md -->
# Current Session Context

## For New AI: How to start
1. Read this file completely
2. Read README.md
3. Check `data/master/master_trades.csv` — alle Trades direkt lesbar
4. Check `data/master/master_stats.csv` — Session-Übersicht
5. Check `data/traders/martin/exports/` für neue rohe CSVs
6. Say to Martin in German: "Ich bin auf dem aktuellen Stand. [Was noch fehlt]."
7. Never ask Martin to re-explain what's already in this file

## Filesystem MCP
Claude hat direkten Zugriff auf `/Users/martinsambauer/Documents/Trading/` — kein Upload nötig.
Dateien direkt lesen und schreiben. Nach Änderungen: Martin pusht mit:
```bash
cd ~/Documents/Trading && ./scripts/update.sh "2026-05-29 session close"
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
- After Japan session (2026-05-28 night): ~$19,091 (+$1,742 net)
- Open position: Short 1500 JAPAN225 @ 65891 (unresolved, -$961 unrealized at close of data)

## Data Structure
- `data/master/master_trades.csv` — ALLE Trades, append-only, direkt lesbar
- `data/master/master_stats.csv` — eine Zeile pro Session
- `data/traders/martin/exports/YYYY-MM-DD/` — rohe TradingView CSVs
- `data/market/YYYY-MM-DD_SYMBOL.csv` — 5M Kerzen (via fetch_market_data.py)

## Scripts
```bash
# Alles auf einmal (Marktdaten + Trades parsen + Screenshots + Git Push):
./scripts/update.sh [YYYY-MM-DD] [trader] [kommentar]

# Nur Marktdaten:
python3 scripts/fetch_market_data.py [YYYY-MM-DD]

# Nur Trades parsen:
python3 scripts/parse_trades.py [YYYY-MM-DD] [trader]
```

## Day 1 — 2026-05-28 (COMPLETE)
- 33 trades, +$7,349 net, Win Rate 78.8%
- Anchor Trade: USTEC Long 11:13 +$2,911
- Behaviour cost: -$1,302 (FOMO Top Scale + Context Switch Exit)
- Report: reports/2026-05-28/report_standalone.html ✅

## Japan Session — 2026-05-28 night (COMPLETE in master_trades.csv)
- 23 order-fills, +$1,742 net
- Key event: Barbwire Reversal at market open (~08:30 JST)
- Missed ~$3,000 due to Concentration Loss (Pattern #3)
- Report: FEHLT NOCH → reports/martin/2026-05-28_japan/

## Open Items
- [ ] Japan session report erstellen (reports/martin/2026-05-28_japan/)
- [ ] Open position JAPAN225 Short 1500 — finales P&L unbekannt
- [ ] yfinance installieren: `pip3 install yfinance`
- [ ] update.sh ausführbar machen: `chmod +x scripts/update.sh`
- [ ] Katya GitHub account (waiting)
- [ ] Data migration: data/trades/ → data/traders/martin/trades/

## Key Method Insights
- Barbwire Reversal documented in SITUATIONS.md
- H5: Barbwire → high probability strong move
- All terminology in English
- Hypothesis check mandatory on every data analysis (H1–H5)

## File Delivery Rule
Always: ZIP with only changed files + one terminal command:
```bash
cd ~/Downloads && unzip -o ZIPNAME.zip -d ~/Documents/ && cd ~/Documents/Trading && git add -A && git commit -m "vX.X - description" && git push origin main
```
