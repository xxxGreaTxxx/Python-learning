"""
                           Задача 2
Задание
Определите функцию sum_if_less_than_fifty, принимающую два параметра:

Имя     Тип Пример входа
num_one int 20
num_two Int 25

Функция должна возвращать:
- сумму двух чисел, если эта сумма меньше 50;
- None, если сумма двух чисел больше или равна 50.
"""


def sum_if_less_than_fifty(num_one:int, num_two: int) -> int | None:
    summ = num_one + num_two
    if summ < 50:
        return summ
    return None


print(sum_if_less_than_fifty(20, 20))
print(sum_if_less_than_fifty(20, 30))
print(sum_if_less_than_fifty(20, 100))
