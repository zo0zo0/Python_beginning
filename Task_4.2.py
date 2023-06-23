'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, 
у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
'''

import random


def harvest(bush_qty, bed_dict):
    selection = random.randint(1, bush_qty)
    max_qty = 0
    lst_berries = []
    for _ in range(3):
        if selection - _ == 0:
            lst_berries.append(bed_dict[bush_qty])
        elif selection - _ == -1:
            lst_berries.append(bed_dict[bush_qty - 1])
        elif selection - _ == -2:
            lst_berries.append(bed_dict[bush_qty - 2])
        else:
            lst_berries.append(bed_dict[selection - _])
    return lst_berries


bush_qty = random.randint(3, 10)  # кол-во кустов

bed_dict = dict()
for i in range(bush_qty):
    bed_dict[i + 1] = random.randint(5, 50)

berries_qty = harvest(bush_qty, bed_dict)

# print(berries_qty)
print(f'Максимальное количество ягод у 1го куста среди 3: {max(berries_qty)}')
