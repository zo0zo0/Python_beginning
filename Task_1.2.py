"""
1ый урок. Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
"""


def amount():
    user_imp = input('Введите 3 любых цифры: ')
    sum = 0
    for el in user_imp:
        sum = sum + int(el)
    return sum


if __name__ == "__main__":
    print(f'Результат:{amount()}')
