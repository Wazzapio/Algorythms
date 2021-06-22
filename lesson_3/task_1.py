"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

diapason_2_99 = []
diapason_2_9 = []
pos1 = 0
pos2 = 0

for el in range(2, 100):
    diapason_2_99.append(el)
for el in range(2, 10):
    diapason_2_9.append(el)

for el in diapason_2_9:
    point = 0
    for i in diapason_2_99:
        if i % el == 0:
            point += 1
    print(f'Количество чисел кратно {el} : {point}')
