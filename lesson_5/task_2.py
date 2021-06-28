"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

# Задачу решил при помощи приведения шестнадцатеричных чисел в десятичные, произвел неободиые операции
# и произвел обратное приведение в шестнадцатиричную систему счисления.

import math


def letter_to_num(list_):  # Функция для перевода букв в цифры
    pos = 0
    for el_1 in list_:
        for el_2 in keys_letters:
            if el_1 == el_2:
                value = letters_num.get(el_2)
                list_[pos] = value
                break
        pos += 1


def convert_to_10(a):  # Функция для перевода числа из 16ой в 10ую систему
    n = len(a) - 1
    conv = 0
    for j in range(len(a)):
        conv = conv + (int(a[j]) * (16 ** int(n)))
        n -= 1
    return conv


def convert_to_16(a):  # Функция для перевода числа из 10ой в 16ую систему
    answer = []
    while a > 1:
        remainder = a % 16
        answer.append(math.trunc(remainder))
        a = a / 16

    answer.reverse()

    return answer


def num_to_letter(list_):  # Функция перевода цифр в буквы
    pos = 0
    for el_1 in list_:
        for el_2 in keys_num:
            if str(el_1) == el_2:
                value = num_letters.get(el_2)
                list_[pos] = value
                break
            else:
                list_[pos] = str(el_1)
        pos += 1

    return list_


letters_num = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
num_letters = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

keys_letters = letters_num.keys()
keys_num = num_letters.keys()

num1_list = []
num2_list = []

num1 = input('Введите первое шестнадцатеричное число: ').upper()
num2 = input('Введите второе шестнадцатеричное число: ').upper()

for i in num1:
    num1_list.append(i)

for i in num2:
    num2_list.append(i)

letter_to_num(num1_list)
letter_to_num(num2_list)

conv_sum_to_10 = convert_to_10(num1_list) + convert_to_10(num2_list)
conv_prod_to_10 = convert_to_10(num1_list) * convert_to_10(num2_list)

conv_sum_to_16 = convert_to_16(conv_sum_to_10)
conv_prod_to_16 = convert_to_16(conv_prod_to_10)


print(f'Сумма чисел: {num_to_letter(conv_sum_to_16)}')
print(f'Произведение чисел: {num_to_letter(conv_prod_to_16)}')
