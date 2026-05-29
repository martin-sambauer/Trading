#!/usr/bin/env python3
# parse_and_export.py v3.0
# Liest master_stats.csv + master_trades.csv, berechnet alle v2.0 KPIs
# und exportiert als data/master/dashboard_data.json.
# Kein HTML hier. Das Dashboard-HTML laedt das JSON via fetch().

import os, json, csv
from datetime import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATS_CSV = os.path.join(REPO, "data", "master", "master_stats.csv")
OUT_JSON  = os.path.join(REPO, "data", "master", "dashboard_data.json")


# ── Barometer-Klassifizierung ──────────────────────────────────

def t2be_level(avg_t2be_str):
    """GREEN <= 2 Min | YELLOW 2-10 Min | RED > 10 Min"""
    try:
        parts = avg_t2be_str.split(":")
        minutes = int(parts[0]) * 60 + int(parts[1]) + int(parts[2]) / 60
        if minutes <= 2:
            return "GREEN"
        elif minutes <= 10:
            return "YELLOW"
        return "RED"
    except Exception:
        return "UNKNOWN"


def stress_level(cluster_dd, account_balance):
    """GREEN <= 1% | YELLOW 1-3% | RED > 3%"""
    try:
        pct = abs(float(cluster_dd)) / float(account_balance) * 100
        if pct <= 1:
            return "GREEN"
        elif pct <= 3:
            return "YELLOW"
        return "RED"
    except Exception:
        return "UNKNOWN"


def t2be_to_seconds(t2be_str):
    try:
        h, m, s = t2be_str.split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)
    except Exception:
        return 0


# ── Session laden ──────────────────────────────────────────────

def load_sessions():
    sessions = []
    if not os.path.exists(STATS_CSV):
        print("WARNUNG: " + STATS_CSV + " nicht gefunden")
        return sessions
    with open(STATS_CSV, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sessions.append(row)
    return sessions


# ── Aggregierte Gesamt-KPIs ────────────────────────────────────

def aggregate(sessions):
    if not sessions:
        return {}

    total_pnl  = sum(float(s["Net_PnL"]) for s in sessions)
    win_rates  = [float(s["Win_Rate"]) for s in sessions]
    avg_wr     = sum(win_rates) / len(win_rates)

    all_t2be_s = [t2be_to_seconds(s["Avg_T2BE"]) for s in sessions]
    avg_t2be_s = sum(all_t2be_s) / len(all_t2be_s) if all_t2be_s else 0
    avg_t2be   = "{:02d}:{:02d}:{:02d}".format(
        int(avg_t2be_s // 3600),
        int((avg_t2be_s % 3600) // 60),
        int(avg_t2be_s % 60)
    )

    total_pp   = sum(float(s["Net_PnL_PP"]) for s in sessions)
    total_lp   = sum(float(s["Net_PnL_LP"]) for s in sessions)
    worst_pp   = min(float(s["Worst_Loss_PP"]) for s in sessions)
    worst_lp   = min(float(s["Worst_Loss_LP"]) for s in sessions)

    max_dd_lp  = min(float(s["Max_Cluster_DD_LP"]) for s in sessions)
    avg_dd_lp  = sum(float(s["Avg_Cluster_DD_LP"]) for s in sessions) / len(sessions)

    # Bestes und schlechtestes Session
    by_pnl     = sorted(sessions, key=lambda s: float(s["Net_PnL"]), reverse=True)
    best2      = [s["Session_Date"] for s in by_pnl[:2]]
    worst2     = [s["Session_Date"] for s in by_pnl[-2:]]

    return {
        "total_net_pnl": round(total_pnl, 2),
        "session_count": len(sessions),
        "avg_win_rate": round(avg_wr, 1),
        "avg_t2be": avg_t2be,
        "avg_t2be_level": t2be_level(avg_t2be),
        "total_pnl_pp": round(total_pp, 2),
        "total_pnl_lp": round(total_lp, 2),
        "worst_loss_pp": round(worst_pp, 2),
        "worst_loss_lp": round(worst_lp, 2),
        "max_cluster_dd_lp": round(max_dd_lp, 2),
        "avg_cluster_dd_lp": round(avg_dd_lp, 2),
        "best_sessions": best2,
        "worst_sessions": worst2,
    }


# ── Screenshot-Map aufbauen ────────────────────────────────────

def screenshot_map():
    shots_dir = os.path.join(REPO, "screenshots")
    result = {}
    if not os.path.exists(shots_dir):
        return result
    for fname in sorted(os.listdir(shots_dir)):
        if fname.lower().endswith((".png", ".jpg", ".jpeg")):
            # Dateiname-Prefix als Schluessel: INSTRUMENT_YYYY-MM-DD
            parts = fname.split("_")
            if len(parts) >= 3:
                key = parts[0] + "_" + parts[1]
                if key not in result:
                    result[key] = []
                result[key].append(fname)
    return result


# ── Hauptfunktion ──────────────────────────────────────────────

def main():
    print("Lade Sessions aus " + STATS_CSV + " ...")
    sessions = load_sessions()
    print("  " + str(len(sessions)) + " Sessions geladen")

    print("Berechne Gesamt-KPIs ...")
    overall = aggregate(sessions)

    print("Baue Screenshot-Map ...")
    shots = screenshot_map()

    data = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "schema_version": "2.0",
        "account_type": "paper",
        "trader": "Martin",
        "overall": overall,
        "sessions": sessions,
        "screenshots": shots,
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("JSON exportiert: " + OUT_JSON)
    print("  Sessions: " + str(len(sessions)))
    print("  Screenshots gemappt: " + str(sum(len(v) for v in shots.values())))


if __name__ == "__main__":
    main()
