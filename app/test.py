from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

import os
from selenium import webdriver
from PIL import Image
import pytesseract

from selenium.webdriver.support.ui import Select



'''
# Khởi tạo trình duyệt
service = Service("C:/Users/dienmd/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  # ← sửa đường dẫn nếu cần
options = webdriver.ChromeOptions()
try:
    driver = webdriver.Chrome(service=service, options=options)
except Exception as e:
    print("Lỗi",e)

# Truy cập URL
driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
time.sleep(2)  # Chờ ảnh tải

# Tìm phần tử ảnh
img_element = driver.find_element(By.ID , "imgCaptcha")

# Chụp ảnh phần tử (không gọi lại URL)
img_element.screenshot("captcha_rendered.png")
print("✅ Ảnh đã được lưu từ trình duyệt.")
time.sleep(2000)
driver.quit()
'''




# Cấu hình Tesseract (thay đường dẫn nếu cần)
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# Khởi tạo trình duyệt
service = Service("C:/Users/dienmd/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Mở trang web
driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
time.sleep(2)  # Chờ ảnh tải

# Tìm ảnh CAPTCHA
img_element = driver.find_element(By.ID, "imgCaptcha")  # ← sửa lại nếu cần

# Lưu ảnh CAPTCHA
img_path = "captcha_rendered.png"
img_element.screenshot(img_path)

# Mở ảnh và nhận dạng chữ
image = Image.open(img_path)
text = pytesseract.image_to_string(image)

print("🔍 Văn bản trong ảnh CAPTCHA là:", text.strip())


driver.find_element(By.NAME, "BienKiemSoat").send_keys("30e681931")

# Tìm thẻ select theo name
select_element = driver.find_element(By.NAME, "LoaiXe")
time.sleep(2)  # Chờ ảnh tải
# Khởi tạo đối tượng Select
select = Select(select_element)

# Chọn loại phương tiện theo text hiển thị
select.select_by_visible_text("Ô tô")  # ← hoặc "Xe máy", "Xe đạp điện"
time.sleep(2)  # Chờ ảnh tải

# Nhập mã CAPTCHA
driver.find_element(By.NAME, "txt_captcha").send_keys(text)
time.sleep(2)  # Chờ ảnh tải
# Nhấn nút Tra cứu
driver.find_element(By.CLASS_NAME, "btnTraCuu").click()

time.sleep(5)
# Tìm thẻ theo ID, class, tag, hoặc CSS selector
element = driver.find_element(By.ID, "bodyPrint123")  # ← thay bằng ID thật

# Lấy nội dung dạng text
text = element.text
print("📄 Nội dung thẻ:", text)




time.sleep(2000)  # Chờ ảnh tải

# Đóng trình duyệt
driver.quit()