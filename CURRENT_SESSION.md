<!-- AUTO-UPDATED after every session. New AI: read this first, then README.md -->
# Current Session Context

## For New AI: How to start
1. Read this file completely
2. Read README.md v2.0
3. Read method/OBSERVATIONS.md v1.1 (OBS-003 Key-Level Validation Strategy neu)
4. Read data/master/master_stats.csv (3 Sessions, v2.0 Schema)
5. Say to Martin in German: "Ich bin auf dem aktuellen Stand. [Was noch fehlt]."

## Filesystem MCP
Direct access to /Users/martinsambauer/Documents/Trading/
Push command: cd ~/Documents/Trading && ./scripts/update.sh YYYY-MM-DD martin "description"

## Account Status
- Start: $10,000 (2026-05-28)
- After Day 1 (2026-05-28): $17,348.87 (+73.5%)
- After Japan Session (2026-05-28/29): $21,276.93 (+112.8%)
- After Day 3 (2026-05-29): $27,797 (+178%)
- Total: +$17,797 in 3 Handelstagen

## Sessions
### Day 1 — 2026-05-28
- 33 Trades, +$7,349, Win Rate 78.8%
- Anchor: USTEC Long 11:13 +$2,911
- Behaviour: Pattern #1 FOMO Top Scale -$966, Pattern #2 Context Switch -$336

### Japan Session — 2026-05-28/29
- 68 Fills, +$3,880, Win Rate 78.6%
- Bester Trade: Limit TP @ 66,014 +$1,240
- Kickstarten SL -$801 (Technik korrekt, Slippage ungünstig)
- Pattern #3 Concentration Loss (Claude-Konversation)

### Day 3 — 2026-05-29
- ~48 Fills, +$6,568, Win Rate 71.4%
- Anchor: US30 Long 40 Units 10:37–11:53 UTC +$4,394
- Taktisches LP am Support 50,860–50,875 (OBS-003) korrekt
- Pattern #4 TDS NEU: Short nach TP in 11h-UTC-Zone ~-$3,000 Schaden
- Pattern #3 Concentration Loss: Claude-Konversation während Session

## New Pattern documented
Pattern #4 — TDS (Target Derangement Syndrome):
Nach grossem TP impulsiv in Gegenrichtung handeln obwohl Methoden-Regel dagegen spricht.
Day 3: Short nach US30-Exit 11:53 UTC — gegen H3 (11h-Zone = Long-Bias).
Regel: Nach TP in 11h-UTC-Zone kein Short bis 13:30 UTC oder SMA20 dreht.

## Report System (3 HTML files, shared nav)
open -a Firefox ~/Documents/Trading/reports/master_report.html  # Uebersicht + Day 3
open -a Firefox ~/Documents/Trading/reports/sessions.html       # Alle Sessions
open -a Firefox ~/Documents/Trading/reports/observations.html   # OBS + Terminology

## Hypotheses Updated
- H3 (11h UTC Peak Performance): BESTAETIGT nach Day 3 (+$4,394 in 11–13h = 67% des Session-P&L)
- H4 (Hold > Scalp): WEITERHIN BESTAETIGT — Day 3 Anchor 26 Min = +$4,394

## Known Issues
- master_trades.csv: Duplikate aus altem Parse — vor nächstem Parse bereinigen
- {data Ordner im Root: manuell löschen via rm -rf ~/Documents/Trading/\{data
- Screenshots für Day 3 noch nicht in screenshots/ (kommen via update.sh aus Google Drive)
- generate_reports.py v2.3 noch aktiv (JSON-Architektur noch nicht implementiert)
