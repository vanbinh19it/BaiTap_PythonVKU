import math

x = float(input("Nhập cạnh tam giác đều: "))
a = b = c = x
A = B = C = math.pi / 3

S7 = 0.5 * a * b * math.sin(C)
print(f"Diện tích từ Bài 7: {S7}")

# Chạy lại Bài 8
p = (x + x + x) / 2
S8 = math.sqrt(p * (p - x) * (p - x) * (p - x))
print(f"Diện tích từ Bài 8: {S8}")

# Đánh giá
print("Kết quả từ Bài 7 và Bài 8 gần giống nhau (sai số do làm tròn số thập phân)")