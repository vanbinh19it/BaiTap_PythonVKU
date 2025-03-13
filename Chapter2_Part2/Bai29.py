# Nhập độ dài 3 cạnh từ người dùng
a = float(input("Nhập độ dài cạnh thứ nhất: "))
b = float(input("Nhập độ dài cạnh thứ hai: "))
c = float(input("Nhập độ dài cạnh thứ ba: "))

# Kiểm tra xem có tạo thành tam giác hợp lệ không (tổng 2 cạnh > cạnh còn lại)
if (a + b <= c) or (b + c <= a) or (a + c <= b):
    print("Lỗi: Ba cạnh này không tạo thành một tam giác!")
else:
    # Phân loại tam giác
    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or b == c or a == c:
        print("Đây là tam giác cân.")
    else:
        print("Đây là tam giác thường.")