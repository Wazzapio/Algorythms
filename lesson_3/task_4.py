"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random

my_list = []
el_count_list = []
answer_list = []
max_count_pos = 2

for el in range(10):
    my_list.append(random.randint(1, 10))

print(f'Список: {my_list}')

for el in my_list:
    el_count = my_list.count(el)
    el_count_list.append(el_count)

for i in range(len(el_count_list)):
    if el_count_list[i] >= max_count_pos:
        max_count_pos = el_count_list[i]
        max_count_num = my_list[i]
        if max_count_num not in answer_list:
            answer_list.append(max_count_num)

print(f'Число(а), которое(ые) встречается чаще всего: {answer_list}')
