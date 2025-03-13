# Tệp duy nhất: tu_dien_test.py

def Tao_TD(Max):
    """Tạo từ điển với key từ 1 đến Max và value là bình phương của key"""
    TD = {}
    for i in range(1, Max + 1):
        TD[i] = i ** 2
    return TD

def Print_Item(TD):
    """In các phần tử của từ điển (cả key và value)"""
    print("Các phần tử của từ điển:")
    for key, value in TD.items():
        print(f"Key: {key}, Value: {value}")

def Print_Key(TD):
    """In các key của từ điển"""
    print("Các key của từ điển:")
    for key in TD.keys():
        print(key, end=" ")
    print()  # Xuống dòng sau khi in xong

def Print_Value(TD):
    """In các value của từ điển"""
    print("Các value của từ điển:")
    for value in TD.values():
        print(value, end=" ")
    print()  # Xuống dòng sau khi in xong

# Phần kiểm tra (main)
if __name__ == "__main__":
    # Nhập giá trị Max từ bàn phím
    Max = int(input("Nhập số Max: "))

    # Tạo từ điển
    my_dict = Tao_TD(Max)

    # Sử dụng các hàm để in kết quả
    Print_Item(my_dict)
    Print_Key(my_dict)
    Print_Value(my_dict)