<!-- Version: 1.9 | Last updated: 2026-05-29 -->
# Trading Journal — Martin & Katya

## Technical Setup & Recovery
In case of computer failure or new device: see `TECHSTACK.md` — complete step-by-step recovery guide.

---

## For AI Agents: Read This First

This repository is the central brain of the trading development system for Martin (Trader A) and Katya (Trader B).
Everything is documented so you as an AI can immediately step in and continue seamlessly.

### File Delivery Rule — ALWAYS FOLLOW
When delivering updated files to Martin:
1. Create a ZIP containing ONLY changed files (not the full repo)
2. Present the ZIP as a single download
3. Provide ONE terminal command that does everything: unzip + git add + commit + push
4. Martin does: download ZIP → paste one command → done
5. Never ask Martin to manually copy, move or rename files
6. Never deliver more than one ZIP per update

**Template command:**
```bash
cd ~/Downloads && unzip -o ZIPNAME.zip -d ~/Documents/ && cd ~/Documents/Trading && git add -A && git commit -m "vX.X - description" && git push origin main
```

---

### Mandatory Reading Before Every Session
1. This README — context, logistics, current status
2. `method/METHOD.md` — the trading method
3. `method/TERMINOLOGY.md` — all terms defined
4. `method/HYPOTHESES.md` — current behaviour hypotheses
5. `method/SITUATIONS.md` — documented market situation types
6. `method/OBSERVATIONS.md` — editorial market observations (phase structure, character, transitions)
7. `data/master/master_trades.csv` — all trades, append-only
8. `data/master/master_stats.csv` — session overview

---

### Hypothesis Check — MANDATORY for every data analysis
Every time you analyse trading data, check each open hypothesis:
- Is there evidence that confirms the hypothesis?
- Is there evidence that contradicts it?
- Update `method/HYPOTHESES.md` accordingly with date and data reference
- If confirmed by 5+ data points → mark as "Confirmed"
- If contradicted → mark as "Refuted" with explanation

Current hypotheses to check: H1 (SMA200 Breakout → Trend Duration), H2 (Aircushion Collapse as Exit), H3 (Best Performance 11–13h), H4 (Hold > Scalp), H5 (Barbwire Reversal)

---

### Report Structure Rule — ALWAYS FOLLOW

The report system consists of **three separate HTML files**, each accessible via a shared navigation bar. They are generated together by `generate_reports.py` and opened from the `reports/` directory.

**File 1 — `reports/master_report.html` (Overview + Current Session)**
This is the default landing page. It contains:
- Total KPIs across all sessions
- Equity curve spanning all sessions
- Time-of-day P&L breakdown
- Instrument distribution
- Behaviour pattern summary and development across sessions
- Benchmark comparison (retail / prop / algo)
- Hypotheses status
- The most recent session in full (stats bar, all charts annotated, highlights, errors/weaknesses)

**File 2 — `reports/sessions.html` (All Sessions)**
All sessions in full detail, chronological, newest first.
Each session: stats bar, all charts annotated, highlights, errors/weaknesses.
The current session appears here too — this page is the complete archive.

**File 3 — `reports/observations.html` (Observations)**
All entries from `method/OBSERVATIONS.md` rendered in full.
Each observation: ID, title, confidence level, core observation, chart markers, trading implication, break signals, examples with embedded screenshots.
This page grows automatically as new observations are added to OBSERVATIONS.md.

**Shared navigation:** All three files share the same nav bar with links to each other.
Opening any one file gives access to all three via the nav.

**No duplication within a file:** Within each file, every session and every observation appears exactly once.

**Typography Rule — STRICTLY ENFORCED**
- Body text, analysis paragraphs, chart annotations: minimum 15px
- Secondary labels, stat captions: minimum 12px
- Never below 12px for any readable content
- Headlines: clean readable weight (600–700 max). No heavy display fonts (800/900).

**Screenshot Rule**
- Every screenshot annotated directly below: 3 columns — what happened · highlights · errors
- If same instrument with and without executions exists: always use the one WITH execution marks

---

### AI Instructions per Session Type
- **Martin solo:** Read `data/master/` → generate all three report files
- **Katya solo:** Read `data/traders/katya/` → report in `reports/katya/`
- **Comparison:** Read both → additional report in `reports/comparison/`
- **Always:** Update README, METHOD, TERMINOLOGY, HYPOTHESES, SITUATIONS, OBSERVATIONS if new insights

---

## The Traders

### Martin (Trader A)
- Active daytrader, paper trading for method development
- Goal: develop own analytically described method
- Main instruments: USTEC, GER40 morning session, JAPAN225 night session
- Typical trading hours: 07:00–09:00 (GER40), 11:00–14:00 (USTEC), 16:30–17:30 (US30/SPX), 20:51–01:12 UTC (JAPAN225)
- TradingView account: arthurdigbysellers2
- Local repo: `~/Documents/Trading`
- Google Drive screenshots: `~/Library/CloudStorage/GoogleDrive-arthurdigbysellers2@googlemail.com/My Drive/Trading_Journal/Screenshots/`

### Katya (Trader B)
- Active trader, own setup parallel to Martin
- Goal: parallel data collection for behaviour comparison
- GitHub: to be added as Collaborator
- Onboarding guide: `KATYA_ONBOARDING.md`

---

## Trading Setup
- **Platform:** TradingView (charts + execution) + TradeNation / Forex.com / WH SelfInvest (brokers)
- **Timeframes:** 1D (left, context/bias) + 5M (right, entry/execution)
- **Indicators:** BB 20, SMA20, SMA200, PDH/PDL, PWH/W

### Instruments
| Symbol | TradingView | Broker | Typical Session |
|--------|-------------|--------|----------------|
| USTEC | TRADENATION:USTEC | TradeNation | 11:00–14:00 UTC |
| US30 | FOREXCOM:US30 | Forex.com | 16:30–17:30 UTC |
| GER40 | FOREXCOM:GER40 | Forex.com | 07:00–09:00 UTC |
| SPX | TVC:SPX | TradingView | 16:30–17:30 UTC |
| JAPAN225 | WHSELFINVEST:JAPAN225CFD | WH SelfInvest | 20:51–01:12 UTC |
| OILGAS | — | — | Context indicator only |

---

## Project Structure
```
Trading/
├── README.md                          ← You are here (v1.9)
├── CHANGELOG.md
├── CURRENT_SESSION.md                 ← Quick context for new AI instances
├── TECHSTACK.md
├── KATYA_ONBOARDING.md
├── method/
│   ├── METHOD.md                      ← v0.1
│   ├── TERMINOLOGY.md                 ← v1.3 — includes Kickstarten
│   ├── HYPOTHESES.md                  ← v1.1 — H1–H5
│   ├── SITUATIONS.md                  ← v1.0 — Barbwire Reversal
│   └── OBSERVATIONS.md               ← v1.0 — OBS-001, OBS-002
├── data/
│   ├── master/
│   │   ├── master_trades.csv          ← ALL trades, append-only
│   │   └── master_stats.csv           ← One row per session
│   ├── traders/
│   │   └── martin/
│   │       └── exports/YYYY-MM-DD/    ← Raw TradingView CSVs
│   └── market/
│       └── YYYY-MM-DD_SYMBOL.csv      ← 5M candles via yfinance
├── reports/
│   ├── master_report.html             ← Overview + current session
│   ├── sessions.html                  ← All sessions, full detail
│   └── observations.html             ← All observations with screenshots
├── screenshots/
│   └── INSTRUMENT_YYYY-MM-DD_*.png
└── scripts/
    ├── update.sh                      ← v2.1
    ├── fetch_market_data.py           ← v2.1
    ├── parse_trades.py                ← v2.1
    └── generate_reports.py            ← v2.3 — generates all 3 report files
```

---

## Data Architecture

### master_trades.csv
All trades from all sessions, all traders. Append-only — never overwrite.
Fields: `trade_id, date, time, symbol, side, type, quantity, fill_price, pnl_usd, commission_usd, session, trader`

### master_stats.csv
One row per session. Fields: `date, session, trader, instrument, trades, wins, losses, be, win_rate, gross_pnl, commissions, net_pnl, start_balance, end_balance, biggest_win, biggest_loss, notes`

---

## Daily Workflow

### What Martin delivers
1. **Balance History CSV** — TradingView → Paper Trading → Balance History → Export
2. **Order History CSV** — TradingView → Paper Trading → Order History → Export (All)
3. **Screenshots** — `Cmd+Shift+4` with Execution Marks visible (NOT TradingView camera button)

### What the AI does
1. Save CSVs to `data/traders/martin/exports/YYYY-MM-DD/`
2. Parse data → update `master_trades.csv` + `master_stats.csv`
3. Check all hypotheses (H1–H5) → update `HYPOTHESES.md`
4. Check for new market situations → update `SITUATIONS.md`
5. Check for new observations → update `OBSERVATIONS.md`
6. Generate all three report files following the Report Structure Rule above
7. Update TERMINOLOGY, METHOD if new insights
8. Update CHANGELOG and this README

### One command after every session
```bash
cd ~/Documents/Trading && ./scripts/update.sh YYYY-MM-DD martin "description"
```

### Open the reports
```bash
open -a Firefox ~/Documents/Trading/reports/master_report.html
```
**Note:** Always use Firefox — Chrome blocks Base64 embedded images in local HTML files.

---

## Screenshot Convention
- **Enable Execution Marks:** Chart settings (gear) → "Trading" tab → "Executions"
- **Connect broker:** TradeNation for USTEC, Forex.com for US30/GER40, WH SelfInvest for JAPAN225
- **Save to:** Google Drive → Trading_Journal → Screenshots
- **Auto-copied** to `screenshots/` on next `update.sh` run

---

## Account System
| Type | Description |
|------|-------------|
| `paper` | Paper trading — no real money |
| `live` | Live account — real money |

P&L comparisons only within same account type. Account resets are documented.

---

## Duplicate Rule
Every trade is uniquely identified by `trade_id = YYYY-MM-DD_OrderID_trader`.
Never overwrite existing entries — append only. `parse_trades.py` enforces this automatically.

---

## Current Status
- **Last update:** 2026-05-29
- **Trading days documented:** 2 (2026-05-28 Day + Japan session 2026-05-28/29)
- **Total trades in master_trades.csv:** 101 closes with P&L
- **Method version:** 0.1
- **README version:** 1.9
- **Terminology version:** 1.3 (includes Kickstarten)
- **Documented behaviour patterns:** 3 (FOMO Top Scale, Context Switch Exit, Concentration Loss)
- **Open hypotheses:** 5 (H1–H5, H4 first confirmed)
- **Documented situations:** 1 (Barbwire Reversal)
- **Documented observations:** 2 (OBS-001 Horizontal Range, OBS-002 Range-to-Trend Transition)
- **Martin account balance:** $21,276.93 (after Japan session)
- **Katya:** not yet started
