#!/usr/bin/env python3
"""
parse_trades.py — Trading Journal Trade Parser
Liest TradingView Export-CSVs und schreibt in master_trades.csv.
Verwendung: python3 scripts/parse_trades.py [YYYY-MM-DD] [trader]
Defaults: heutiges Datum, trader=martin
"""

import sys
import os
import csv
from datetime import datetime
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
    """Lädt alle bereits vorhandenen trade_ids um Duplikate zu verhindern."""
    ids = set()
    if not os.path.exists(MASTER_TRADES):
        return ids
    with open(MASTER_TRADES, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids.add(row["trade_id"])
    return ids


def load_existing_session_ids():
    """Lädt bereits vorhandene Session-Keys (date+session+trader)."""
    ids = set()
    if not os.path.exists(MASTER_STATS):
        return ids
    with open(MASTER_STATS, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids.add(f"{row['date']}_{row['session']}_{row['trader']}")
    return ids


def parse_balance_history(filepath):
    """
    Parst balance-history CSV.
    Gibt dict zurück: order_id → pnl_usd (nur Close-Zeilen, nicht Commissions)
    Gibt auch Start- und End-Balance zurück.
    """
    pnl_by_order = {}
    balances = []

    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            action = row.get("Action", "")
            pnl_val = row.get("Realized PnL (value)", "0") or "0"
            bal_after = row.get("Balance after", "0") or "0"

            try:
                bal_after_f = float(bal_after)
                balances.append(bal_after_f)
            except ValueError:
                pass

            # Nur echte PnL-Zeilen (nicht Commission-Zeilen)
            if "Commission for:" in action:
                continue
            if "Close" not in action and "Enter" not in action:
                continue

            try:
                pnl = float(pnl_val)
            except ValueError:
                continue

            # Order ID aus Action-Text extrahieren (nicht immer vorhanden)
            # Wir nutzen Zeit+Symbol als Key
            time_str = row.get("Time", "")
            pnl_by_order[time_str] = pnl

    start_balance = balances[-1] if balances else 0
    end_balance   = balances[0]  if balances else 0
    return pnl_by_order, start_balance, end_balance


def parse_order_history(filepath, date_filter, pnl_by_time):
    """
    Parst order-history CSV → Liste von Trade-Dicts.
    Nur Filled Orders, nur der gewünschte date_filter.
    """
    trades = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("Status", "") != "Filled":
                continue

            placing_time = row.get("Placing time", "")
            if not placing_time:
                continue

            # Datum filtern
            try:
                dt = datetime.strptime(placing_time, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue

            # Nur Trades des gewünschten Tages
            if dt.strftime("%Y-%m-%d") != date_filter:
                continue

            symbol   = row.get("Symbol", "")
            side     = row.get("Side", "")
            order_type = row.get("Type", "Market")
            quantity = row.get("Quantity", "0")
            fill_price = row.get("Fill price", "0") or "0"
            commission = row.get("Commission", "0") or "0"
            order_id   = row.get("Order ID", "")

            # PnL aus Balance-History matchen (via Zeit)
            pnl = pnl_by_time.get(placing_time, 0.0)

            try:
                fill_price_f = float(fill_price)
                commission_f = float(commission)
                quantity_i   = int(float(quantity))
            except ValueError:
                continue

            trades.append({
                "order_id":    order_id,
                "datetime":    dt,
                "symbol":      symbol,
                "side":        side,
                "type":        order_type,
                "quantity":    quantity_i,
                "fill_price":  fill_price_f,
                "pnl_usd":     pnl,
                "commission":  commission_f,
            })

    return trades


def compute_stats(trades, date_str, session_name, trader, start_balance, end_balance):
    """Berechnet Session-Stats aus Trade-Liste."""
    # Nur Close-Trades haben PnL != 0
    close_trades = [t for t in trades if t["pnl_usd"] != 0]

    wins   = [t for t in close_trades if t["pnl_usd"] > 0]
    losses = [t for t in close_trades if t["pnl_usd"] < 0]
    be     = [t for t in close_trades if t["pnl_usd"] == 0]

    total_closed = len(close_trades)
    win_rate = f"{len(wins)/total_closed*100:.1f}%" if total_closed > 0 else "0%"
    gross_pnl    = sum(t["pnl_usd"]    for t in close_trades)
    commissions  = sum(t["commission"] for t in trades)
    net_pnl      = gross_pnl - commissions
    biggest_win  = max((t["pnl_usd"] for t in wins),   default=0)
    biggest_loss = min((t["pnl_usd"] for t in losses), default=0)

    # Hauptinstrument bestimmen
    symbol_count = defaultdict(int)
    for t in trades:
        symbol_count[t["symbol"]] += 1
    instrument = max(symbol_count, key=symbol_count.get) if symbol_count else ""

    return {
        "date":          date_str,
        "session":       session_name,
        "trader":        trader,
        "instrument":    instrument,
        "trades":        len(trades),
        "wins":          len(wins),
        "losses":        len(losses),
        "be":            len(be),
        "win_rate":      win_rate,
        "gross_pnl":     round(gross_pnl, 2),
        "commissions":   round(commissions, 2),
        "net_pnl":       round(net_pnl, 2),
        "start_balance": round(start_balance, 2),
        "end_balance":   round(end_balance, 2),
        "biggest_win":   round(biggest_win, 2),
        "biggest_loss":  round(biggest_loss, 2),
        "notes":         "",
    }


def ensure_master_trades():
    os.makedirs(os.path.dirname(MASTER_TRADES), exist_ok=True)
    if not os.path.exists(MASTER_TRADES):
        with open(MASTER_TRADES, "w", newline="") as f:
            csv.writer(f).writerow(MASTER_TRADES_HEADER)
        print(f"  Erstellt: master_trades.csv")


def ensure_master_stats():
    os.makedirs(os.path.dirname(MASTER_STATS), exist_ok=True)
    if not os.path.exists(MASTER_STATS):
        with open(MASTER_STATS, "w", newline="") as f:
            csv.writer(f).writerow(MASTER_STATS_HEADER)
        print(f"  Erstellt: master_stats.csv (neu)")


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
    existing = load_existing_session_ids()
    key = f"{stats['date']}_{stats['session']}_{stats['trader']}"
    if key in existing:
        print(f"  Stats für {key} bereits vorhanden, übersprungen")
        return False
    with open(MASTER_STATS, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=MASTER_STATS_HEADER)
        writer.writerow(stats)
    return True


def process_session(date_str, trader, session_name=None):
    """Verarbeitet alle CSVs in exports/YYYY-MM-DD/ für einen Trader."""
    export_dir = os.path.join(REPO_DIR, "data", "traders", trader, "exports", date_str)

    if not os.path.exists(export_dir):
        print(f"Kein Export-Verzeichnis: {export_dir}")
        return

    # Dateien suchen
    balance_file = order_file = None
    for fname in os.listdir(export_dir):
        if "balance-history" in fname:
            balance_file = os.path.join(export_dir, fname)
        elif "order-history" in fname:
            order_file = os.path.join(export_dir, fname)

    if not balance_file or not order_file:
        print(f"Fehlende Dateien in {export_dir}")
        print(f"  Balance: {'OK' if balance_file else 'FEHLT'}")
        print(f"  Orders:  {'OK' if order_file else 'FEHLT'}")
        return

    print(f"\nVerarbeite: {date_str} / {trader}")

    pnl_by_time, start_bal, end_bal = parse_balance_history(balance_file)
    trades = parse_order_history(order_file, date_str, pnl_by_time)

    if not trades:
        print(f"  Keine Trades gefunden für {date_str}")
        return

    # Session-Name ableiten wenn nicht angegeben
    if not session_name:
        symbols = set(t["symbol"] for t in trades)
        if "WHSELFINVEST:JAPAN225CFD" in symbols:
            session_name = "japan"
        elif any("TRADENATION" in s for s in symbols):
            session_name = "ustec"
        else:
            session_name = "day"

    # Trade-IDs generieren: YYYY-MM-DD_OrderID_Trader
    trades_with_ids = []
    for t in trades:
        trade_id = f"{date_str}_{t['order_id']}_{trader}"
        trades_with_ids.append({
            "trade_id":      trade_id,
            "date":          date_str,
            "time":          t["datetime"].strftime("%H:%M:%S"),
            "symbol":        t["symbol"],
            "side":          t["side"],
            "type":          t["type"],
            "quantity":      t["quantity"],
            "fill_price":    t["fill_price"],
            "pnl_usd":       t["pnl_usd"],
            "commission_usd": t["commission"],
            "session":       session_name,
            "trader":        trader,
        })

    ensure_master_trades()
    ensure_master_stats()

    new_trades = append_trades(trades_with_ids)
    print(f"  Trades: {new_trades} neu hinzugefügt ({len(trades_with_ids)} total)")

    stats = compute_stats(trades, date_str, session_name, trader, start_bal, end_bal)
    stats_added = append_stats(stats)
    if stats_added:
        print(f"  Stats:  Net PnL ${stats['net_pnl']:+.2f} | Win Rate {stats['win_rate']} | {stats['trades']} Trades")

    return stats


if __name__ == "__main__":
    date_str     = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
    trader       = sys.argv[2] if len(sys.argv) > 2 else "martin"
    session_name = sys.argv[3] if len(sys.argv) > 3 else None

    process_session(date_str, trader, session_name)
