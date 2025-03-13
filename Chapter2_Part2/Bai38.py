# Tạo danh sách rỗng
numbers = []

# Đọc số cho đến khi gặp dòng trống
while True:
    line = input("Nhập một số (Enter để dừng): ")
    if line == "":
        break
    numbers.append(int(line))

# Tách thành 3 danh sách
negatives = [num for num in numbers if num < 0]
zeros = [num for num in numbers if num == 0]
positives = [num for num in numbers if num > 0]

# Ghép lại và hiển thị
result = negatives + zeros + positives
print("Danh sách đã sắp xếp:")
for num in result:
    print(num)