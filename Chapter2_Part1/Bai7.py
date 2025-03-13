import math

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
A = float(input("Nhập góc A (radian): "))
B = float(input("Nhập góc B (radian): "))
C = float(input("Nhập góc C (radian): "))

# Diện tích tam giác: S = (1/2)ab*sin(C)
S = 0.5 * a * b * math.sin(C)
print(f"Diện tích tam giác là: {S}")