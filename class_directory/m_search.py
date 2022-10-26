import csv

def contact_finder(seeker):
    """
    Поиск ученика в основной базе.
    Поиск может осуществляться по нескольким параметрам через пробел.
    :param file_csv: Путь к файлу с основной базой
    :param fieldnames: Список с заголовками
    :param seeker: Параметр для поиска
    """
    fieldnames = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Класс', 'Литера', 'Дата_рождения', 'Номер_телефона', 'Пометка_перевода']
    file_csv = './class_directory/class.csv'
    # logger.info('called method contact_finder: file ' + file_csv)
    seeker = seeker.lower().split()
    with open(file_csv, 'r', encoding='utf8') as file:
        lines = file.readlines()
        count = 0
        s_line = ''
        for line in lines:
            if line.strip() == '':
                continue
            else:
                seeker_line = line.strip()
                seeker_line_for_search = seeker_line.split(',', 1)[1].lstrip()
                seeker_line_for_search = seeker_line_for_search.lower()
                # print (seeker_line_for_search)
                # print(seeker)
                count_2 = 0
                for i in range(0, len(seeker)):
                    # print(len(seeker))
                    if seeker_line_for_search.find(seeker[i]) != -1:
                        # print(seeker_line_for_search)
                        # print(seeker[i])
                        count_2 += 1
                        # print(count_2)
                        if count_2 == len(seeker):
                            seeker_line = line.strip().split(',')
                            s_line = s_line + str(contact_output(seeker_line, fieldnames)) + '\n'
                            count += 1
                            # return ('')
        s_line = s_line + '\n' + 'Найдено совпадений: ' + str(count)
        # print(str(s_line))
        return s_line    

def contact_output(seeker_line, fieldnames):
    """
    Вывод найденных данных на экран построчно.
    :param seeker_line: Строка с найденными данными, переведенная в список.
    :param fieldnames: Список с заголовками
    """
    s_line = ''
    for i in range(len(fieldnames)):
        s_line = s_line + str(f'{fieldnames[i]} : {seeker_line[i]}') + '\n'
    return s_line

contact_finder('сокол иван')