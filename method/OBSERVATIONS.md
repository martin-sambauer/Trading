<!-- Version: 1.1 | Last updated: 2026-05-29 -->
# Market Observations

*A growing collection of editorial insights about market character and structure.
These are not trading rules and not hypotheses — they are observed patterns in how markets behave.
They describe recurring states that tend to be stable for a period, but can break without warning.
Goal: train the eye to recognise these states early and adjust trading behaviour accordingly.*

*Language: English (consistent with all method files)*
*Screenshots: embedded inline where available*

---

## How to read this file

Each observation has:
- **Core observation** — what is happening, stated directly
- **How it shows on the chart** — concrete visual markers
- **Trading implication** — what to do when you recognise it
- **Break signals** — early warning that the character is shifting
- **Examples** — real sessions with dates and screenshots

Confidence levels:
- `Anecdotal` — seen once or twice, not yet verified
- `Recurring` — seen multiple times across sessions
- `Reliable` — consistent enough to trade with moderate conviction

---

## OBS-001 — Horizontal Alternating Around SMA20 (Pure Range)

**First documented:** 2026-05-29
**Last confirmed:** 2026-05-29
**Confidence:** Anecdotal

### Core observation
In certain market phases, price oscillates repeatedly around a flat SMA20 — crossing it, returning, crossing again. The market has made no directional decision. This state can persist for anywhere from a few minutes to a few hours before resolving into a trend or breaking down entirely.

### How it shows on the chart
- SMA20 is flat or nearly flat — no meaningful slope in either direction
- Price touches the upper and lower Bollinger Band alternately
- No stable aircushion on either side of SMA20
- Candles are mixed — no sequence of higher highs or lower lows
- Bollinger Bands may be contracting (energy building) or moderately wide

### Trading implication
Fade the Bollinger Bands: enter short near the upper band, enter long near the lower band.
- Use small position sizes — there is no trend to ride
- Keep stops tight — the range defines the risk
- Take profit quickly — the move ends at the opposite band, not beyond it
- Do not pyramid — the market reverses before large positions become profitable
- Stop trading this way the moment SMA20 begins to slope

### Break signals
- SMA20 starts to develop a visible slope
- One side of the Bollinger Band is touched repeatedly without a full reversal to the other side
- Higher lows (bullish break) or lower highs (bearish break) begin forming
- A candle closes significantly beyond the Bollinger Band without snapping back

### Examples
*(No isolated example yet — see OBS-002 Phase 1 for the transition context)*

---

## OBS-002 — Alternating Character That Transforms Into a Trending Channel

**First documented:** 2026-05-29
**Last confirmed:** 2026-05-29
**Confidence:** Anecdotal

### Core observation
A ranging phase (like OBS-001) can gradually transform into a directed move without losing its alternating character. The market does not switch abruptly from range to trend — it drifts. The key early signal is a sequence of higher lows (in an upward transition) visible before the direction becomes obvious to most traders. The alternating behaviour persists into the trend but shifts into the upper (or lower) Bollinger segment, and corrections no longer reach the opposite band.

### How it shows on the chart — three phases

**Phase 1 — Pure Range (OBS-001)**
SMA20 horizontal. Price bounces between both Bollinger Bands. No direction.

**Phase 2 — Transition**
SMA20 begins to slope gently. Corrections fail to reach the opposite band completely. A trendline connecting the lows begins to rise. This phase lasts roughly 20–60 minutes on the 5M chart.

**Phase 3 — Trending Channel**
Price moves primarily in the upper (uptrend) or lower (downtrend) Bollinger segment. Corrections pull back toward SMA20 but not through it. Aircushion is establishing.

### Trading implication
**Phase 1:** Bollinger Band fades as in OBS-001.

**Phase 2 (the critical recognition moment):**
- Stop fading the bands
- Watch for the trendline of higher lows to confirm
- Wait for price to break out of the range on the trend side
- This is the highest-value entry point — early in the trend, before it is obvious

**Phase 3:**
- Trade with the trend
- Use corrections to SMA20 as entry opportunities
- Pyramiding is appropriate — the aircushion supports it
- Hold longer than feels comfortable — the alternating character creates false exit signals

### Break signals
- Price breaks through SMA20 and does not recover within 2–3 candles
- SMA20 flattens again after trending
- The amplitude of counter-moves increases noticeably

### Examples
**Japan Session 2026-05-29 — JAPAN225CFD, 5M**
Phase 1 (~20:50–22:00 UTC): Barbwire zone at market open, flat SMA20.
Phase 2 (~22:00–22:30 UTC): SMA-crossing, higher lows forming — optimal entry window, missed.
Phase 3 (~22:30–01:00 UTC): Trend channel in upper Bollinger segment, counter-trend trades taken instead of following.
Potential: ~$5,000. Realised: ~$2,267 (Pattern #3 Concentration Loss).

![JAPAN225CFD Session Overview](../screenshots/JAPAN225CFD_2026-05-28_19-09-00_cbdae.png)
![JAPAN225CFD with Execution Marks](../screenshots/JAPAN225CFD_2026-05-29_01-29-07_e79b3.png)

---

## OBS-003 — Key-Level Validation Strategy (Tactical Loss Pyramiding)

**First documented:** 2026-05-29
**Last confirmed:** 2026-05-29
**Confidence:** Anecdotal — tactical framework, not yet statistically verified

### Core observation
Loss Pyramiding (adding to a losing position) is generally destructive — but there is one context where it becomes a deliberate, edge-positive tactic: when a position was entered in the direction of the primary trend, and the market temporarily moves against the position toward a significant key level (support for longs, resistance for shorts). At that level, a second entry is made. This is not emotional averaging — it is a pre-planned tactical entry with a defined stop just beyond the key level.

The mathematical advantage: the second entry is made at the best possible price (directly at support), and if the market respects the level, the combined cluster becomes massively profitable with a tight combined stop. If the level breaks, the position is killed immediately with a small additional loss.

This tactic must be distinguished from blind loss averaging. The difference is:
- **Tactical LP:** pre-planned, at a specific level, with a defined stop just beyond it
- **Blind averaging:** reactive, no defined stop, driven by hope rather than structure

### How to identify a valid Key-Level entry point
- The level is a prior structure high/low, a round number, a daily PDH/PDL, or a Bollinger Band confluence
- The primary trend is still intact (SMA20 still slopes in the intended direction)
- The retracement to the level is orderly — not a sharp reversal with increasing momentum
- The level has been respected at least once before in the current session or on the daily chart

### Execution
1. Primary entry: above the key level in trend direction
2. If price retraces to the key level: add second position at or just above the level
3. Stop for the entire cluster: just below the key level (for longs) — tight, defined, non-negotiable
4. If the level breaks: exit immediately, do not wait
5. If the level holds: hold the combined cluster, the average entry is now significantly better

**Extension:** If account PnL and risk management allow, a third level can be used if there is a second significant support below the first. Each level must have its own stop just beyond it.

### The risk — why this tactic is dangerous if misapplied
- Requires pre-planning before the move happens, not in the heat of a retracement
- The stop must be placed and honoured before the second entry is made
- Works only in trend context — not in a ranging market (OBS-001)
- Increases Loss Pyramiding metrics (Net_PnL_LP, Max_Cluster_DD_LP) — these must be tracked and reviewed

### How it shows in the data
- Max_Cluster_DD_LP will spike — this is expected and acceptable if the tactic is working
- Stress_Sentiment_LP may show RED even in a profitable session — review the context
- Most_Lucrative_LP should over time reflect these tactical entries

### Relationship to other metrics
- T2BE will be long for tactical LP entries (the position is in drawdown until the level holds) — HIGH T2BE is acceptable in this specific context
- HSR should be high if the level holds and the full TP is reached

### Examples
*(No direct example documented yet — Japan session had LP but not at a pre-planned key level. First confirmed tactical LP to be documented when it occurs.)*

---

## Further Observations (to be documented)

- **Market Open Momentum** — strong directed move in the first 15–30 minutes after market open, before any ranging phase establishes
- **Aircushion Compression** — the aircushion narrows gradually before a trend reversal, distinct from a sudden Barbwire formation
- **Multi-Market Phase Synchronicity** — when USTEC, US30 and SPX enter the same Bollinger phase simultaneously, the move is amplified
