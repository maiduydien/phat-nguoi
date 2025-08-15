# api/search.py
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

# Bảo đảm có file app/__init__.py và app/services/__init__.py để import được:
from services.violation_service import get_violation_data

class handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        try:
            qs = parse_qs(urlparse(self.path).query)
            BienSo = (qs.get("BienSo") or [None])[0]
            LoaiPhuongTien_raw = (qs.get("LoaiPhuongTien") or ["1"])[0]

            if not BienSo:
                raise ValueError("Thiếu tham số 'BienSo'")

            try:
                LoaiPhuongTien = int(LoaiPhuongTien_raw)
            except Exception:
                LoaiPhuongTien = 1

            data = get_violation_data(BienSo, LoaiPhuongTien)

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self._cors()
            self.end_headers()
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self._cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}, ensure_ascii=False).encode("utf-8"))
