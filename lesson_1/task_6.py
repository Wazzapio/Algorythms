"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

a = int(input('Введите номер буквы в алфавите: '))

num_a = a + 96
letter = chr(num_a)

print(f'Под номером {a} находится буква: {letter}')
