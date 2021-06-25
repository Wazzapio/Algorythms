"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
-- Без использования Решета Эратосфена;
-- Использовать алгоритм решето Эратосфена
"""

import cProfile


def erat(n):

    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a

    return b


def func(n):
    n_list = []

    for i in range(n + 1):  # Перебор элементов до числа n
        n_list.append(i)

    n_list.pop(0)  # Удаляем 0 из списка
    n_list.pop(0)  # Удаляем 1 из списка

    for el in n_list:  # Перебор эл-тов в списке
        if el >= 2:  # Если эл-т больше или равен 2
            for j in n_list:  # Тогда выполняем перебор элементов в списке
                if j % el == 0 and j != el:  # Если эл-т J равен 0, а так же не равен эл-ту EL
                    x = n_list.index(j)  # Получаем индекс эл-та J
                    n_list.pop(x)  # Удаляем его из списка

    return n_list


def main():
    a = 10000
    b = erat(a)
    c = func(a)


cProfile.run('main()')

"""
У функиции erat() и func() квадратичная сложность.


         28778 function calls in 0.226 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.226    0.226 <string>:1(<module>)
        1    0.003    0.003    0.003    0.003 task_2.py:10(erat)
        1    0.052    0.052    0.223    0.223 task_2.py:40(func)
        1    0.000    0.000    0.226    0.226 task_2.py:59(main)
        1    0.000    0.000    0.226    0.226 {built-in method builtins.exec}
    11230    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     8770    0.164    0.000    0.164    0.000 {method 'index' of 'list' objects}
     8772    0.006    0.000    0.006    0.000 {method 'pop' of 'list' objects}
     
"""