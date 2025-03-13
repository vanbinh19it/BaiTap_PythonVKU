# Nhập dãy số từ người dùng
numbers = input("Nhập dãy số, cách nhau bằng dấu phẩy: ")
number_list = [int(x) for x in numbers.split(",")]

# Lọc số lẻ
odd_numbers = [num for num in number_list if num % 2 != 0]

# Hiển thị kết quả
print("Danh sách số lẻ:", ", ".join(map(str, odd_numbers)))