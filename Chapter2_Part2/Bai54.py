# Định nghĩa hàm định dạng
def format_list(words):
    if not words:
        return ""
    elif len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return f"{words[0]} and {words[1]}"
    else:
        return ", ".join(words[:-1]) + f" and {words[-1]}"

# Chương trình chính
print("Nhập các từ (Enter để dừng):")
word_list = []
while True:
    word = input("Nhập từ: ")
    if word == "":
        break
    word_list.append(word)

result = format_list(word_list)
print("Kết quả:", result)