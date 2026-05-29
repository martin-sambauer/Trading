<!-- Version: 1.0 | Letzte Änderung: 2026-05-28 -->
# Katya Onboarding — Trading Journal

Hallo Katya! Diese Anleitung erklärt wie du dich in das Trading-Journal-System einbindest das Martin und ich aufgebaut haben. Danach können wir eure Performances direkt vergleichen.

---

## Für deine KI: Lies das zuerst
Du arbeitest mit Katya Sambauer an ihrem Trading-Journal. Das Haupt-System ist in `README.md` dokumentiert. Katyas Daten liegen in `data/traders/katya/`, ihre Reports in `reports/katya/`. Erstelle nach jeder Session einen Report im gleichen Format wie Martins Reports. Falls Martin am gleichen Tag gehandelt hat, erstelle zusätzlich einen Vergleichsreport in `reports/comparison/`.

---

## Schritt 1 — GitHub Zugang (einmalig, 2 Minuten)

Martin gibt dir Zugang zum Repo:
- Du bekommst eine Email-Einladung von GitHub
- Klick auf den Link und akzeptiere die Einladung
- Das war's — du hast Schreibzugriff auf das Repo

---

## Schritt 2 — Technisches Setup (einmalig, 15 Minuten)

### Git installieren
```bash
xcode-select --install
```

### Repo klonen
```bash
cd ~/Documents
git clone https://github.com/martin-sambauer/Trading.git
cd Trading
```

### Python-Abhängigkeiten
```bash
pip3 install --break-system-packages git+https://github.com/rongardF/tvdatafeed.git pandas
```

### imagemagick installieren
```bash
brew install imagemagick
```

### GitHub Token erstellen
1. Geh auf github.com → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. "Generate new token (classic)" → Scope: `repo` → Generate
3. Token kopieren, dann:
```bash
git remote set-url origin https://katya-github-username:DEIN_TOKEN@github.com/martin-sambauer/Trading.git
```

### Google Drive
- Google Drive Desktop App installieren: drive.google.com/drive/download
- Screenshots-Ordner anlegen: `~/Google Drive/Trading_Journal/Screenshots_Katya/`

---

## Schritt 3 — TradingView Setup

### Execution Marks aktivieren
1. Chart öffnen → Zahnrad-Symbol (oben rechts) → Tab "Trading"
2. "Executions" aktivieren → OK
3. Paper Trading Panel öffnen → richtigen Broker verbinden

### Broker für Execution Marks
| Instrument | Broker im Panel |
|------------|----------------|
| USTEC | TradeNation |
| US30, GER40 | Forex.com |

---

## Schritt 4 — Täglicher Workflow

### Nach dem Trading
1. **Balance History exportieren:**
   TradingView → Paper Trading Panel → "Balance History" Tab → Export CSV

2. **Order History exportieren:**
   TradingView → Paper Trading Panel → "Order History" Tab → Export (All) CSV

3. **Screenshots machen:**
   - `Cmd+Shift+4` für jeden gehandelten Markt (zeigt Execution Marks)
   - Screenshots nach `~/Google Drive/Trading_Journal/Screenshots_Katya/` verschieben

4. **Alles hochladen und pushen:**
```bash
cd ~/Documents/Trading && ./scripts/update_katya.sh "$(date +%Y-%m-%d) session close"
```

5. **KI Session starten:**
   - CSV-Dateien hier im Chat hochladen
   - KI erstellt automatisch deinen Report und den Vergleichsreport

---

## Was die KI mit deinen Daten macht

Die KI liest deine Daten und erstellt:
- Einen persönlichen Report (Dashboard, Sessions, Trades, Behaviour, Methode)
- Einen Vergleichsreport mit Martin (gleicher Tag, gleiche Märkte)
- Tracking deiner eigenen Behaviour Patterns über Zeit
- Hypothesen über dein Trading-Verhalten

---

## Wichtige Hinweise

- **Reports öffnen:** immer Firefox verwenden (Chrome hat Einschränkungen)
- **Methode:** Lies `method/METHOD.md` — das ist Martins Methode, du kannst deine eigene entwickeln
- **Terminologie:** Lies `method/TERMINOLOGY.md` — damit wir die gleiche Sprache sprechen
- **Fragen:** Einfach die KI fragen — sie kennt das gesamte System

---

## Deine erste Session

Wenn du bereit bist zu starten:
1. Mach ein paar Paper-Trades in TradingView
2. Exportiere Balance History + Order History
3. Mach Screenshots mit Execution Marks
4. Lade alles hier hoch
5. Die KI erstellt deinen ersten Report

Viel Spaß! 🚀
