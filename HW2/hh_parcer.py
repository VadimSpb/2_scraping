import re
import pandas as pd
import requests
import time

from bs4 import BeautifulSoup as bs
from vac_name_cleener import vac_name_cleener
from HH_vac_block_parcer import get_info


def HH_parcer(vacancy_name):
    vacancy_name = vac_name_cleener(vacancy_name)

    vacancy_list = []
    salary_list = []
    min_salary = []
    max_salary = []
    url_list = []
    currency_list = []
    source_name_list = []
    employer_list = []
    pages = 2  # !!!!!!!!!!!!!!!!!!!!!!!!!

    domain = 'hh.ru'
    main_link = 'https://hh.ru/search/vacancy?text='

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/76.0.3809.100 Safari/537.36 OPR/63.0.3368.53'
    }

    for pg_num in range(0, pages):

        # создаем запрос и получаем ответ
        page = str(pg_num);
        html = requests.get(main_link + vacancy_name + '&page=' + page, headers=headers)

        # проверяем доступность страницы
        if html.status_code is not requests.codes.ok:
            print('Страница ' + html.url + ' не доступна')
            break

        # делаем объект bs
        soup = bs(html.text, 'lxml')

        # ищем блок с вакансиями
        vacancy_block = soup.find_all('div', class_='vacancy-serp-item')
###

        for vacancy in vacancy_block:
            vac_name, salary_min, salary_max, currency, link, employer  = get_info(vacancy)
            vacancy_list.append(vac_name)
            min_salary.append(salary_min)
            max_salary.append(salary_max)
            currency_list.append(currency)
            url_list.append(link)
            source_name_list.append(domain)
            employer_list.append(employer)

        time.sleep(1);

# ###
#
#         # создаем список вакансий
#         for salary_block in len , vacancy in enumerate(vacancy_block):
#             vacancy_list.append(vacancy_block[i].getText())
#
#         # создаем список информационных элементов по вакансиям
#         item_info_block = soup.findAll(class_="vacancy-serp-item__row vacancy-serp-item__row_header")
#
#         # создаем список элементов с информациям по зарплатам
#         for i, salary in enumerate(item_info_block):
#             salary_list.append(item_info_block[i].findChildren()[-1].getText())
#             salary_list[i] = re.sub('\xa0', "", salary_list[i])
#
#         # # создаем список нижней границы зарплат
#         # for salary in salary_list:
#         #     if re.findall(sal_min_1, salary):
#         #         min_salary.append(re.findall(sal_min_1, salary))
#         #     elif re.findall(sal_min_2, salary):
#         #         min_salary.append(re.findall(sal_min_2, salary))
#         #     else:
#         #         min_salary.append('')
#         #
#         # # создаем список верхней границы зарплат
#         # for salary in salary_list:
#         #     if re.findall(sal_max_1, salary):
#         #         max_salary.append(re.findall(sal_max_1, salary))
#         #     elif re.findall(sal_min_2, salary):
#         #         max_salary.append(re.findall(sal_max_2, salary))
#         #     else:
#         #         max_salary.append('')
#
#         # создаем список ссылок на вакансию
#         for i, url in enumerate(item_info_block):
#             if item_info_block[i].findChildren()[-3].get('href') is not None:
#                 url_list.append(item_info_block[i].findChildren()[-3].get('href'))
#             else:
#                 url_list.append(item_info_block[i].findChildren()[-3].findChildren()[0].get('href'))
#
#         # создаем список ссылок на источник данных
#         for i, info in enumerate(item_info_block):
#             source_name_list.append('hh.ru')
#
#         # ищем блок с работодателями
#         employer_block = soup.findAll(class_="bloko-link bloko-link_secondary")
#
#         # создаем список работодателей
#         for i, employer in enumerate(employer_block):
#             employer_list.append(employer_block[i].getText())
#         time.sleep(1);

    s_vacancy_list = pd.Series(vacancy_list)
    s_salary_list = pd.Series(salary_list)
    # s_min_salary = pd.Series(min_salary)
    # s_max_salary = pd.Series(max_salary)
    s_url_list = pd.Series(url_list)
    s_source_name_list = pd.Series(source_name_list)
    s_employer_list = pd.Series(employer_list)

    # Создаем результирующий датафрейм
    df = pd.DataFrame()
    df['vacancy'] = s_vacancy_list
    df['salary'] = salary_list
    #df['min_salary'] = s_min_salary
    #df['max_salary'] = s_max_salary
    df['url'] = s_url_list
    df['source'] = s_source_name_list
    df['employer'] = s_employer_list
    # vacancy_name= re.sub('\+', " ", vacancy);
    # vacancy_name= re.sub('%2B', "+", vacancy);
    # vacancy_name= re.sub('%23', "#", vacancy);
    # df.to_csv('hh ' + vacancy_name+ '.csv', index=False, header=True, encoding='utf-8')
    return df
### DELETE IT!!!!
vacancy_name = 'sql'
df = HH_parcer(vacancy_name)

df.to_csv('hh.csv', index=False, header=True, encoding='utf-8')
print()