"""
5.
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

num = 32
update = 0
my_dict = {f'№ {num}': (chr(num))}

while num != 127:
    if update < 9:
        num += 1
        my_dict.update({f'№ {num}': (chr(num))})
        update += 1
    else:
        print(my_dict)
        num += 1
        update = 0
        my_dict = {f'№ {num}': (chr(num))}
        
print(my_dict)
