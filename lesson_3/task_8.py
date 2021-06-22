"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
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
