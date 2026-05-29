<!-- AUTO-UPDATED after every session. New AI: read this first, then README.md -->
# Current Session Context

## For New AI: How to start
1. Read this file completely
2. Read README.md
3. Check `data/traders/martin/exports/` for latest raw CSVs
4. Say to Martin in German: "Ich bin auf dem aktuellen Stand. [Was noch fehlt]."
5. Never ask Martin to re-explain what's already in this file

## Repo
Private: https://github.com/martin-sambauer/Trading
Token: Martin stores it locally. Ask him to run:
```bash
git remote set-url origin https://martin-sambauer:TOKEN@github.com/martin-sambauer/Trading.git
```

## Who is Martin
- Daytrader, paper trading on TradingView (account: arthurdigbysellers2 USD)
- Building his own trading method — see method/METHOD.md
- Language: German
- Brokers: TradeNation (USTEC), Forex.com (US30/GER40), WH SelfInvest (JAPAN225)

## Account Status
- Start: $10,000 (2026-05-28)
- After Day 1 (2026-05-28): $17,348.87 (+73.5%)
- Japan session (2026-05-29): +$1,763 realized (final P&L pending)
- Estimated total: ~$19,100+

## Raw Data Location
All CSVs Martin uploads are saved to `data/traders/martin/exports/` and pushed automatically.
Check there first before asking Martin to re-upload anything.

## Day 1 — 2026-05-28 (COMPLETE)
- 33 trades, +$7,349, Win Rate 78.8%
- Anchor Trade: USTEC Long 11:13 +$2,911
- Behaviour cost: -$1,302 (FOMO Top Scale + Context Switch Exit)
- Report: reports/2026-05-28/report_standalone.html ✅

## Japan Session — 2026-05-29 (INCOMPLETE)
**Status:** CSVs uploaded in previous chat, report NOT yet created

**What happened:**
- Instrument: WHSELFINVEST:JAPAN225CFD
- Realized P&L: +$1,763
- Key event: Barbwire Reversal at market open (~08:30 JST)
- SMA20 horizontal → fast crossing → Barbwire candles → 600+ point move
- Missed ~$3,000 due to Concentration Loss (Pattern #3, distracted by Claude chat)

**Raw CSVs in repo** (`data/traders/martin/exports/2026-05-29/`):
- paper-trading-balance-history-2026-05-29.csv
- paper-trading-order-history-2026-05-29.csv
- paper-trading-trading-journal-2026-05-29.csv
- paper-trading-positions-2026-05-29.csv

**Screenshots in Google Drive** (also in `screenshots/`):
- JAPAN225CFD_2026-05-28_19-09-00_cbdae.png
- JAPAN225CFD_2026-05-28_21-12-25_1b04d.png
- JAPAN225CFD_2026-05-28_21-15-00_6982c.png

## Open Items
- [ ] Japan session report erstellen (reports/martin/2026-05-29/)
- [ ] master_stats.csv mit Japan-Daten updaten
- [ ] Katya GitHub account (waiting)
- [ ] Data migration: data/trades/ → data/traders/martin/trades/

## Key Method Insights (latest)
- Barbwire Reversal documented in SITUATIONS.md
- H5 added: Barbwire → high probability strong move
- All terminology now in English
- Hypothesis check mandatory on every data analysis

## File Delivery Rule
Always: ZIP with only changed files + one terminal command:
```bash
cd ~/Downloads && unzip -o ZIPNAME.zip -d ~/Documents/ && cd ~/Documents/Trading && git add -A && git commit -m "vX.X - description" && git push origin main
```
