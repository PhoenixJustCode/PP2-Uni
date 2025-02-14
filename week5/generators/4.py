def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


a, b = 1, 5  

for square in squares(a, b):
    print(square)
