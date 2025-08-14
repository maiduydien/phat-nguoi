import requests
from bs4 import BeautifulSoup
def get_violation_data(BienSO: str,LoaiPhuongTien:int = 1):
    url = "https://api.phatnguoi.vn/web/tra-cuu/"+BienSO+"/"+str(LoaiPhuongTien)
    response = requests.get(url)

    # Kiểm tra mã phản hồi
    if response.status_code == 200:
        try:
            return extract_violation_data(response.text) 
        except ValueError:
            return {"Biên kiểm soát":"error","Màu biển":"error","Loại phương tiện":"error","Thời gian vi phạm":"error","Địa điểm vi phạm":"error","Hành vi vi phạm":"error","Trạng thái":"error","Đơn vị phát hiện vi phạm":"error","Nơi giải quyết vụ việc":"error"}
    else:
        return {"Biên kiểm soát":"error","Màu biển":"error","Loại phương tiện":"error","Thời gian vi phạm":"error","Địa điểm vi phạm":"error","Hành vi vi phạm":"error","Trạng thái":"error","Đơn vị phát hiện vi phạm":"error","Nơi giải quyết vụ việc":"error"}
def get_violation_data_item(data:str,item: str,loi:str):
    so_loi=int(loi)
    #print(so_loi)
    start={"Start_Biển_Kiểm_Soát":0,"Start_Màu_Biển":0,"Start_Loại_Phương_Tiện":0,"Start_Thời_Gian_Vi_Phạm":0,"Start_Địa_Điểm_Vi_Phạm":0,"Start_Hành_Vi_Vi_Phạm":0,"Start_Trạng_Thái":0,"Start_Đơn_Vị_Phát_Hiện_Vi_Phạm":0,"Start_Nơi_Giải_Quyết_Vụ_Việc":0}
    temp = {
                "Biển kiểm soát":"" ,
                "Màu biển":"",
                "Loại phương tiện": "",
                "Thời gian vi phạm": " ",
                "Địa điểm vi phạm": "",
                "Hành vi vi phạm": "",
                "Trạng thái": "",
                "Đơn vị phát hiện vi phạm": "",
                "Nơi giải quyết vụ việc": ""
            }
    for k in range(so_loi):
        if item=="Biển kiểm soát":
            pos=data.find("Biển kiểm soát",start["Start_Biển_Kiểm_Soát"])
            start["Start_Biển_Kiểm_Soát"]=pos+len("Biển kiểm soát")
            if pos != -1:
                temp["Biển kiểm soát"]= data[pos+len("Biển kiểm soát")+2:data.find("Màu biển",start["Start_Biển_Kiểm_Soát"])-1].strip()
            else: temp["Biển kiểm soát"]= ""
        if item=="Màu biển":
            pos=data.find("Màu biển",start["Start_Màu_Biển"])
            start["Start_Màu_Biển"]=pos+len("Màu biển")
            if pos != -1:
                temp["Màu biển"]= data[pos+len("Màu biển")+2:data.find("Loại phương tiện",start["Start_Màu_Biển"])-1].strip()
            else: temp["Màu biển"]= ""
          
        if item=="Loại phương tiện":
            pos=data.find("Loại phương tiện",start["Start_Loại_Phương_Tiện"])
            start["Start_Loại_Phương_Tiện"]=pos+len("Loại phương tiện")
            if pos != -1:
                temp["Loại phương tiện"]= data[pos+len("Loại phương tiện")+2:data.find("Thời gian vi phạm",start["Start_Loại_Phương_Tiện"])-1].strip()
            else: temp["Loại phương tiện"]= ""
        if item=="Thời gian vi phạm":
            pos=data.find("Thời gian vi phạm",start["Start_Thời_Gian_Vi_Phạm"])
            start["Start_Thời_Gian_Vi_Phạm"]=pos+len("Thời gian vi phạm")
            if pos != -1:
                temp["Thời gian vi phạm"] =data[pos+len("Thời gian vi phạm")+2:data.find("Địa điểm vi phạm", start["Start_Thời_Gian_Vi_Phạm"])-1].strip()
            else: temp["Thời gian vi phạm"]= ""
        if item=="Địa điểm vi phạm":
            pos=data.find("Địa điểm vi phạm",   start["Start_Địa_Điểm_Vi_Phạm"])
            start["Start_Địa_Điểm_Vi_Phạm"]=pos+len("Địa điểm vi phạm")
            if pos != -1:
                temp["Địa điểm vi phạm"]= data[pos+len("Địa điểm vi phạm")+2:data.find("Hành vi vi phạm", start["Start_Địa_Điểm_Vi_Phạm"])-1].strip()
            else: temp["Địa điểm vi phạm"]= ""
        if item=="Hành vi vi phạm":
            pos=data.find("Hành vi vi phạm", start["Start_Hành_Vi_Vi_Phạm"])
            start["Start_Hành_Vi_Vi_Phạm"]=pos+len("Hành vi vi phạm")
            if pos != -1:
                print(data[pos+len("Hành vi vi phạm")+2:data.find("Trạng thái")-1])
                temp["Hành vi vi phạm"]= data[pos+len("Hành vi vi phạm")+2:data.find("Trạng thái", start["Start_Hành_Vi_Vi_Phạm"])-1].strip()
            else: temp["Hành vi vi phạm"]= ""
        if item=="Trạng thái":  
            pos=data.find("Trạng thái", start["Start_Trạng_Thái"])
            start["Start_Trạng_Thái"]=pos+len("Trạng thái")
            if pos != -1:
                temp["Trạng thái"]= data[pos+len("Trạng thái")+2:data.find("Đơn vị phát hiện vi phạm", start["Start_Trạng_Thái"])-1].strip()
            else: temp["Trạng thái"]= ""
        if item=="Đơn vị phát hiện vi phạm":
            pos=data.find("Đơn vị phát hiện vi phạm", start["Start_Đơn_Vị_Phát_Hiện_Vi_Phạm"])
            start["Start_Đơn_Vị_Phát_Hiện_Vi_Phạm"]=pos+len("Đơn vị phát hiện vi phạm")
            if pos != -1:
                temp["Đơn vị phát hiện vi phạm"]= data[pos+len("Đơn vị phát hiện vi phạm")+2:data.find("Nơi giải quyết vụ việc", start["Start_Đơn_Vị_Phát_Hiện_Vi_Phạm"])-1].strip()
            else: temp["Đơn vị phát hiện vi phạm"]= ""
        if item=="Nơi giải quyết vụ việc":
            pos=data.find("Nơi giải quyết vụ việc", start["Start_Nơi_Giải_Quyết_Vụ_Việc"])
            start["Start_Nơi_Giải_Quyết_Vụ_Việc"]=pos+len("Nơi giải quyết vụ việc")
            if pos != -1:
                if k==TongSoLoi-1:
                    if item.find("Tra cứu nhanh hơn tại ứng dụng") != -1:
                        temp["Nơi giải quyết vụ việc"]= data[pos+len("Nơi giải quyết vụ việc")+2:data.find("Tra cứu nhanh hơn tại ứng dụng", start["Start_Nơi_Giải_Quyết_Vụ_Việc"])-1].strip()
                    else:
                        temp["Nơi giải quyết vụ việc"]= data[pos+len("Nơi giải quyết vụ việc")+2:].strip()    
                else:
                    
                    temp["Nơi giải quyết vụ việc"]= data[pos+len("Nơi giải quyết vụ việc")+2:data.find("Biển kiểm soát", start["Start_Nơi_Giải_Quyết_Vụ_Việc"])-1].strip()
            else: temp["Nơi giải quyết vụ việc"]= ""
    return temp[item]

#Tìm tổng số lỗi
def Tong_So_Loi(response_text):
    so_loi=int(0)
    start = int(0)
    while response_text.find("Biển kiểm soát",start) != -1 :
        so_loi+=1
        pos= response_text.find("Biển kiểm soát",start)
        start = pos +len("Biển kiểm soát")
        print(start)
    return so_loi

def extract_violation_data(response_text):
    ket_qua = {
        "So_Loi": "",
        "Da_Xu_Phat": "",
        "Chua_Xu_Phat": "",
        "DanhSachLoi":[]
    }
    TestText = str('''
        Nội dung thẻ: Biển kiểm soát:
30E-681.93
Màu biển:
Nền màu vàng, chữ và số màu đen
Loại phương tiện:
Ô tô
Thời gian vi phạm:
10:30, 18/02/2025
Địa điểm vi phạm:
Đường Giải Phóng đoạn qua Bệnh Viện Bạch Mai, Phường Đồng Tâm, Quận Hai Bà Trưng, Thành phố Hà Nội
Hành vi vi phạm:
16824.6.2.đ.21.Dừng xe nơi có biển “Cấm dừng xe và đỗ xe”
Trạng thái:
ĐÃ XỬ PHẠT
Đơn vị phát hiện vi phạm:
Đội Chỉ huy giao thông và điều khiển đèn tín hiệu giao thông - Phòng CSGT Hà Nội
Nơi giải quyết vụ việc:
1. Đội Chỉ huy giao thông và điều khiển đèn tín hiệu giao thông - Phòng CSGT Hà Nội
Địa chỉ: 54 Trần Hưng Đạo, P. Hàng Bài, Q. Hoàn Kiếm, Tp. Hà Nội
Số điện thoại liên hệ: 0692196440
2. Đội 2
Địa chỉ: 8A Xuân La - Tây Hồ - Hà Nội
Số điện thoại liên hệ: 02437616913
Biển kiểm soát:
30E-681.93
Màu biển:
Nền màu vàng, chữ và số màu đen
Loại phương tiện:
Ô tô
Thời gian vi phạm:
10:30, 13/02/2025
Địa điểm vi phạm:
Đường Giải Phóng đoạn qua Bệnh Viện Bạch Mai, Phường Đồng Tâm, Quận Hai Bà Trưng, Thành phố Hà Nội
Hành vi vi phạm:
16824.6.2.đ.21.Dừng xe nơi có biển “Cấm dừng xe và đỗ xe”
Trạng thái:
ĐÃ XỬ PHẠT
Đơn vị phát hiện vi phạm:
Đội Chỉ huy giao thông và điều khiển đèn tín hiệu giao thông - Phòng CSGT Hà Nội
Nơi giải quyết vụ việc:
1. Đội Chỉ huy giao thông và điều khiển đèn tín hiệu giao thông - Phòng CSGT Hà Nội
Địa chỉ: 54 Trần Hưng Đạo, P. Hàng Bài, Q. Hoàn Kiếm, Tp. Hà Nội
Số điện thoại liên hệ: 0692196440
2. Đội 2
Địa chỉ: 8A Xuân La - Tây Hồ - Hà Nội
Số điện thoại liên hệ: 02437616913
Biển kiểm soát:
30E-681.93
Màu biển:
Nền màu vàng, chữ và số màu đen
Loại phương tiện:
Ô tô
Thời gian vi phạm:
15:56, 26/09/2024
Địa điểm vi phạm:
Đường Giải Phóng đoạn qua Bệnh Viện Bạch Mai, Phường Đồng Tâm, Quận Hai Bà Trưng, Thành phố Hà Nội
Hành vi vi phạm:
12321.5.2.h.11.Dừng xe nơi có biển "Cấm dừng xe và đỗ xe"
Trạng thái:
ĐÃ XỬ PHẠT
Đơn vị phát hiện vi phạm:
Đội Chỉ huy giao thông và điều khiển đèn tín hiệu giao thông - Phòng CSGT Hà Nội
Nơi giải quyết vụ việc:
1. Đội Chỉ huy giao thông và điều khiển đèn tín hiệu giao thông - Phòng CSGT Hà Nội
Địa chỉ: 54 Trần Hưng Đạo, P. Hàng Bài, Q. Hoàn Kiếm, Tp. Hà Nội
Số điện thoại liên hệ: 0692196440
2. Đội Cảnh sát giao thông, Trật tự - Công an quận Tây Hồ - Thành phố Hà Nội

Biển kiểm soát:
30E-681.93
Màu biển:
Nền màu vàng, chữ và số màu đen
Loại phương tiện:
Ô tô
Thời gian vi phạm:
08:33, 28/09/2024
Địa điểm vi phạm:
Đường Giải Phóng đoạn qua Bệnh Viện Bạch Mai, Phường Đồng Tâm, Quận Hai Bà Trưng, Thành phố Hà Nội
Hành vi vi phạm:
12321.5.2.h.11.Dừng xe nơi có biển "Cấm dừng xe và đỗ xe"
Trạng thái:
ĐÃ XỬ PHẠT
Đơn vị phát hiện vi phạm:
Đội Chỉ huy giao thông và điều khiển đèn tín hiệu giao thông - Phòng CSGT Hà Nội
Nơi giải quyết vụ việc:
1. Đội Chỉ huy giao thông và điều khiển đèn tín hiệu giao thông - Phòng CSGT Hà Nội
Địa chỉ: 54 Trần Hưng Đạo, P. Hàng Bài, Q. Hoàn Kiếm, Tp. Hà Nội
Số điện thoại liên hệ: 0692196440
2. Đội Cảnh sát giao thông, Trật tự - Công an quận Tây Hồ - Thành phố Hà Nội
    ''')
    html = response_text
    #html=TestText
   
    soup = BeautifulSoup(html, "html.parser")
    plain_text = soup.get_text(separator=' ', strip=True)
    global TongSoLoi

    Da_Xu_Phat=int(0)
    Chua_Xu_Phat=int(0)
   
    #newText=plain_text.replace("\n", " ")
    #print( newText)
    #tìm tổng số lỗi
    one_line=" ".join(plain_text.splitlines())
    print(one_line)
    plain_text=one_line
    plain_text = plain_text.replace("Xem mức phạt","")


    if plain_text.find("Địa điểm vi phạm") != -1:
        print("Tổng số lỗi",Tong_So_Loi(plain_text))
        ket_qua["So_Loi"] = Tong_So_Loi(plain_text)
        #ket_qua["So_Loi"] = plain_text[plain_text.find("Vi phạm:") + len("Vi phạm:"):plain_text.find("Vi phạm:") + len("Vi phạm:")+3].strip()
        #ket_qua["Da_Xu_Ly"] = plain_text[plain_text.find("Đã xử lý:") + len("Đã xử lý:"):plain_text.find("Đã xử lý:") + len("Đã xử lý:")+3].strip()
        #ket_qua["Chua_Xu_Ly"] = plain_text[plain_text.find("Chưa xử lý:") + len("Chưa xử lý:"):plain_text.find("Chưa xử lý:") + len("Chưa xử lý:")+3].strip()
        SoLoi=int(ket_qua["So_Loi"])
        TongSoLoi= SoLoi
        for i in range(SoLoi):
            #print(i)
            loi = {
                "Biển kiểm soát": get_violation_data_item(plain_text,"Biển kiểm soát",str(i+1)),
                "Màu biển": get_violation_data_item(plain_text,"Màu biển",str(i+1)),
                "Loại phương tiện": get_violation_data_item(plain_text,"Loại phương tiện",str(i+1)),
                "Thời gian vi phạm": get_violation_data_item(plain_text,"Thời gian vi phạm",str(i+1)),
                "Địa điểm vi phạm": get_violation_data_item(plain_text,"Địa điểm vi phạm",str(i+1)),
                "Hành vi vi phạm": get_violation_data_item(plain_text,"Hành vi vi phạm",str(i+1)),
                "Trạng thái": get_violation_data_item(plain_text,"Trạng thái",str(i+1)),
                "Đơn vị phát hiện vi phạm": get_violation_data_item(plain_text,"Đơn vị phát hiện vi phạm",str(i+1)),
                "Nơi giải quyết vụ việc": get_violation_data_item(plain_text,"Nơi giải quyết vụ việc",str(i+1))
            }
            ket_qua["DanhSachLoi"].append(loi)
        for i in range(SoLoi):  
            if ket_qua["DanhSachLoi"][i]["Trạng thái"]=="ĐÃ XỬ PHẠT":Da_Xu_Phat += 1
            if ket_qua["DanhSachLoi"][i]["Trạng thái"]=="CHƯA XỬ PHẠT":Chua_Xu_Phat += 1
        ket_qua["Chua_Xu_Phat"]=Chua_Xu_Phat
        ket_qua["Da_Xu_Phat"]=Da_Xu_Phat
    else:
        ket_qua["So_Loi"] = "0"
        ket_qua["Chua_Xu_Phat"]="0"
        ket_qua["Da_Xu_Phat"]="0"
        ket_qua["DanhSachLoi"]=[]
  
    return ket_qua


