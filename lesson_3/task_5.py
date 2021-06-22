"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

my_list = []

for el in range(10):
    my_list.append(random.randint(-100, -1))

print(f'Список: {my_list}')

max_num = my_list[0]

for i in range(len(my_list)):
    if my_list[i] >= max_num:
        max_num = my_list[i]
        max_num_pos = i

print(f'Максимальный отрицательный элемент списка: {max_num}\nПозиция в списке: {my_list.index(max_num) + 1}')
