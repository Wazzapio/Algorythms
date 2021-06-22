"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

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

my_list[max_num_pos], my_list[min_num_pos] = my_list[min_num_pos], my_list[max_num_pos]

print(f'Максимальный элемент списка: {max_num}\nМинимальный элемент списка: {min_num}\nСписок c заменеными элементами: {my_list}')
