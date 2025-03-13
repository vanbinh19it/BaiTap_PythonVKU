# Định nghĩa hàm
def average(a, b, c):
    return (a + b + c) / 3

# Chương trình chính
n1 = float(input("Nhập số thứ nhất: "))
n2 = float(input("Nhập số thứ hai: "))
n3 = float(input("Nhập số thứ ba: "))
result = average(n1, n2, n3)
print(f"Giá trị trung bình là: {result}")