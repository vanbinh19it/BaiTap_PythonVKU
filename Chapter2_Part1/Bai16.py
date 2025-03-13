import math

d = float(input("Nhập chiều cao (m): "))
v_i = 0  # Tốc độ ban đầu
a = 9.8  # Gia tốc trọng trường
v_f = math.sqrt(v_i**2 + 2 * a * d)
print(f"Tốc độ khi chạm đất: {v_f} m/s")