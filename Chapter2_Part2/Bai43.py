# Định nghĩa hàm so sánh chuỗi
def compare_strings(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    else:
        print(str1)
        print(str2)

# Nhập chuỗi và gọi hàm
s1 = input("Nhập chuỗi thứ nhất: ")
s2 = input("Nhập chuỗi thứ hai: ")
compare_strings(s1, s2)