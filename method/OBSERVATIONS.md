<!-- Version: 1.0 | Last updated: 2026-05-29 -->
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
In certain market phases, price oscillates repeatedly around a flat SMA20 — crossing it, returning, crossing again. The market has made no directional decision. This state can persist for anywhere from 30 minutes to a few hours before resolving into a trend or breaking down entirely.

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
- Volume or momentum spike in one direction

### Examples
*(No isolated example yet — see OBS-002 Phase 1 for the transition context)*

---

## OBS-002 — Alternating Character That Transforms Into a Trending Channel

**First documented:** 2026-05-29
**Last confirmed:** 2026-05-29
**Confidence:** Anecdotal

### Core observation
A ranging phase (like OBS-001) can gradually transform into a directed move without losing its alternating character. The market does not switch abruptly from range to trend — it drifts. The key early signal is a sequence of higher lows (in an upward transition) visible before the direction becomes obvious to most traders. The alternating behaviour persists into the trend but shifts into the upper (or lower) Bollinger segment, and corrections no longer reach the opposite band.

This transition is gradual and easy to miss. It is more useful to recognise it in real time than to identify it in hindsight.

### How it shows on the chart — three phases

**Phase 1 — Pure Range (OBS-001)**
SMA20 horizontal. Price bounces between both Bollinger Bands. No direction.

**Phase 2 — Transition**
SMA20 begins to slope gently. Corrections still look like full reversals but fail to reach the opposite band completely. A trendline connecting the lows begins to rise (or fall). The SMA-crossing behaviour continues but price spends more time on one side. This phase lasts roughly 20–60 minutes on the 5M chart.

**Phase 3 — Trending Channel**
Price moves primarily in the upper (uptrend) or lower (downtrend) Bollinger segment. Corrections pull back toward SMA20 but not through it — SMA20 acts as support (or resistance). Aircushion is establishing. The alternating character is still present but contained within the trend direction.

### Trading implication
**Phase 1:** Bollinger Band fades as in OBS-001.

**Phase 2 (transition — the critical recognition moment):**
- Stop fading the bands
- Reduce or close counter-trend positions
- Watch for the trendline of higher lows to confirm
- Wait for price to break out of the range on the trend side before entering
- This is the highest-value entry point — early in the trend, before it is obvious

**Phase 3:**
- Trade with the trend
- Use corrections to SMA20 as entry opportunities
- Pyramiding is appropriate — the aircushion supports it
- Hold positions longer than feels comfortable — the alternating character creates false exit signals

### Break signals
- Price breaks through SMA20 convincingly and does not recover within 2–3 candles
- SMA20 flattens again after trending
- The amplitude of counter-moves increases noticeably
- A candle closes below the most recent higher low (for uptrend)

### Examples

**Japan Session 2026-05-29 — JAPAN225CFD, 5M**

The full session shows all three phases clearly on the chart below.

**Phase 1 (Pure Range, ~20:50–22:00 UTC):**
At the start of the Japan session (market open ~22:00 JST = 13:00 UTC), price oscillated in a tight zone. SMA20 was flat. Both Bollinger Bands were touched alternately. This is the Barbwire zone described in SITUATIONS.md — the alternating character was compressed into long-wick candles, energy building.

**Phase 2 (Transition, ~22:00–22:30 UTC):**
SMA-crossing occurred. Higher lows became visible — a rising trendline could be drawn connecting the correction lows. Price still made counter-moves but they were shallower each time. This was the optimal entry window for a long position with the emerging trend.

**Phase 3 (Trending Channel, ~22:30–01:00 UTC):**
Price moved primarily in the upper Bollinger segment. Corrections returned to SMA20 but not through it. The alternating character persisted — short counter-moves were visible throughout (the red execution arrows in the chart) — but each correction was a buying opportunity, not a reversal signal. The SMA200 on the 5M chart (pink line) rose steadily from ~63,000 to ~65,000, confirming the trend strength.

**What was missed:**
The transition (Phase 2) was not cleanly recognised at the time. Entry came after the trend was already established, reducing the potential gain significantly. The correction moves in Phase 3 triggered several unnecessary counter-trend trades (Pattern #3 Concentration Loss).

**Potential vs. realised:**
Had Phase 2 been recognised and a long position entered at the trendline breakout (~22:00–22:15 UTC), the full 600+ point move would have been capturable in both directions. Realised: ~$2,267. Potential with clean execution: ~$5,000.

![JAPAN225CFD Session Overview — 2026-05-29](../screenshots/JAPAN225CFD_2026-05-28_19-09-00_cbdae.png)
*JAPAN225CFD 5M — 2026-05-28/29. Right chart: the three phases are visible. The tight alternating zone at the left of the 5M chart (Phase 1), the rising trendline and SMA-crossing in the middle (Phase 2), and the sustained upper-band trending channel in the right portion (Phase 3). The pink SMA200 line confirms the trend context.*

![JAPAN225CFD with Execution Marks — 2026-05-29](../screenshots/JAPAN225CFD_2026-05-29_01-29-07_e79b3.png)
*JAPAN225CFD 5M with execution marks. The dense cluster of opposing arrows shows the counter-trend trades made during Phase 3 — these were correct in recognising the alternating character but wrong in trading against the dominant direction.*

---

## Further Observations (to be documented)

- **Market Open Momentum** — strong directed move in the first 15–30 minutes after market open, before any ranging phase establishes
- **Aircushion Compression** — the aircushion narrows gradually before a trend reversal, distinct from a sudden Barbwire formation
- **Multi-Market Phase Synchronicity** — when USTEC, US30 and SPX enter the same Bollinger phase simultaneously, the move is amplified
