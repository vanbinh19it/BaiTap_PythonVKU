# Nhập số thập phân từ người dùng
decimal = int(input("Nhập một số thập phân: "))

# Chuyển đổi sang nhị phân
if decimal < 0:
    print("Vui lòng nhập số không âm!")
else:
    binary = ""
    if decimal == 0:
        binary = "0"
    else:
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
    print(f"Số nhị phân tương ứng là: {binary}")