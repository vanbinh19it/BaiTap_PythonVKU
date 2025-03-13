# Nhập số n từ người dùng
n = int(input("Nhập số n: "))

# Tạo dictionary
squares = {i: i * i for i in range(1, n + 1)}

# In kết quả
print(squares)