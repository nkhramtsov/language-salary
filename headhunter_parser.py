import requests
from collections import defaultdict
from utils import fetch_vacancies, predict_salary


def predict_rub_salary_hh(vacancy):
    salary = vacancy['salary']
    if not salary or salary['currency'] != 'RUR':
        return None
    salary_from, salary_to = salary['from'], salary['to']
    return predict_salary(salary_from, salary_to)


def get_salary_by_lang_hh():
    hh_api_url = 'https://api.hh.ru/vacancies'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    hh_itter_key = 'items'
    break_condition_hh = lambda page_data, page: page >= page_data['pages'] or page > 98

    langs = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', '1C', 'Swift']

    salaries = defaultdict(dict)

    for lang in langs:
        params = {'text': f'Программист {lang}', 'area': 1, 'period': 30}

        response = requests.get(hh_api_url, headers=headers, params=params)
        response.raise_for_status()

        if response.json()['found'] > 100:
            salaries[lang]['vacancies_found'] = response.json()['found']

        total = 0
        vacancies_processed = 0
        vacancies = fetch_vacancies(hh_api_url, headers, params, hh_itter_key, break_condition_hh)

        for vacancy in vacancies:
            if predict_rub_salary_hh(vacancy):
                total += predict_rub_salary_hh(vacancy)
                vacancies_processed += 1

        salaries[lang]['vacancies_processed'] = vacancies_processed
        salaries[lang]['average_salary'] = int(total / vacancies_processed)

    return salaries


if __name__ == '__main__':
    print(get_salary_by_lang_hh())
