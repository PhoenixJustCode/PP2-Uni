def countdown(n):
    while n >= 0:
        yield n
        n -= 1


# Input from console
n = int(input("Enter the starting number: "))

# Use the countdown generator
for num in countdown(n):
    print(num)
