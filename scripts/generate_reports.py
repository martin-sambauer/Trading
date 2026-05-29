#!/usr/bin/env python3
"""
generate_reports.py v2.3
Generiert drei separate HTML-Dateien mit gemeinsamer Navigation:
  reports/master_report.html  — Übersicht + aktuelle Session
  reports/sessions.html       — Alle Sessions (vollständig, chronologisch)
  reports/observations.html   — Alle Observations mit Screenshots
"""

import os, base64
from io import BytesIO

REPO_DIR       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(REPO_DIR, "screenshots")
REPORTS_DIR    = os.path.join(REPO_DIR, "reports")

# ─── Image helpers ────────────────────────────────────────────────────────────

def img_to_base64(path, max_width=1400, quality=72):
    try:
        from PIL import Image
        img = Image.open(path).convert("RGB")
        if img.width > max_width:
            ratio = max_width / img.width
            img = img.resize((max_width, int(img.height * ratio)), Image.LANCZOS)
        buf = BytesIO()
        img.save(buf, format="JPEG", quality=quality, optimize=True)
        return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"
    except ImportError:
        with open(path, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    except Exception as e:
        print(f"  Fehler {path}: {e}")
        return None

def collect_screenshots():
    shots = {}
    if not os.path.exists(SCREENSHOTS_DIR):
        return shots
    for fname in sorted(os.listdir(SCREENSHOTS_DIR)):
        if fname.lower().endswith(('.png', '.jpg', '.jpeg')):
            fpath = os.path.join(SCREENSHOTS_DIR, fname)
            print(f"  Einbetten: {fname}...")
            uri = img_to_base64(fpath)
            if uri:
                shots[fname] = uri
    return shots

# ─── Shared CSS & nav ─────────────────────────────────────────────────────────

def nav(active):
    pages = [
        ("master_report.html", "Übersicht"),
        ("sessions.html",      "Sessions"),
        ("observations.html",  "Observations"),
    ]
    links = ""
    for href, label in pages:
        cls = ' class="active"' if href == active else ""
        links += f'<a href="{href}"{cls}>{label}</a>'
    return f'''<nav class="nav">
  <div class="nav-logo">Martin<span>.</span>Trading</div>
  {links}
</nav>'''

CSS = '''
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&family=Inter:wght@400;500;600&display=swap');
:root {
  --bg:#08090d; --s1:#0d1018; --s2:#12161f; --border:#1a2030; --border2:#222b3a;
  --gold:#e8b84b; --green:#38c87a; --red:#e85858; --blue:#4f9de0; --purple:#9b7fe8;
  --text:#b8c4da; --muted:#354057; --muted2:#5d6f8a;
  --mono:'DM Mono',monospace; --sans:'Inter',sans-serif;
}
* { margin:0; padding:0; box-sizing:border-box }
html { scroll-behavior:smooth }
body { background:var(--bg); color:var(--text); font-family:var(--mono);
       font-size:15px; line-height:1.75 }

.nav { position:sticky; top:0; z-index:100; background:rgba(8,9,13,0.97);
  backdrop-filter:blur(16px); border-bottom:1px solid var(--border);
  padding:0 48px; display:flex; align-items:center; height:46px }
.nav-logo { font-family:var(--sans); font-weight:600; font-size:14px; color:#fff;
  margin-right:36px; letter-spacing:0.01em; flex-shrink:0 }
.nav-logo span { color:var(--gold) }
.nav a { font-size:12px; color:var(--muted2); text-decoration:none; padding:0 16px;
  height:46px; display:flex; align-items:center; border-bottom:2px solid transparent;
  transition:color 0.15s; white-space:nowrap }
.nav a:hover { color:var(--text) }
.nav a.active { color:var(--gold); border-bottom-color:var(--gold) }

.hero { padding:56px 48px 44px; border-bottom:1px solid var(--border) }
.hero-eyebrow { font-size:11px; letter-spacing:0.18em; text-transform:uppercase;
  color:var(--muted2); margin-bottom:12px }
.hero-title { font-family:var(--sans); font-size:34px; font-weight:600; color:#e0e8f4;
  letter-spacing:-0.01em; line-height:1.15; margin-bottom:8px }
.hero-title span { color:var(--gold) }
.hero-sub { font-size:14px; color:var(--muted2); margin-bottom:36px }
.kpi-row { display:grid; grid-template-columns:repeat(5,1fr); gap:1px; background:var(--border) }
.kpi { background:var(--s1); padding:20px 24px }
.kpi-label { font-size:11px; letter-spacing:0.12em; text-transform:uppercase;
  color:var(--muted); margin-bottom:8px }
.kpi-val { font-family:var(--sans); font-size:26px; font-weight:600; line-height:1 }
.kpi-val.g{color:var(--green)} .kpi-val.gold{color:var(--gold)}
.kpi-val.w{color:#e0e8f4}      .kpi-val.r{color:var(--red)}
.kpi-sub { font-size:12px; color:var(--muted); margin-top:5px }

.page { max-width:1300px; margin:0 auto; padding:0 48px 80px }
.section { margin-top:52px }
.sec-head { display:flex; align-items:baseline; gap:14px; margin-bottom:20px;
  border-bottom:1px solid var(--border); padding-bottom:10px }
.sec-title { font-family:var(--sans); font-size:11px; font-weight:600;
  letter-spacing:0.18em; text-transform:uppercase; color:var(--muted2) }
.sec-meta { font-size:12px; color:var(--muted) }

.page-header { padding:44px 48px 0 }
.page-label { font-size:10px; letter-spacing:0.22em; text-transform:uppercase;
  color:var(--muted); margin-bottom:6px }
.page-title { font-family:var(--sans); font-size:28px; font-weight:600; color:#d0daea;
  letter-spacing:-0.01em; margin-bottom:4px }
.page-title span { color:var(--gold) }
.page-sub { font-size:14px; color:var(--muted2); margin-bottom:0 }

.g2 { display:grid; grid-template-columns:1fr 1fr; gap:14px }
.g3 { display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px }

.card { background:var(--s1); border:1px solid var(--border); padding:22px 26px }
.card-title { font-size:11px; letter-spacing:0.12em; text-transform:uppercase;
  color:var(--muted); margin-bottom:14px }

svg.equity { width:100%; height:220px; display:block }

.bar-chart { display:flex; gap:3px; height:100px; align-items:flex-end; margin-bottom:10px }
.bar { flex:1; border-radius:2px 2px 0 0; min-height:3px; cursor:default; position:relative }
.bar:hover::after { content:attr(data-tip); position:absolute; bottom:108%; left:50%;
  transform:translateX(-50%); background:var(--s2); border:1px solid var(--border2);
  padding:4px 10px; font-size:12px; white-space:nowrap; z-index:10 }

.bench-row { display:flex; align-items:center; gap:12px; margin-bottom:11px }
.bench-name { font-size:14px; color:var(--muted2); width:230px; flex-shrink:0 }
.bench-track { flex:1; height:5px; background:var(--border2); position:relative }
.bench-fill { height:100%; position:absolute; left:0; top:0 }
.bench-num { font-size:14px; font-weight:500; width:60px; text-align:right; flex-shrink:0 }

.beh-table { width:100%; border-collapse:collapse }
.beh-table th { font-size:11px; letter-spacing:0.1em; text-transform:uppercase;
  color:var(--muted); padding:10px 14px; text-align:left;
  border-bottom:1px solid var(--border); font-weight:400 }
.beh-table td { padding:13px 14px; border-bottom:1px solid rgba(26,32,48,0.7);
  vertical-align:top; font-size:14px }

.tag { display:inline-block; padding:2px 9px; border-radius:2px; font-size:11px;
  font-weight:600; letter-spacing:0.04em }
.tag.r    { background:rgba(232,88,88,0.12);   color:var(--red) }
.tag.g    { background:rgba(56,200,122,0.12);  color:var(--green) }
.tag.gold { background:rgba(232,184,75,0.12);  color:var(--gold) }
.tag.m    { background:rgba(53,64,87,0.3);     color:var(--muted2) }

.hypo { background:var(--s1); border:1px solid var(--border); padding:18px 22px }
.hypo-id { font-size:11px; letter-spacing:0.12em; text-transform:uppercase;
  color:var(--muted); margin-bottom:5px }
.hypo-text { font-size:15px; color:var(--text); line-height:1.75; margin-bottom:10px }
.hypo-ev { font-size:13px; color:var(--muted2); line-height:1.65 }

.badge { display:inline-block; padding:2px 9px; border-radius:2px; font-size:11px;
  font-weight:600; letter-spacing:0.07em; text-transform:uppercase; margin-bottom:10px }
.badge.ev { background:rgba(232,184,75,0.12); color:var(--gold) }
.badge.ok { background:rgba(56,200,122,0.12); color:var(--green) }
.badge.op { background:rgba(53,64,87,0.2);    color:var(--muted2) }

.insight { background:var(--s1); border:1px solid var(--border);
  border-left:2px solid var(--gold); padding:18px 22px; margin-bottom:12px }
.insight h4 { font-family:var(--sans); font-size:14px; font-weight:600;
  color:var(--gold); margin-bottom:8px }
.insight p { font-size:15px; color:var(--text); line-height:1.85 }
.insight.g { border-left-color:var(--green) } .insight.g h4 { color:var(--green) }
.insight.r { border-left-color:var(--red) }   .insight.r h4 { color:var(--red) }
.ins-row { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:20px }

.sess-block { background:var(--s1); border:1px solid var(--border); margin-bottom:44px }
.sess-head { display:grid; grid-template-columns:1fr auto; align-items:start;
  padding:24px 28px 20px; border-bottom:1px solid var(--border) }
.sess-name { font-family:var(--sans); font-size:18px; font-weight:600;
  color:#d8e2f4; margin-bottom:4px }
.sess-date { font-size:13px; color:var(--muted2) }
.sess-pnl  { font-family:var(--sans); font-size:30px; font-weight:600 }
.sess-stats { display:grid; grid-template-columns:repeat(6,1fr);
  border-bottom:1px solid var(--border) }
.stat { padding:16px 20px; border-right:1px solid var(--border) }
.stat:last-child { border-right:none }
.stat-label { font-size:11px; letter-spacing:0.1em; text-transform:uppercase;
  color:var(--muted); margin-bottom:5px }
.stat-val { font-family:var(--sans); font-size:18px; font-weight:600 }
.sess-body { padding:26px 28px }

.chart-block { margin-bottom:32px }
.chart-title { font-family:var(--sans); font-size:14px; font-weight:500;
  color:var(--muted2); margin-bottom:8px }
.chart-ann { display:grid; grid-template-columns:2fr 1fr 1fr;
  border:1px solid var(--border); border-top:none; background:var(--s2) }
.ann-col { padding:16px 20px; border-right:1px solid var(--border) }
.ann-col:last-child { border-right:none }
.ann-label { font-size:11px; letter-spacing:0.12em; text-transform:uppercase;
  color:var(--muted); margin-bottom:9px }
.ann-body { font-size:15px; color:var(--text); line-height:1.8 }
.ann-list { list-style:none; padding:0 }
.ann-list li { font-size:15px; line-height:1.75; padding:3px 0 }
.ann-list.green li::before { content:"✓ "; color:var(--green) }
.ann-list.red   li::before { content:"✗ "; color:var(--red) }

/* Observations page */
.obs-block { background:var(--s1); border:1px solid var(--border); margin-bottom:44px }
.obs-head { padding:22px 28px 18px; border-bottom:1px solid var(--border) }
.obs-id { font-size:10px; letter-spacing:0.2em; text-transform:uppercase;
  color:var(--muted); margin-bottom:4px }
.obs-name { font-family:var(--sans); font-size:18px; font-weight:600; color:#d8e2f4 }
.obs-body { padding:24px 28px }
.obs-section-title { font-family:var(--sans); font-size:11px; font-weight:600;
  letter-spacing:0.15em; text-transform:uppercase; color:var(--muted2);
  margin:20px 0 8px }
.obs-text { font-size:15px; color:var(--text); line-height:1.8 }
.obs-text ul { list-style:none; padding:0; margin-top:6px }
.obs-text ul li { padding:2px 0; font-size:15px; line-height:1.75 }
.obs-text ul li::before { content:"— "; color:var(--muted2) }
.obs-chart { margin-top:20px }
.obs-chart img { width:100%; display:block; border:1px solid var(--border) }
.obs-caption { font-size:13px; color:var(--muted2); line-height:1.6;
  padding:10px 14px; background:var(--s2); border:1px solid var(--border);
  border-top:none; font-style:italic }

.footer { margin-top:72px; padding:22px 0; border-top:1px solid var(--border);
  display:flex; justify-content:space-between; font-size:12px; color:var(--muted) }
'''

def html_shell(title, active_nav, body):
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Martin Trading</title>
<style>{CSS}</style>
</head>
<body>
{nav(active_nav)}
{body}
</body>
</html>'''

# ─── Component builders ───────────────────────────────────────────────────────

def chart_block(src, title, what_happened, highlights, weaknesses):
    img = (f'<img src="{src}" style="width:100%;display:block;border:1px solid var(--border)">'
           if src else
           f'<div style="background:var(--s1);border:1px solid var(--border);padding:40px;text-align:center;color:var(--muted)">{title} — Screenshot nicht gefunden</div>')
    hl = "".join(f"<li>{h}</li>" for h in highlights)
    wk = "".join(f"<li>{w}</li>" for w in weaknesses)
    return f'''<div class="chart-block">
  <div class="chart-title">{title}</div>
  {img}
  <div class="chart-ann">
    <div class="ann-col"><div class="ann-label">Was passiert ist</div><div class="ann-body">{what_happened}</div></div>
    <div class="ann-col"><div class="ann-label" style="color:var(--green)">✓ Highlights</div><ul class="ann-list green">{hl}</ul></div>
    <div class="ann-col"><div class="ann-label" style="color:var(--red)">✗ Fehler / Schwächen</div><ul class="ann-list red">{wk}</ul></div>
  </div>
</div>'''

def session_block(name, date_str, pnl, pnl_color, stats, body_html):
    stats_html = "".join(
        f'<div class="stat"><div class="stat-label">{s[0]}</div><div class="stat-val" style="color:{s[2]}">{s[1]}</div></div>'
        for s in stats)
    return f'''<div class="sess-block">
  <div class="sess-head">
    <div><div class="sess-name">{name}</div><div class="sess-date">{date_str}</div></div>
    <div class="sess-pnl" style="color:{pnl_color}">{pnl}</div>
  </div>
  <div class="sess-stats">{stats_html}</div>
  <div class="sess-body">{body_html}</div>
</div>'''

# ─── Shared content builders ──────────────────────────────────────────────────

def build_charts_and_sessions(shots):
    ustec  = shots.get("USTEC_2026-05-28_20-16-56_68476.png",    "")
    ger40  = shots.get("GER40_2026-05-28_20-18-29_f7a92.png",    "")
    us30   = shots.get("US30_2026-05-28_20-21-55_3e5f2.png",     "")
    japan1 = shots.get("JAPAN225CFD_2026-05-28_19-09-00_cbdae.png", "")
    japan2 = shots.get("JAPAN225CFD_2026-05-29_01-29-07_e79b3.png", "")

    c_ger40 = chart_block(ger40, "GER40 — Früh-Session 07:36–08:08 UTC",
        "DAX-Eröffnung mit kurzem Short-Move. Links 1D: Aufwärtstrend nahe PDH — Range-Kontext. Rechts 5M: Sofortiger Sell-off bei Open von 25,073. Bollinger Bands weit geöffnet. Drei profitable Shorts, dann Long-Gegentrade gegen den Trend.",
        ["Richtung bei Open korrekt erkannt — Short", "3 Shorts in Folge profitabel (+$713 +$39 +$68)", "Sauberes Timing direkt bei Market Open"],
        ["Long-Einstieg 08:08 gegen den Trend (-$8) — unnötig", "Zu früh aus Short raus — Markt fiel auf 24,700 weiter", "Positionsgrösse zu klein"])

    c_ustec = chart_block(ustec, "USTEC — Hauptsession 11:08–13:58 UTC",
        "Links 1D: USTEC weit über SMA200 (25,441). Rechts 5M: Sell-off bei Open bis 29,600, dann SMA200-Breakout und SMA-Crossing ~10:00 UTC. Long-Aufbau 10 → 40+ Units. Anchor Trade 11:13 @ 30,055 → +$2,911. Markt ohne Gegenbewegung bis 30,270. Ab 13:30 Aircushion-Kollaps.",
        ["SMA200 Breakout + SMA-Crossing korrekt als Einstiegssignal erkannt", "Anchor Trade pyramidiert und bis TP gehalten → +$2,911", "88% des Tages-P&L in 2.5 Stunden"],
        ["12:15 FOMO Top Scale: 40 Units zu Top-of-Range → -$966 (Pattern #1)", "13:58 Context Switch Exit: Short unter Termindruck → -$336 (Pattern #2)", "Aircushion-Kollaps als Exit-Signal nicht konsequent angewendet"])

    c_us30 = chart_block(us30, "US30 — Afternoon Session 16:43–17:03 UTC",
        "Links 1D: US30 nahe ATH (51,139) bei 50,700. Rechts 5M: Aufwärtstrend mit stabilem Aircushion. SPX als Sondierungsinstrument, dann Long-Aufbau US30. Markt-Synchronizität SPX/US30 bestätigt Richtung.",
        ["SPX als Confirmation-Instrument vor US30-Einstieg", "Markt-Synchronizität erkannt und genutzt", "+$680 mit geringem Aufwand"],
        ["Positionsgrösse zu klein für ATH-Kontext", "Zu früh aus US30 raus — Markt lief noch bis 50,720"])

    c_japan1 = chart_block(japan1, "JAPAN225CFD — Session-Überblick",
        "Links 1D: JAPAN225 im massiven Aufwärtstrend ~61,000 auf 65,755. SMA200 weit unten (52,466). Rechts 5M: Eröffnung ~22:00 UTC mit Volatilität. Klarer Aufwärtstrend bis 65,800 um 23:00 UTC. Konsolidierung bis Mitternacht, dann Push auf 66,200+. SMA200 steigt mit — Aircushion enger gegen Ende.",
        ["Trend von 63,000 bis 66,200 vollständig mitgemacht", "Trendstruktur über 4+ Stunden erkannt"],
        ["Barbwire-Zone bei Eröffnung nicht voll genutzt", "Spätphase nach Mitternacht zu aktiv betraded"])

    c_japan2 = chart_block(japan2, "JAPAN225CFD — Session mit Execution Marks",
        "Links 1D: PDH 66,695 noch nicht erreicht. Rechts 5M: Alle Executions sichtbar. Dichte Aktivität 20:00–22:00 UTC. Viele rote Pfeile nach unten während Aufwärtsbewegung. Bester Trade: Limit TP @ 66,014 um 21:26 UTC (+$1,240). Ab 23:00 Unentschlossenheit. Kickstarten ~00:20 UTC: Slippage 120 Punkte → -$801.",
        ["Limit TP @ 66,014 korrekt gesetzt → +$1,240", "Nach SL-Hit sofortiger rationaler Reentry", "Kickstarten-Technik methodisch korrekt", "Kein FOMO, kein Context Switch"],
        ["Barbwire Reversal nicht voll ausgenutzt — Pattern #3 Concentration Loss", "Viele kleine Gegenrichtungs-Trades während Aufwärtsbewegung", "Spätphase 23:00–01:00 UTC: richtungslos, Aktivität trotzdem hoch", "Kickstarten-Slippage: -$801 statt ~$0"])

    japan_stats = [
        ("Win Rate", "78.6%", "var(--gold)"), ("Order-Fills", "68", "#d8e2f4"),
        ("Bester Trade", "+$1,240", "var(--green)"), ("Grösster Verl.", "−$801", "var(--red)"),
        ("Beh. Cost", "~−$3k", "var(--red)"), ("Konto Ende", "$21,277", "#d8e2f4"),
    ]
    japan_body = c_japan2 + c_japan1 + '''<div class="ins-row">
      <div class="insight g"><h4>Stärken</h4><p>Die drei grossen Anchor Trades (+$1,240 / +$1,027 / +$1,077) konsequent bis TP gehalten — bestätigt H4 (Positionen halten schlägt Schnellskalps). Pattern #1 und #2 aus Day 1 nicht mehr aufgetreten. Kickstarten-Technik korrekt angewendet. Recovery nach SL-Hit rational und schnell.</p></div>
      <div class="insight r"><h4>Schwächen</h4><p>Barbwire Reversal bei Marktöffnung war eine ~$5,000-Situation — realisiert wurden ~$2,267 (Pattern #3 Concentration Loss). Spätphase nach Mitternacht hätte mit deutlich reduzierter Size oder Pause gehandelt werden sollen.</p></div>
    </div>'''

    day1_stats = [
        ("Win Rate", "78.8%", "var(--gold)"), ("Trades", "33", "#d8e2f4"),
        ("Anchor Trade", "+$2,911", "var(--green)"), ("Grösster Verl.", "−$966", "var(--red)"),
        ("Beh. Cost", "−$1,302", "var(--red)"), ("Konto Ende", "$17,349", "#d8e2f4"),
    ]
    day1_body = c_ustec + c_ger40 + c_us30 + '''<div class="ins-row">
      <div class="insight g"><h4>Stärken</h4><p>Methodik perfekt umgesetzt: SMA200 Breakout erkannt, Pyramidierung im laufenden Trade, Anchor Trade konsequent gehalten. H4 bestätigt — Hold Ø +$612 vs Scalp Ø +$12.</p></div>
      <div class="insight r"><h4>Schwächen</h4><p>Pattern #1 (FOMO Top Scale 12:15) und Pattern #2 (Context Switch 13:58) kosteten zusammen −$1,302 direkt und weitere ~$1,300 an entgangenem Gewinn. In der Japan Session nicht mehr aufgetreten.</p></div>
    </div>'''

    japan_block = session_block(
        "Japan Session — Barbwire Reversal bei Marktöffnung",
        "2026-05-28 20:51 – 2026-05-29 01:12 UTC · WHSELFINVEST:JAPAN225CFD",
        "+$3,880", "var(--green)", japan_stats, japan_body)

    day1_block = session_block(
        "Day 1 — Starker USTEC Trendtag",
        "2026-05-28 · 07:36–17:03 UTC · GER40 · USTEC · US30 · SPX",
        "+$7,349", "var(--green)", day1_stats, day1_body)

    return japan_block, day1_block

# ─── Page 1: master_report.html ───────────────────────────────────────────────

def build_overview(shots):
    japan_block, _ = build_charts_and_sessions(shots)

    body = f'''
<div class="hero">
  <div class="page" style="padding-bottom:0">
    <div class="hero-eyebrow">Master Report · Paper Trading · arthurdigbysellers2 · USD</div>
    <div class="hero-title">Übersicht — <span>2026-05-28 bis 2026-05-29</span></div>
    <div class="hero-sub">2 Handelstage · 3 Sessions · USTEC · GER40 · US30 · SPX · JAPAN225</div>
    <div class="kpi-row">
      <div class="kpi"><div class="kpi-label">Gesamtperformance</div><div class="kpi-val g">+$11,277</div><div class="kpi-sub">$10,000 → $21,277 · +112.8%</div></div>
      <div class="kpi"><div class="kpi-label">Win Rate gesamt</div><div class="kpi-val gold">78.7%</div><div class="kpi-sub">37W · 8L · 2BE</div></div>
      <div class="kpi"><div class="kpi-label">Beste Stunde</div><div class="kpi-val w">11h UTC</div><div class="kpi-sub">+$6,514 in 60 Min · USTEC</div></div>
      <div class="kpi"><div class="kpi-label">Bester Trade</div><div class="kpi-val g">+$2,911</div><div class="kpi-sub">USTEC Long 11:13 · Anchor</div></div>
      <div class="kpi"><div class="kpi-label">Behaviour Cost</div><div class="kpi-val r">−$2,497</div><div class="kpi-sub">+~$5,800 Opportunitätsverlust</div></div>
    </div>
  </div>
</div>

<div class="page">

  <div class="section">
    <div class="sec-head"><div class="sec-title">Equity Kurve</div><div class="sec-meta">$10,000 Startkapital</div></div>
    <div style="background:var(--s1);border:1px solid var(--border);padding:24px">
      <svg class="equity" viewBox="0 0 1200 220" preserveAspectRatio="none">
        <defs><linearGradient id="eqG" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#38c87a" stop-opacity="0.18"/>
          <stop offset="100%" stop-color="#38c87a" stop-opacity="0"/>
        </linearGradient></defs>
        <line x1="0" y1="44" x2="1200" y2="44" stroke="#1a2030" stroke-width="1"/>
        <line x1="0" y1="88" x2="1200" y2="88" stroke="#1a2030" stroke-width="1"/>
        <line x1="0" y1="132" x2="1200" y2="132" stroke="#1a2030" stroke-width="1"/>
        <line x1="0" y1="176" x2="1200" y2="176" stroke="#1a2030" stroke-width="1"/>
        <text x="6" y="42" fill="#354057" font-size="10" font-family="DM Mono">$21k</text>
        <text x="6" y="86" fill="#354057" font-size="10" font-family="DM Mono">$18k</text>
        <text x="6" y="130" fill="#354057" font-size="10" font-family="DM Mono">$15k</text>
        <text x="6" y="174" fill="#354057" font-size="10" font-family="DM Mono">$12k</text>
        <line x1="490" y1="0" x2="490" y2="200" stroke="#e8b84b" stroke-width="1" stroke-dasharray="4,4" opacity="0.3"/>
        <line x1="730" y1="0" x2="730" y2="200" stroke="#4f9de0" stroke-width="1" stroke-dasharray="4,4" opacity="0.25"/>
        <polyline points="60,188 110,174 160,167 210,130 260,112 310,99 360,92 415,96 465,79 515,68 565,60 615,54 665,48 715,43 760,46 810,38 860,33 908,40 945,36 985,30 1025,25 1065,19 1105,13 1145,9" fill="none" stroke="#38c87a" stroke-width="2" stroke-linejoin="round"/>
        <polygon points="60,188 110,174 160,167 210,130 260,112 310,99 360,92 415,96 465,79 515,68 565,60 615,54 665,48 715,43 760,46 810,38 860,33 908,40 945,36 985,30 1025,25 1065,19 1105,13 1145,9 1145,205 60,205" fill="url(#eqG)"/>
        <circle cx="360" cy="92" r="4" fill="#e8b84b"/><text x="318" y="86" fill="#e8b84b" font-size="10" font-family="DM Mono">+$2,911</text>
        <circle cx="665" cy="48" r="4" fill="#38c87a"/><text x="624" y="42" fill="#38c87a" font-size="10" font-family="DM Mono">+$1,240</text>
        <circle cx="860" cy="33" r="4" fill="#e85858"/><text x="868" y="28" fill="#e85858" font-size="10" font-family="DM Mono">SL −$801</text>
        <text x="62" y="214" fill="#354057" font-size="10" font-family="DM Mono">07:36</text>
        <text x="434" y="214" fill="#e8b84b" font-size="10" font-family="DM Mono">Japan 20:51</text>
        <text x="738" y="214" fill="#4f9de0" font-size="10" font-family="DM Mono">29. Mai 00:00</text>
        <text x="1090" y="214" fill="#354057" font-size="10" font-family="DM Mono">01:12</text>
      </svg>
    </div>
  </div>

  <div class="section">
    <div class="sec-head"><div class="sec-title">Zeitanalyse &amp; Instrumente</div></div>
    <div class="g2">
      <div class="card">
        <div class="card-title">P&amp;L nach Handelsstunde (UTC) — hover für Details</div>
        <div class="bar-chart">
          <div class="bar" style="background:rgba(155,127,232,0.55);height:12%" data-tip="07h GER40: +$838"></div>
          <div class="bar" style="background:rgba(155,127,232,0.3);height:5%"   data-tip="08h GER40: +$154"></div>
          <div class="bar" style="background:var(--border2);height:2%"           data-tip="09–10h: $0"></div>
          <div class="bar" style="background:var(--border2);height:2%"           data-tip="10h: $0"></div>
          <div class="bar" style="background:rgba(232,184,75,0.85);height:100%" data-tip="11h USTEC: +$6,514 ★"></div>
          <div class="bar" style="background:rgba(232,184,75,0.6);height:45%"   data-tip="12h USTEC: +$2,942"></div>
          <div class="bar" style="background:rgba(232,184,75,0.45);height:22%"  data-tip="13h USTEC: +$1,066"></div>
          <div class="bar" style="background:var(--border2);height:2%"           data-tip="14–15h: $0"></div>
          <div class="bar" style="background:rgba(79,157,224,0.5);height:5%"    data-tip="16h US30/SPX: +$278"></div>
          <div class="bar" style="background:rgba(79,157,224,0.45);height:9%"   data-tip="17h US30: +$432"></div>
          <div class="bar" style="background:var(--border2);height:2%"           data-tip="18–20h: $0"></div>
          <div class="bar" style="background:rgba(56,200,122,0.7);height:52%"   data-tip="21h Japan: +$1,428"></div>
          <div class="bar" style="background:rgba(56,200,122,0.65);height:60%"  data-tip="22h Japan: +$2,660"></div>
          <div class="bar" style="background:rgba(56,200,122,0.3);height:11%"   data-tip="23h Japan: +$204"></div>
          <div class="bar" style="background:rgba(232,88,88,0.45);height:20%"   data-tip="00h Japan: −$617 (SL)"></div>
          <div class="bar" style="background:rgba(56,200,122,0.45);height:13%"  data-tip="01h Japan: +$422"></div>
        </div>
        <div style="display:flex;justify-content:space-between;font-size:12px;color:var(--muted)">
          <span>07h</span><span style="color:var(--gold)">11h ★</span><span>17h</span><span style="color:var(--green)">21h</span><span>01h</span>
        </div>
        <div style="margin-top:12px;font-size:13px;color:var(--muted2);line-height:1.8">
          USTEC 11–13h: 88% des Day-P&L in 2.5h · Japan 21–22h: 37% des Session-P&L in der ersten Stunde
        </div>
      </div>
      <div class="card">
        <div class="card-title">Instrumente — P&amp;L Verteilung</div>
        <div style="display:flex;align-items:center;gap:28px;margin-bottom:18px">
          <div style="width:88px;height:88px;border-radius:50%;flex-shrink:0;background:conic-gradient(var(--gold) 0% 58%,var(--green) 58% 89%,var(--blue) 89% 95%,var(--purple) 95% 100%)"></div>
          <div style="display:flex;flex-direction:column;gap:9px">
            <div style="display:flex;align-items:center;gap:9px;font-size:15px"><div style="width:10px;height:10px;border-radius:50%;background:var(--gold)"></div>USTEC <strong style="color:#d8e2f4;margin-left:4px">$7,378</strong> <span style="color:var(--muted);margin-left:4px">58%</span></div>
            <div style="display:flex;align-items:center;gap:9px;font-size:15px"><div style="width:10px;height:10px;border-radius:50%;background:var(--green)"></div>JAPAN225 <strong style="color:#d8e2f4;margin-left:4px">$3,941</strong> <span style="color:var(--muted);margin-left:4px">31%</span></div>
            <div style="display:flex;align-items:center;gap:9px;font-size:15px"><div style="width:10px;height:10px;border-radius:50%;background:var(--blue)"></div>US30 <strong style="color:#d8e2f4;margin-left:4px">$680</strong> <span style="color:var(--muted);margin-left:4px">5%</span></div>
            <div style="display:flex;align-items:center;gap:9px;font-size:15px"><div style="width:10px;height:10px;border-radius:50%;background:var(--purple)"></div>GER40 <strong style="color:#d8e2f4;margin-left:4px">$839</strong> <span style="color:var(--muted);margin-left:4px">7%</span></div>
          </div>
        </div>
        <div style="font-size:15px;color:var(--muted2);line-height:1.8;border-top:1px solid var(--border);padding-top:12px">
          USTEC ist das Hauptinstrument — 58% des Gross P&L mit nur 33 Trades. JAPAN225 lieferte 31% in einer einzigen Nacht.
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="sec-head"><div class="sec-title">Behaviour — Alle Sessions</div></div>
    <div class="g2" style="margin-bottom:16px">
      <div class="card">
        <div class="card-title">Cost Summary</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px">
          <div><div style="font-size:11px;color:var(--muted);letter-spacing:0.1em;text-transform:uppercase">Direktkosten</div><div style="font-family:var(--sans);font-size:28px;font-weight:600;color:var(--red);margin-top:5px">−$2,497</div></div>
          <div><div style="font-size:11px;color:var(--muted);letter-spacing:0.1em;text-transform:uppercase">Opportunitätsverlust</div><div style="font-family:var(--sans);font-size:28px;font-weight:600;color:var(--red);margin-top:5px">~−$5,800</div></div>
        </div>
        <div style="font-size:15px;color:var(--muted2);line-height:1.8;border-top:1px solid var(--border);padding-top:12px">
          Ohne Behaviour-Kosten: <strong style="color:#d8e2f4">~$17,000+</strong>. 50% Verbesserungspotenzial durch reine Verhaltensoptimierung.
        </div>
      </div>
      <div class="card">
        <div class="card-title">Pattern-Entwicklung Day 1 → Japan</div>
        <div class="bench-row" style="margin-top:8px"><div class="bench-name">Pattern #1 FOMO Top Scale</div><div class="bench-track"><div class="bench-fill" style="width:50%;background:var(--red)"></div></div><div class="bench-num" style="color:var(--gold)">1× → 0×</div></div>
        <div class="bench-row"><div class="bench-name">Pattern #2 Context Switch Exit</div><div class="bench-track"><div class="bench-fill" style="width:50%;background:var(--red)"></div></div><div class="bench-num" style="color:var(--gold)">1× → 0×</div></div>
        <div class="bench-row"><div class="bench-name">Pattern #3 Concentration Loss</div><div class="bench-track"><div class="bench-fill" style="width:80%;background:var(--red)"></div></div><div class="bench-num" style="color:var(--red)">0× → 2×</div></div>
        <div class="bench-row"><div class="bench-name">✓ Anchor Trade Hold</div><div class="bench-track"><div class="bench-fill" style="width:100%;background:var(--green)"></div></div><div class="bench-num" style="color:var(--green)">2× → 3×</div></div>
      </div>
    </div>
    <table class="beh-table">
      <thead><tr><th>Pattern</th><th>Session</th><th>Direkt</th><th>Opportunität</th><th>Status</th><th>Details</th></tr></thead>
      <tbody>
        <tr><td><strong style="color:var(--red)">FOMO Top Scale</strong><br><span style="font-size:12px;color:var(--muted)">Pattern #1</span></td><td><span class="tag gold">Day 1</span></td><td style="color:var(--red)">−$966</td><td style="color:var(--muted2)">~−$500</td><td><span class="tag gold">Verbessert</span></td><td>12:15 USTEC Long 40 Units zu Top-of-Range. In Japan nicht mehr aufgetreten.</td></tr>
        <tr><td><strong style="color:var(--red)">Context Switch Exit</strong><br><span style="font-size:12px;color:var(--muted)">Pattern #2</span></td><td><span class="tag gold">Day 1</span></td><td style="color:var(--red)">−$336</td><td style="color:var(--muted2)">~−$800</td><td><span class="tag gold">Verbessert</span></td><td>13:58 USTEC Short wegen Abendessen. In Japan nicht mehr aufgetreten.</td></tr>
        <tr><td><strong style="color:var(--red)">Concentration Loss</strong><br><span style="font-size:12px;color:var(--muted)">Pattern #3</span></td><td><span class="tag g">Japan</span></td><td style="color:var(--muted2)">$0</td><td style="color:var(--red)">~−$3,000</td><td><span class="tag r">Hauptthema</span></td><td>Barbwire Reversal nicht voll genutzt — beide Richtungen möglich. Durch parallele Claude-Konversation abgelenkt.</td></tr>
        <tr><td><strong style="color:var(--muted2)">Kickstarten Slippage</strong><br><span style="font-size:12px;color:var(--muted)">Marktrisiko</span></td><td><span class="tag g">Japan</span></td><td style="color:var(--red)">−$801</td><td style="color:var(--muted2)">—</td><td><span class="tag m">Technik korrekt</span></td><td>Stop knapp über Break-Even, Slippage ~120 Punkte. Methodik korrekt.</td></tr>
        <tr><td><strong style="color:var(--green)">Anchor Trade Hold</strong><br><span style="font-size:12px;color:var(--muted)">Positiv</span></td><td><span class="tag gold">Day 1</span> <span class="tag g">Japan</span></td><td style="color:var(--green)">+$7,628</td><td style="color:var(--muted2)">—</td><td><span class="tag g">Konsistent 5×</span></td><td>5 Anchor Trades bis TP gehalten. Ø +$1,526. Hold 51× besser als Scalps.</td></tr>
      </tbody>
    </table>
  </div>

  <div class="section">
    <div class="sec-head"><div class="sec-title">Benchmark vs. Retail &amp; Profis</div><div class="sec-meta">FINRA 2025 · UC Berkeley · QuantifiedStrategies 2026</div></div>
    <div class="g2">
      <div class="card">
        <div class="card-title">Win Rate Vergleich</div>
        <div class="bench-row" style="margin-top:8px"><div class="bench-name" style="color:#d8e2f4;font-weight:500">Martin (2 Tage)</div><div class="bench-track"><div class="bench-fill" style="width:78.7%;background:var(--gold)"></div></div><div class="bench-num" style="color:var(--gold)">78.7%</div></div>
        <div class="bench-row"><div class="bench-name">Top Algo-Systeme</div><div class="bench-track"><div class="bench-fill" style="width:65%;background:var(--green)"></div></div><div class="bench-num" style="color:var(--green)">55–70%</div></div>
        <div class="bench-row"><div class="bench-name">Profitable Prop Trader</div><div class="bench-track"><div class="bench-fill" style="width:55%;background:var(--blue)"></div></div><div class="bench-num" style="color:var(--blue)">~55%</div></div>
        <div class="bench-row"><div class="bench-name">Profitable Retail Trader</div><div class="bench-track"><div class="bench-fill" style="width:47%;background:var(--muted)"></div></div><div class="bench-num" style="color:var(--muted2)">~47%</div></div>
        <div class="bench-row"><div class="bench-name">Ø Retail Day Trader</div><div class="bench-track"><div class="bench-fill" style="width:28%;background:var(--red)"></div></div><div class="bench-num" style="color:var(--red)">&lt;28%</div></div>
        <div style="margin-top:12px;font-size:15px;color:var(--muted2);line-height:1.8">72% aller Retail Trader verlieren Geld pro Jahr (FINRA). Nur 13% bleiben über 6 Monate profitabel (UC Berkeley). 2 Tage sind noch kein statistischer Beweis.</div>
      </div>
      <div class="card">
        <div class="card-title">Return auf Startkapital</div>
        <div class="bench-row" style="margin-top:8px"><div class="bench-name" style="color:#d8e2f4;font-weight:500">Martin (2 Tage)</div><div class="bench-track"><div class="bench-fill" style="width:100%;background:var(--gold)"></div></div><div class="bench-num" style="color:var(--gold)">+113%</div></div>
        <div class="bench-row"><div class="bench-name">Top Hedge Funds (Jahres)</div><div class="bench-track"><div class="bench-fill" style="width:40%;background:var(--green)"></div></div><div class="bench-num" style="color:var(--green)">30–50%</div></div>
        <div class="bench-row"><div class="bench-name">Profitable Retail (Jahres)</div><div class="bench-track"><div class="bench-fill" style="width:20%;background:var(--blue)"></div></div><div class="bench-num" style="color:var(--blue)">10–25%</div></div>
        <div class="bench-row"><div class="bench-name">S&amp;P 500 (~2024)</div><div class="bench-track"><div class="bench-fill" style="width:24%;background:var(--muted)"></div></div><div class="bench-num" style="color:var(--muted2)">~24%</div></div>
        <div class="bench-row"><div class="bench-name">Ø Retail Day Trader (Jahres)</div><div class="bench-track"><div class="bench-fill" style="width:5%;background:var(--red)"></div></div><div class="bench-num" style="color:var(--red)">−4.5%</div></div>
        <div style="margin-top:12px;font-size:13px;background:rgba(232,184,75,0.05);border-left:2px solid var(--gold);padding:10px 14px;color:var(--muted2)">⚠ Paper Trading · außergewöhnlicher Trendtag · 2 Datenpunkte. Valide Statistik braucht 30+ Handelstage.</div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="sec-head"><div class="sec-title">Hypothesen Status</div><div class="sec-meta">Stand nach 2 Handelstagen</div></div>
    <div class="g2">
      <div class="hypo"><div class="hypo-id">SMA200-Breakout führt zu längerem Trend (H1)</div><span class="badge ev">1 Datenpunkt</span><div class="hypo-text">Wenn der Preis auf dem 5M-Chart den SMA200 von unten durchbricht, setzt sich der Trend statistisch für X Minuten / Y Punkte fort.</div><div class="hypo-ev">28. Mai 10:00 UTC: USTEC → Trend bis 13:30 = 3.5h, ~300 Punkte.</div></div>
      <div class="hypo"><div class="hypo-id">Aircushion-Kollaps ist besserer Exit als fixer Stop (H2)</div><span class="badge ev">Indirekte Evidenz</span><div class="hypo-text">Das Erkennen eines kollabierenden Aircushions ist ein zuverlässigeres Exit-Signal als ein fix gesetzter Stop Loss.</div><div class="hypo-ev">Japan Session: beide SL-Events nach Aircushion-Kollaps.</div></div>
      <div class="hypo"><div class="hypo-id">Beste Performance zwischen 11–13:30 Uhr UTC (H3)</div><span class="badge ev">Erste Bestätigung</span><div class="hypo-text">Die höchste Win Rate und das beste R:R entstehen bei USTEC zwischen 11:00 und 13:30 UTC.</div><div class="hypo-ev">Day 1: $6,514 von $7,349 in 11–13h = 88.6%.</div></div>
      <div class="hypo"><div class="hypo-id">Positionen halten schlägt Schnellskalps in Trend-Phasen (H4)</div><span class="badge ok">Bestätigt</span><div class="hypo-text">In Trend-Phasen mit stabilem Aircushion generieren längere Haltedauern ein signifikant besseres P&L pro Trade.</div><div class="hypo-ev">Day 1: Ø Hold +$612 vs Ø Scalp +$12 — 51×. Japan: 12.5×. Konsistent.</div></div>
      <div class="hypo" style="grid-column:1/-1;border-left:2px solid var(--gold)"><div class="hypo-id">Barbwire Reversal kündigt starke Bewegung an (H5)</div><span class="badge ev">2 Datenpunkte</span><div class="hypo-text">SMA20 horizontal + SMA-Crossing + Barbwire-Kerzen → starke Bewegung wahrscheinlich, oft gegen den vorherigen Trend. Verstärkt bei: Marktöffnung, nach 3h+ Trend, an wichtigen Preisniveaus.</div><div class="hypo-ev">JAPAN225, 29. Mai 08:30 JST: alle Signale aktiv → 600+ Punkte in beide Richtungen. Nicht voll ausgenutzt (Pattern #3). Potenzial ~$5,000, realisiert ~$2,267.</div></div>
    </div>
  </div>

  <div class="section">
    <div class="sec-head"><div class="sec-title">Aktuelle Session</div><div class="sec-meta">Japan Session 2026-05-28/29</div></div>
    {japan_block}
  </div>

  <div class="footer">
    <div>Martin Sambauer · Master Report · Paper Trading · arthurdigbysellers2 · USD · v1.9</div>
    <div>Generiert 2026-05-29 · In Firefox öffnen</div>
  </div>
</div>'''

    return html_shell("Übersicht", "master_report.html", body)

# ─── Page 2: sessions.html ────────────────────────────────────────────────────

def build_sessions(shots):
    japan_block, day1_block = build_charts_and_sessions(shots)

    body = f'''
<div class="page-header">
  <div class="page" style="padding-bottom:0;padding-top:0">
    <div style="padding-top:44px">
      <div class="page-label">Sessions</div>
      <div class="page-title">Alle Sessions — <span>chronologisch, neuste zuerst</span></div>
      <div class="page-sub" style="margin-top:6px;margin-bottom:0">2 Handelstage · 3 Sessions</div>
    </div>
  </div>
</div>

<div class="page" style="padding-top:36px">
  {japan_block}
  {day1_block}
  <div class="footer">
    <div>Martin Sambauer · Sessions · Paper Trading · arthurdigbysellers2 · v1.9</div>
    <div>Generiert 2026-05-29 · In Firefox öffnen</div>
  </div>
</div>'''

    return html_shell("Sessions", "sessions.html", body)

# ─── Page 3: observations.html ───────────────────────────────────────────────

def build_observations(shots):
    japan1 = shots.get("JAPAN225CFD_2026-05-28_19-09-00_cbdae.png", "")
    japan2 = shots.get("JAPAN225CFD_2026-05-29_01-29-07_e79b3.png", "")

    img1 = f'<div class="obs-chart"><img src="{japan1}" alt="JAPAN225CFD Session Overview"><div class="obs-caption">JAPAN225CFD 5M — 2026-05-28/29. Rechts: die drei Phasen sind erkennbar — enge Alternierungszone links (Phase 1), steigende Tiefs in der Mitte beim SMA-Crossing (Phase 2), klarer Trend-Kanal rechts im oberen Bollinger-Segment (Phase 3). SMA200 (rosa) bestätigt den Trend-Kontext.</div></div>' if japan1 else ""
    img2 = f'<div class="obs-chart"><img src="{japan2}" alt="JAPAN225CFD with Execution Marks"><div class="obs-caption">JAPAN225CFD 5M mit Execution Marks. Die dichten roten Pfeile nach unten während der Aufwärtsbewegung in Phase 3 zeigen die Gegenrichtungs-Trades — der alternierende Charakter wurde erkannt, aber fälschlicherweise gegen den Trend gehandelt statt mit ihm.</div></div>' if japan2 else ""

    body = f'''
<div class="page-header">
  <div class="page" style="padding-bottom:0;padding-top:0">
    <div style="padding-top:44px">
      <div class="page-label">Observations</div>
      <div class="page-title">Market Observations — <span>Redaktionelle Einsichten</span></div>
      <div class="page-sub" style="margin-top:6px;margin-bottom:0;font-size:14px;color:var(--muted2)">
        Keine Regeln, keine Hypothesen — beobachtete Markt-Charakteristiken die sich wiederholen und auf die man mit Vorsicht setzen kann. Brüche in der Charakteristik sind möglich.
      </div>
    </div>
  </div>
</div>

<div class="page" style="padding-top:36px">

  <!-- OBS-001 -->
  <div class="obs-block">
    <div class="obs-head">
      <div class="obs-id">OBS-001</div>
      <div class="obs-name">Horizontales Alternieren um SMA20 — Pure Range</div>
      <div style="margin-top:8px;display:flex;gap:8px;align-items:center">
        <span class="badge op">Anecdotal</span>
        <span style="font-size:12px;color:var(--muted2)">Erstmals dokumentiert: 2026-05-29</span>
      </div>
    </div>
    <div class="obs-body">
      <div class="obs-section-title">Kernbeobachtung</div>
      <div class="obs-text">In bestimmten Marktphasen pendelt der Preis wiederholt um einen flachen SMA20 — er kreuzt ihn, kehrt zurück, kreuzt wieder. Der Markt hat keine Richtungsentscheidung getroffen. Diese Phase kann von wenigen Minuten bis einige Stunden andauern, bevor sie sich entweder in einen Trend transformiert oder ohne klares Ergebnis endet.</div>

      <div class="obs-section-title">Wie es sich auf dem Chart zeigt</div>
      <div class="obs-text"><ul>
        <li>SMA20 ist flach oder nahezu flach — keine erkennbare Neigung</li>
        <li>Preis berührt das obere und untere Bollinger Band abwechselnd</li>
        <li>Kein stabiler Aircushion auf einer Seite des SMA20</li>
        <li>Kerzen sind gemischt — keine Sequenz von höheren Hochs oder tieferen Tiefs</li>
        <li>Bollinger Bands können sich zusammenziehen (Energie baut sich auf) oder moderat weit sein</li>
      </ul></div>

      <div class="obs-section-title">Trading-Implikation</div>
      <div class="obs-text">Bollinger Bands faden: Short nahe dem oberen Band, Long nahe dem unteren Band.<ul>
        <li>Kleine Positionsgrössen — es gibt keinen Trend zu reiten</li>
        <li>Enge Stops — die Range definiert das Risiko</li>
        <li>Gewinn schnell nehmen — der Move endet am gegenüberliegenden Band</li>
        <li>Nicht pyramidieren — der Markt dreht bevor grosse Positionen profitabel werden</li>
        <li>Diese Taktik sofort stoppen wenn SMA20 anfängt sich zu neigen</li>
      </ul></div>

      <div class="obs-section-title">Bruch-Signale</div>
      <div class="obs-text"><ul>
        <li>SMA20 entwickelt eine sichtbare Neigung</li>
        <li>Eine Seite des Bollinger Bands wird wiederholt berührt ohne vollständige Gegenbewegung</li>
        <li>Höhere Tiefs (bullisches Bruch) oder niedrigere Hochs (bärisches Bruch) entstehen</li>
        <li>Eine Kerze schliesst signifikant ausserhalb des Bollinger Bands ohne sofortiges Zurückschnappen</li>
      </ul></div>

      <div class="obs-section-title">Beispiele</div>
      <div class="obs-text">Noch kein isoliertes Beispiel dokumentiert. Siehe OBS-002 Phase 1 für den Übergangskontext.</div>
    </div>
  </div>

  <!-- OBS-002 -->
  <div class="obs-block">
    <div class="obs-head">
      <div class="obs-id">OBS-002</div>
      <div class="obs-name">Alternieren mit Drift — Range transformiert sich in Trend-Kanal</div>
      <div style="margin-top:8px;display:flex;gap:8px;align-items:center">
        <span class="badge op">Anecdotal</span>
        <span style="font-size:12px;color:var(--muted2)">Erstmals dokumentiert: 2026-05-29 · Japan Session</span>
      </div>
    </div>
    <div class="obs-body">
      <div class="obs-section-title">Kernbeobachtung</div>
      <div class="obs-text">Eine Range-Phase (wie OBS-001) kann sich graduell in eine gerichtete Bewegung transformieren, ohne ihren alternierenden Charakter zu verlieren. Der Markt wechselt nicht abrupt von Range zu Trend — er driftet. Das entscheidende Frühsignal ist eine Sequenz von höheren Tiefs (bei Aufwärts-Transition), erkennbar bevor die Richtung offensichtlich wird. Der alternierende Charakter bleibt in Phase 3 erhalten, verlagert sich aber ins obere (oder untere) Bollinger-Segment — Korrekturen erreichen das gegenüberliegende Band nicht mehr.</div>

      <div class="obs-section-title">Drei Phasen auf dem Chart</div>
      <div class="obs-text">
        <strong style="color:#d8e2f4">Phase 1 — Pure Range:</strong> SMA20 horizontal. Preis bounced zwischen beiden Bollinger Bändern. Keine Richtung. Entspricht OBS-001.
        <br><br>
        <strong style="color:#d8e2f4">Phase 2 — Transition (das kritische Erkennungs-Fenster):</strong> SMA20 beginnt sich leicht zu neigen. Korrekturen sehen noch wie vollständige Umkehrungen aus, erreichen das gegenüberliegende Band aber nicht mehr vollständig. Eine Trendlinie die die Tiefs verbindet beginnt zu steigen. Das SMA-Crossing-Verhalten setzt sich fort, aber der Preis verbringt mehr Zeit auf einer Seite. Diese Phase dauert typischerweise 20–60 Minuten auf dem 5M-Chart.
        <br><br>
        <strong style="color:#d8e2f4">Phase 3 — Trend-Kanal:</strong> Preis bewegt sich überwiegend im oberen (Aufwärtstrend) oder unteren (Abwärtstrend) Bollinger-Segment. Korrekturen ziehen zurück zum SMA20 aber nicht darunter — SMA20 wirkt als Support. Aircushion bildet sich. Das alternierende Verhalten ist noch präsent aber innerhalb der Trendrichtung — jede Korrektur ist eine Kaufgelegenheit, kein Umkehrsignal.
      </div>

      <div class="obs-section-title">Trading-Implikation</div>
      <div class="obs-text">
        <strong style="color:#d8e2f4">Phase 1:</strong> Bollinger Band Fades wie OBS-001.
        <br><br>
        <strong style="color:#d8e2f4">Phase 2 — höchste Priorität:</strong> Gegenrichtungs-Trades stoppen. Bestehende Positionen reduzieren oder schliessen. Trendlinie der höheren Tiefs beobachten. Auf den Ausbruch aus der Range auf der Trend-Seite warten bevor man einsteigt. Dies ist das höchste-Wert-Einstiegsfenster — früh im Trend, bevor er offensichtlich ist.
        <br><br>
        <strong style="color:#d8e2f4">Phase 3:</strong> Mit dem Trend handeln. Korrekturen zum SMA20 als Einstiegsgelegenheit nutzen. Pyramidieren ist angebracht. Positionen länger halten als sich intuitiv richtig anfühlt — der alternierende Charakter erzeugt falsche Exit-Signale.
      </div>

      <div class="obs-section-title">Bruch-Signale</div>
      <div class="obs-text"><ul>
        <li>Preis bricht durch SMA20 und erholt sich nicht innerhalb von 2–3 Kerzen</li>
        <li>SMA20 flacht nach einer Neigungsphase wieder ab</li>
        <li>Die Amplitude der Gegenbewegungen nimmt merklich zu</li>
        <li>Eine Kerze schliesst unterhalb des letzten höheren Tiefs (bei Aufwärtstrend)</li>
      </ul></div>

      <div class="obs-section-title">Beispiel — Japan Session 2026-05-29, JAPAN225CFD 5M</div>
      <div class="obs-text">
        <strong style="color:#d8e2f4">Phase 1 (~20:50–22:00 UTC):</strong> Marktöffnung mit Barbwire-Zone (siehe SITUATIONS.md). SMA20 flach. Preis alterniert in enger Zone zwischen den Bollinger Bändern. Energie baut sich auf.
        <br><br>
        <strong style="color:#d8e2f4">Phase 2 (~22:00–22:30 UTC):</strong> SMA-Crossing. Höhere Tiefs erkennbar — eine steigende Trendlinie verbindet die Korrektions-Tiefs. Preis macht noch Gegenbewegungen, aber jede ist flacher als die vorherige. Dies war das optimale Einstiegsfenster für eine Long-Position mit dem entstehenden Trend.
        <br><br>
        <strong style="color:#d8e2f4">Phase 3 (~22:30–01:00 UTC):</strong> Preis bewegt sich primär im oberen Bollinger-Segment. Korrekturen zur SMA20 aber nicht darunter. Der alternierende Charakter bleibt sichtbar — zahlreiche kurze Rücksetzer — aber jeder Rücksetzer ist eine Kaufgelegenheit.
        <br><br>
        <strong style="color:#d8e2f4">Was verpasst wurde:</strong> Die Transition (Phase 2) wurde nicht klar genug erkannt. Einstieg kam erst nach Bestätigung des Trends. Mehrere Gegenrichtungs-Trades in Phase 3 (rote Pfeile im Chart) — der alternierende Charakter wurde erkannt, aber fälschlicherweise als Umkehrsignal interpretiert statt als temporäre Korrektur innerhalb des Trends.
        <br><br>
        <strong style="color:#d8e2f4">Potenzial vs. Realisiert:</strong> Hätte Phase 2 erkannt und ein Long bei Trendlinien-Ausbruch (~22:00–22:15 UTC) platziert, wäre der vollständige 600+ Punkte-Move erreichbar gewesen. Realisiert: ~$2,267. Potenzial mit sauberem Execution: ~$5,000.
      </div>

      {img1}
      {img2}
    </div>
  </div>

  <div class="footer">
    <div>Martin Sambauer · Observations · Paper Trading · arthurdigbysellers2 · v1.9</div>
    <div>Generiert 2026-05-29 · In Firefox öffnen</div>
  </div>
</div>'''

    return html_shell("Observations", "observations.html", body)

# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    os.makedirs(REPORTS_DIR, exist_ok=True)

    print("Sammle Screenshots...")
    shots = collect_screenshots()
    print(f"  {len(shots)} Screenshots eingebettet")

    print("Generiere master_report.html...")
    with open(os.path.join(REPORTS_DIR, "master_report.html"), "w") as f:
        f.write(build_overview(shots))

    print("Generiere sessions.html...")
    with open(os.path.join(REPORTS_DIR, "sessions.html"), "w") as f:
        f.write(build_sessions(shots))

    print("Generiere observations.html...")
    with open(os.path.join(REPORTS_DIR, "observations.html"), "w") as f:
        f.write(build_observations(shots))

    print("Fertig! Drei Dateien in reports/")
    print("  → open -a Firefox ~/Documents/Trading/reports/master_report.html")
