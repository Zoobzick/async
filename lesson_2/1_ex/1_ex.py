import os
import re
import csv



def get_data():
    """ Извлечение данных из TXT (запускать скрипт в папке с файлами TXT) """
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    pwd = os.getcwd()

    for el in os.listdir(pwd):
        if el.startswith('info'):
            with open(f'{pwd}/{el}', 'r', encoding='cp1251') as f:
                for raw in f:
                    prod_pattern = re.compile('Изготовитель ОС:\s*(\w*\s*)*')
                    name_pattern = re.compile('Название ОС:.*')
                    code_pattern = re.compile('Код продукта:.*')
                    type_pattern = re.compile('Тип системы:.+')
                    if prod_pattern.match(raw):
                        os_prod_list.append(re.split(r'Изготовитель ОС:\s*', raw.strip('\n'))[1])
                    elif name_pattern.match(raw):
                        os_name_list.append(re.split(r'Название ОС:\s+', raw.strip('\n'))[1])
                    elif code_pattern.match(raw):
                        os_code_list.append(re.split(r'Код продукта:\s+', raw.strip('\n'))[1])
                    elif type_pattern.match(raw):
                        os_type_list.append(re.split(r'Тип системы:\s+', raw.strip('\n'))[1])

    for i in range(len(os_prod_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
    return main_data


def write_to_csv(output_file):
    """ Запись данных в CSV файл """
    data = get_data()
    with open(output_file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            writer.writerow(row)


write_to_csv('output_file.csv')

