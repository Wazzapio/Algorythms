"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import cProfile


def func(num):
    sum_ = int(sum(range(num + 1)))

    return sum_


def func2(num):
    sum_ = 0
    for i in range(num + 1):
        sum_ = sum_ + i

    return sum_


def func3(num):
    if num > 0:
        sum_ = num + func3(num - 1)

        return sum_

    return num


def main():
    a = 999999
    b = func(a)
    c = func2(a)
    d = func3(a)


cProfile.run('main()')

"""
У функции func() func2() линейная сложность.
У функиции func3() квадратичная сложность.

         999 function calls (8 primitive calls) in 0.064 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.063    0.063 <string>:1(<module>)
        1    0.000    0.000    0.028    0.028 task_1.py:10(func)
        1    0.034    0.034    0.034    0.034 task_1.py:16(func2)
    992/1    0.002    0.000    0.002    0.002 task_1.py:24(func3)
        1    0.000    0.000    0.063    0.063 task_1.py:33(main)
        1    0.000    0.000    0.064    0.064 {built-in method builtins.exec}
        1    0.028    0.028    0.028    0.028 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Правда программа отругалась "RecursionError: maximum recursion depth exceeded in comparison", но алгоритм выполнила.
"""
