"""
2.
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

even_num = []
not_even_num = []
even_num_sum = 0
not_even_num_sum = 0
user_num = input('Введите число: ')

for el in user_num:
    if int(el) % 2 == 0:
        even_num.append(el)
        even_num_sum += 1
    else:
        not_even_num.append(el)
        not_even_num_sum += 1

print(f'Введено число: {user_num}. \nЧетные цифры в кол-ве: {even_num_sum} шт. {even_num}'
      f'\nНечетные цифры в кол-ве: {not_even_num_sum} шт. {not_even_num}')
