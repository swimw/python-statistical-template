#  Công Cụ Thống Kê & Đồ Thị Tự Động (Python)

Template này giúp bạn thực hiện thống kê mô tả và vẽ đồ thị tự động chỉ trong 1 giây.

##  Tính năng chính
- **Tự động quét file:** Tự tìm file `.xlsx` hoặc `.csv` trong thư mục `data/`.
- **Thống kê mô tả:** Tính toán Mean, Median, Std, Skewness... và xuất ra file CSV.
- **Trực quan hóa:** Tự động vẽ Histogram và Boxplot cho tất cả các cột dữ liệu số.

##  Hướng dẫn sử dụng

### Bước 1: Chuẩn bị môi trường
Cài đặt các thư viện cần thiết bằng lệnh:
```bash
pip install -r requirements.txt
### Bước 2: Chèn dữ liệu
Tạo thư mục tên là data (nếu chưa có).
Copy file Excel hoặc CSV của bạn vào thư mục data.
### Bước 3: Chạy chương trình
Mở terminal/cmd và gõ:
bash
python main.py
### Kết quả đầu ra
Sau khi chạy, kết quả sẽ nằm trong thư mục output/:
bao_cao_thong_ke.csv: Bảng số liệu chi tiết.
do_thi_tong_hop.png: Ảnh các biểu đồ phân phối.
