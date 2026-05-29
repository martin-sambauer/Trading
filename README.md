<!-- Version: 1.4 | Letzte Änderung: 2026-05-29 -->
# Trading Journal — Trader A & Trader B

## Technical Setup & Recovery
In case of computer failure or new device: see `TECHSTACK.md` — complete step-by-step recovery guide.

---

## For AI Agents: Read This First

This repository is the central brain of the trading development system for Trader A and Trader B.
Everything is documented so you as an AI can immediately step in and continue seamlessly.

### File Delivery Rule — ALWAYS FOLLOW
When delivering updated files to Trader A:
1. Create a ZIP containing ONLY changed files (not the full repo)
2. Present the ZIP as a single download
3. Provide ONE terminal command that does everything: unzip + git add + commit + push
4. Trader A does: download ZIP → paste one command → done
5. Never ask Trader A to manually copy, move or rename files
6. Never deliver more than one ZIP per update

**Template command:**
```bash
cd ~/Downloads && unzip -o ZIPNAME.zip -d ~/Documents/ && cd ~/Documents/Trading && git add -A && git commit -m "vX.X - description" && git push origin main
```

### Mandatory Reading Before Every Session
1. This README — context, logistics, current status
2. `method/METHOD.md` — the trading method
3. `method/TERMINOLOGY.md` — all terms defined
4. `method/HYPOTHESES.md` — current behaviour hypotheses
5. `method/SITUATIONS.md` — documented market situation types
6. `data/traders/trader a/master_stats.csv` — Trader A's aggregated performance
7. `data/traders/trader b/master_stats.csv` — Trader B's aggregated performance (when available)
8. Latest report in `reports/trader a/` or `reports/trader b/`

### Hypothesis Check — MANDATORY for every data analysis
**Every time you analyse trading data, check each open hypothesis:**
- Is there evidence that confirms the hypothesis?
- Is there evidence that contradicts it?
- Update `method/HYPOTHESES.md` accordingly with date and data reference
- If confirmed by 5+ data points → mark as "Confirmed"
- If contradicted → mark as "Refuted" with explanation

Current hypotheses to check: H1, H2, H3, H4, H5

### AI Instructions per Session Type
- **Trader A solo:** Read `data/traders/trader a/` → report in `reports/trader a/`
- **Trader B solo:** Read `data/traders/trader b/` → report in `reports/trader b/`
- **Comparison:** Read both → additional report in `reports/comparison/`
- **Always:** Update README, METHOD, TERMINOLOGY, HYPOTHESES, SITUATIONS if new insights

---

## The Traders

### Trader A
- Active daytrader, paper trading for method development
- Goal: develop own analytically described method
- Main instruments: USTEC, GER40 morning session, JAPAN225 night session
- Typical trading hours: 07:00–09:00 (GER40), 11:00–14:00 (USTEC), 16:30–17:30 (US30/SPX), 22:00–09:00 JST (JAPAN225)
- GitHub: trader-journal
- Local repo: `~/Documents/Trading`
- Google Drive screenshots: `~/Google Drive/Trading_Journal/Screenshots/`

### Trader B
- Active trader, own setup parallel to Trader A
- Goal: parallel data collection for behaviour comparison
- GitHub: to be added as Collaborator
- Local repo: `~/Documents/Trading` (cloned from same repo)
- Onboarding guide: `KATYA_ONBOARDING.md`

---

## Trading Setup (both traders)
- **Platform:** TradingView (charts + execution) + TradeNation / Forex.com / WH SelfInvest (brokers)
- **Timeframes:** 1D (left, context/bias) + 5M (right, entry/execution)
- **Indicators:** BB 20, SMA20, SMA200, PDH/PDL, PWH/W

### Instruments
| Symbol | TradingView | Broker | Typical Session |
|--------|-------------|--------|----------------|
| USTEC | TRADENATION:USTEC | TradeNation | 11:00–14:00 |
| US30 | FOREXCOM:US30 | Forex.com | 16:30–17:30 |
| GER40 | FOREXCOM:GER40 | Forex.com | 07:00–09:00 |
| SPX | TVC:SPX | TradingView | 16:30–17:30 |
| JAPAN225 | WHSELFINVEST:JAPAN225CFD | WH SelfInvest | 22:00–09:00 JST |
| OILGAS | — | — | Context indicator only |

---

## Project Structure
```
Trading/
├── README.md                          ← You are here (v1.4)
├── CHANGELOG.md                       ← All changes documented
├── TECHSTACK.md                       ← Complete technical setup
├── KATYA_ONBOARDING.md                ← Onboarding guide for Trader B
├── method/
│   ├── METHOD.md                      ← Trading method (living document)
│   ├── TERMINOLOGY.md                 ← All terms in English
│   ├── HYPOTHESES.md                  ← Behaviour hypotheses
│   └── SITUATIONS.md                  ← Market situation library
├── data/
│   ├── traders/
│   │   ├── trader a/
│   │   │   ├── trades/YYYY-MM-DD.csv
│   │   │   ├── market/YYYY-MM-DD_SYMBOL.csv
│   │   │   ├── exports/
│   │   │   └── master_stats.csv
│   │   └── trader b/
│   │       ├── trades/YYYY-MM-DD.csv
│   │       ├── market/YYYY-MM-DD_SYMBOL.csv
│   │       ├── exports/
│   │       └── master_stats.csv
├── reports/
│   ├── trader a/YYYY-MM-DD/report.html
│   ├── trader b/YYYY-MM-DD/report.html
│   └── comparison/YYYY-MM-DD/report.html
├── screenshots/
│   ├── trader a/
│   └── trader b/
└── scripts/
    ├── update.sh
    └── fetch_market_data.py
```

**Note:** Trader A's Day 1 data is in `data/trades/`, `data/market/`, `reports/2026-05-28/` — will be migrated to new structure.

---

## Account System
| Type | Description |
|------|-------------|
| `paper` | Paper trading — no real money |
| `live` | Live account — real money |

P&L comparisons only within same account type. Account resets are documented.

---

## Duplicate Rule
Every trade is uniquely identified by `Date + Time + Symbol + Trader`.
Never overwrite existing entries — append only.

---

## Daily Workflow

### What each trader delivers
1. **Balance History CSV** — TradingView → Paper Trading → Balance History → Export
2. **Order History CSV** — TradingView → Paper Trading → Order History → Export (All)
3. **Screenshots** — `Cmd+Shift+4` with Execution Marks visible (NOT TradingView camera button)
4. **Comments** — observations, reasons for decisions

### What the AI does
1. Parse data → create trade table → update master_stats.csv
2. **Check all hypotheses** (H1–H5) against new data → update HYPOTHESES.md
3. Check for new market situations → update SITUATIONS.md if relevant
4. Create HTML report (5 pages: Dashboard, Sessions, Trades, Behaviour, Method)
5. Create standalone report with embedded screenshots
6. If both traders have data → create comparison report
7. Update METHOD, TERMINOLOGY, HYPOTHESES, SITUATIONS if new insights
8. Update CHANGELOG
9. Update README status

### Screenshot Convention
- **Enable Execution Marks:** Chart settings (gear) → "Trading" tab → "Executions"
- **Connect broker:** TradeNation for USTEC, Forex.com for US30/GER40, WH SelfInvest for JAPAN225
- **Screenshot:** `Cmd+Shift+4` — captures what you see including marks
- **Save to:** `~/Google Drive/Trading_Journal/Screenshots/`
- **Auto-compressed** to `screenshots/` on next push via `update.sh`

### Open Reports
```bash
open -a Firefox ~/Documents/Trading/reports/trader a/YYYY-MM-DD/report_standalone.html
```
**Note:** Use Firefox — Chrome blocks Base64 images in local files.

---

## Daily Push (one command)
```bash
cd ~/Documents/Trading && python3 scripts/fetch_market_data.py && ./scripts/update.sh "$(date +%Y-%m-%d) session close"
```

---

## CSV Formats

### Balance History
```
Time, Balance before, Balance after, Realized PnL (value), Realized PnL (currency), Action
```

### Order History
```
Symbol, Side, Type, Quantity, Limit price, Stop price, Fill price, Status, Commission, Placing time, Closing time, Order ID
```
Includes cancelled orders → shows Spike Catchers and original intentions.

---

## Current Status
- **Last update:** 2026-05-29
- **Trading days documented:** 1 full (Trader A 2026-05-28), 1 partial (Trader A Japan session 2026-05-29)
- **Method version:** 0.1
- **README version:** 1.4
- **Documented behaviour patterns:** 3 (FOMO Top Scale, Context Switch Exit, Concentration Loss)
- **Open hypotheses:** 5 (H1–H5)
- **Documented situations:** 1 (Barbwire Reversal)
- **Trader A account balance:** $17,348.87 + Japan session (open)
- **Trader B:** not yet started
