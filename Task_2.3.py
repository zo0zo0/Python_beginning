'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

n = int(input('Введи число N: '))
_ = 0
while 2 ** _ <= n:
    print(f' 2 в степени {_} равна {2 ** _}')
    _ += 1
