# Nhập chuỗi từ người dùng
text = input("Nhập một chuỗi: ").lower()

# Kiểm tra palindrome bằng vòng lặp
is_palindrome = True
for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        is_palindrome = False
        break

# Hiển thị kết quả
if is_palindrome:
    print(f"Chuỗi '{text}' là một palindrome.")
else:
    print(f"Chuỗi '{text}' không phải là một palindrome.")