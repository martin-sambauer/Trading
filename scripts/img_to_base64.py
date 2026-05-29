#!/usr/bin/env python3
"""Komprimiert Screenshots und gibt Base64 zurück für HTML-Einbettung."""
import base64, sys, os

try:
    from PIL import Image
    import io
    img = Image.open(sys.argv[1])
    img = img.convert("RGB")
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 1400
    ratio = width / img.width
    height = int(img.height * ratio)
    img = img.resize((width, height), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=72, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    print(b64)
except ImportError:
    # Fallback: direkt Base64 ohne Komprimierung
    with open(sys.argv[1], "rb") as f:
        print(base64.b64encode(f.read()).decode())
