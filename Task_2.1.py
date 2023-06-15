'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''


def coin_switching():
    coin_qty = int(input("Введите количество монет: "))
    coin_reshka = 0
    coin_gerb = 0
    for _ in range(coin_qty):
        user_input = input(
            f'{_ + 1} монетка является Решкой (Р) или Орлом (О)? ')
        if user_input == 'Р':
            coin_reshka += 1
        elif user_input == "О":
            coin_gerb += 1
        else:
            print("Вы ввели некорретктное значение, было присвоено значение Орла")
            coin_gerb += 1
        _ += 1
    if coin_gerb > coin_reshka:
        return f'Количество решек меньше, чем орлов. Нужно перевернуть монеток с решками {coin_reshka} раз. Чтобы были одинаковые стороны'
    elif coin_gerb < coin_reshka:
        return f'Количество орлов меньше, чем решек. Нужно перевернуть монеток с орлами {coin_gerb} раз. Чтобы были одинаковые стороны'
    else:
        return f'Количество одинаковое. Можете перевернуть {coin_gerb} раз, чтобы были одинаковые стороны'


if __name__ == "__main__":
    print(coin_switching())
