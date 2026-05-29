#!/usr/bin/env python3
"""
fetch_market_data.py — Trading Journal Market Data Fetcher v2.1
Holt 5M Kerzen für alle Instrumente via yfinance.
Verwendung: python3 scripts/fetch_market_data.py [YYYY-MM-DD]
Ohne Datum: holt heutigen Tag.
"""

import sys
import os
import csv
from datetime import datetime, timedelta

try:
    import yfinance as yf
except ImportError:
    print("yfinance nicht installiert. Bitte: pip3 install yfinance")
    sys.exit(1)

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARKET_DIR = os.path.join(REPO_DIR, "data", "market")

# Symbol-Mapping: internes Kürzel → yfinance Ticker
# Ticker-Notizen:
#   NQ=F  = NASDAQ 100 Futures (liquid, gute 5M Daten)
#   YM=F  = Dow Jones Futures
#   ^GDAXI = DAX Index (Caret nötig, kein 5M via yfinance → 1h als Fallback)
#   NKD=F = Nikkei 225 Dollar Futures
#   ES=F  = S&P 500 Futures
SYMBOLS = {
    "USTEC":    ("NQ=F",   "5m"),
    "US30":     ("YM=F",   "5m"),
    "GER40":    ("^GDAXI", "1h"),   # yfinance hat kein 5M für DAX, 1h als Annäherung
    "JAPAN225": ("NKD=F",  "5m"),
    "SPX":      ("ES=F",   "5m"),
}

def fetch_day(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"Ungültiges Datum: {date_str}. Format: YYYY-MM-DD")
        sys.exit(1)

    # Breites Fenster: 2 Tage vor bis 2 nach dem Zieldatum
    # Nötig weil yfinance UTC liefert und Märkte verschiedene Zeitzonen haben
    start = (date - timedelta(days=2)).strftime("%Y-%m-%d")
    end   = (date + timedelta(days=2)).strftime("%Y-%m-%d")

    os.makedirs(MARKET_DIR, exist_ok=True)
    fetched = []
    skipped = []

    for symbol, (ticker, interval) in SYMBOLS.items():
        outfile = os.path.join(MARKET_DIR, f"{date_str}_{symbol}.csv")

        if os.path.exists(outfile):
            print(f"  {symbol}: bereits vorhanden, übersprungen")
            skipped.append(symbol)
            continue

        try:
            df = yf.download(
                ticker,
                start=start,
                end=end,
                interval=interval,
                progress=False,
                auto_adjust=True
            )

            if df.empty:
                print(f"  {symbol}: keine Daten erhalten ({ticker})")
                continue

            # Timezone entfernen für einfachen Datumsvergleich
            if hasattr(df.index, 'tz') and df.index.tz is not None:
                df.index = df.index.tz_convert("UTC").tz_localize(None)

            # Spalten normalisieren (yfinance gibt manchmal MultiIndex zurück)
            if hasattr(df.columns, 'levels'):
                df.columns = df.columns.get_level_values(0)

            # Zieldatum + Vortag einschließen (Japan-Session geht über Mitternacht UTC)
            prev_date = date - timedelta(days=1)
            df_day = df[
                (df.index.date >= prev_date.date()) &
                (df.index.date <= date.date())
            ]

            if df_day.empty:
                print(f"  {symbol}: keine Daten für {date_str} (±1 Tag)")
                continue

            # CSV schreiben
            with open(outfile, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["datetime", "symbol", "open", "high", "low", "close", "volume"])
                for ts, row in df_day.iterrows():
                    try:
                        writer.writerow([
                            ts.strftime("%Y-%m-%d %H:%M:%S"),
                            symbol,
                            round(float(row["Open"]),   2),
                            round(float(row["High"]),   2),
                            round(float(row["Low"]),    2),
                            round(float(row["Close"]),  2),
                            int(float(row["Volume"])) if "Volume" in row and str(row["Volume"]) not in ("nan", "") else 0,
                        ])
                    except Exception:
                        continue

            print(f"  {symbol} ({interval}): {len(df_day)} Kerzen → {os.path.basename(outfile)}")
            fetched.append(symbol)

        except Exception as e:
            print(f"  {symbol}: Fehler — {e}")

    print(f"\nFertig: {len(fetched)} neu, {len(skipped)} übersprungen")
    return fetched


if __name__ == "__main__":
    date_str = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
    print(f"Marktdaten für {date_str}...")
    fetch_day(date_str)
