'''
1ый урок. Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1    
24 -> 4  16  4
    60 -> 10  40  10
'''


def paper_bird():
    user_input = int(input("Введите количество корабликов:"))
    return f'Всего дети сделали {user_input}, из которых сделал каждый отдельный ребенок: Петя {user_input/6}, Катя {user_input*2/3}, Сережа {user_input/6}'


if __name__ == "__main__":
    print(paper_bird())
