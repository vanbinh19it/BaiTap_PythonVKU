import math

a = float(input("Nhập cạnh tam giác đều: "))

# Nửa chu vi
p = (a + a + a) / 2
# Diện tích theo định lý Heron: S = sqrt(p(p-a)(p-b)(p-c))
S = math.sqrt(p * (p - a) * (p - a) * (p - a))
print(f"Diện tích tam giác đều là: {S}")