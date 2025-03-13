# Nhập tin nhắn và số dịch chuyển từ người dùng
message = input("Nhập tin nhắn: ")
shift = int(input("Nhập số vị trí dịch chuyển: "))
mode = input("Bạn muốn mã hóa (e) hay giải mã (d)? ").lower()

# Hàm mã hóa/giải mã một ký tự
def caesar_shift_char(char, shift, encrypt=True):
    if char.isalpha():
        base = 'A' if char.isupper() else 'a'
        pos = ord(char) - ord(base)
        if encrypt:
            new_pos = (pos + shift) % 26
        else:  # Giải mã thì dịch ngược
            new_pos = (pos - shift) % 26
        return chr(ord(base) + new_pos)
    return char

# Xử lý theo chế độ
if mode == 'e':
    result = ''.join(caesar_shift_char(char, shift, True) for char in message)
    print(f"Tin nhắn đã mã hóa: {result}")
elif mode == 'd':
    result = ''.join(caesar_shift_char(char, shift, False) for char in message)
    print(f"Tin nhắn đã giải mã: {result}")
else:
    print("Lỗi: Vui lòng chọn 'e' để mã hóa hoặc 'd' để giải mã!")