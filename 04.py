# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

import random

k = int(input("Введите натуральное число: "))

with open('file.txt', 'w') as result:
    for i in range(k, -1, -1):
        r = random.randint(0, 100)
        if i > 1:
            if r > 1:
                result_1 = f'{r}*x**{i} + '
                result.write(result_1)
            elif r == 1:
                result_2 = f'x**{i} + '
                result.write(result_2)
        elif i == 1:
            if r > 1:
                result_3 = f'{r}*x + '
                result.write(result_3)
            elif r == 1:
                result_4 = f'x + '
                result.write(result_4)
        elif i == 0:
            if r > 0:
                result_5 = f'{r}'
                result.write(result_5)
    result.write(' = 0')            