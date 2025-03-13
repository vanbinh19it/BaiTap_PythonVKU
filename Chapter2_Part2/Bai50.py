import random

# Định nghĩa hàm
def generate_password():
    length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    return password

# Chương trình chính
pwd = generate_password()
print(f"Mật khẩu ngẫu nhiên: {pwd}")