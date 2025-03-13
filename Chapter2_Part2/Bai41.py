# Tuple cho trước
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Tạo tuple số chẵn
even_tuple = tuple(x for x in t if x % 2 == 0)

# In kết quả
print(even_tuple)