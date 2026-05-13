import threading
import webbrowser
from app import app, get_lan_ip

PORT = 8080
URL = f"http://localhost:{PORT}"


def _run_flask():
    app.run(host="0.0.0.0", port=PORT, use_reloader=False)


def _print_banner(network_url: str):
    border = "─" * 35
    print(f"\n┌{border}┐")
    print(f"│  Portfolio running on:             │")
    print(f"│  Local:   {URL:<24s}│")
    print(f"│  Network: {network_url:<24s}│")
    print(f"│  Scan QR on phone to preview       │")
    print(f"└{border}┘\n")


if __name__ == "__main__":
    ip = get_lan_ip()
    network_url = f"http://{ip}:{PORT}"
    _print_banner(network_url)

    flask_thread = threading.Thread(target=_run_flask, daemon=True)
    flask_thread.start()

    try:
        import webview  # type: ignore
        webview.create_window(
            "Fernando Gamiochipi — Portfolio",
            URL,
            width=1280,
            height=800,
        )
        webview.start()
    except ImportError:
        webbrowser.open(URL)
        flask_thread.join()
