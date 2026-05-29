#!/usr/bin/env python3
"""
parse_trades.py — Trading Journal Trade Parser v2.1
Liest TradingView Export-CSVs und schreibt in master_trades.csv.
Verwendung: python3 scripts/parse_trades.py [YYYY-MM-DD] [trader] [session_name]
Defaults: heutiges Datum, trader=martin

WICHTIG: TradingView exportiert mit UTC-Zeit. Die Japan-Session vom Abend des
Vortags erscheint als Datum des Exporttags. Das Script filtert deshalb den
Ordnernamen (Exportdatum) statt das Datum in den Timestamps.
"""

import sys
import os
import csv
from datetime import datetime, timedelta
from collections import defaultdict

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_TRADES = os.path.join(REPO_DIR, "data", "master", "master_trades.csv")
MASTER_STATS  = os.path.join(REPO_DIR, "data", "master", "master_stats.csv")

MASTER_TRADES_HEADER = [
    "trade_id", "date", "time", "symbol", "side", "type",
    "quantity", "fill_price", "pnl_usd", "commission_usd",
    "session", "trader"
]

MASTER_STATS_HEADER = [
    "date", "session", "trader", "instrument", "trades", "wins", "losses", "be",
    "win_rate", "gross_pnl", "commissions", "net_pnl",
    "start_balance", "end_balance", "biggest_win", "biggest_loss", "notes"
]


def load_existing_trade_ids():
    ids = set()
    if not os.path.exists(MASTER_TRADES):
        return ids
    with open(MASTER_TRADES, "r") as f:
        for row in csv.DictReader(f):
            ids.add(row["trade_id"])
    return ids


def load_existing_session_ids():
    ids = set()
    if not os.path.exists(MASTER_STATS):
        return ids
    with open(MASTER_STATS, "r") as f:
        for row in csv.DictReader(f):
            ids.add(f"{row['date']}_{row['session']}_{row['trader']}")
    return ids


def parse_balance_history(filepath):
    """
    Gibt zurück:
      pnl_by_time: dict timestamp_str → pnl_float (nur Close-Zeilen)
      start_balance, end_balance: float
    """
    pnl_by_time = {}
    balances = []

    with open(filepath, "r") as f:
        for row in csv.DictReader(f):
            action = row.get("Action", "")
            bal_after = row.get("Balance after", "0") or "0"
            pnl_val   = row.get("Realized PnL (value)", "0") or "0"
            time_str  = row.get("Time", "")

            try:
                balances.append(float(bal_after))
            except ValueError:
                pass

            if "Commission for:" in action:
                continue

            try:
                pnl = float(pnl_val)
                if pnl != 0:
                    pnl_by_time[time_str] = pnl
            except ValueError:
                pass

    start_balance = balances[-1] if balances else 0.0
    end_balance   = balances[0]  if balances else 0.0
    return pnl_by_time, start_balance, end_balance


def parse_order_history(filepath, pnl_by_time):
    """
    Parst ALLE Filled Orders aus dem File — kein Datumsfilter.
    (Wir vertrauen dem Ordnernamen als Exportdatum.)
    """
    trades = []
    with open(filepath, "r") as f:
        for row in csv.DictReader(f):
            if row.get("Status", "") != "Filled":
                continue

            placing_time = row.get("Placing time", "")
            if not placing_time:
                continue

            try:
                dt = datetime.strptime(placing_time, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue

            try:
                fill_price   = float(row.get("Fill price", "0") or "0")
                commission   = float(row.get("Commission", "0") or "0")
                quantity     = int(float(row.get("Quantity", "0") or "0"))
            except ValueError:
                continue

            pnl = pnl_by_time.get(placing_time, 0.0)

            trades.append({
                "order_id":   row.get("Order ID", ""),
                "datetime":   dt,
                "symbol":     row.get("Symbol", ""),
                "side":       row.get("Side", ""),
                "type":       row.get("Type", "Market"),
                "quantity":   quantity,
                "fill_price": fill_price,
                "pnl_usd":    pnl,
                "commission": commission,
            })

    return trades


def infer_session(trades):
    """Leitet Session-Name aus den gehandelten Symbolen ab."""
    symbols = set(t["symbol"] for t in trades)
    if any("JAPAN225" in s for s in symbols):
        return "japan"
    if any("USTEC" in s or "TRADENATION" in s for s in symbols):
        return "ustec"
    if any("GER40" in s for s in symbols):
        return "ger40"
    return "day"


def compute_stats(trades, export_date, session_name, trader, start_balance, end_balance):
    close_trades = [t for t in trades if t["pnl_usd"] != 0]
    wins   = [t for t in close_trades if t["pnl_usd"] > 0]
    losses = [t for t in close_trades if t["pnl_usd"] < 0]
    be     = [t for t in close_trades if t["pnl_usd"] == 0]

    total_closed = len(close_trades)
    win_rate    = f"{len(wins)/total_closed*100:.1f}%" if total_closed > 0 else "0%"
    gross_pnl   = round(sum(t["pnl_usd"]    for t in close_trades), 2)
    commissions = round(sum(t["commission"] for t in trades), 2)
    net_pnl     = round(gross_pnl - commissions, 2)
    biggest_win  = round(max((t["pnl_usd"] for t in wins),   default=0), 2)
    biggest_loss = round(min((t["pnl_usd"] for t in losses), default=0), 2)

    symbol_count = defaultdict(int)
    for t in trades:
        symbol_count[t["symbol"]] += 1
    instrument = max(symbol_count, key=symbol_count.get) if symbol_count else ""

    return {
        "date":          export_date,
        "session":       session_name,
        "trader":        trader,
        "instrument":    instrument,
        "trades":        len(trades),
        "wins":          len(wins),
        "losses":        len(losses),
        "be":            len(be),
        "win_rate":      win_rate,
        "gross_pnl":     gross_pnl,
        "commissions":   commissions,
        "net_pnl":       net_pnl,
        "start_balance": round(start_balance, 2),
        "end_balance":   round(end_balance, 2),
        "biggest_win":   biggest_win,
        "biggest_loss":  biggest_loss,
        "notes":         "",
    }


def ensure_file(path, header):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", newline="") as f:
            csv.writer(f).writerow(header)
        print(f"  Erstellt: {os.path.basename(path)}")


def append_trades(trades_to_add):
    existing_ids = load_existing_trade_ids()
    new_count = 0
    with open(MASTER_TRADES, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=MASTER_TRADES_HEADER)
        for t in trades_to_add:
            if t["trade_id"] in existing_ids:
                continue
            writer.writerow(t)
            existing_ids.add(t["trade_id"])
            new_count += 1
    return new_count


def append_stats(stats):
    key = f"{stats['date']}_{stats['session']}_{stats['trader']}"
    if key in load_existing_session_ids():
        print(f"  Stats für {key} bereits vorhanden, übersprungen")
        return False
    with open(MASTER_STATS, "a", newline="") as f:
        csv.DictWriter(f, fieldnames=MASTER_STATS_HEADER).writerow(stats)
    return True


def process_session(export_date, trader, session_name=None):
    """Verarbeitet alle CSVs in exports/YYYY-MM-DD/ für einen Trader."""
    export_dir = os.path.join(REPO_DIR, "data", "traders", trader, "exports", export_date)

    if not os.path.exists(export_dir):
        print(f"Kein Export-Verzeichnis: {export_dir}")
        return

    balance_file = order_file = None
    for fname in os.listdir(export_dir):
        fpath = os.path.join(export_dir, fname)
        if "balance-history" in fname:
            balance_file = fpath
        elif "order-history" in fname and "all" not in fname.lower():
            order_file = fpath
        elif "order-history" in fname:
            order_file = fpath  # Fallback: nimm auch "all"-Files

    if not balance_file or not order_file:
        print(f"Fehlende Dateien in {export_dir}")
        print(f"  Balance: {'OK' if balance_file else 'FEHLT'}")
        print(f"  Orders:  {'OK' if order_file else 'FEHLT'}")
        return

    print(f"\nVerarbeite: {export_date} / {trader}")

    pnl_by_time, start_bal, end_bal = parse_balance_history(balance_file)
    trades = parse_order_history(order_file, pnl_by_time)

    if not trades:
        print(f"  Keine Trades gefunden")
        return

    if not session_name:
        session_name = infer_session(trades)

    # Trade-IDs: exportdatum_orderid_trader (stabil, duplikatsicher)
    trades_with_ids = []
    for t in trades:
        # Fallback-ID wenn Order ID leer
        oid = t["order_id"] or f"{t['datetime'].strftime('%H%M%S')}_{t['symbol'][-6:]}"
        trade_id = f"{export_date}_{oid}_{trader}"
        trades_with_ids.append({
            "trade_id":       trade_id,
            "date":           t["datetime"].strftime("%Y-%m-%d"),
            "time":           t["datetime"].strftime("%H:%M:%S"),
            "symbol":         t["symbol"],
            "side":           t["side"],
            "type":           t["type"],
            "quantity":       t["quantity"],
            "fill_price":     t["fill_price"],
            "pnl_usd":        t["pnl_usd"],
            "commission_usd": t["commission"],
            "session":        session_name,
            "trader":         trader,
        })

    ensure_file(MASTER_TRADES, MASTER_TRADES_HEADER)
    ensure_file(MASTER_STATS,  MASTER_STATS_HEADER)

    new_trades = append_trades(trades_with_ids)
    print(f"  Trades: {new_trades} neu ({len(trades_with_ids)} total in Export)")

    stats = compute_stats(trades, export_date, session_name, trader, start_bal, end_bal)
    if append_stats(stats):
        print(f"  Stats:  Net PnL ${stats['net_pnl']:+.2f} | {stats['win_rate']} Win Rate | {stats['trades']} Trades")

    return stats


if __name__ == "__main__":
    export_date  = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
    trader       = sys.argv[2] if len(sys.argv) > 2 else "martin"
    session_name = sys.argv[3] if len(sys.argv) > 3 else None

    process_session(export_date, trader, session_name)
