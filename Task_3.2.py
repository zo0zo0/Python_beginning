"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

import random


def calculation():
    N = int(input("Введите количество элементов в массиве \n"))
    lst = [random.randint(1, 30) for _ in range(N)]
    print(lst)
    x = int(input("Введите искомое число \n"))
    el_index = 0
    min_el = abs(x - lst[0])
    for m in range(1, N):
        elem = abs(x - lst[m])
        if elem < min_el:
            min_el = elem
            el_index = m
    print(
        f"Самый близкий по величине элемент к заданному числу {lst[el_index]}")


if __name__ == "__main__":
    calculation()
