"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""

import random

m = int(input('Введите натуральное число: '))

li = []
len_li = 2 * m + 1
more_el = int((len_li - 1) / 2)
less_el = int((len_li - 1) / 2)
pos = 0

for i in range(len_li):
    li.append(random.randint(0, 10))

while True:
    more = 0
    less = 0
    equally = 0

    for el in range(len(li)):
        if li[pos] > li[el]:
            more += 1
        elif li[pos] < li[el]:
            less += 1
        elif li[pos] == li[el]:
            equally += 1

    for i in range(equally):
        if equally >= 1 and more < more_el:
            equally -= 1
            more += 1
        if equally >= 1 and less < less_el:
            equally -= 1
            less += 1

    pos += 1

    if more == more_el and less == less_el:
        print(f'Исходный список: {li}')
        print(f'Медиана равна: {li[pos - 1]}')
        break
