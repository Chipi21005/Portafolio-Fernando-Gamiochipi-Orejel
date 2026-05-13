import io
import base64
import socket

import qrcode
from flask import Flask, render_template, send_from_directory, redirect

app = Flask(__name__)


def get_lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def generate_qr_b64(url: str) -> str:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#2de2a7", back_color="#07100e")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


# ── Landing ────────────────────────────────────────────────────────────────────

@app.route("/")
def landing():
    ip = get_lan_ip()
    network_url = f"http://{ip}:8080"
    qr_b64 = generate_qr_b64(network_url)
    return render_template("landing.html", qr_b64=qr_b64, network_url=network_url)


# ── CV ─────────────────────────────────────────────────────────────────────────

@app.route("/cv")
def cv_redirect():
    return redirect("/cv/")


@app.route("/cv/")
def cv():
    resp = send_from_directory("static/cv", "index.html")
    resp.headers["Cache-Control"] = "no-cache"
    return resp


@app.route("/cv/<path:filename>")
def cv_assets(filename):
    return send_from_directory("static/cv", filename)


# ── Demos ──────────────────────────────────────────────────────────────────────

@app.route("/demos/integkox")
def demo_integkox():
    resp = send_from_directory("static/demos", "integkox.html")
    resp.headers["Cache-Control"] = "no-cache"
    return resp


@app.route("/demos/cafe-aroma")
def demo_cafe_aroma():
    resp = send_from_directory("static/demos", "cafe-aroma.html")
    resp.headers["Cache-Control"] = "no-cache"
    return resp
