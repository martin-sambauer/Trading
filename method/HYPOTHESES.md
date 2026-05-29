<!-- Version: 1.2 | Letzte Änderung: 2026-05-29 -->
# Behaviour Hypotheses
*Confirmed or refuted through daily data.*

---

## Documented Behaviour Patterns

### Pattern #1: FOMO Top Scale
**What:** Late entry into an already far-moved position + immediately scaling to maximum size. No buffer reserve for counter-move.
**Example:** 2026-05-28 12:15 USTEC Long −$966
**Status:** Confirmed · Not repeated in Japan session

### Pattern #2: Context Switch Exit
**What:** External event (appointment, distraction) forces a trading decision under pressure — premature exit or wrong entry.
**Example:** 2026-05-28 13:58 USTEC Short −$336 (dinner appointment)
**Status:** Confirmed · Not repeated in Japan session

### Pattern #3: Concentration Loss
**What:** Reduced attention due to parallel activities leads to missing obvious signals and underperformance.
**Example:** 2026-05-29 Japan session — Barbwire Reversal partially missed due to conversation with Claude. Potential ~$5,000, realized ~$2,267.
**Status:** Active · Dominant pattern in Japan session · 2 occurrences

---

## Open Hypotheses

### H1 — SMA200 Breakout → Trend Duration
**Hypothesis:** Breakout above SMA200 on 5M → trend continues statistically for X minutes / Y points
**Needs:** 30+ events for statistical validity
**Evidence so far:**
- 2026-05-28: USTEC breakout 10:00 UTC → trend until ~13:30 = 3.5 hours, ~300 points
**Status:** 1 data point — open

### H2 — Aircushion Collapse as Exit Signal
**Hypothesis:** Aircushion collapse (price approaching SMA20 after stable gap) is more reliable exit signal than fixed stop loss in points.
**Evidence so far:**
- Japan session: both SL events occurred after aircushion collapse
- Day 1 Context Switch Exit would have been avoidable with aircushion rule
**Status:** Indirect evidence — open, needs direct comparison

### H3 — Best Performance 11–13:30h UTC
**Hypothesis:** Highest win rate and best R:R at USTEC between 11:00 and 13:30 UTC — the first 2.5 hours after US market open.
**Evidence so far:**
- 2026-05-28: $6,514 of $7,349 total in 11–13h = 88.6% of daily P&L in 2.5 hours
- Japan analogy: first hour after market open (21h UTC) = 37% of session P&L
**Status:** First evidence — needs more trading days

### H4 — Hold > Scalp in Trend Phases
**Hypothesis:** In trend phases with stable aircushion, longer holds generate significantly better P&L per trade than quick scalps.
**Evidence so far:**
- Day 1: Hold avg +$612 vs Scalp avg +$12 — 51× difference
- Japan session: Anchor trade avg +$1,114 vs Rest avg +$89 — 12.5× difference
- Consistent across both sessions
**Status:** ✅ Confirmed — consistent across 2 sessions

### H5 — Barbwire Reversal Probability
**Hypothesis:** SMA20 horizontal + fast SMA crossing + Barbwire candles (long wicks both directions, small bodies) → high probability of strong move, often against prior trend. Signal strengthens at: Market Open, after 3h+ trends, at key levels (PDH/PDL/SMA200).
**Evidence so far:**
- 2026-05-29 JAPAN225 (08:30 JST = 22:00 UTC): all signals active → 600+ point move in both directions
- Second Barbwire structure visible at 01:00 UTC — not yet fully documented
- Both directions not fully exploited due to Pattern #3 Concentration Loss
**Important:** Barbwire defines a situation type, not a fixed entry rule. No two situations are identical. Goal: train pattern recognition, not create rigid rules.
**Status:** 2 data points — open, see SITUATIONS.md for full documentation
