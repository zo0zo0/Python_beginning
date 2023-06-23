"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

"""

import random

user_input1 = int(input("Введите колв-во чисел: "))
# user_input1 = random.randint(1, 5)
user_input2 = int(input("Введите колв-во чисел: "))
# user_input2 = random.randint(1, 5)

# gen_for_user1 = [random.randint(1, 100) for i in range(user_input1)]
gen_for_user1 = [int(input(
    f'Введите значение для {i + 1} числа, 1го списка: ')) for i in range(user_input1)]
# gen_for_user2 = [random.randint(1, 100) for i in range(user_input2)]
gen_for_user2 = [int(input(
    f'Введите значение для {i + 1} числа, 2го списка: ')) for i in range(user_input2)]

# res_list = gen_for_user1 + gen_for_user2
res_list = list(set([j for a in [gen_for_user1, gen_for_user2] for j in a]))
res_list.sort()

print(res_list)
