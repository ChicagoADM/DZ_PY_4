# Вычислить число c заданной точностью d
import os
clear = lambda: os.system('cls')
clear()
from math import pi

d =  int(input("Введите число для заданной точности числа Пи: "))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
print()
input('Нажмите Enter для выхода ...')