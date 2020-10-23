import pandas as pd
import time

from name_cleener import hh_name_cleener
from HH_vac_block_parcer import get_info
from getpage import getpage

domain = 'https://www.hh.ru'


def hh_page_parcer(link):

    # Создаем списки целевых показателей:
    vacancy_list = []
    min_salary = []
    max_salary = []
    url_list = []
    currency_list = []
    source_name_list = []
    employer_list = []

    print(f'Conneting to page {link}')
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

    # Создаем результирующий датафрейм
    df = pd.DataFrame()
    df['vacancy'] = pd.Series(vacancy_list)
    df['min_salary'] = pd.Series(min_salary)
    df['max_salary'] = pd.Series(max_salary)
    df['currency'] = pd.Series(currency_list)
    df['url'] = pd.Series(url_list)
    df['source'] = pd.Series(source_name_list)
    df['employer'] = pd.Series(employer_list)

    # обрабатываем пейджератор
    try:
        next_link = domain + bsObj.find(text='Дальше').parent.parent.parent.parent['href']
    except:
        next_link = None

    time.sleep(1)
    return df, next_link

def hh_parcer(vacancy_name):
    # Запускаем проход по страницам:
    df = pd.DataFrame()
    link_suffix = main_link = '/search/vacancy?text='
    link = domain + link_suffix + hh_name_cleener(vacancy_name)
    res, link = hh_page_parcer(link)
    df = pd.concat([res, df], ignore_index=True)
    while link:
        res, link = sj_page_parcer(link)
        df = pd.concat([res, df], ignore_index=True)
    print(f'{len(df)} vacancies was found')
    return df
