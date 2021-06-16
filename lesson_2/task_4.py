"""
4.
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""


def rec(a, b, qu):
    if qu > 1:
        qu -= 1
        return float(a) + float(rec((a / b), b, qu))
    else:
        return float(a)


qu_user = int(input('Введите кол-во элементов: '))
answer = rec(1, -2, qu_user)

print(f'Сумма элементов в кол-ве {qu_user} = {answer}')
