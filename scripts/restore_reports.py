#!/usr/bin/env python3
# restore_reports.py — stellt die v2.1 Reports wieder her und bettet Screenshots ein
# Einmalig ausfuehren: python3 scripts/restore_reports.py

import os, base64, sys
from io import BytesIO

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS_DIR = os.path.join(REPO, "screenshots")
REPORTS_DIR = os.path.join(REPO, "reports")
CSS_PATH = os.path.join(REPORTS_DIR, "assets", "style_v1.0.css")


def b64(path, w=1400, q=72):
    try:
        from PIL import Image
        img = Image.open(path).convert("RGB")
        if img.width > w:
            img = img.resize((w, int(img.height * w / img.width)), Image.LANCZOS)
        buf = BytesIO()
        img.save(buf, "JPEG", quality=q, optimize=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    except Exception:
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode()


def load_shots():
    s = {}
    for n in sorted(os.listdir(SHOTS_DIR)):
        if n.lower().endswith((".png", ".jpg", ".jpeg")):
            print("  " + n)
            u = b64(os.path.join(SHOTS_DIR, n))
            if u:
                s[n] = u
    return s


def css():
    with open(CSS_PATH) as f:
        return f.read()


def img(shots, key, alt=""):
    src = shots.get(key, "")
    if src:
        return '<img src="' + src + '" style="width:100%;display:block;border:1px solid var(--border)" alt="' + alt + '">'
    return '<div style="padding:32px;text-align:center;color:var(--muted);background:var(--s1);border:1px solid var(--border)">' + key + ' — wird beim naechsten update.sh eingebettet</div>'


def nav(active):
    pages = [("master_report.html","Uebersicht"),("sessions.html","Sessions"),("observations.html","Observations")]
    lnk = "".join('<a href="' + h + '"' + (' class="active"' if h==active else "") + ">" + l + "</a>" for h,l in pages)
    return '<nav class="nav"><div class="nav-logo">Martin<span>.</span>Trading</div>' + lnk + "</nav>"


def shell(title, active, body, c):
    return ('<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8">'
            '<title>' + title + ' - Martin Trading</title>'
            '<style>' + c + '</style></head><body>'
            + nav(active) + body + '</body></html>')


def baro(cls, pct, label, sub):
    return ('<div style="background:var(--s2);border:1px solid var(--border);padding:16px 18px">'
            '<div class="baro-label">' + label + '</div>'
            '<div class="baro ' + cls + '"><div class="baro-fill" style="width:' + str(pct) + '%"></div></div>'
            '<div class="baro-val ' + cls.replace("baro-","") + '">' + sub + '</div></div>')


def chart(img_html, title, what, hl, wk):
    h = "".join("<li>" + x + "</li>" for x in hl)
    w = "".join("<li>" + x + "</li>" for x in wk)
    return ('<div class="chart-block"><div class="chart-title">' + title + '</div>'
            + img_html +
            '<div class="chart-ann">'
            '<div class="ann-col"><div class="ann-label">Was passiert ist</div><div class="ann-body">' + what + '</div></div>'
            '<div class="ann-col"><div class="ann-label" style="color:var(--green)">&#10003; Highlights</div><ul class="ann-list green">' + h + '</ul></div>'
            '<div class="ann-col"><div class="ann-label" style="color:var(--red)">&#10007; Fehler</div><ul class="ann-list red">' + w + '</ul></div>'
            '</div></div>')


def sess(name, ds, pnl, col, stats, body):
    sh = "".join('<div class="stat"><div class="stat-label">' + s[0] + '</div><div class="stat-val" style="color:' + s[2] + '">' + s[1] + '</div></div>' for s in stats)
    return ('<div class="sess-block"><div class="sess-head">'
            '<div><div class="sess-name">' + name + '</div><div class="sess-date">' + ds + '</div></div>'
            '<div class="sess-pnl" style="color:' + col + '">' + pnl + '</div></div>'
            '<div class="sess-stats">' + sh + '</div><div class="sess-body">' + body + '</div></div>')


# ── Session content ───────────────────────────────────────────────────────────

def day3_body(shots):
    i_us30 = img(shots, "US30_2026-05-29_16-24-33_702f6.png", "US30 Day3")
    baros = ('<div style="margin-bottom:28px"><div style="font-size:11px;letter-spacing:0.12em;text-transform:uppercase;color:var(--muted2);margin-bottom:16px">Barometer</div>'
             '<div class="g3">'
             + baro("baro-yellow", 44, "T2BE Avg", "00:04:22 &mdash; YELLOW")
             + baro("baro-green", 20, "Stress Profit Pyramiding", "GREEN &mdash; Max DD -$180")
             + baro("baro-green", 15, "Stress Loss Pyramiding (Taktisch)", "GREEN &mdash; Max DD -$14")
             + '</div></div>')
    c_us30 = chart(i_us30, "US30 &mdash; Day 3, 09:53&ndash;13:48 UTC",
        "1D links: US30 nahe ATH (51,139). BB Upper 51,166 fast erreicht. SMA200 bei 47,834 weit darunter. 5M rechts: Open 09:53 bei ~50,820. Direkte Aufwaertsbewegung ohne Barbwire. Long-Aufbau 10 &rarr; 40 Units (10:37&ndash;11:46 UTC) mit taktischem LP am Support 50,860&ndash;50,875. Anchor Exit 40 Units @ 50,989 um 11:53 = +$4,394. Danach TDS: Short 12:07 gegen Trend. US30 lief auf 51,168. Recovery Long 13:32&ndash;13:44 UTC +$377.",
        ["Anchor Trade 40 Units 26 Min gehalten +$4,394",
         "Taktisches LP 50,860&ndash;50,875 korrekt (OBS-003)",
         "SPX500 Sondierung bei Open",
         "Aircushion-Kollaps als Exit genutzt",
         "Recovery nach TDS rational"],
        ["TDS 12:07: Short nach TP in 11h-UTC-Long-Zone ~-$1k direkt",
         "Opportunitaet ~-$2k durch TDS (US30 lief auf 51,168)",
         "Concentration Loss: Claude-Konversation waehrend Session"])
    tds_block = ('<div style="background:var(--s2);border:1px solid var(--border);border-left:2px solid var(--red);padding:18px 22px;margin-bottom:16px">'
                 '<div style="font-family:var(--sans);font-size:14px;font-weight:600;color:var(--red);margin-bottom:8px">Pattern #4 &mdash; TDS: Target Derangement Syndrome (NEU)</div>'
                 '<div style="font-size:15px;color:var(--text);line-height:1.85">'
                 '<strong style="color:#d8e2f4">Was passierte:</strong> Nach US30-Exit +$4,394 um 11:53 UTC wurde SHORT er&ouml;ffnet &mdash; obwohl 11h-UTC-Zone = Long-Bias (H3). US30 lief direkt auf 51,168. ~-$1,000 direkt, ~-$2,000 Opportunitaet.<br><br>'
                 '<strong style="color:#d8e2f4">Ursache:</strong> Euphorie nach grossem Gewinn + Claude-Konversation (Concentration Loss) = Uhrzeitregel ignoriert.<br><br>'
                 '<strong style="color:#d8e2f4">Regel:</strong> Nach TP in 11h-UTC-Zone: kein Short bis SMA20 dreht oder 13:30 UTC.'
                 '</div></div>')
    ins = ('<div class="ins-row">'
           '<div class="insight g"><h4>Staerken Day 3</h4><p>Anchor Trade perfekt: 40 Units aufgebaut, 26 Min gehalten, sauber geschlossen. Taktisches LP am Support (OBS-003) korrekt. H4 erneut bestaetigt. T2BE YELLOW war geplanter Drawdown beim LP-Aufbau, nicht Timing-Fehler.</p></div>'
           '<div class="insight r"><h4>TDS &mdash; Pattern #4 NEU</h4><p>~$3,000 Schaden durch Short nach TP in Long-Bias-Zone. Mitverursacht durch parallele Claude-Konversation. Neues Muster dokumentiert: nach grossem TP nicht sofort in Gegenrichtung. Regel gilt ab sofort.</p></div>'
           '</div>')
    return baros + c_us30 + tds_block + ins


def japan_body(shots):
    j2 = img(shots, "JAPAN225CFD_2026-05-29_01-29-07_e79b3.png", "JAPAN225CFD Executions")
    j1 = img(shots, "JAPAN225CFD_2026-05-28_19-09-00_cbdae.png", "JAPAN225CFD Overview")
    baros = ('<div style="margin-bottom:28px"><div class="g3">'
             + baro("baro-red", 85, "T2BE Avg", "00:21:05 &mdash; RED (LP)")
             + baro("baro-green", 5, "Stress PP", "GREEN")
             + baro("baro-red", 75, "Stress LP", "RED &mdash; Max DD -$1,100")
             + '</div></div>')
    cj2 = chart(j2, "JAPAN225CFD &mdash; Session mit Execution Marks",
        "Marktoeffnung ~22:00 UTC. Barbwire-Zone (OBS-002 Phase 1). SMA-Crossing &rarr; Long-Trend bis 66,200+. Bester Trade: Limit TP @ 66,014 +$1,240. Kickstarten ~00:20 UTC: Slippage 120 Pkt = -$801.",
        ["Limit TP @ 66,014 korrekt +$1,240", "Rationaler Reentry nach SL-Hit", "Kickstarten Technik korrekt", "Kein FOMO / Context Switch"],
        ["Barbwire nicht voll genutzt (Pattern #3)", "Gegenrichtungs-Trades im Trend", "Spaetphase zu aktiv", "Kickstarten-Slippage -$801"])
    cj1 = chart(j1, "JAPAN225CFD &mdash; Session-Ueberblick",
        "Aufwaertstrend 63,000 auf 66,200+. Drei Phasen erkennbar (OBS-002): Barbwire, Transition, Trend-Kanal.",
        ["Trend 4h+ vollstaendig mitgemacht", "OBS-002 Phasen sichtbar"],
        ["Barbwire Entry-Fenster verpasst", "Spaetphase zu aktiv"])
    ins = ('<div class="ins-row">'
           '<div class="insight g"><h4>Staerken</h4><p>Anchor Trades +$1,240/+$1,027/+$1,077 bis TP gehalten. Pattern #1+#2 nicht aufgetreten. Kickstarten korrekt angewendet.</p></div>'
           '<div class="insight r"><h4>Schwaehen</h4><p>Barbwire ~$5,000 Situation, nur ~$2,267 realisiert (Pattern #3). Spaetphase nach Mitternacht zu aktiv.</p></div>'
           '</div>')
    return baros + cj2 + cj1 + ins


def day1_body(shots):
    cu = img(shots, "USTEC_2026-05-28_20-16-56_68476.png", "USTEC Day1")
    cg = img(shots, "GER40_2026-05-28_20-18-29_f7a92.png", "GER40 Day1")
    cu30 = img(shots, "US30_2026-05-28_20-21-55_3e5f2.png", "US30 Day1")
    baros = ('<div style="margin-bottom:28px"><div class="g3">'
             + baro("baro-green", 20, "T2BE Avg", "00:01:45 &mdash; GREEN")
             + baro("baro-green", 15, "Stress PP", "GREEN &mdash; Max DD -$85")
             + baro("baro-green", 30, "Stress LP", "GREEN &mdash; Max DD -$290")
             + '</div></div>')
    c1 = chart(cu, "USTEC &mdash; Hauptsession 11:08&ndash;13:58 UTC",
        "SMA200-Breakout + SMA-Crossing ~10:00 UTC. Long-Aufbau 10 &rarr; 40+ Units. Anchor Trade 11:13 @ 30,055 &rarr; +$2,911. Aircushion-Kollaps ab 13:30.",
        ["SMA200 Breakout + Crossing erkannt", "Anchor bis TP +$2,911", "88% des P&L in 2.5h"],
        ["FOMO Top Scale 12:15 -$966 (P#1)", "Context Switch Exit 13:58 -$336 (P#2)"])
    c2 = chart(cg, "GER40 &mdash; 07:36&ndash;08:08 UTC",
        "DAX-Eroeffnung Short-Move. Drei profitable Shorts, dann Long gegen Trend.",
        ["Richtung erkannt", "3 Shorts: +$713+$39+$68"],
        ["Long 08:08 gegen Trend -$8", "Zu frueh aus Short"])
    c3 = chart(cu30, "US30 &mdash; 16:43&ndash;17:03 UTC",
        "ATH-Naehe. SPX Sondierung, dann Long US30.",
        ["SPX Confirmation genutzt", "+$680"],
        ["Groesse zu klein", "Zu frueh raus"])
    ins = ('<div class="ins-row">'
           '<div class="insight g"><h4>Staerken</h4><p>SMA200 Breakout erkannt, Pyramidierung, Anchor bis TP. H4 erstmals bestaetigt: Hold &Oslash; +$612 vs Scalp &Oslash; +$12.</p></div>'
           '<div class="insight r"><h4>Schwaehen</h4><p>Pattern #1+#2 kosteten -$1,302. In Japan und Day 3 nicht mehr aufgetreten.</p></div>'
           '</div>')
    return baros + c1 + c2 + c3 + ins


# ── master_report.html ────────────────────────────────────────────────────────

def build_master(shots, c):
    d3b = day3_body(shots)
    d3s = [("Win Rate","71.4%","var(--gold)"),("Fills","~48","#d8e2f4"),
           ("Anchor","+$4,394","var(--green)"),("TDS-Fehler","~-$3k","var(--red)"),
           ("Avg T2BE","4:22","var(--gold)"),("Konto","$27,797","#d8e2f4")]
    current = sess("Day 3 &mdash; US30 Breakout &amp; TDS-Fehler",
                   "2026-05-29 &middot; 09:53&ndash;13:48 UTC &middot; US30 &middot; USTEC &middot; JAPAN225 &middot; SPX500",
                   "+$6,568","var(--green)",d3s,d3b)

    body = ('<div class="hero"><div class="page" style="padding-bottom:0">'
            '<div class="hero-eyebrow">Master Report &middot; Paper Trading &middot; arthurdigbysellers2 &middot; USD</div>'
            '<div class="hero-title">Uebersicht &mdash; <span>2026-05-28 bis 2026-05-29</span></div>'
            '<div class="hero-sub">3 Handelstage &middot; 4 Sessions &middot; US30 &middot; USTEC &middot; JAPAN225 &middot; GER40 &middot; SPX500</div>'
            '<div class="kpi-row">'
            '<div class="kpi"><div class="kpi-label">Gesamtperformance</div><div class="kpi-val g">+$17,797</div><div class="kpi-sub">$10,000 &rarr; $27,797 &middot; +178%</div></div>'
            '<div class="kpi"><div class="kpi-label">Win Rate gesamt</div><div class="kpi-val gold">76.4%</div><div class="kpi-sub">4 Sessions</div></div>'
            '<div class="kpi"><div class="kpi-label">Bester Trade</div><div class="kpi-val g">+$4,394</div><div class="kpi-sub">US30 Long 40 Units Day 3</div></div>'
            '<div class="kpi"><div class="kpi-label">Behaviour Cost</div><div class="kpi-val r">-$3,497</div><div class="kpi-sub">TDS allein ~$3k Day 3</div></div>'
            '<div class="kpi"><div class="kpi-label">Konto Stand</div><div class="kpi-val w">$27,797</div><div class="kpi-sub">Nach Day 3</div></div>'
            '</div></div></div>'
            '<div class="page">'
            '<div class="section">'
            '<div class="sec-head"><div class="sec-title">Equity Kurve</div><div class="sec-meta">$10,000 Startkapital</div></div>'
            '<div style="background:var(--s1);border:1px solid var(--border);padding:24px">'
            '<svg width="100%" height="220" viewBox="0 0 1200 220" preserveAspectRatio="none">'
            '<defs><linearGradient id="eqG" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38c87a" stop-opacity="0.18"/><stop offset="100%" stop-color="#38c87a" stop-opacity="0"/></linearGradient></defs>'
            '<line x1="0" y1="44" x2="1200" y2="44" stroke="#1a2030"/><line x1="0" y1="88" x2="1200" y2="88" stroke="#1a2030"/><line x1="0" y1="132" x2="1200" y2="132" stroke="#1a2030"/><line x1="0" y1="176" x2="1200" y2="176" stroke="#1a2030"/>'
            '<text x="6" y="42" fill="#354057" font-size="10" font-family="DM Mono">$27k</text><text x="6" y="86" fill="#354057" font-size="10" font-family="DM Mono">$21k</text><text x="6" y="130" fill="#354057" font-size="10" font-family="DM Mono">$17k</text><text x="6" y="174" fill="#354057" font-size="10" font-family="DM Mono">$12k</text>'
            '<line x1="300" y1="0" x2="300" y2="200" stroke="#e8b84b" stroke-width="1" stroke-dasharray="4,4" opacity="0.3"/>'
            '<line x1="580" y1="0" x2="580" y2="200" stroke="#4f9de0" stroke-width="1" stroke-dasharray="4,4" opacity="0.25"/>'
            '<line x1="800" y1="0" x2="800" y2="200" stroke="#38c87a" stroke-width="1" stroke-dasharray="4,4" opacity="0.25"/>'
            '<polyline points="40,198 120,180 200,162 260,138 300,118 360,108 420,100 480,108 530,92 580,72 630,62 680,58 730,50 785,42 820,50 870,38 910,28 960,18 1000,10 1060,8 1120,6 1145,4" fill="none" stroke="#38c87a" stroke-width="2" stroke-linejoin="round"/>'
            '<polygon points="40,198 120,180 200,162 260,138 300,118 360,108 420,100 480,108 530,92 580,72 630,62 680,58 730,50 785,42 820,50 870,38 910,28 960,18 1000,10 1060,8 1120,6 1145,4 1145,205 40,205" fill="url(#eqG)"/>'
            '<circle cx="420" cy="100" r="4" fill="#e8b84b"/><text x="378" y="94" fill="#e8b84b" font-size="10" font-family="DM Mono">+$2,911</text>'
            '<circle cx="660" cy="58" r="4" fill="#38c87a"/><text x="618" y="52" fill="#38c87a" font-size="10" font-family="DM Mono">+$1,240</text>'
            '<circle cx="910" cy="28" r="4" fill="#38c87a"/><text x="870" y="22" fill="#38c87a" font-size="10" font-family="DM Mono">+$4,394</text>'
            '<text x="42" y="214" fill="#354057" font-size="10" font-family="DM Mono">28. Mai</text>'
            '<text x="256" y="214" fill="#e8b84b" font-size="10" font-family="DM Mono">Japan 20:51</text>'
            '<text x="588" y="214" fill="#4f9de0" font-size="10" font-family="DM Mono">29. Mai 00:00</text>'
            '<text x="808" y="214" fill="#38c87a" font-size="10" font-family="DM Mono">Day 3 09:53</text>'
            '</svg></div></div>'

            '<div class="section"><div class="sec-head"><div class="sec-title">Behaviour &mdash; Alle Sessions</div></div>'
            '<div class="g2" style="margin-bottom:16px">'
            '<div class="card"><div class="card-title">Cost Summary</div>'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px">'
            '<div><div style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:0.1em">Direktkosten</div><div style="font-family:var(--sans);font-size:28px;font-weight:600;color:var(--red);margin-top:5px">-$3,497</div></div>'
            '<div><div style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:0.1em">Opportunitaet</div><div style="font-family:var(--sans);font-size:28px;font-weight:600;color:var(--red);margin-top:5px">~-$7,800</div></div>'
            '</div><div style="font-size:15px;color:var(--muted2);line-height:1.8;border-top:1px solid var(--border);padding-top:12px">Ohne Behaviour-Kosten: <strong style="color:#d8e2f4">~$25,000+</strong>. TDS allein kostet ~$3,000 in Day 3.</div></div>'
            '<div class="card"><div class="card-title">Pattern-Entwicklung</div>'
            '<div class="bench-row" style="margin-top:8px"><div class="bench-name">Pattern #1 FOMO Top Scale</div><div class="bench-track"><div class="bench-fill" style="width:33%;background:var(--gold)"></div></div><div class="bench-num" style="color:var(--gold)">Day1&rarr;0</div></div>'
            '<div class="bench-row"><div class="bench-name">Pattern #2 Context Switch</div><div class="bench-track"><div class="bench-fill" style="width:33%;background:var(--gold)"></div></div><div class="bench-num" style="color:var(--gold)">Day1&rarr;0</div></div>'
            '<div class="bench-row"><div class="bench-name">Pattern #3 Concentration Loss</div><div class="bench-track"><div class="bench-fill" style="width:60%;background:var(--red)"></div></div><div class="bench-num" style="color:var(--red)">3 Sessions</div></div>'
            '<div class="bench-row"><div class="bench-name">Pattern #4 TDS NEU</div><div class="bench-track"><div class="bench-fill" style="width:80%;background:var(--red)"></div></div><div class="bench-num" style="color:var(--red)">Day3</div></div>'
            '<div class="bench-row"><div class="bench-name">&#10003; Anchor Trade Hold</div><div class="bench-track"><div class="bench-fill" style="width:100%;background:var(--green)"></div></div><div class="bench-num" style="color:var(--green)">6&times; konst.</div></div>'
            '</div></div>'

            '<div class="section"><div class="sec-head"><div class="sec-title">Aktuelle Session</div><div class="sec-meta">Day 3 &mdash; 2026-05-29</div></div>'
            + current + '</div>'

            '<div class="footer">'
            '<div>Martin Sambauer &middot; Master Report &middot; Paper Trading &middot; v2.1</div>'
            '<div>style_v1.0.css &middot; Firefox oeffnen</div>'
            '</div></div>')
    return shell("Uebersicht", "master_report.html", body, c)


# ── sessions.html ─────────────────────────────────────────────────────────────

def build_sessions(shots, c):
    d3s = [("Win Rate","71.4%","var(--gold)"),("Fills","~48","#d8e2f4"),
           ("Anchor","+$4,394","var(--green)"),("TDS-Fehler","~-$3k","var(--red)"),
           ("Avg T2BE","4:22","var(--gold)"),("Konto","$27,797","#d8e2f4")]
    js  = [("Win Rate","78.6%","var(--gold)"),("Fills","68","#d8e2f4"),
           ("Best","+$1,240","var(--green)"),("Worst","-$801","var(--red)"),
           ("BehCost","~-$3k","var(--red)"),("Konto","$21,277","#d8e2f4")]
    d1s = [("Win Rate","78.8%","var(--gold)"),("Trades","33","#d8e2f4"),
           ("Anchor","+$2,911","var(--green)"),("Worst","-$966","var(--red)"),
           ("BehCost","-$1,302","var(--red)"),("Konto","$17,349","#d8e2f4")]

    body = ('<div class="page-header"><div class="page" style="padding-bottom:0;padding-top:44px">'
            '<div class="page-label">Sessions</div>'
            '<div class="page-title">Alle Sessions &mdash; <span>neuste zuerst</span></div>'
            '</div></div>'
            '<div class="page" style="padding-top:36px">'
            + sess("Day 3 &mdash; US30 Breakout &amp; TDS-Fehler",
                   "2026-05-29 &middot; 09:53&ndash;13:48 UTC &middot; US30 &middot; USTEC &middot; JAPAN225 &middot; SPX500",
                   "+$6,568","var(--green)",d3s,day3_body(shots))
            + sess("Japan Session &mdash; Barbwire Reversal",
                   "2026-05-28 20:51&ndash;2026-05-29 01:12 UTC &middot; JAPAN225CFD",
                   "+$3,880","var(--green)",js,japan_body(shots))
            + sess("Day 1 &mdash; USTEC Trendtag",
                   "2026-05-28 &middot; 07:36&ndash;17:03 UTC &middot; GER40 &middot; USTEC &middot; US30 &middot; SPX",
                   "+$7,349","var(--green)",d1s,day1_body(shots))
            + '<div class="footer"><div>Sessions &middot; v2.1</div><div>Firefox oeffnen</div></div></div>')
    return shell("Sessions", "sessions.html", body, c)


# ── observations.html — unveraendert (enthaelt keine Screenshots die aktualisiert werden muessen) ──

def build_observations(shots, c):
    j1 = img(shots, "JAPAN225CFD_2026-05-28_19-09-00_cbdae.png", "JAPAN225CFD Overview")
    j2 = img(shots, "JAPAN225CFD_2026-05-29_01-29-07_e79b3.png", "JAPAN225CFD Executions")
    us30d3 = img(shots, "US30_2026-05-29_16-24-33_702f6.png", "US30 Day3")

    body = ('<div class="page-header"><div class="page" style="padding-bottom:0;padding-top:44px">'
            '<div class="page-label">Observations</div>'
            '<div class="page-title">Market Observations &mdash; <span>Redaktionelle Einsichten</span></div>'
            '<div class="page-sub" style="margin-top:6px">Beobachtete Markt-Charakteristiken. Keine Regeln. Brueche moeglich.</div>'
            '</div></div>'
            '<div class="page" style="padding-top:36px">'

            '<div class="obs-block"><div class="obs-head"><div class="obs-id">OBS-001</div>'
            '<div class="obs-name">Horizontales Alternieren um SMA20 &mdash; Pure Range</div>'
            '<div style="margin-top:8px;display:flex;gap:8px"><span class="badge op">Anecdotal</span><span style="font-size:12px;color:var(--muted2)">2026-05-29</span></div>'
            '</div><div class="obs-body">'
            '<div class="obs-section-title">Kernbeobachtung</div><div class="obs-text">Preis pendelt um flachen SMA20 ohne Richtungsentscheidung. Minuten bis Stunden.</div>'
            '<div class="obs-section-title">Chartmerkmale</div><div class="obs-text"><ul><li>SMA20 flach</li><li>Preis alterniert zwischen beiden Bollinger Baendern</li><li>Kein stabiler Aircushion</li></ul></div>'
            '<div class="obs-section-title">Trading</div><div class="obs-text">Bollinger faden. Kleine Positionen, schnelle Exits. Stoppen wenn SMA20 sich neigt.</div>'
            '</div></div>'

            '<div class="obs-block"><div class="obs-head"><div class="obs-id">OBS-002</div>'
            '<div class="obs-name">Alternieren mit Drift &mdash; Range transformiert sich in Trend-Kanal</div>'
            '<div style="margin-top:8px;display:flex;gap:8px"><span class="badge op">Anecdotal</span><span style="font-size:12px;color:var(--muted2)">Japan 2026-05-29</span></div>'
            '</div><div class="obs-body">'
            '<div class="obs-section-title">Kernbeobachtung</div><div class="obs-text">Range transformiert sich graduell in Trend ohne alternierenden Charakter zu verlieren. Fruehsignal: hoehere Tiefs vor der Richtungsentscheidung.</div>'
            '<div class="obs-section-title">Drei Phasen</div><div class="obs-text">'
            '<strong style="color:#d8e2f4">Phase 1:</strong> SMA20 horizontal, beide Baender alternierend.<br><br>'
            '<strong style="color:#d8e2f4">Phase 2 (kritisch):</strong> SMA20 neigt sich, hoehere Tiefs, 20&ndash;60 Min auf 5M &mdash; hoechster Entry-Wert.<br><br>'
            '<strong style="color:#d8e2f4">Phase 3:</strong> Oberes Bollinger-Segment, Korrekturen bis SMA20.</div>'
            '<div class="obs-section-title">Beispiel Japan 2026-05-29</div>'
            '<div class="obs-text">P1 ~20:50&ndash;22:00 UTC. P2 ~22:00&ndash;22:30: Entry-Fenster verpasst. P3 ~22:30&ndash;01:00: Gegenrichtungs-Trades statt Trend. Potenzial ~$5k, realisiert ~$2.3k.</div>'
            '<div class="obs-chart">' + j1 + '<div class="obs-caption">Phase 1 Alternierungszone, Phase 2 SMA-Crossing, Phase 3 Trend-Kanal.</div></div>'
            '<div class="obs-chart">' + j2 + '<div class="obs-caption">Execution Marks: rote Pfeile in Phase 3 = Gegenrichtungs-Trades.</div></div>'
            '</div></div>'

            '<div class="obs-block" style="border-left:2px solid var(--gold)"><div class="obs-head"><div class="obs-id">OBS-003 &mdash; NEU</div>'
            '<div class="obs-name">Key-Level Validation Strategy &mdash; Taktisches Loss Pyramiding am Support</div>'
            '<div style="margin-top:8px;display:flex;gap:8px"><span class="badge ev">Anecdotal</span><span style="font-size:12px;color:var(--muted2)">Day 3 2026-05-29</span></div>'
            '</div><div class="obs-body">'
            '<div class="obs-section-title">Kernbeobachtung</div><div class="obs-text">LP ist generell destruktiv &mdash; aber bei einem Ruecklauf zum vorher identifizierten Key-Level (Support bei Longs) wird es zur edge-positiven Taktik: zweiter geplanter Einstieg mit Stop direkt hinter dem Level. Bei Level-Haltung: massiv profitabler Cluster. Bei Level-Bruch: sofortiger Exit mit minimalem Zusatzverlust.</div>'
            '<div class="obs-section-title">Taktisches LP vs Blindes Averaging</div><div class="obs-text"><ul>'
            '<li><strong style="color:var(--green)">Taktisch:</strong> Vorab geplant, spezifisches Level, definierter Stop dahinter</li>'
            '<li><strong style="color:var(--red)">Blind:</strong> Reaktiv, kein Stop, Hoffnungskauf</li>'
            '</ul></div>'
            '<div class="obs-section-title">Beispiel &mdash; Day 3 US30 2026-05-29</div><div class="obs-text">'
            'Support-Zone 50,860&ndash;50,875 identifiziert. LP-Aufbau bei Ruecklauf. Stop unter 50,850. Level hielt &rarr; Exit 40 Units @ 50,989 = +$4,394. Ohne taktisches LP ca. 30% weniger Gewinn.</div>'
            '<div class="obs-chart">' + us30d3 + '<div class="obs-caption">US30 5M Day 3. LP-Aufbau am Support 50,860&ndash;50,875 erkennbar als dichte Long-Entry-Cluster.</div></div>'
            '</div></div>'

            '<div id="terminology" style="margin-top:52px">'
            '<div class="sec-head"><div class="sec-title">Terminologie &mdash; Quick Reference</div></div>'
            '<div class="g2">'
            '<div style="background:var(--s1);border:1px solid var(--border);padding:18px 22px"><div style="font-family:var(--sans);font-size:14px;font-weight:600;color:#d8e2f4;margin-bottom:6px">T2BE &mdash; Time to Break-Even</div><div style="font-size:15px;color:var(--text);line-height:1.75">Zeit vom ersten Entry bis nie mehr im unrealisierten Verlust. GREEN &le;2 Min, YELLOW 2&ndash;10, RED &gt;10. Langer T2BE = schlechtes Timing ODER bewusstes LP (Kontext!).</div></div>'
            '<div style="background:var(--s1);border:1px solid var(--border);padding:18px 22px"><div style="font-family:var(--sans);font-size:14px;font-weight:600;color:#d8e2f4;margin-bottom:6px">Profit Pyramiding (PP)</div><div style="font-size:15px;color:var(--text);line-height:1.75">Nachskalieren im Gewinn. Korrekte Art zu skalieren. Zeigt sich in stabilen Stress-Barometern.</div></div>'
            '<div style="background:var(--s1);border:1px solid var(--border);padding:18px 22px"><div style="font-family:var(--sans);font-size:14px;font-weight:600;color:#d8e2f4;margin-bottom:6px">Loss Pyramiding (LP)</div><div style="font-size:15px;color:var(--text);line-height:1.75">Nachskalieren im Verlust. Riskant wenn blind &mdash; edge-positiv als taktisches LP am Key-Level (OBS-003) mit definiertem Stop.</div></div>'
            '<div style="background:var(--s1);border:1px solid var(--border);padding:18px 22px"><div style="font-family:var(--sans);font-size:14px;font-weight:600;color:#d8e2f4;margin-bottom:6px">TDS &mdash; Target Derangement Syndrome</div><div style="font-size:15px;color:var(--text);line-height:1.75">Pattern #4 NEU. Nach grossem TP impulsiv in Gegenrichtung trotz Methoden-Regel dagegen. Regel: Nach TP in 11h-Zone kein Short bis 13:30 UTC.</div></div>'
            '<div style="background:var(--s1);border:1px solid var(--border);padding:18px 22px"><div style="font-family:var(--sans);font-size:14px;font-weight:600;color:#d8e2f4;margin-bottom:6px">Risiko-Stressbarometer</div><div style="font-size:15px;color:var(--text);line-height:1.75">Cluster-DD relativ zum Konto. GREEN &le;1%, YELLOW 1&ndash;3%, RED &gt;3%. Direkt bei Session-Screenshots.</div></div>'
            '<div style="background:var(--s1);border:1px solid var(--border);padding:18px 22px"><div style="font-family:var(--sans);font-size:14px;font-weight:600;color:#d8e2f4;margin-bottom:6px">HSR &mdash; Hold-to-Scalp Ratio</div><div style="font-size:15px;color:var(--text);line-height:1.75">Realisierter PnL / Potenziellem PnL beim initialen TP. Niedriger HSR = zu fruehes Schliessen (Angst). Hoher HSR = Conviction gehalten.</div></div>'
            '</div></div>'

            '<div class="footer"><div>Observations &middot; v2.1</div><div>Firefox oeffnen</div></div>'
            '</div>')
    return shell("Observations", "observations.html", body, c)


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Lade CSS...")
    c = css()
    print("Lade Screenshots...")
    shots = load_shots()
    print(str(len(shots)) + " Screenshots")

    print("Schreibe master_report.html...")
    with open(os.path.join(REPORTS_DIR, "master_report.html"), "w") as f:
        f.write(build_master(shots, c))

    print("Schreibe sessions.html...")
    with open(os.path.join(REPORTS_DIR, "sessions.html"), "w") as f:
        f.write(build_sessions(shots, c))

    print("Schreibe observations.html...")
    with open(os.path.join(REPORTS_DIR, "observations.html"), "w") as f:
        f.write(build_observations(shots, c))

    print("Fertig! open -a Firefox ~/Documents/Trading/reports/master_report.html")
