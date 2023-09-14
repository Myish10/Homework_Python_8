from pathlib import Path

file_path = Path('Phone_book.txt')


def read_all(book):
    with open(book, 'r', encoding='utf8') as text_file:
        for line in text_file:
            print(line.strip())


def write_contact(book):
    new_str1 = input('Фамилия: ')
    new_str2 = input('Имя: ')
    new_str3 = input('Отчество: ')
    new_str4 = input('Телефон: ')
    new_str = '\n' + new_str1 + ', ' + new_str2 + ', ' + new_str3 + ', ' + new_str4
    with open(book, 'a',encoding='utf8') as text_file:
        text_file.write(new_str)


def find_item(book):
    item = input('Введите искомый элемент: ')
    with open(book, 'r', encoding='utf8') as text_file:
        for line in text_file:
            if item.lower() in line.lower():
                print(line.strip())


def find_item2(book):
    item = input('Введите искомый элемент: ')
    item_type = int(
        input('Введите номер характеристики для поиска (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    if ((item_type < 0) or (item_type > 4)):
        while ((item_type < 0) or (item_type > 4)):
            print('Такой характеристики нет.')
            item_type = int(input('Введите номер характеристики для поиска (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(book, 'r', encoding='utf8') as text_file:
        for line in text_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                print(*line)


def sort_item(book):
    list_1 = []
    item_type = int(input('Введите номер характеристики для сортировки (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    if ((item_type < 0) or (item_type > 4)):
        while ((item_type < 0) or (item_type > 4)):
            print('Такой характеристики нет.')
            item_type = int(
                input('Введите номер характеристики для сортировки (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(book, 'r', encoding='utf8') as text_file:
        for line in text_file:
            line = line.split(', ')
            list_1.append(line)
        list_1.sort(key=lambda person: person[item_type])
    with open(book, 'w', encoding='utf8') as text_file:
        for line in list_1:
            line = ', '.join(line)
            text_file.writelines(line)


def del_person(book):
    item = input('Что удаляем: ')
    item_type = int(
        input('Введите номер характеристики для поиска (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    if ((item_type < 0) or (item_type > 4)):
        while ((item_type < 0) or (item_type > 4)):
            print('Такой характеристики нет.')
            item_type = int(input('Введите номер характеристики для поиска (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(book, 'r', encoding='utf8') as text_file:
        lines = text_file.readlines()
        for line in lines:
            line = line.strip().split(', ')
            if item.lower() == line[item_type].lower():
                n = input(f'Вы действительно хотите удалить {item} ')
                if n.lower() == 'да':
                    with open(book, 'w', encoding='utf8') as text_file:
                        for line in lines:
                            line = line.strip().split(', ')
                            if item.lower() != line[item_type].lower():
                                text_file.write(', '.join(line) + '\n')


def change_person(book):
    item = input('Что будем менять? ')
    item_type = int(input('Введите номер характеристики для поиска (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    if ((item_type < 0) or (item_type > 4)):
        while ((item_type < 0) or (item_type > 4)):
            print('Такой характеристики нет.')
            item_type = int(input('Введите номер характеристики для поиска (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    item_new = input('Введите новое значение: ')
    with open(book, 'r', encoding='utf8') as text_file:
        lines = text_file.readlines()
        for line in lines:
            line = line.strip().split(', ')
            if item.lower() == line[item_type].lower():
                n = input(f'Вы действительно хотите заменить {item} на {item_new}? ')
                if n.lower() == 'да':
                    with open(book, 'w', encoding='utf8') as text_file:
                        for line in lines:
                            line = line.strip().split(', ')
                            if item.lower() == line[item_type].lower():
                                line[item_type] = item_new
                            text_file.write(', '.join(line) + '\n')


# read_all(file_path)
# write_contact(file_path)
# find_item2(file_path)
# sort_item(file_path)
# del_person(file_path)
# read_all(file_path)
change_person(file_path)
