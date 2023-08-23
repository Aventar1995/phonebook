import csv


def display_phonebook(page_number, page_size):
    """
Функция отображения записей на экране
    :param page_number:Принимает номер страницы:
    :param page_size:Принимает количество записей на странице:

    """
    with open('phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        total_pages = len(rows) // page_size + 1
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        page_rows = rows[start_index:end_index]
        for row in page_rows:
            print(row)

        print(f'Страница {page_number} из {total_pages}')

        choice = input('Нажмите Enter для следующей страницы или e для выхода: ')

        if choice == 'e' or choice == 'е':
            return False

        return True


def add_contact():
    """
Функция добавления новой записи в справочник. Запрашивает у пользователя данные для нового контакта. Затем добавляет
новый контакт в список.
    """
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    father_name = input('Введите отчество: ')
    organization = input('Введите название организации: ')
    work_phone = input('Введите рабочий телефон: ')
    personal_phone = input('Введите личный телефон: ')

    with open('phonebook.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([last_name, first_name, father_name, organization, work_phone, personal_phone])


def edit_contact():
    """
Функция редактирования записей в справочнике. Запрашивает у пользователя фамиллию для редактирования.
затем запрашивает новые данные для выбранного контакта и сохраняет изменения в списке.
    """
    # Для наглядности поиск совершается по last_name, Вы можете заменить last_name на что угодно
    last_name = input('Введите фамилию для редактирования: ')
    with open('phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for i in range(len(rows)):
            if rows[i][0] == last_name:
                rows[i][0] = input('Введите новую фамилию: ')  # это
                rows[i][1] = input('Введите новое имя: ')
                rows[i][2] = input('Введите новое отчество: ')
                rows[i][3] = input('Введите новое название организации: ')
                rows[i][4] = input('Введите новый рабочий телефон: ')
                rows[i][5] = input('Введите новый личный телефон: ')
                break

    with open('phonebook.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def search_contacts():
    """
Запрашивает у пользователя строку для поиска. Затем выводит на экран все записи в которых эта строка встречается.
    """
    search_query = input('Введите запрос для поиска: ')
    with open('phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            if search_query in row:
                print(row)


def main():
    """
    Основная функция. Она отображает меню и запрашивает у пользователя выбранный
    пункт менюшки и вызывает соответсвующую функцию.
    """
    while True:
        print('Вывод записей из справочника клавиша ①')
        print('Добавление новой записи в справочник клавиша ②')
        print('Редактирование записей в справочнике клавиша ③')
        print('Поиск записей в справочнике клавиша ④')
        print('Выход клавиша ⑤')

        choice = input('Выберите действие: ')

        if choice == '1':
            page_number = 1
            page_size = 10
            while display_phonebook(page_number, page_size):
                page_number += 1
        elif choice == '2':
            add_contact()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            search_contacts()
        elif choice == '5':
            break


if __name__ == '__main__':
    main()
