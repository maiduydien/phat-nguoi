from fastapi import APIRouter, Query, HTTPException
from app.services.violation_service import get_violation_data
from app.services.violation_pay_service import tra_cuu_phap_luat_voi_gemini
#from .. services.violation_service import get_violation_data

router = APIRouter()

@router.get("/search")
def search_violation(BienSo: str = Query(..., description="Biển số xe"),LoaiPhuongTien: int = Query(1, description="Loại phương tiện (1: Ô tô, 2: Xe máy,3: Xe máy điện)") ):
    return get_violation_data(BienSo, LoaiPhuongTien)

routerOpenAI = APIRouter()
@router.get("/fine")
def get_fine_info(
    vehicle_type: str = Query(..., description="Loại phương tiện: ô tô, xe máy, xe máy điện"),
    violation_desc: str = Query(..., description="Mô tả hành vi vi phạm"),
   
):
    """
    Trả về đúng chuỗi fine_info (plain text).
    """
    
    try:
        #print("tham số truyền vào :",vehicle_type,violation_desc)  # Debugging
        fine_info = tra_cuu_phap_luat_voi_gemini(vehicle_type, violation_desc)
       
        return fine_info
    except Exception as e:
        # Trả lỗi text (cũng là plain text)
        raise HTTPException(status_code=500, detail=f"Lỗi tra cứu mức phạt: {e}")