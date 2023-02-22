# Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON.
import pickle
import csv
import os
from sys import platform
from datetime import datetime


def first_init() -> list:
    main_list = [
        # (main_items_group, items_group, item, vendor_code, manufacture, price, quantity)
        ('алфавітні книги', '', 'Книга алфавітна 100х190мм, 80 листів', '210 05', 'ПОЛІГРАФІСТ', '105', '480',),
        ('алфавітні книги', '', 'Книга алфавітна 135х285мм, 176 листів', '213 05', 'ПОЛІГРАФІСТ', '275', '500',),
        ('алфавітні книги', '', 'Книга алфавітна 145х202мм, 112 листів', '211 05', 'ПОЛІГРАФІСТ', '192', '500',),
        ('папір для нотаток', 'папір для нотаток білий', 'Блок білого паперу для нотаток 152х102мм, 170 аркушів',
         'BE.7159', 'BUROMAX', '34.60', '10000',),
        ('папір для нотаток', 'папір для нотаток білий', 'Блок білого паперу для нотаток 90х90х30мм не склеєний',
         'BM.2209', 'BUROMAX', '45.90', '11000',),
        ('папір для нотаток', 'папір для нотаток білий', 'Блок білого паперу для нотаток Elit White 90х90х40мм '
                                                           'не склеєний', '8006АХ', 'AXENT', '76.89', '25000',),
        ('папір для нотаток', 'папір для нотаток білий', 'Блок білого паперу для нотаток Elit White 90х90х70мм '
                                                           'не склеєний', '8008АХ', 'AXENT', '126.72', '15000',),
        ('папір для нотаток', 'стікери', 'Блок паперу для нотаток 38*51мм 4х50ар. НЕОН', '7578001PL', 'DONAU', '87.28',
         '100',),
        ('папір для нотаток', 'стікери', 'Блок паперу для нотаток 50*50мм 250ар.', '7575001PL', 'DONAU', '118.25',
         '11230',),
        ('папір для нотаток', 'стікери', 'Блок паперу для нотаток 38*51мм*3шт по 100ар.', 'BM.2319-99', 'BUROMAX',
         '25.51', '17423',),
        ('папір для нотаток', 'стікери', 'Блок паперу для нотаток 76*76мм НЕОН ГІРЛЯНДА, 100ар.', 'BM.2323-97',
         'BUROMAX', '40.30', '6000',),
        ('папір для нотаток', 'стікери', 'Блок паперу для нотаток 76*76мм 400ар.', '7574001PL', 'DONAU', '315.28',
         '5000',),
        ('папір для нотаток', 'папір для записів кольоровий', 'Блок кольорового паперу для записів ВЕСЕЛКА 80х80х30мм '
                                                             'склеєний', 'BM.2232', 'BUROMAX', '32.90', '55000',),
        ('папір для нотаток', 'папір для записів кольоровий',
         'Блок кольорового паперу для записів Elit Color 90х90х70мм не склеєний', '8028АХ', 'AXENT', '190.08', '500',),
        ('блокноти й зошити', 'блокноти формат А4', 'Блокнот на пружине сверху METROPOLIS формат А4, 48ар., червоний',
         '144.BM.24445101-05', 'BUROMAX', '47.75', '1000',),
        ('блокноти й зошити', 'блокноти формат А4', 'Блокнот на спирали формат А4, 48ар.', '152.48-194', 'РЕВЕРС',
         '48.54', '2000',),
        ('блокноти й зошити', 'блокноти формат А4', 'Зошит канцелярський формат А4, 96ар.', 'BM.2428', 'BUROMAX',
         '102.15', '9000',),
        ('блокноти й зошити', 'блокноти формат А5', 'Блокнот SIGHT формат А5, 80ар.', 'BM.24582105-13', 'BUROMAX',
         '85.19', '10000',),
        ('блокноти й зошити', 'блокноти формат А5', 'Блокнот на пружині збоку SENSE, клетка, формат А5, 80ар, м\'ятний',
         'BM.24572101-38', 'BUROMAX ', '99.58', '1200',),
        ('блокноти й зошити', 'блокноти формат А5', 'Блокнот на пружині зверху METROPOLIS формат А5, 48ар., салатовий',
         'BM.24545101-15', 'BUROMAX', '27.48', '5500',),
        ('блокноти й зошити', 'блокноти формат А5', 'Блокнот на спірали формат А5, 48ар.', '48-168', 'РЕВЕРС', '28.44',
         '60',),
        ('блокноти й зошити', 'блокноти формат А6', 'Блокнот у твердій обкладинці FLORA А6 64 ар. у клітинку білий',
         'BM.24614102-12', 'BUROMAX', '49.07', '4000',),
        ('блокноти й зошити', 'блокноти формат А6', 'Блокнот на спірали формат А6, 48ар.', '48-169', 'РЕВЕРС', '15.66',
         '10000',),
        ('блокноти та зошити', 'блокноти формат А6', 'Блокнот на спирали формат А6, 96ар.', 'BM.2422', 'BUROMAX',
         '48.93',   '9000',),
        ('блокноти та зошити', 'блокноти формат А6', 'Записная книга на пружине формат А6, 192ар., клітинка', '192-199',
         'РЕВЕРС', '59.32', '5000',),
        ('блокноти та зошити', 'блокноти формат А7', 'Блокнот на пружине сверху формат А7, 48ар., бордовий',
          'BM.2490-13', 'BUROMAX', '10.48', '2000',),
        ('блокноти та зошити', 'блокноти формат А7', 'Блокнот на пружине сверху формат А7, 48ар., синий', 'BM.2490-02',
         'BUROMAX', '10.48', '2000',),
        ('блокноти та зошити', 'блокноти формат А7', 'Блокнот на спирали формат А7, 48ар.', '48-152', 'РЕВЕРС', '10.53',
         '100',),
        ('блокноти та зошити', 'блокноти формат А7', 'Записная книга на пружине формат А7, 96ар., клітинка', '	96-213',
         'РЕВЕРС', '17.33', '100',),
        ('блокноти та зошити', 'книги канцелярскі', 'Книга канцелярська А4 192 ар. у клітинку Axent Dubai',
         '8423-23АХ', 'AXENT', '251', '1000',),
        ('блокноти та зошити', 'книги канцелярскі', 'Книга канцелярська А4 144 ар. у клітинку MODEST',
         'BM.24419102-03 ', 'BUROMAX', '175.38', '2000',),
        ('блокноти та зошити', 'книги канцелярскі', 'Книга канцелярска А4 96 ар. СЕЗОНИ', 'BM.2408', 'BUROMAX',
         '121.53', '3000',),
        ('блокноти та зошити', 'книги канцелярскі',
         'Книга канцелярська А4 96 аркушів у клітинку FAVOURITE PASTEL бузкова',
         'BM.2400-426', 'BUROMAX', '161.85', '3000',),
        ('конверти', 'стандартні конверти', 'Конверт DL(Е65) скл білий', '2052 ', 'KUVERT', '3.50', '10000',),
        ('конверти', 'стандартні конверти', 'Конверт В4 скл коричневий', '5240 ', 'KUVERT', '10', '10000',),
        ('конверти', 'стандартні конверти', 'Конверт С4 скл білий', '4040 ', 'KUVERT', '8', '10000',),
        ('конверти', 'стандартні конверти', 'Конверт С5 скл білий', '3444', 'KUVERT', '4.50', '10000',),
        ('конверти', 'протиударні конверти', 'Конверт протиударний AIRPOK №11', '9111', 'KUVERT', '3.47', '5000',),
        ('конверти', 'протиударні конверти', 'Конверт протиударний AIRPOK №12', '9116', 'KUVERT', '4.55', '5000',),
        ('конверти', 'протиударні конверти', 'Конверт протиударний AIRPOK №13', '9121', 'KUVERT', '5.55', '5000',),
        ('конверти', 'протиударні конверти', 'Конверт протиударний AIRPOK №14', '9126', 'KUVERT', '7.25', '5000',),
        ('', '', 'Калькулятор 8 розрядів 100*124*33мм', 'BS-208', 'Brilliant ', '220', '500',),
        ('', '', 'Калькулятор 14 розрядів 150*200*25мм', 'SDC-554S', 'Citizen', '540', '500',),
        ('', '', 'Калькулятор 12 розрядів бухгалтерський 203*158*30,5мм', 'O75575', 'Optima ', '465', '500',),
    ]
    return main_list


def get_list_main_groups(main_list, n: int = 0) -> list:
    """
    receive list from [n] elements row of main_list
    :return: list from [n] elements row main_list
    """

    return list(set([x[n] for x in main_list if x[n]]))


def add_new_item_to_main_list(main_list) -> None:
    """
    collect information data from user about new item and add this data to the start of main_list
    :return: None
    """
    i_ = 1
    new_item_main_group = ''
    new_item_subgroup = ''
    main_groups_lst = get_list_main_groups(main_list)
    main_groups_lst.append('товари без групи')
    main_groups_lst_ = sorted(main_groups_lst)
    print()

    while i_ <= len(main_groups_lst_):
        print(f'{i_}. {main_groups_lst_[i_ - 1].capitalize()}')
        i_ += 1
    num_main_group_n = int(input('\nОберіть номер групи нового товару: '))
    if num_main_group_n != main_groups_lst_.index('товари без групи') + 1:
        new_item_main_group = main_groups_lst_[num_main_group_n - 1]
        print(f'\n{new_item_main_group.capitalize()}')
        subgroups_lst_ = list(set([y[1] for y in main_list if y[0] == new_item_main_group]))
        subgroups_lst_.append('без групи')
        print()
        y = 1
        while y <= len(subgroups_lst_):
            if subgroups_lst_[y - 1]:
                print(f'{y}. {subgroups_lst_[y - 1].capitalize()}')
            y += 1
        num_subgroup_n = int(input('\nОберіть номер підгрупи нового товару: '))
        if num_subgroup_n != subgroups_lst_.index('без групи') + 1:
            new_item_subgroup = subgroups_lst_[num_subgroup_n - 1]
    new_item_name = input('\nВведіть назву нового товару: ')
    new_item_vendor_code = input('\nВведіть артикул нового товару: ')
    new_item_manufacture = input('\nВведіть виробника нового товару: ')
    new_item_price = float(input('\nВведіть ціну нового товару: '))
    new_item_quantity = int(input('\nВведіть кількість нового товару: '))
    main_list.insert(0, (new_item_main_group, new_item_subgroup, new_item_name,
                         new_item_vendor_code, new_item_manufacture, new_item_price, new_item_quantity,))


def main():
    num_ex = ''
    file_name = ''
    price_file_name = ''
    items_list = []
    today_str = datetime.now().strftime('%d_%m_%Y')
    # коригуємо ім'я файлу залежно від платформи
    if platform == "linux" or platform == "linux2":
        file_name = r'_files\items.bin'
    elif platform == "darwin":
        file_name = r'_files\items.bin'
    elif platform == "win32":
        file_name = r'_files/items.bin'
    # перевіряємо існування файлу та безпроблемного доступу до нього
    # звідси отримуємо словник
    if os.path.exists(file_name) and os.access(file_name, os.R_OK):
        with open(file_name, 'rb') as f_in:
            items_list = pickle.load(f_in)
    if len(items_list) == 0:
        items_list = first_init()

    while num_ex != '7':
        print('\n', 'Прототип програми "Магазин канцтоварів"'.center(80, '-'), """
              1. Пошук товару                        
              2. Додати запис                        
              3. Надрукувати каталог товарів         
              4. Надрукувати товари відповідної групи
              5. Вивантажити прайс-лист у форматі JSON
              6. Вивантажити прайс-лист у форматі CSV
              7. Вихід""")
        num_ex = input('\nОберіть дію: ')
        match num_ex:
            case '1':
                find_name_item = input('Введіть назву товару: ').strip().lower()
                list_finded_items = []
                for str_item in items_list:
                    item = str_item[2].lower()
                    if item.find(find_name_item) != -1:
                        list_finded_items.append(items_list.index(str_item))
                if len(list_finded_items) > 0:
                    print()
                    for str_index_item in list_finded_items:
                        print('%-50s %s%-10s %s%d' % (items_list[str_index_item][2], 'Ціна: ',
                                                      items_list[str_index_item][5] + ' грн.', 'Залишок: ',
                                                      int(items_list[str_index_item][6])))
                else:
                    print('\n... Зазначений товар не знайдено.')
            case '2':
                add_new_item_to_main_list(items_list)
            case '3':
                main_groups_lst = get_list_main_groups(items_list)
                for group_ in sorted(main_groups_lst):
                    print(f'\n{group_.capitalize()}')
                    subgroups_lst = list(set([y[1] for y in items_list if y[0] == group_]))
                    for subgroup_ in sorted(subgroups_lst):
                        if subgroup_:
                            print(f'  {subgroup_.capitalize()}')
                        for str_item in items_list:
                            if str_item[0] == group_ and str_item[1] == subgroup_:
                                print(f'    {str_item[2].strip()} | {str_item[3].strip()}'
                                      f' | {str_item[4].strip()} | {float(str_item[5]):.2f} грн. | {str_item[6]}')
                # елементи без групи
                for str_item in items_list:
                    if not str_item[0] and not str_item[1]:
                        print(f'{str_item[2].strip()} | {str_item[3].strip()}'
                              f' | {str_item[4].strip()} | {float(str_item[5]):.2f} грн. | {str_item[6]}')
            case '4':
                main_groups_lst = get_list_main_groups(items_list)
                main_groups_lst.append('товари без групи')
                main_groups_lst = sorted(main_groups_lst)
                print()
                i = 1
                while i <= len(main_groups_lst):
                    print(f'{i}. {main_groups_lst[i - 1].capitalize()}')
                    i += 1
                num_main_group = int(input('\nОберіть номер групи товару: '))
                if num_main_group == main_groups_lst.index('товари без групи') + 1:
                    print('\nТовари без групи')
                    for str_item in items_list:
                        if not str_item[0] and not str_item[1]:
                            print(f'{str_item[2].strip()} | {str_item[3].strip()}'
                                  f' | {str_item[4].strip()} | {float(str_item[5]):.2f} грн. | {str_item[6]}')
                else:
                    group_ = main_groups_lst[num_main_group - 1]
                    print(f'\n{group_.capitalize()}')
                    subgroups_lst = list(set([y[1] for y in items_list if y[0] == group_]))
                    for subgroup_ in sorted(subgroups_lst):
                        if subgroup_:
                            print(f'  {subgroup_.capitalize()}')
                        for str_item in items_list:
                            if str_item[0] == group_ and str_item[1] == subgroup_:
                                print(f'    {str_item[2].strip()} | {str_item[3].strip()}'
                                      f' | {str_item[4].strip()} | {float(str_item[5]):.2f} грн. | {str_item[6]}')
            case '5':
                if platform == "linux" or platform == "linux2":
                    price_file_name = r'my_files\price_list_'+f'{today_str}'+'.json'
                elif platform == "darwin":
                    price_file_name = r'my_files\price_list_'+f'{today_str}'+'.json'
                elif platform == "win32":
                    price_file_name = r'my_files/price_list_'+f'{today_str}'+'.json'
                if len(items_list) == 0:
                    items_list = first_init()
                with open(price_file_name, 'wb') as f_out:
                    pickle.dump(items_list, f_out)
                if os.path.exists(price_file_name) and os.access(price_file_name, os.R_OK):
                    with open(price_file_name, 'rb') as f_in:
                        print(f_in.read())
                    print(f'Прайс-лист {price_file_name} у форматі JSON успішно вивантажено!')
            case '6':
                if platform == "linux" or platform == "linux2":
                    price_file_name = r'my_files\price_list_' + f'{today_str}' + '.csv'
                elif platform == "darwin":
                    price_file_name = r'my_files\price_list_' + f'{today_str}' + '.csv'
                elif platform == "win32":
                    price_file_name = r'my_files/price_list_' + f'{today_str}' + '.csv'
                if len(items_list) == 0:
                    items_list = first_init()
                with open(price_file_name, 'w') as f_out:
                    csv.writer(f_out).writerows(items_list)
                if os.path.exists(price_file_name) and os.access(price_file_name, os.R_OK):
                    with open(price_file_name, 'r') as f_in:
                        print(f_in.read())
                    print(f'Прайс-лист {price_file_name} у форматі CSV успішно вивантажено!')
            case '7':
                with open(file_name, 'wb') as f_out:
                    pickle.dump(items_list, f_out)
                break
            case _:
                with open(file_name, 'wb') as f_out:
                    pickle.dump(items_list, f_out)
                print('Введено некоректні дані!!!')
                break


if __name__ == '__main__':
    main()
