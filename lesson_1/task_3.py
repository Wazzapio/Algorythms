"""
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида
y = kx + b, проходящей через эти точки.
"""

x_1 = int(input('Введите координату Х первой точки: '))
y_1 = int(input('Введите координату Y первой точки: '))
x_2 = int(input('Введите координату Х второй точки: '))
y_2 = int(input('Введите координату Y второй точки: '))

k = (y_2 - y_1) / (x_2 - x_1)
b = y_1 - k * x_1

print(f'Уравнение прямой: y = {k} * x + {b}')
