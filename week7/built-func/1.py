from functools import reduce
import time
import math

# 1. Multiply all numbers in a list
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(multiply_list([1, 2, 3, 4, 5])) 

# 2. Count uppercase and lowercase letters in a string
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return {"Uppercase": upper, "Lowercase": lower}

print(count_case("Hello World!")) 

# 3. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam")) 
print(is_palindrome("hello"))

# 4. Invoke square root function after specific milliseconds
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

delayed_sqrt(25100, 2123)  # Example execution

# 5. Check if all elements of a tuple are True
def all_true(t):
    return all(t)

print(all_true((True, True, True)))  # Output: True
print(all_true((True, False, True)))  # Output: False
