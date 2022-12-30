# Вычислить число c заданной точностью d.

from math import pi

d = float(input("Введите число: "))
count = 0
temp = d
while temp != 1:
    temp *= 10
    count += 1

print(f'При d = {d}, pi = {round(pi, count)}')