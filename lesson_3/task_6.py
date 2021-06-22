"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random


def sum_el(a, b):  # Функция для вычисления суммы в определенном диапазоне.
    diapason = []
    if a > b:
        quantity_num = a - b - 1
        for i in range(quantity_num):
            diapason.append(my_list[max_num_pos + i + 1])
    elif a < b:
        quantity_num = b - a - 1
        for i in range(quantity_num):
            diapason.append(my_list[min_num_pos + i + 1])
    sum_diapason = sum(diapason)

    return sum_diapason


my_list = []

for el in range(10):
    my_list.append(random.randint(1, 100))

print(f'Список: {my_list}')

max_num = my_list[0]
min_num = my_list[1]

for i in range(len(my_list)):
    if my_list[i] >= max_num:
        max_num = my_list[i]
        max_num_pos = i
    elif my_list[i] <= min_num:
        min_num = my_list[i]
        min_num_pos = i

print(f'Минимальный элемент списка: {min_num}\nМаксимальный элемент списка: {max_num}\n'
      f'Сумма эл-тов между мин. эл-том и макс.: {sum_el(min_num_pos, max_num_pos)}')
