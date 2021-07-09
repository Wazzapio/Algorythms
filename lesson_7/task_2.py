"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def mergesort(a):
    if len(a) > 1:
        mid = len(a)//2
        lefthalf = a[:mid]
        righthalf = a[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a[k] = lefthalf[i]
                i = i+1
            else:
                a[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            a[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            a[k] = righthalf[j]
            j = j+1
            k = k+1
    return a


li = []
mergesort(li)

for i in range(10):
    li.append(random.randint(0, 50))

print(f'Исходный массив: {li}')
print(f'Отсортированный массив: {mergesort(li)}')
