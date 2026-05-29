#!/usr/bin/env python3
"""
fetch_market_data.py — Trading Journal Market Data Fetcher
Holt 5M Kerzen für alle Instrumente via yfinance.
Verwendung: python3 scripts/fetch_market_data.py [YYYY-MM-DD]
Ohne Datum: holt heutigen Tag.
"""

import sys
import os
import csv
from datetime import datetime, timedelta, timezone

try:
    import yfinance as yf
except ImportError:
    print("yfinance nicht installiert. Bitte: pip3 install yfinance")
    sys.exit(1)

# Repo-Verzeichnis
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARKET_DIR = os.path.join(REPO_DIR, "data", "market")

# Symbol-Mapping: internes Kürzel → yfinance Ticker
SYMBOLS = {
    "USTEC":   "NQ=F",     # NASDAQ 100 Futures
    "US30":    "YM=F",     # Dow Jones Futures
    "GER40":   "GDAXI",    # DAX (Tageskerzen, kein 5M via yfinance)
    "JAPAN225":"NKD=F",    # Nikkei 225 Futures
    "SPX":     "ES=F",     # S&P 500 Futures
}

def fetch_day(date_str):
    """Holt 5M Kerzen für einen Tag für alle Symbole."""
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"Ungültiges Datum: {date_str}. Format: YYYY-MM-DD")
        sys.exit(1)

    # Download-Fenster: einen Tag vor bis einen nach (yfinance braucht Puffer)
    start = (date - timedelta(days=1)).strftime("%Y-%m-%d")
    end   = (date + timedelta(days=2)).strftime("%Y-%m-%d")

    os.makedirs(MARKET_DIR, exist_ok=True)
    fetched = []
    skipped = []

    for symbol, ticker in SYMBOLS.items():
        outfile = os.path.join(MARKET_DIR, f"{date_str}_{symbol}.csv")

        if os.path.exists(outfile):
            print(f"  {symbol}: bereits vorhanden, übersprungen")
            skipped.append(symbol)
            continue

        try:
            df = yf.download(ticker, start=start, end=end, interval="5m", progress=False, auto_adjust=True)

            if df.empty:
                print(f"  {symbol}: keine Daten erhalten ({ticker})")
                continue

            # Nur den gewünschten Tag filtern
            df.index = df.index.tz_localize(None) if df.index.tz is not None else df.index
            df_day = df[df.index.date == date.date()]

            if df_day.empty:
                print(f"  {symbol}: keine Daten für {date_str}")
                continue

            # Spalten normalisieren (yfinance gibt MultiIndex zurück)
            if hasattr(df_day.columns, 'levels'):
                df_day.columns = df_day.columns.get_level_values(0)

            # Schreibe CSV
            with open(outfile, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["datetime", "symbol", "open", "high", "low", "close", "volume"])
                for ts, row in df_day.iterrows():
                    writer.writerow([
                        ts.strftime("%Y-%m-%d %H:%M:%S"),
                        symbol,
                        round(float(row["Open"]), 2),
                        round(float(row["High"]), 2),
                        round(float(row["Low"]),  2),
                        round(float(row["Close"]),2),
                        int(row["Volume"]) if "Volume" in row else 0,
                    ])

            print(f"  {symbol}: {len(df_day)} Kerzen → {os.path.basename(outfile)}")
            fetched.append(symbol)

        except Exception as e:
            print(f"  {symbol}: Fehler — {e}")

    print(f"\nFertig: {len(fetched)} neu, {len(skipped)} übersprungen")
    return fetched


if __name__ == "__main__":
    date_str = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
    print(f"Marktdaten für {date_str}...")
    fetch_day(date_str)
