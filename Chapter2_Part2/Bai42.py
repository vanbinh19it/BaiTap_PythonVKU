# Định nghĩa hàm tính giai thừa
def factorial(n):
    if n < 0:
        return "Không có giai thừa cho số âm"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Nhập số từ người dùng
n = int(input("Nhập số cần tính giai thừa: "))

# In kết quả
print(f"Giai thừa của {n} là: {factorial(n)}")