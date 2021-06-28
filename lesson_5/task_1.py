"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
"""

import collections


def m_v(a):  # Функция для расчета средней прибыли компаний

    sum_ = 0
    pos = 0

    for j in range(a):
        sum_ = sum_ + all_data[pos][1]
        pos += 1

    mean_val = sum_ / a

    return mean_val


all_data = []
high_companies = []
low_companies = []
my_tuple = ['name', 'qu1', 'qu2', 'qu3', 'qu4']
form = collections.namedtuple('Company', my_tuple)

quantity_company = int(input('Введите кол-во компаний: '))

for i in range(quantity_company):
    company = input(f'Введите название {i + 1}-й компании: ')
    qu1 = float(input(f'Введите прибыль за 1-ый квартал: '))
    qu2 = float(input(f'Введите прибыль за 2-ой квартал: '))
    qu3 = float(input(f'Введите прибыль за 3-ий квартал: '))
    qu4 = float(input(f'Введите прибыль за 4-ый квартал: '))

    profit = qu1 + qu2 + qu3 + qu4

    my_tuple_sum = ['name', 'profit']
    form = collections.namedtuple('Company', my_tuple_sum)
    x = form(company, profit)
    all_data.append(x)

mean_value = m_v(quantity_company)

for i in range(quantity_company):
    if all_data[i][1] > mean_value:
        high_companies.append(all_data[i][0])
    elif all_data[i][1] < mean_value:
        low_companies.append(all_data[i][0])

print('Название предприятий и прибыль: ')
for k in range(len(all_data)):
    print(f'{all_data[k][0]} - {all_data[k][1]}')

print(f'Средняя прибыль за год для всех предприятий: {mean_value}')
print(f'Предприятие у которых прибыль выше среднего: {high_companies}')
print(f'Предприятие у которых прибыль ниже среднего: {low_companies}')
