# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

N = int(input("Введите длину последовательности: "))
min = int(input("Введите минимальное число последовательности: "))
max = int(input("Введите максимальное число последовательности: "))

list = []
for i in range(N + 1):
    list.append(random.randint(min, max))
print(list)

result = []
for i in list:
    if i not in result:
        result.append(i)
print(result)