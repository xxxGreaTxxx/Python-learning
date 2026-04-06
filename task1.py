"""
                       Задача 1
Задание
Определите функцию filter_strings_containing_a, принимающую
один параметр:
Имя        Тип          Пример входа
input_strs список строк ["apple", "banana", "cherry", "date"]

Функция должна возвращать новый список, содержащий только
строки, содержащие букву «a».
"""

def filter_strings_containing_a(input_strs: list[str]) -> list[str]:
    output_strs = []
    for input_str in input_strs:
        if "a" in input_str:
            output_strs.append(input_str)
    return output_strs


print(filter_strings_containing_a(["apple", "banana", "cherry", "date"]))
print(filter_strings_containing_a([]))
print(filter_strings_containing_a(["bbbb", "cccc"]))
