import re
test_string = "aabbb_camelCaseExample TestStringToSplit"

# Задача 1: Проверяет, содержит ли строка символ 'a', за которым следует ноль или больше символов 'b'
def match_a_zero_or_more_b(string):
    return bool(re.fullmatch(r"ab*", string))
print(match_a_zero_or_more_b("abbb"))


# Задача 2: Проверяет, содержит ли строка символ 'a', за которым следует от двух до трёх символов 'b'
def match_a_two_to_three_b(string):
    return bool(re.fullmatch(r"ab{2,3}", string))
print(match_a_two_to_three_b("abbb")) 


# Задача 3: Ищет последовательности из строчных букв, соединённых символом подчёркивания
def find_lowercase_with_underscore(string):
    return re.findall(r"[a-z]+_[a-z]+", string)


print(find_lowercase_with_underscore(test_string))


# Задача 4: Ищет последовательности, где одна заглавная буква идёт перед строчными буквами
def find_uppercase_followed_by_lowercase(string):
    return re.findall(r"[A-Z][a-z]+", string)


print(find_uppercase_followed_by_lowercase(test_string))



# Задача 5: Проверяет, содержит ли строка символ 'a', за которым следует что угодно, заканчивающееся на 'b'
def match_a_anything_b(string):
    return bool(re.fullmatch(r"a.*b", string))


print(match_a_anything_b("aAnythingHereb"))  # True



# Задача 6: Заменяет все пробелы, запятые и точки на двоеточие
def replace_with_colon(string):
    return re.sub(r"[ ,.]", ":", string)
print(replace_with_colon("Hello, world. How are you?"))


# Задача 7: Преобразует строку в формате snake_case в формат camelCase
def snake_to_camel(string):
    return ''.join(word.title() if i > 0 else word for i, word in enumerate(string.split('_')))


print(snake_to_camel("snake_case_example"))  



# Задача 8: Разбивает строку на части по заглавным буквам
def split_at_uppercase(string):
    return re.findall(r"[A-Z][^A-Z]*", string)


print(split_at_uppercase("TestStringToSplit"))



# Задача 9: Вставляет пробелы между словами, начинающимися с заглавной буквы
def insert_spaces_capitals(string):
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", string)
print(insert_spaces_capitals("TestStringToSplit"))  




# Задача 10: Преобразует строку из camelCase в snake_case
def camel_to_snake(string):
    return re.sub(r"(?<=[a-z])(?=[A-Z])", "_", string).lower()


print(camel_to_snake("camelCaseExample"))  # camel_case_example
