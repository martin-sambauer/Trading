<!-- Version: 1.4 | Last updated: 2026-05-29 -->
# Terminology & KPI Glossary

*All terms used in the trading method, reports, and dashboard.*
*Language: English (consistent with all method files)*

---

## Market Structure Terms

**Aircushion**
The visible gap between the current price and the SMA20. When price is in a trend, it stays above (long) or below (short) the SMA20 with a consistent gap. A healthy aircushion = trend is stable. A collapsing aircushion = trend is weakening.

**Barbwire**
A cluster of candles with long wicks in both directions and small bodies, forming around a flat SMA20. The market is undecided. Often precedes a strong directional move. See SITUATIONS.md for the full pattern definition.

**Barbwire Reversal**
A Barbwire formation that resolves into a strong move, typically against the prior trend direction. See H5 in HYPOTHESES.md.

**Market Synchronicity**
When multiple correlated instruments (e.g. USTEC, US30, SPX) enter the same Bollinger phase simultaneously. Amplifies the expected move. Use as confirmation before scaling.

**PDH / PDL**
Previous Day High / Previous Day Low. Key reference levels for context and bias.

**PWH / PWL / PWM**
Previous Week High / Low / Mid. Wider context levels.

**TDS (Trend Decision Spot)**
The moment when a ranging market makes its first committed move in one direction — visible as the first candle that closes clearly beyond the Bollinger Band after a compression phase.

---

## Trade Management Terms

**Anchor Trade**
The single best trade in a session — the one held longest, scaled correctly, and exited at target. Benchmark for all other trades in the session.

**Account Fuse**
A hard daily loss limit (e.g. 5% of account). If hit, trading stops for the day. Non-negotiable.

**Mental Stop**
A stop loss level held in mind rather than placed in the order book, to avoid stop hunts. Requires discipline. Only valid when the trader is actively watching.

**Pyramiding**
Adding to a position as it moves in the intended direction. Requires a stable aircushion. See Profit Pyramiding vs Loss Pyramiding below.

**Spike Catcher**
A limit order placed at a key level to catch a sudden price spike. Typically used at support/resistance with a tight stop just beyond the level.

**Kickstarten**
A deliberate risk management technique: entering a position with a stop loss placed just beyond the entry price (near break-even). If the market moves in your direction, the stop trails up. If not, the loss is minimal. The goal is to initiate a position at a key level with minimal risk before the expected move. Note: subject to slippage in fast markets.

---

## KPI Definitions (v2.0)

### T2BE — Time to Break-Even
**What it measures:** How long from the first partial entry until the trade cluster never goes into unrealised loss again.
**Why it matters:** A short T2BE means the entry timing was precise — the market moved in your direction immediately. A long T2BE means you were sweating in drawdown before the trade worked out.
**Values:** Avg_T2BE · Min_T2BE · Max_T2BE
**Barometer thresholds:**
- GREEN: <= 2 minutes (immediate confirmation)
- YELLOW: 2–10 minutes (acceptable stress)
- RED: > 10 minutes (high stress, potential entry timing issue)

### HSR — Hold-to-Scalp Ratio
**What it measures:** Ratio of realised PnL to the potential PnL at the initial take-profit target.
**Formula:** Realised PnL / Potential PnL at initial TP
**Why it matters:** A low HSR means you closed too early (fear scalping). A high HSR means you held with conviction.
**Example:** Initial TP at +$500, realised +$350 → HSR = 0.70 (70%)

### ITPE — Initial TP Efficiency
**What it measures:** How often the initial TP target was actually reached, broken down by TP type.
**TP Types (classified by 5M ATR):**
- Normal TP: distance from entry to TP is within 2 × ATR
- Extreme TP: distance exceeds 3 × ATR — these are the "magnet targets" (key levels, round numbers, structure highs/lows)
**Measurement stages:** 30% · 50% · 80% · 100% of the distance to the initial TP, based on maximum price excursion during hold time.
**Why it matters:** Extreme TPs with high ITPE confirm that key levels act as magnets. Normal TPs with low ITPE signal premature exits.

### Profit Pyramiding (PP)
**What it is:** Adding to a position while the overall cluster is in unrealised profit. The correct way to scale.
**Metrics tracked:**
- Net_PnL_PP: total net profit from PP clusters
- Worst_Loss_PP: the biggest single loss from a PP cluster (risk of giving back gains)
- Most_Lucrative_PP: the single best PP cluster (date + asset)
- Max_Cluster_DD_PP: deepest unrealised drawdown within a PP cluster
- Avg_Cluster_DD_PP: average unrealised drawdown in PP clusters

### Loss Pyramiding (LP)
**What it is:** Adding to a position while the overall cluster is in unrealised loss. High risk if done blindly. Can be valid as a deliberate tactic — see Key-Level Validation Strategy in OBSERVATIONS.md.
**Metrics tracked:**
- Net_PnL_LP: total net profit/loss from LP clusters
- Worst_Loss_LP: the biggest single loss from an LP cluster
- Most_Lucrative_LP: the single best LP cluster (date + asset)
- Max_Cluster_DD_LP: deepest unrealised drawdown within an LP cluster
- Avg_Cluster_DD_LP: average unrealised drawdown in LP clusters

### Risiko-Stressbarometer (Stress Barometer)
**What it measures:** The psychological stress level of a session based on the maximum cluster drawdown relative to account size.
**Three dimensions:** PP stress · LP stress · T2BE stress (reported separately)
**Thresholds:**
- GREEN: cluster drawdown <= 1% of account (comfortable, in control)
- YELLOW: cluster drawdown 1–3% of account (elevated stress, monitor closely)
- RED: cluster drawdown > 3% of account (acute stress, high risk of emotional decision-making)
**Where shown:** Directly in the Session Screenshots section for visual stress post-analysis.

---

## Behaviour Patterns

**Pattern #1 — FOMO Top Scale**
Late entry into an already extended move, immediately scaling to maximum size without buffer reserve. Triggered by the fear of missing out on a trade that has already moved far.

**Pattern #2 — Context Switch Exit**
An external event (appointment, distraction, interruption) forces a trading decision under time pressure — premature exit or wrong direction entry.

**Pattern #3 — Concentration Loss**
Reduced attention due to parallel activities leads to missing clear signals or underperforming in obvious setups. Often accompanied by overtrading in the distracted state.
