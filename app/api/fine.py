# api/fine.py
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from app.services.violation_pay_service import tra_cuu_phap_luat_voi_gemini

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
            vehicle_type = (qs.get("vehicle_type") or [None])[0]
            violation_desc = (qs.get("violation_desc") or [None])[0]

            if not vehicle_type or not violation_desc:
                missing = []
                if not vehicle_type: missing.append("vehicle_type")
                if not violation_desc: missing.append("violation_desc")
                raise ValueError(f"Thiếu tham số: {', '.join(missing)}")

            fine_info = tra_cuu_phap_luat_voi_gemini(vehicle_type, violation_desc)

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self._cors()
            self.end_headers()
            # fine_info là chuỗi text — ghi thẳng ra body
            self.wfile.write((fine_info or "").encode("utf-8"))

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self._cors()
            self.end_headers()
            self.wfile.write(f"Lỗi tra cứu mức phạt: {e}".encode("utf-8"))
