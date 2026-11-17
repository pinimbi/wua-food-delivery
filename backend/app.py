"""Small JSON HTTP API for WUA Cafeteria Express (Python standard library only)."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import json
from backend.auth import register_user, login_user
from backend.menu import MENUS, get_menu
from backend.order import Order, get_order, list_orders, update_order_status, serialize_order

ROOT = Path(__file__).resolve().parents[1]
class Handler(BaseHTTPRequestHandler):
    def _send(self, status: int, payload, content_type="application/json"):
        body = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
        self.send_response(status); self.send_header("Content-Type", content_type); self.send_header("Content-Length", str(len(body))); self.send_header("Access-Control-Allow-Origin", "*"); self.end_headers(); self.wfile.write(body)
    def do_OPTIONS(self):
        self.send_response(204); self.send_header("Access-Control-Allow-Origin", "*"); self.send_header("Access-Control-Allow-Headers", "Content-Type"); self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS"); self.end_headers()
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/": return self._send(200, (ROOT / "frontend" / "index.html").read_bytes(), "text/html; charset=utf-8")
        if path == "/app.js": return self._send(200, (ROOT / "frontend" / "app.js").read_bytes(), "text/javascript; charset=utf-8")
        if path == "/api/health": return self._send(200, {"status":"ok","service":"WUA Cafeteria Express"})
        if path == "/api/cafeterias": return self._send(200, list(MENUS.keys()))
        if path == "/api/menu":
            cafe = parse_qs(urlparse(self.path).query).get("cafeteria", ["Main Cafeteria"])[0]
            return self._send(200, {"cafeteria":cafe,"items":get_menu(cafe)})
        if path.startswith("/api/orders/"):
            order = get_order(path.rsplit("/", 1)[-1]); return self._send(200 if order else 404, serialize_order(order) if order else {"error":"Order not found"})
        if path == "/api/orders": return self._send(200, [serialize_order(o) for o in list_orders()])
        return self._send(404, {"error":"Not found"})
    def do_POST(self):
        try:
            data = json.loads(self.rfile.read(int(self.headers.get("Content-Length", "0"))) or b"{}")
            path = urlparse(self.path).path
            if path == "/api/register": return self._send(201, register_user(data.get("name", ""), data.get("email", ""), data.get("student_id", ""), data.get("password", "")))
            if path == "/api/login":
                user = login_user(data.get("email", ""), data.get("password", "")); return self._send(200 if user else 401, user or {"error":"Invalid email or password"})
            if path == "/api/orders":
                order = Order.create(data.get("student_id", ""), data.get("items", [])); return self._send(201, serialize_order(order))
            if path.startswith("/api/orders/") and path.endswith("/status"):
                order = update_order_status(path.split("/")[-2], data.get("status", "")); return self._send(200, serialize_order(order))
            return self._send(404, {"error":"Not found"})
        except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            return self._send(400, {"error":str(exc)})
    def log_message(self, fmt, *args): print("%s - %s" % (self.address_string(), fmt % args))

def main():
    print("WUA Cafeteria Express running at http://127.0.0.1:8000")
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
if __name__ == "__main__": main()
