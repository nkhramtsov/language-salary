import requests
from itertools import count


def predict_salary(salary_from, salary_to):
    if not salary_from:
        return 0.8 * salary_to
    if not salary_to:
        return 1.2 * salary_from
    return (salary_to + salary_from) / 2


def fetch_vacancies(url, headers, params, itter_key, break_condition):
    for page in count():
        params.update({'page': page})
        page_response = requests.get(url, headers=headers, params=params)
        page_response.raise_for_status()
        page_data = page_response.json()

        yield from page_data[itter_key]

        if break_condition(page_data, page):
            break
