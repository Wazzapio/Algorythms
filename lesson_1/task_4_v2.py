"""
4. Написать программу, которая генерирует в указанных пользователем границах
случайное целое число,
случайное вещественное число,
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random

a = int(input('Введите нижнюю границу диапазона (целое число): '))
b = int(input('Введите верхнюю границу диапозона (целое число): '))
c = input('Введите символ с которого начинается граница диапазона: ')
d = input('Введите символ на котором заканчивается граница диапазона: ')

ran_int = random.randint(a, b)
ran_float = random.uniform(a, b)
ran_symbol = random.randint(ord(c), ord(d))
ran_symbol = chr(ran_symbol)

print(f'Случайное целое число в диапазоне от {a} до {b} включительно = {ran_int}')
print(f'Случайное вещественное число в диапазоне от {a} до {b} включительно = {ran_float}')
print(f'Случайный символ в диапазоне от {c} до {d} включительно = {ran_symbol}')
