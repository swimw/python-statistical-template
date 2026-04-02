import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import glob
import os

# 1. Tự tạo thư mục output nếu chưa có
os.makedirs("output", exist_ok=True)

# 2. Tự tìm file đầu tiên trong thư mục data/
files = glob.glob("data/*.xlsx") + glob.glob("data/*.csv")
if not files:
    print("❌ Lỗi: Hãy bỏ file Excel hoặc CSV vào thư mục 'data'!")
    exit()

file_path = files[0]
df = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)
print(f"✅ Đang xử lý: {file_path}")

# 3. Thống kê & Lưu báo cáo
stats = df.describe(include='all').T
stats.to_csv("output/bao_cao_thong_ke.csv")

# 4. Vẽ đồ thị & Lưu ảnh
num_cols = df.select_dtypes(include=['number']).columns
if not num_cols.empty:
    df[num_cols].hist(bins=15, figsize=(15, 10), edgecolor='black')
    plt.tight_layout()
    plt.savefig("output/do_thi_tong_hop.png")
    print("🚀 Đã xuất kết quả vào thư mục 'output'!")
