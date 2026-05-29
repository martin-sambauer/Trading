<!-- Version: 1.1 | Letzte Änderung: 2026-05-28 -->
# Trader B Onboarding — Trading Journal

---

## Für Trader Bs KI: Lies das zuerst

Du arbeitest mit Trader B. Deine Aufgabe ist es, sie durch dieses Onboarding zu führen und danach täglich ihre Trading-Daten auszuwerten. Hier ist alles was du wissen musst:

**Das System:** Trader A und Trader B handeln parallel. Ihre Daten landen im selben GitHub Repo. Du analysierst Trader Bs Trades, erstellst Reports und vergleichst ihre Performance mit Trader A.

**Das Repo:** `https://github.com/trader-journal/Trading`

**Pflichtlektüre vor jeder Session:**
1. `README.md` — das Gesamtsystem
2. `method/METHOD.md` — die Handelsmethode
3. `method/TERMINOLOGY.md` — alle Begriffe (Aircushion, Battle Zone, etc.)
4. `method/HYPOTHESES.md` — aktuelle Hypothesen
5. `data/traders/trader b/master_stats.csv` — Trader Bs aggregierte Stats (sobald vorhanden)

**Trader Bs Daten liegen in:**
- `data/traders/trader b/trades/YYYY-MM-DD.csv` — tägliche Trades
- `data/traders/trader b/market/YYYY-MM-DD_SYMBOL.csv` — Marktdaten
- `reports/trader b/YYYY-MM-DD/` — Reports
- `screenshots/trader b/` — Chart-Screenshots

**Nach jeder Session:**
1. Trades aus Balance History CSV parsen
2. `data/traders/trader b/trades/YYYY-MM-DD.csv` erstellen
3. `data/traders/trader b/master_stats.csv` updaten
4. Report erstellen: `reports/trader b/YYYY-MM-DD/report.html`
5. Standalone Report: `reports/trader b/YYYY-MM-DD/report_standalone.html`
6. Falls Trader A am gleichen Tag gehandelt hat → Vergleichsreport: `reports/comparison/YYYY-MM-DD/report.html`
7. Hypothesen und Terminologie updaten falls neue Erkenntnisse
8. CHANGELOG updaten

**Führe Trader B jetzt durch das Onboarding** — fang mit Schritt 1 an und warte auf ihre Bestätigung bevor du weitermachst.

---

## Hallo Trader B! 👋

Ich bin deine KI und ich führe dich jetzt durch das Setup. Das dauert etwa 20 Minuten und danach läuft alles automatisch.

Wir bauen das gleiche System wie Trader A — du lieferst täglich deine Trading-Daten, ich analysiere sie und wir vergleichen eure Performances. Sag einfach "weiter" wenn du einen Schritt abgeschlossen hast.

---

## Schritt 1 — GitHub Account erstellen

GitHub ist wo alle Daten gespeichert werden. Du brauchst einen kostenlosen Account.

**Was du tust:**
1. Geh auf **github.com**
2. Klick auf "Sign up"
3. Email, Username und Passwort eingeben
4. Account bestätigen

**Dann:** Schick Trader A deinen GitHub Username. Er lädt dich als Collaborator ein — du bekommst eine Email von GitHub, klick auf "Accept invitation".

Sag mir deinen GitHub Username wenn du fertig bist, dann machen wir weiter.

---

## Schritt 2 — Git und Tools installieren

Öffne das Terminal (Spotlight → "Terminal") und führe diese Befehle aus:

```bash
# Git installieren
xcode-select --install
```
Ein Fenster öffnet sich → "Installieren" klicken → warten bis fertig.

```bash
# Homebrew installieren (falls noch nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# imagemagick für Screenshot-Komprimierung
brew install imagemagick

# Python-Abhängigkeiten
pip3 install --break-system-packages git+https://github.com/rongardF/tvdatafeed.git pandas
```

Sag "weiter" wenn alles installiert ist.

---

## Schritt 3 — Repo klonen

```bash
cd ~/Documents
git clone https://github.com/trader-journal/Trading.git
cd Trading
```

Das lädt das komplette Trading-Journal auf deinen Rechner.

---

## Schritt 4 — GitHub Token erstellen

GitHub braucht einen Token statt Passwort zum Hochladen.

**Was du tust:**
1. Geh auf **github.com** → oben rechts dein Profilbild → "Settings"
2. Ganz unten links: "Developer settings"
3. "Personal access tokens" → "Tokens (classic)"
4. "Generate new token (classic)"
5. Note: "Trading"
6. Expiration: "No expiration"
7. Haken bei **repo** setzen
8. "Generate token" klicken
9. Den Token kopieren (du siehst ihn nur einmal!)

**Dann im Terminal:**
```bash
git remote set-url origin https://DEIN_GITHUB_USERNAME:DEIN_TOKEN@github.com/trader-journal/Trading.git
```

Ersetze `DEIN_GITHUB_USERNAME` und `DEIN_TOKEN` mit deinen Werten.

---

## Schritt 5 — Google Drive einrichten

Du brauchst die Google Drive Desktop App für deine Screenshots.

**Was du tust:**
1. Geh auf **drive.google.com/drive/download**
2. App herunterladen und installieren
3. Mit deinem Google Account einloggen
4. Im Finder: Google Drive → neuen Ordner anlegen: `Trading_Journal_Trader B`
5. Darin einen Unterordner: `Screenshots`

---

## Schritt 6 — TradingView einrichten

### Account
Falls du noch keinen TradingView Account hast: **tradingview.com** → "Sign up" (kostenlos)

### Paper Trading aktivieren
1. Einen Chart öffnen (z.B. USTEC suchen)
2. Unten im Browser: "Trading Panel" klicken
3. "Paper Trading" auswählen → "Connect"
4. Startkapital ist automatisch $100,000 (du kannst es in den Einstellungen ändern)

### Execution Marks aktivieren (WICHTIG!)
Damit deine Ein- und Ausstiegspunkte auf dem Chart sichtbar sind:
1. Zahnrad-Symbol oben rechts im Chart
2. Tab "Trading" öffnen
3. Haken bei **"Executions"** setzen
4. OK klicken

### Richtigen Broker verbinden
Je nach Instrument musst du den richtigen Broker im Paper Trading Panel haben:
| Instrument | Broker |
|------------|--------|
| USTEC (US Tech 100) | TradeNation |
| US30 (Dow Jones) | Forex.com |
| GER40 (DAX) | Forex.com |

Im Paper Trading Panel oben: auf den Account-Namen klicken → Broker wechseln falls nötig.

---

## Schritt 7 — Täglich: So exportierst du deine Daten

### Nach dem Trading — diese 4 Dinge tun:

**1. Balance History exportieren**
- TradingView → unten "Paper Trading" Panel öffnen
- Tab "Balance history" klicken
- Oben rechts: Export-Symbol (Pfeil nach unten) klicken
- CSV wird automatisch in Downloads gespeichert

**2. Order History exportieren**
- Tab "Order history" klicken
- Oben rechts: Export-Symbol → "Export all"
- CSV wird automatisch in Downloads gespeichert

**3. Screenshots machen**
- **WICHTIG:** Nicht den Kamera-Button in TradingView benutzen!
- Stattdessen: **Cmd+Shift+4** auf dem Mac
- Einen Bereich um den Chart ziehen
- Screenshot landet automatisch auf dem Desktop
- Screenshots nach `~/Google Drive/Trading_Journal_Trader B/Screenshots/` verschieben

**4. Alles pushen**
```bash
cd ~/Documents/Trading && ./scripts/update.sh "$(date +%Y-%m-%d) trader b session close"
```

---

## Schritt 8 — KI Session starten

Nach dem Trading öffnest du einen neuen Chat mit mir (deiner KI) und lädst hoch:
- Balance History CSV
- Order History CSV
- Optional: Screenshots hier im Chat

Ich analysiere alles, erstelle deinen Report und vergleiche mit Trader A falls er auch gehandelt hat.

**Wichtig beim Öffnen eines neuen Chats:** Sag mir kurz:
> "Ich bin Trader B. Bitte lies zuerst die README unter https://github.com/trader-journal/Trading"

Dann bin ich sofort im Kontext und kann loslegen.

---

## Schritt 9 — Report ansehen

Reports öffnest du immer in **Firefox** (nicht Chrome):
```bash
open -a Firefox ~/Documents/Trading/reports/trader b/YYYY-MM-DD/report_standalone.html
```

Oder einfach die HTML-Datei im Finder doppelklicken — falls sie in Firefox öffnet, perfekt.

---

## Häufige Fragen

**Was ist der Unterschied zwischen Balance History und Order History?**
Balance History zeigt was wirklich passiert ist (Gewinne, Verluste, Kommissionen). Order History zeigt alle Orders inklusive gecancelte — das hilft zu verstehen was du ursprünglich geplant hattest.

**Warum Cmd+Shift+4 statt TradingView Kamera?**
Der TradingView Kamera-Button speichert die Execution Marks (Pfeile für Ein/Ausstieg) nicht. Mit Cmd+Shift+4 fotografierst du was du wirklich siehst — inklusive aller Marks.

**Was wenn ich einen Tag nicht handle?**
Kein Problem — einfach nichts hochladen. Die KI weiß dann dass an diesem Tag nicht gehandelt wurde.

**Kann ich meine eigene Methode entwickeln?**
Ja! Trader As Methode in `method/METHOD.md` ist ein Ausgangspunkt. Du kannst deine eigene entwickeln und wir dokumentieren sie parallel.

---

## Glossar (wichtigste Begriffe)

Lies `method/TERMINOLOGY.md` für alle Begriffe. Die wichtigsten:

- **Aircushion** — stabiler Abstand zwischen Preis und SMA20 im Trend
- **Battle Zone** — Konsolidierungszone bevor ein Breakout
- **SMA Crossing** — SMA20 kreuzt SMA200, starkes Trendsignal
- **Daily Bias** — übergeordnete Richtungserwartung für den Tag
- **Anchor Trade** — der wichtigste Trade des Tages
- **FOMO Top Scale** — zu spät einsteigen und sofort auf Maximum skalieren (Fehler!)

---

## Los geht's!

Sag mir wo du gerade stehst und ich führe dich durch den nächsten Schritt. 🚀
