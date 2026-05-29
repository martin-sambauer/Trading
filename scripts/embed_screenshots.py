#!/usr/bin/env python3
# embed_screenshots.py v1.0
# Bettet Screenshots als Base64 in bestehende HTML-Reports ein.
# Ersetzt NUR Platzhalter-Divs — ueberschreibt NICHT den HTML-Inhalt.

import os, base64, re
from io import BytesIO

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(REPO_DIR, "screenshots")
REPORTS_DIR = os.path.join(REPO_DIR, "reports")

REPORT_FILES = ["master_report.html", "sessions.html", "observations.html"]


def img_b64(path, max_width=1400, quality=72):
    try:
        from PIL import Image
        img = Image.open(path).convert("RGB")
        if img.width > max_width:
            img = img.resize((max_width, int(img.height * max_width / img.width)), Image.LANCZOS)
        buf = BytesIO()
        img.save(buf, "JPEG", quality=quality, optimize=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    except ImportError:
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode()
    except Exception as e:
        print("  Fehler: " + str(e))
        return None


def build_shot_map():
    shots = {}
    if not os.path.exists(SCREENSHOTS_DIR):
        return shots
    for fname in os.listdir(SCREENSHOTS_DIR):
        if fname.lower().endswith((".png", ".jpg", ".jpeg")):
            fpath = os.path.join(SCREENSHOTS_DIR, fname)
            print("  Lade: " + fname)
            uri = img_b64(fpath)
            if uri:
                shots[fname] = uri
    return shots


def embed_in_file(html_path, shots):
    with open(html_path) as f:
        html = f.read()

    original = html
    replaced = 0

    for fname, uri in shots.items():
        # Ersetze: <img src="..." alt="fname"> oder <img src="" mit data-src="fname">
        # Hauptfall: Platzhalter-Divs die den Dateinamen nennen
        if fname in html:
            # Ersetze Platzhalter-Div durch echtes img
            placeholder = (
                r'<div[^>]*>[\s\S]*?' + re.escape(fname) + r'[\s\S]*?</div>'
            )
            replacement = '<img src="' + uri + '" style="width:100%;display:block;border:1px solid var(--border)" alt="' + fname + '">'
            new_html, n = re.subn(placeholder, replacement, html, count=1)
            if n > 0:
                html = new_html
                replaced += 1

    if html != original:
        with open(html_path, "w") as f:
            f.write(html)
        print("  " + os.path.basename(html_path) + ": " + str(replaced) + " Screenshots eingebettet")
    else:
        print("  " + os.path.basename(html_path) + ": keine Aenderungen")


if __name__ == "__main__":
    print("Lade Screenshots...")
    shots = build_shot_map()
    print("  " + str(len(shots)) + " Screenshots geladen")

    for fname in REPORT_FILES:
        fpath = os.path.join(REPORTS_DIR, fname)
        if os.path.exists(fpath):
            embed_in_file(fpath, shots)
        else:
            print("  " + fname + " nicht gefunden, uebersprungen")
