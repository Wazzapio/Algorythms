"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
"""

#  ОС Windows 10, 64-разрядная.
# Python 3.9.5

"""
Урок 2. Задание 2.
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

import sys

even_num = []
not_even_num = []
even_num_sum = 0
not_even_num_sum = 0
user_num = input('Введите число: ')

for el in user_num:
    if int(el) % 2 == 0:
        even_num.append(el)
        even_num_sum += 1
    else:
        not_even_num.append(el)
        not_even_num_sum += 1

print(f'Введено число: {user_num}. \nЧетные цифры в кол-ве: {even_num_sum} шт. {even_num}'
      f'\nНечетные цифры в кол-ве: {not_even_num_sum} шт. {not_even_num}')

size_usr = 24
link_usr = sys.getrefcount(user_num)
size_even_num_sum = 24
link_even_num_sum = sys.getrefcount(even_num_sum)
size_not_even_num_sum = 24
link_not_even_num_sum = sys.getrefcount(not_even_num_sum)

size_even_num_list = 40 + 8 * len(even_num)
link_even_num_list = sys.getrefcount(even_num)
size_not_even_num_list = 40 + 8 * len(not_even_num)
link_not_even_num_list = sys.getrefcount(not_even_num)

size_even_num_elem = 0
size_not_even_num_elem = 0
for i in even_num:
    size_even_num_elem = size_even_num_elem + 37
for i in not_even_num:
    size_not_even_num_elem = size_not_even_num_elem + 37

link_even_num_elem = 0
link_not_even_num_elem = 0
for i in even_num:
    link_even_num_elem = link_not_even_num_elem + sys.getrefcount(i)
for i in not_even_num:
    link_not_even_num_elem = link_not_even_num_elem + sys.getrefcount(i)

print(f'Размер числа: {size_usr}, ссылки числа: {link_usr}\nРазмер четн 0: {size_even_num_sum}, '
      f'ссылки четн 0: {link_even_num_sum}\nРазмер нечет 0: {size_not_even_num_sum}, '
      f'ссылки нечет 0: {link_not_even_num_sum}\nРазмер спис четн: {size_even_num_list}, '
      f'ссылки спис четн: {link_even_num_list}\nРазмер спис нечет: {size_not_even_num_list}, '
      f'ссылки спис нечет: {link_not_even_num_list}\nРазмер эл-тов спис четн: {size_even_num_elem}, '
      f'ссылки эл-тов чет: {link_even_num_elem}\nРазмер эл-тов спис нечет: {size_not_even_num_elem}, '
      f'ссылки эл-тов нечет: {link_not_even_num_elem}')

size_all = size_usr + link_usr + size_even_num_sum + link_even_num_sum + size_not_even_num_sum + link_not_even_num_sum\
           + size_even_num_list + link_even_num_list + size_not_even_num_list + link_not_even_num_list + \
           size_even_num_elem + link_even_num_elem + size_not_even_num_elem + link_not_even_num_elem

print(f'Выделено памяти под переменные: {size_all}')

"""
Урок №3. Задание №8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

a = 5
b = 4
pos = 0
matrix = []

for i in range(b):
    my_list = []
    for j in range(a):
        if j == a - 1:
            x = sum(my_list)
            my_list.append(x)
        else:
            my_list.append(int(input(f'Введите число {i + 1}-ой(ей) строки: ')))
    matrix.append(my_list)

for k in range(len(matrix)):
    for s in matrix[pos]:
        print('%3d' % s, end='')
    pos += 1
    print()

size_a = 24
link_a = sys.getrefcount(a)
size_b = 24
link_b = sys.getrefcount(b)
size_pos = 24
link_pos = sys.getrefcount(pos)

size_matrix_list = 40 + 8 * len(matrix)
link_matrix_list = sys.getrefcount(matrix)

size_matrix_in_list = 0
link_matrix_in_list = 0
for i in matrix:
    size_matrix_in_list = size_matrix_in_list + (40 + 8 * len(i))
    link_matrix_in_list = link_matrix_in_list + sys.getrefcount(i)
    pos += 1

size_el_in_list = 0
link_el_in_list = 0
for i in matrix:
    for el in i:
        size_el_in_list = size_el_in_list + 24
        link_el_in_list = link_el_in_list + sys.getrefcount(el)

print(f'Размер пер "a": {size_a}, ссылки пер "a": {link_a}\nРазмер пер "b": {size_b}, ссылки пер "b": {link_b}\n'
      f'Размер пер "pos": {size_pos}, ссылки пер "pos": {link_pos}\n'
      f'Размер списка "matrix": {size_matrix_list}, ссылки списка "matrix": {link_matrix_list}\n'
      f'Размер спис. в списке "matrix": {size_matrix_in_list}, ссылки спис. в списке "matrix": {link_matrix_in_list}\n'
      f'Размер эл-тов матрицы: {size_el_in_list}, ссылки эл-тов матрицы: {link_el_in_list}\n')

size_all = size_a + link_a + size_b + link_b + size_pos + link_pos + size_matrix_list + link_matrix_list + \
           size_matrix_in_list + link_matrix_in_list + size_el_in_list + link_el_in_list

print(f'Выделено памяти под переменные: {size_all}')

''' 
Обе задачи имеют право быть наиболее эффетивной в использовании памяти, это зависит от объема введенных данных
пользователем в первой задаче. Во второй задаче уже есть четкий размер массива, поэтому размер выделенной памяти будет
всегда таким какой он есть. Поэтому, если объем данных в первой задаче меньше, то именно она будет эффективной, если
нет, тогда наоборот.
'''
