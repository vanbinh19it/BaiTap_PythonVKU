import math

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

print(f"Tổng: {a + b}")
print(f"Hiệu: {a - b}")
print(f"Tích: {a * b}")
print(f"Thương: {a / b if b != 0 else 'Không chia được cho 0'}")
print(f"Phần dư: {a % b if b != 0 else 'Không chia được cho 0'}")
print(f"log10(a): {math.log10(a) if a > 0 else 'Không xác định'}")
print(f"a^b: {a ** b}")