from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print(f'Данные добавлены в {var} файл')


def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i
        print(''.join(data_list))

    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(''.join(data))


def delete_data():
    user_variant = int(input(
        "Вы хотите 1 - удалить все данные из файла или 2 - удалить какие-то данные из файла? "))
    if user_variant == 1:
        open('data_first_variant.csv', 'w').close()
        open('data_second_variant.csv', 'w').close()
    else:
        user_sel_file = int(input(
            "Выберите номер файла для удаления данных: 1 или 2: "))
        if user_sel_file == 1:
            print("Первый файл: ")
            with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
                data = file.read()
                print(data)
            user_row = int(input("Введите номер строки для удаления: ")) - 1
            book_line = data.split("\n")
            del_book_lines = book_line[user_row]
            book_line.pop(user_row)
            print(f"Удалена запись: {del_book_lines}\n")
            with open('data_first_variant.csv', "w", encoding='utf-8') as file:
                file.write("\n".join(book_line))
        else:
            print("Второй файл: ")
            with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
                data = file.read()
                print(data)
            user_row = int(input("Введите номер строки для удаления: ")) - 1
            book_line = data.split("\n")
            del_book_lines = book_line[user_row]
            book_line.pop(user_row)
            print(f"Удалена запись: {del_book_lines}\n")
            with open('data_second_variant.csv', "w", encoding='utf-8') as file:
                file.write("\n".join(book_line))
