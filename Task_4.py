# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
import os
clear = lambda: os.system('cls')
clear()
from random import Random, randint

degree = int(input("Введите натуральную степень k: "))
polyn = ""
st = degree
f = open('file.txt', 'w')

while st >= 0:
    num = randint(0, 100)
    if st > 1:
        polyn += f'{num}x^{st}'
    elif st == 1:
        polyn += f'{num}x'
    elif st == 0:
        polyn += f'{num} = 0'
    if st > 0:
        polyn += ' + '
    st -= 1
    
f.write(str(polyn))
f.close()
print()
print(f'Многочлен степени k [{polyn}] записан в файл file.txt')
print()
input('Нажмите Enter для выхода ...')