<!-- AUTO-UPDATED after every session. New AI: read this first, then README.md -->
# Current Session Context

## How to use this file
You are a new Claude instance. Martin has just opened a new chat because the previous one hit its limit.
Read this file + README.md and you are fully up to speed. No uploads needed from Martin to continue.

## Repo Access
```
https://github.com/martin-sambauer/Trading (private)
```
Martin will provide the GitHub token in the first message if needed for pushing.
Ask him: "Please run: git remote set-url origin https://martin-sambauer:TOKEN@github.com/martin-sambauer/Trading.git"

## Who is Martin
- Daytrader, paper trading on TradingView (account: arthurdigbysellers2 USD)
- Building his own trading method — see method/METHOD.md
- Language: German (talk to him in German)
- Brokers: TradeNation (USTEC), Forex.com (US30/GER40), WH SelfInvest (JAPAN225)

## Current Account Status
- Start: $10,000 (2026-05-28)
- After Day 1 (2026-05-28): $17,348.87 (+73.5%)
- Japan session (2026-05-29): ~$1,763 realized + open position (closed, final P&L unknown)
- Total estimated: ~$19,000+

## What has been built
- Full trading journal system on GitHub
- HTML reports with embedded screenshots (open in Firefox)
- Daily workflow: export CSVs → screenshots → one terminal command
- Method v0.1 documented
- Terminology fully in English
- 5 hypotheses (H1-H5)
- SITUATIONS.md with Barbwire Reversal as first entry
- Katya onboarding guide (KATYA_ONBOARDING.md)

## Last Session — 2026-05-28 (Day 1, complete)
- 33 trades, +$7,349, Win Rate 78.8%
- Anchor Trade: USTEC Long 11:13 +$2,911
- Behaviour cost: -$1,302 (FOMO Top Scale + Context Switch Exit)
- Report: reports/2026-05-28/report_standalone.html (open in Firefox)

## Current Session — 2026-05-29 (Japan, partial)
**Status:** Data uploaded, session partially documented, report NOT yet created

**What happened:**
- Instrument: WHSELFINVEST:JAPAN225CFD
- Session: ~20:52–22:08 UTC+2 (Japanese market open)
- Realized P&L: +$1,763
- Key observation: Barbwire Reversal pattern at market open — SMA20 horizontal, fast crossing, long wicks both directions, then 600+ point move
- Missed opportunity: ~$5,000 possible if Barbwire recognized and both directions traded
- Reason for underperformance: Concentration Loss (Pattern #3) — distracted by Claude conversation

**Files already uploaded in previous chat (not available here — Martin needs to re-upload):**
- paper-trading-balance-history-2026-05-29T01_21_07_720Z_080a3.csv
- paper-trading-order-history-all-2026-05-29T01_20_58_776Z_608bc.csv
- paper-trading-trading-journal-2026-05-29T01_21_11_697Z_fdf83.csv
- paper-trading-positions-2026-05-29T01_21_02_902Z_69e3e.csv
- Screenshots: JAPAN225CFD_2026-05-28_19-09-00_cbdae.png (already in Google Drive)
- Screenshots: JAPAN225CFD_2026-05-28_21-12-25_1b04d.png (already in Google Drive)
- Screenshots: JAPAN225CFD_2026-05-28_21-15-00_6982c.png (already in Google Drive)

**What still needs to be done:**
1. Japan session report erstellen (reports/martin/2026-05-29/)
2. Screenshots komprimieren und pushen
3. master_stats.csv mit Japan-Daten updaten
4. SITUATIONS.md — Barbwire Reversal Beispiel ist bereits dokumentiert

## Open Items
- [ ] Japan session report erstellen
- [ ] Katya GitHub account (waiting for her to create one)
- [ ] Martin as Collaborator inviter sobald Katya Account hat
- [ ] Data migration: data/trades/ → data/traders/martin/trades/
- [ ] embed_screenshots script für standalone reports

## File Delivery Rule (ALWAYS follow)
1. ZIP with only changed files
2. One terminal command: `cd ~/Downloads && unzip -o ZIPNAME.zip -d ~/Documents/ && cd ~/Documents/Trading && git add -A && git commit -m "vX.X - description" && git push origin main`
3. Never ask Martin to manually copy or move files

## How to continue
If Martin uploads CSVs → parse them and create the Japan session report
If Martin just wants to talk → discuss method, hypotheses, or review existing reports
If Martin uploads screenshots → embed them in the report

**First thing to say to Martin in a new chat:**
"Ich bin auf dem aktuellen Stand. Japan Session Report fehlt noch — hast du die finalen CSVs dabei?"
