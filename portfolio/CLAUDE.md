# Portfolio — Fernando Gamiochipi Orejel

Flask-based portfolio app that serves a CV and two interactive business demos over a local network.

## Run

```bash
pip install -r requirements.txt
python run.py
```

Scan the QR in the terminal or open the printed URL on any device on the same Wi-Fi network.

## Structure

```
portfolio/
├── app.py              Flask app — routes, QR generation, LAN IP detection
├── run.py              Entry point — pywebview or browser fallback
├── requirements.txt
├── templates/
│   └── landing.html    Landing page with QR + nav cards
└── static/
    ├── cv/
    │   ├── index.html          CV (Fernando Gamiochipi Orejel)
    │   └── IMG_6683_enhanced.png
    └── demos/
        ├── integkox.html       3D Print Automation Platform demo
        └── cafe-aroma.html     WhatsApp CRM demo (React)
```

## Routes

| Path | Description |
|------|-------------|
| `GET /` | Landing page with QR code and nav cards |
| `GET /cv` | CV static HTML |
| `GET /demos/integkox` | Integkox 3D print platform demo |
| `GET /demos/cafe-aroma` | Café Aroma WhatsApp CRM demo |

## Dependencies

- `flask` — web server
- `qrcode[pil]` — QR code generation
- `Pillow` — image support for qrcode
- `pywebview` — optional native desktop window (falls back to browser)

## Notes

- All demo files are standalone HTML — no build step needed.
- The app auto-detects the LAN IP so any device on the same network can access it via QR.
- HTML routes send `Cache-Control: no-cache` headers.
