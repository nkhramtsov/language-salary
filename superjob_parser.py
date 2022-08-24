import requests
from environs import Env
from collections import defaultdict
from utils import fetch_vacancies, predict_salary
import urllib3.exceptions

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
env = Env()
env.read_env()

MOSCOW_AREA_SJ_CODE = 4
SJ_CATALOGUE_ID = 48


def predict_rub_salary_sj(vacancy):
    if vacancy['currency'] != 'rub':
        return None
    salary_from, salary_to = vacancy['payment_from'], vacancy['payment_to']
    if salary_from == salary_to == 0:
        return None
    return predict_salary(salary_from, salary_to)


def get_salary_by_lang_sj():
    sj_api_url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': env('SUPERJOB_SECRET_KEY')}
    sj_itter_key = 'objects'
    break_condition_sj = lambda page_json, page: not page_json['more']

    langs = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', '1C', 'Swift']

    salaries = defaultdict(dict)

    for lang in langs:
        params = {'keyword': f'Программист {lang}', 'catalogues': SJ_CATALOGUE_ID, 'town': MOSCOW_AREA_SJ_CODE}

        response = requests.get(sj_api_url, headers=headers, params=params, verify=False)
        response.raise_for_status()

        salaries[lang]['vacancies_found'] = response.json()['total']

        total = 0
        vacancies_processed = 0
        vacancies = fetch_vacancies(sj_api_url, headers, params, sj_itter_key, break_condition_sj)

        for vacancy in vacancies:
            predicted_salary = predict_rub_salary_sj(vacancy)
            if predicted_salary:
                total += predicted_salary
                vacancies_processed += 1

        salaries[lang]['vacancies_processed'] = vacancies_processed
        salaries[lang]['average_salary'] = int(total / vacancies_processed)

    return salaries


if __name__ == '__main__':
    print(get_salary_by_lang_sj())
