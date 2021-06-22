"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

my_list = []
min_el = []
quantity_min_el = 2

for el in range(10):
    my_list.append(random.randint(1, 100))

print(f'Список: {my_list}')

while quantity_min_el != 0:
    min_num = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] <= min_num:
            min_num = my_list[i]
    min_el.append(min_num)
    my_list.remove(min_num)
    quantity_min_el -= 1


print(f'Первый минимальный элемент списка: {min_el[0]}\n'
      f'Второй минимальный элемент списка: {min_el[1]}')

