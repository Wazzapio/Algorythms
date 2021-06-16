"""
9.
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

import random


def sum_num(a):  # Функция вычисления суммы цифр числа.
    su = []
    for i in a:
        answer = int(i) % 10
        su.append(answer)
    return sum(su)


my_list = []  # Список случайных чисел.
sum_list = []  # Список сумм случайных чисел.

for el in range(10):
    my_list.append(random.randint(100, 10000))
for number in my_list:
    sum_list.append(sum_num(str(number)))

print(f'Список чисел : {my_list}')
print(f'Список сумм цифр чисел : {sum_list}')

while len(sum_list) != 1:
    if sum_list[0] > sum_list[1]:
        my_list.pop(1)
        sum_list.pop(1)
    else:
        my_list.pop(0)
        sum_list.pop(0)

print(f'Наибольшее число: {my_list}\nСумма цифр наибольшего числа: {sum_list}')
