# Nhập chữ cái từ người dùng
letter = input("Vui lòng nhập một chữ cái: ").lower()

# Kiểm tra xem input có phải là một chữ cái đơn hay không
if len(letter) != 1 or not letter.isalpha():
    print("Vui lòng chỉ nhập một chữ cái hợp lệ!")
else:
    # Kiểm tra các trường hợp
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print(f"Chữ cái '{letter}' là một nguyên âm.")
    elif letter == 'y':
        print(f"Chữ cái 'y' có thể là nguyên âm hoặc phụ âm tùy vào cách sử dụng.")
    else:
        print(f"Chữ cái '{letter}' là một phụ âm.")