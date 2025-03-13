meal_cost = float(input("Nhập chi phí bữa ăn: "))
tax = meal_cost * 0.05  # Thuế 5%
tip = meal_cost * 0.18  # Tiền boa 18%
total = meal_cost + tax + tip

print(f"Thuế: {tax:.2f}")
print(f"Tiền boa: {tip:.2f}")
print(f"Tổng chi phí: {total:.2f}")