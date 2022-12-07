# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import os
clear = lambda: os.system('cls')
clear()
lst = list(map(int, input("Введите числа через пробел: ").split()))
print()
print(f"Исходный список: {lst}")
print()
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(f"Список из неповторяющихся элементов: {new_lst}")
print()
input('Нажмите Enter для выхода ...')