# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import os
clear = lambda: os.system('cls')
clear()
num = int(input("Введите число: "))
i = 2 # первое простое число
lists = []
old = num
while i <= num:
    if num % i == 0:
        lists.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} - {lists}")
print()
input('Нажмите Enter для выхода ...')