# services/openai_service.py
import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
import time

# --- Load .env ---
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV = PROJECT_ROOT / ".env"
LOCAL_ENV = Path(__file__).resolve().parent / ".env"

if DEFAULT_ENV.exists():
    load_dotenv(dotenv_path=DEFAULT_ENV)
elif LOCAL_ENV.exists():
    load_dotenv(dotenv_path=LOCAL_ENV)
else:
    load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise EnvironmentError("Thiếu GOOGLE_API_KEY trong biến môi trường hoặc file .env")

genai.configure(api_key=GOOGLE_API_KEY)
print("Google Gemini API đã được cấu hình với API key.", GOOGLE_API_KEY)  # In một phần của key để xác nhận
prompt = '''
        Hãy đóng vai là một chuyên gia về pháp luật giao thông đường bộ Việt Nam. 
        Luôn luôn trích dẫn nghiêm ngặt, chính xác điều, Khoản, điểm tại Nghị định 100/2019/NĐ-CP và 168/2024/NĐ-CP. 
        Trả lời câu hỏi: Với phương tiện {vehicle_type}, hành vi vi phạm {violation_desc} sẽ bị phạt như thế nào? 
        Câu trả lời phải bằng tiếng Việt. Ngắn gọn, rõ ràng, không dài dòng, không giói thiệu vai trò.
    '''

   
models = genai.list_models()
for model in models:
    print(model.name)


def tra_cuu_phap_luat_voi_gemini(vehicle_type: str, violation_desc: str) -> str:
    print(vehicle_type, violation_desc)  # Debugging
    prompt_user = prompt.format(vehicle_type=vehicle_type, violation_desc=violation_desc)
    print("Prompt gửi đến Gemini:", prompt_user)  # Debugging

    delay : int = 2  # Thời gian chờ giữa các lần gọi API
    max_retries : int = 3  # Số lần thử lại nếu gặp lỗi tạm thời
    for attempt in range(max_retries):
        try:
            model = genai.GenerativeModel("gemini-2.5-pro")  # Sử dụng model Gemini gemini-2.5-flash-lite
            response = model.generate_content(prompt_user)
            return response.text
        except Exception as e:
            print(f"Lỗi khi gọi API Gemini: {e}")
            time.sleep(delay)  # Chờ trước khi thử lại
    return "Không thể tra cứu thông tin lúc này. Bạn vui lòng thử lại sau."
