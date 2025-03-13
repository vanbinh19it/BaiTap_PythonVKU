M = float(input("Nhập khối lượng nước (gram): "))
delta_T = float(input("Nhập thay đổi nhiệt độ (độ C): "))

C = 4.186  # Nhiệt dung riêng của nước (J/g°C)
Q = M * C * delta_T  # Năng lượng (Joules)
kWh = Q * 2.777e-7  # Chuyển sang kWh
cost = kWh * 8.9  # Chi phí (cent)

print(f"Năng lượng cần thiết: {Q} Joules")
print(f"Chi phí: {cost:.2f} cent")