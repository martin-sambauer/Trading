<!-- Version: 1.2 | Letzte Änderung: 2026-05-29 -->
# Terminology
*Combination of standard trading terminology and proprietary terms.
All terms are in English for universal AI readability. Continuously updated.*

---

## Proprietary Terms

### Aircushion
Stable, constant gap between price and SMA20 during a trend phase.
Intact aircushion = trend is running. Collapsing aircushion (price approaches SMA20) = warning signal for trend end.
The longer the aircushion stays stable, the stronger the trend phase.

### Battle Zone
Price zone where buyers and sellers fight — identifiable by repeated reversals and tight range.
**Breakout from Battle Zone = strong entry signal.**
Key: no return after breakout confirms the trend.

### Barbwire
A price area where candles show long wicks in BOTH directions — up AND down. Small bodies, long wicks. Price is "trembling" in a tight zone, unable to decide direction. Visually resembles barbed wire on a chart.
Barbwire is NOT an entry signal — it is an **attention signal** that a strong move is building up.
See `method/SITUATIONS.md` for full documentation.

### Barbwire Reversal
Specific situation where Barbwire occurs in a context suggesting an upcoming strong move — typically against the prior trend.
Signal constellation: horizontal SMA20 + fast SMA crossing + Barbwire candles + compressed Bollinger Bands.
First documented: JAPAN225, 2026-05-29.

### Target Derangement Syndrome (TDS)
Psychological error that occurs when price is already 60–80% toward a target but momentum has already reversed.
**Sequence:** Price near target → momentum reverses → instead of exiting, position is scaled up because "so close" → price runs against → large losses.
**Important:** TDS is NOT the unrealistic target itself (that can be a deliberate Spike Catcher) — it's holding onto the target despite reversed momentum combined with scaling up.

### Spike Catcher
Deliberately far-away limit order that is NOT set as a realistic target but to automatically capture unexpected strong moves (spikes).
Used together with a close Mental Stop.
Not TDS — because the expectation was never that the target would be reached.

### Mental Stop
Subjective, experience-based feeling of when a trade is "wrong" — triggers early, often before price reaches a technical level. Protects the individual trade. Closer to price than the Account Fuse.

### Account Fuse
The hard daily loss limit that protects the account — regardless of whether the trade setup still appears intact. Rarely triggered. Absolute lower boundary. Triggers significantly later than the Mental Stop.

### Market Synchronicity
State when multiple markets (USTEC, US30, GER40, SPX) simultaneously show the same phase or pattern.
Inspired by the metronome experiment: 5 metronomes on a shared platform synchronize themselves.
**Types:**
- Candle Sync: candles form similar patterns simultaneously
- Bollinger Phase Sync: markets are simultaneously in range or trend phase

### Frontrunner
Market that leads within a synchronized move. Sets direction and timing.

### Laggard
Market that follows. Offers entry opportunities based on Frontrunner signal.

### Anticyclical Marker
Instrument not directly traded but used as context indicator.
**Example:** OILGAS (Oil) often runs counter to equity indices.

### Anchor Trade
The decisive trade of a day — usually the biggest winner that sets the tone.
**Example:** 2026-05-28 11:13 USTEC Long +$2,911

---

## Behaviour Patterns

### FOMO Top Scale (Pattern #1)
Late entry into an already far-moved position + immediately scaling to maximum.
Double risk: bad entry price + no buffer reserve.
Mental Stop triggers even though setup is often still intact.
**Example:** 2026-05-28 12:15 USTEC Long −$966

### Context Switch Exit (Pattern #2)
External event (appointment, distraction) forces a trading decision under pressure.
**Variants:** Premature exit, or entry into a trade that doesn't match the setup.
**Example:** 2026-05-28 13:58 USTEC Short −$336 (dinner appointment)

### Concentration Loss (Pattern #3)
Reduced focus due to parallel activities (conversations, distractions) leads to missing obvious signals and underperformance.
**Example:** 2026-05-29 Japan session — Barbwire Reversal partially missed due to conversation with Claude. Potential ~$5,000, realized ~$1,763.

---

## Standard Terminology

### SMA (Simple Moving Average)
- **SMA20:** Short-term trend, main reference for aircushion and phase detection
- **SMA200:** Long-term trend, breakout = strong signal

### PDH / PDL
Previous Day High / Previous Day Low.

### PWH / W
Previous Week High / Weekly Level.

### SMA Crossing
SMA20 crosses SMA200. Strong trend signal.

### Bollinger Bands (BB 20)
Volatility band around SMA20 (±2 standard deviations).

### Pyramiding
Stepwise increase of position size while a trade runs. Style: 10-unit blocks up to 30-40 units.

### Confluence
Multiple independent signals pointing in the same direction simultaneously.

### Daily Bias
Overall directional expectation for the day based on the 1D chart.
