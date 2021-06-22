"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

a = 5
b = 4
pos = 0
matrix = []
min_el = []

for i in range(b):  # Создаем матрицу 5 х 4
    my_list = []
    for j in range(a):
        my_list.append(random.randint(1, 100))
        print('%4d' % my_list[j], end='')
    matrix.append(my_list)
    print('')

for s in range(a):  # Собираем минимальные эл-ты столбцов матрицы
    min_num = matrix[0][pos]
    for k in range(b):
        if matrix[k][s] <= min_num:
            min_num = matrix[k][s]
    min_el.append(min_num)
    pos += 1

max_num = min_el[0]

for i in range(len(min_el)):  # Ищем максимальный эл-т среди минимальных эл-тов столбцов матрицы
    if min_el[i] >= max_num:
        max_num = min_el[i]

print(f'Минимальные эл-ты столбцов матрицы: {min_el}')
print(f'Максимальный эл-т среди минимальных эл-тов столбцов матрицы: {max_num}')
