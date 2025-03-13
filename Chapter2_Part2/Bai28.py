# Nhập tên tháng từ người dùng
month = input("Nhập tên tháng: ").lower()

# Dictionary chứa tên tháng và số ngày tương ứng
days_in_month = {
    "tháng 1": 31,
    "tháng 2": "28 hoặc 29",
    "tháng 3": 31,
    "tháng 4": 30,
    "tháng 5": 31,
    "tháng 6": 30,
    "tháng 7": 31,
    "tháng 8": 31,
    "tháng 9": 30,
    "tháng 10": 31,
    "tháng 11": 30,
    "tháng 12": 31
}

# Kiểm tra và hiển thị kết quả
if month in days_in_month:
    print(f"Tháng {month} có {days_in_month[month]} ngày.")
else:
    print("Lỗi: Tên tháng không hợp lệ!")