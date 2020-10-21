import pandas as pd
import time

from .vac_name_cleener import vac_name_cleener
from .HH_vac_block_parcer import get_info
from .getpage import getpage


def HH_parcer(vacancy_name):
    # Создаем списки целевых показателей:
    vacancy_list = []
    # salary_list = [] !!!!!!!!DEL
    min_salary = []
    max_salary = []
    url_list = []
    currency_list = []
    source_name_list = []
    employer_list = []
    pages = 1  # !!!!!!!!!!!!!!!!!!!!!!!!!

    domain = 'hh.ru'
    main_link = 'https://hh.ru/search/vacancy?text='
    vacancy_name = vac_name_cleener(vacancy_name)

    for pg_num in range(0, pages):

        # создаем запрос и получаем ответ
        page = str(pg_num)
        link = main_link + vacancy_name + '&page=' + page
        soup = getpage(link)

        # ищем блок с вакансиями
        vacancy_block = soup.find_all('div', class_='vacancy-serp-item')

        for vacancy in vacancy_block:
            vac_name, salary_min, salary_max, currency, link, employer = get_info(vacancy)
            vacancy_list.append(vac_name)
            min_salary.append(salary_min)
            max_salary.append(salary_max)
            currency_list.append(currency)
            url_list.append(link)
            source_name_list.append(domain)
            employer_list.append(employer)

        time.sleep(1);

    s_vacancy_list = pd.Series(vacancy_list)
    # s_salary_list = pd.Series(salary_list) ###DEL
    s_min_salary = pd.Series(min_salary)
    s_max_salary = pd.Series(max_salary)
    s_currency_list = pd.Series(currency_list)
    s_url_list = pd.Series(url_list)
    s_source_name_list = pd.Series(source_name_list)
    s_employer_list = pd.Series(employer_list)

    # Создаем результирующий датафрейм
    df = pd.DataFrame()
    df['vacancy'] = s_vacancy_list
    # df['salary'] = salary_list !!!!!DEL
    df['min_salary'] = s_min_salary
    df['max_salary'] = s_max_salary
    df['currency'] = s_currency_list
    df['url'] = s_url_list
    df['source'] = s_source_name_list
    df['employer'] = s_employer_list

    return df


### DELETE IT!!!!
vacancy_name = 'sql'
df = HH_parcer(vacancy_name)

# df.to_csv('hh.csv', index=False, header=True, encoding='utf-8')
print()