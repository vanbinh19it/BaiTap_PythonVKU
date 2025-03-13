# Định nghĩa hàm tạo danh sách con
def all_subsets(lst):
    subsets = [[]]  # Bắt đầu với tập rỗng
    for item in lst:
        new_subsets = [subset + [item] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets

# Ví dụ sử dụng
my_list = [1, 2, 3]
result = all_subsets(my_list)
print(result)