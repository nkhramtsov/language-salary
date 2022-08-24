from terminaltables import AsciiTable
from headhunter_parser import get_salary_by_lang_hh
from superjob_parser import get_salary_by_lang_sj


def transform_language_dict_to_list(languages_dict):
    table_list = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]

    for language_name, language_dict in languages_dict.items():
        row = list()
        row.append(language_name)
        row.extend(language_dict.values())
        table_list.append(row)

    return table_list


if __name__ == '__main__':
    hh_table_list = transform_language_dict_to_list(get_salary_by_lang_hh())
    sj_table_list = transform_language_dict_to_list(get_salary_by_lang_sj())

    hh_table = AsciiTable(hh_table_list, title='HeadHunter Moscow')
    sj_table = AsciiTable(sj_table_list, title='SuperJob Moscow')

    print(hh_table.table)
    print(sj_table.table)
