# Tạo danh sách rỗng
numbers = []

# Đọc số cho đến khi gặp 0
while True:
    num = int(input("Nhập một số (0 để dừng): "))
    if num == 0:
        break
    numbers.append(num)

# Sắp xếp và hiển thị
numbers.sort()
print("Danh sách đã sắp xếp:")
for num in numbers:
    print(num)