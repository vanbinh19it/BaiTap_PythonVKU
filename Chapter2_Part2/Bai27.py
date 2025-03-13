# Nhập số cạnh từ người dùng
sides = int(input("Nhập số cạnh của hình (từ 3 đến 10): "))

# Dictionary chứa số cạnh và tên hình tương ứng
shapes = {
    3: "tam giác",
    4: "tứ giác",
    5: "ngũ giác",
    6: "lục giác",
    7: "thất giác",
    8: "bát giác",
    9: "cửu giác",
    10: "thập giác"
}

# Kiểm tra và hiển thị kết quả
if sides in shapes:
    print(f"Hình với {sides} cạnh là hình {shapes[sides]}.")
else:
    print("Lỗi: Chương trình chỉ hỗ trợ hình có số cạnh từ 3 đến 10!")