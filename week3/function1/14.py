from exe1 import grams_to_ounces
from exe2 import fahrenheit_to_celsius
from exe3 import solve
from exe4 import filter_prime
from exe6 import reverse_words

# Testing imported functions
print("100 grams in ounces:", grams_to_ounces(100))
print("Fahrenheit 100 in Celsius:", fahrenheit_to_celsius(100))
print("Chickens and Rabbits:", solve(35, 94))
print("Prime numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:",
      filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Reversed words:", reverse_words("We are ready"))
