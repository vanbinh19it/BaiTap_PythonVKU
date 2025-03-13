# Tạo danh sách rỗng
words = []

# Đọc từ cho đến khi gặp dòng trống
while True:
    word = input("Nhập một từ (Enter để dừng): ")
    if word == "":
        break
    words.append(word)

# Loại bỏ trùng lặp, giữ thứ tự ban đầu
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

# Hiển thị kết quả
print("Danh sách từ không trùng lặp:")
for word in unique_words:
    print(word)