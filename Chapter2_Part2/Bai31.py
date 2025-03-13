# Nhập tin nhắn từ người dùng
message = input("Nhập tin nhắn cần mã hóa: ")

# Hàm mã hóa một ký tự
def caesar_encrypt_char(char):
    if char.isalpha():
        # Xác định bảng chữ cái (hoa/thường) và vị trí cơ sở
        base = 'A' if char.isupper() else 'a'
        # Dịch chuyển 3 vị trí, lấy modulo 26 để quay vòng
        new_pos = (ord(char) - ord(base) + 3) % 26
        return chr(ord(base) + new_pos)
    return char  # Giữ nguyên ký tự không phải chữ cái

# Mã hóa toàn bộ tin nhắn
encrypted = ''.join(caesar_encrypt_char(char) for char in message)
print(f"Tin nhắn đã mã hóa: {encrypted}")