<!-- Version: 2.0 | Last updated: 2026-05-29 -->
# Trading Journal — Martin & Katya

## Technical Setup & Recovery
In case of computer failure or new device: see `TECHSTACK.md` for complete step-by-step recovery.

---

## For AI Agents: Read This First

This repository is the central brain of the trading development system for Martin (Trader A) and Katya (Trader B). Everything is documented so a new AI instance can step in seamlessly.

### File Delivery Rule — ALWAYS FOLLOW
1. Only changed files in a ZIP — never the full repo
2. One terminal command: unzip + git add + commit + push
3. Martin runs it — done

```bash
cd ~/Downloads && unzip -o ZIPNAME.zip -d ~/Documents/ && cd ~/Documents/Trading && git add -A && git commit -m "vX.X - description" && git push origin main
```

---

## Document Architecture

| Path | Function | Version | Access |
|------|----------|---------|--------|
| `README.md` | Master context, rules, architecture | v2.0 | Martin: R/W via Git · Claude: R/W via MCP |
| `CHANGELOG.md` | Full version history | v1.9 | Martin: R · Claude: R/W via MCP |
| `CURRENT_SESSION.md` | Quick context for new AI instances | v1.0 | Martin: R · Claude: R/W via MCP |
| `TECHSTACK.md` | Recovery guide, dev environment | v1.1 | Martin: R/W · Claude: R via MCP |
| `KATYA_ONBOARDING.md` | Onboarding guide for Trader B | v1.1 | Martin: R/W · Claude: R/W via MCP |
| `method/METHOD.md` | Core trading method description | v0.1 | Martin: R · Claude: R/W via MCP |
| `method/TERMINOLOGY.md` | All terms + v2.0 KPI definitions | v1.4 | Martin: R · Claude: R/W via MCP |
| `method/HYPOTHESES.md` | Behaviour hypotheses H1–H5 | v1.2 | Martin: R · Claude: R/W via MCP |
| `method/SITUATIONS.md` | Market situation types | v1.0 | Martin: R · Claude: R/W via MCP |
| `method/OBSERVATIONS.md` | Editorial market observations OBS-001–003 | v1.1 | Martin: R · Claude: R/W via MCP |
| `data/master/master_stats.csv` | One row per session, v2.0 schema with all KPIs | v2.0 | Martin: R · Claude: R/W via MCP |
| `data/master/master_trades.csv` | All individual trades, append-only | v1.0 | Martin: R · Claude: R/W via MCP |
| `data/master/dashboard_data.json` | Computed KPIs exported by parser, read by dashboard | v2.0 | Martin: R · Claude: R/W via MCP |
| `data/traders/martin/exports/` | Raw TradingView CSV exports per date | — | Martin: R/W · Claude: R via MCP |
| `data/market/` | 5M candle data per symbol per date | — | Martin: R · Claude: R/W via MCP |
| `reports/master_report.html` | Dashboard landing page (Frontpage tab) | v2.0 | Martin: R/W · Claude: R/W via MCP |
| `reports/sessions.html` | All sessions, newest first | v2.0 | Martin: R/W · Claude: R/W via MCP |
| `reports/observations.html` | All OBS entries with screenshots | v2.0 | Martin: R/W · Claude: R/W via MCP |
| `reports/assets/style_v1.0.css` | Central stylesheet — single source of truth for all UI | v1.0 | Martin: R · Claude: R/W via MCP |
| `scripts/parse_and_export.py` | Reads CSVs, computes v2.0 KPIs, exports JSON | v3.0 | Martin: executes · Claude: R/W via MCP |
| `scripts/generate_reports.py` | Reads JSON, generates HTML reports | v2.4 | Martin: executes · Claude: R/W via MCP |
| `scripts/fetch_market_data.py` | Fetches 5M candles via yfinance | v2.1 | Martin: executes · Claude: R/W via MCP |
| `scripts/update.sh` | Master orchestration script | v2.1 | Martin: executes · Claude: R via MCP |
| `screenshots/` | Chart screenshots, auto-copied from Google Drive | — | Martin: R/W · Claude: R via MCP |

---

## Mandatory Reading Before Every Session
1. `README.md` (this file)
2. `CURRENT_SESSION.md`
3. `method/METHOD.md`
4. `method/TERMINOLOGY.md`
5. `method/HYPOTHESES.md`
6. `method/SITUATIONS.md`
7. `method/OBSERVATIONS.md`
8. `data/master/master_stats.csv`

---

## Report Structure Rule — ALWAYS FOLLOW

Three separate HTML files, shared navigation bar. Generated together by `generate_reports.py`.
Dashboard reads `data/master/dashboard_data.json` via JavaScript fetch — no HTML in the Python script.

**Five tabs (nav links across all three files):**

| Tab | File | Content |
|-----|------|---------|
| Frontpage | `master_report.html` | Global KPIs across all sessions, equity curve, T2BE chart, PP/LP summary, behaviour overview, benchmark, hypotheses |
| Sessions | `sessions.html` | All sessions newest first, each with full stats + barometers + screenshots + annotations |
| Best & Worst | `master_report.html#bestworst` | Top 2 and bottom 2 sessions isolated, side-by-side comparison |
| Observations | `observations.html` | All OBS entries with screenshots, confidence levels, examples |
| Terminology | `observations.html#terminology` | All KPI definitions, barometer thresholds, behaviour patterns |

**Future extension:** Add account type switcher (Paper Trading / Live Trading) to Frontpage. Structure is already present in `dashboard_data.json` via the `account_type` field.

**No duplication:** Every session appears exactly once across all files.

**Typography:**
- Body text, annotations: min 15px
- Labels, captions: min 12px
- Section headers: Inter 600 max — no 800/900 weight
- CSS single source: `reports/assets/style_v1.0.css`

**Screenshots:** Always use the version WITH execution marks. One screenshot per instrument per session.

---

## Hypothesis Check — MANDATORY for every data analysis
Check each hypothesis against new data. Update `HYPOTHESES.md` with date and data reference.
Current: H1 (SMA200 Breakout), H2 (Aircushion Exit), H3 (11–13h UTC), H4 (Hold > Scalp — confirmed), H5 (Barbwire Reversal)

---

## Workflow & Roles

### Martin's role (Trader)
1. Execute trades on TradingView
2. Export Balance History CSV and Order History CSV from Paper Trading panel
3. Save screenshots with Execution Marks enabled (Cmd+Shift+4, NOT TradingView camera)
4. Screenshots auto-sync to Google Drive: `~/Library/CloudStorage/GoogleDrive-arthurdigbysellers2@googlemail.com/My Drive/Trading_Journal/Screenshots/`
5. Run one terminal command to parse, export JSON, generate reports, and push to GitHub

### Claude's role (AI)
1. Read this README and CURRENT_SESSION.md at session start
2. Parse raw TradingView CSVs into master_trades.csv (append-only, dedup by trade_id)
3. Compute all v2.0 KPIs: T2BE, HSR, ITPE, PP/LP metrics, stress barometers
4. Export computed data as dashboard_data.json
5. Generate HTML reports that read the JSON via fetch
6. Check all hypotheses against new data — update HYPOTHESES.md
7. Check for new market situations — update SITUATIONS.md
8. Check for new observations — update OBSERVATIONS.md
9. Update TERMINOLOGY, METHOD if new concepts emerge
10. Update CHANGELOG and this README
11. Deliver only changed files as ZIP + one terminal command

### One command after every session
```bash
cd ~/Documents/Trading && ./scripts/update.sh YYYY-MM-DD martin "description"
```

### Open the reports
```bash
open -a Firefox ~/Documents/Trading/reports/master_report.html
```
Always use Firefox — Chrome blocks local Base64 images.

---

## The Traders

### Martin (Trader A)
- Paper trading for method development
- Instruments: USTEC (TradeNation), GER40 (Forex.com), US30 (Forex.com), SPX (TradingView), JAPAN225 (WH SelfInvest)
- Typical hours: 07:00–09:00 GER40 · 11:00–14:00 USTEC · 16:30–17:30 US30/SPX · 20:51–01:12 UTC JAPAN225
- TradingView: arthurdigbysellers2
- Local repo: ~/Documents/Trading

### Katya (Trader B)
- Parallel setup for behaviour comparison
- GitHub: to be added as Collaborator
- See KATYA_ONBOARDING.md

---

## Data Architecture

### master_stats.csv (v2.0 schema)
One row per session. Fields:
`Session_Date, Trader, Broker_Assets, Net_PnL, Win_Rate, Avg_T2BE, Min_T2BE, Max_T2BE, Net_PnL_PP, Worst_Loss_PP, Most_Lucrative_PP, Net_PnL_LP, Worst_Loss_LP, Most_Lucrative_LP, Max_Cluster_DD_PP, Avg_Cluster_DD_PP, Max_Cluster_DD_LP, Avg_Cluster_DD_LP, Stress_Sentiment_PP, Stress_Sentiment_LP, Stress_Sentiment_T2BE`

### master_trades.csv
All individual trades. Append-only. Dedup by `trade_id = YYYY-MM-DD_OrderID_trader`.

### dashboard_data.json
Generated by `parse_and_export.py`. Contains computed KPIs, session list, screenshot map. Read by HTML reports via JavaScript fetch. Never edit manually.

---

## Known Issues (fix before next parse)
- `{data` directory at repo root is a stale artifact — delete manually via Finder or `rm -rf`
- `master_trades.csv` contains duplicates from a previous double parse run — dedup before next append

---

## Current Status
- README version: 2.0
- Trading days: 2 (2026-05-28 Day + Japan 2026-05-28/29)
- Account balance: $21,276.93
- Method version: 0.1
- Terminology version: 1.4 (T2BE, HSR, ITPE, PP/LP, Stressbarometer)
- Observations: 3 (OBS-001, OBS-002, OBS-003 Key-Level Validation)
- Hypotheses: 5 (H1–H5, H4 confirmed)
- Situations: 1 (Barbwire Reversal)
- Katya: not yet started
- Dashboard v2.0: JSON architecture defined, HTML generation pending new session data
