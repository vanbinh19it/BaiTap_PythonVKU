# Định nghĩa hàm
def square_first_five():
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    print(squares[:5])

# Gọi hàm
square_first_five()