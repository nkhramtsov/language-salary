from terminaltables import AsciiTable
from headhunter_parser import get_salary_by_lang_hh
from superjob_parser import get_salary_by_lang_sj


def modify_data_for_table(data):
    table_data = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]

    for key in data.keys():
        row = list()
        row.append(key)
        for value in data[key].values():
            row.append(value)
        table_data.append(row)

    return table_data


if __name__ == '__main__':
    hh_data = modify_data_for_table(get_salary_by_lang_hh())
    sj_data = modify_data_for_table(get_salary_by_lang_sj())

    hh_table = AsciiTable(hh_data, title='HeadHunter Moscow')
    sj_table = AsciiTable(sj_data, title='SuperJob Moscow')

    print(hh_table.table)
    print(sj_table.table)
