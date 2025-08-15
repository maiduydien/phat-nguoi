from flask import Blueprint, request, jsonify
from app.services.violation_service import get_violation_data
from app.services.violation_pay_service import tra_cuu_phap_luat_voi_gemini

# Blueprint cho API tra cứu vi phạm
router = Blueprint("router", __name__)

@router.route("/search", methods=["GET"])
def search_violation():
    BienSo = request.args.get("BienSo")
    LoaiPhuongTien = request.args.get("LoaiPhuongTien", default=1, type=int)

    if not BienSo:
        return jsonify({"error": "Biển số xe là bắt buộc"}), 400

    try:
        data = get_violation_data(BienSo, LoaiPhuongTien)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Lỗi tra cứu vi phạm: {str(e)}"}), 500


# Blueprint cho API tra cứu mức phạt bằng Gemini
routerOpenAI = Blueprint("routerOpenAI", __name__)

@routerOpenAI.route("/fine", methods=["GET"])
def get_fine_info():
    vehicle_type = request.args.get("vehicle_type")
    violation_desc = request.args.get("violation_desc")

    if not vehicle_type or not violation_desc:
        return jsonify({"error": "Thiếu tham số"}), 400

    try:
        fine_info = tra_cuu_phap_luat_voi_gemini(vehicle_type, violation_desc)
        return jsonify({"fine_info": fine_info})
    except Exception as e:
        return jsonify({"error": f"Lỗi tra cứu mức phạt: {str(e)}"}), 500
