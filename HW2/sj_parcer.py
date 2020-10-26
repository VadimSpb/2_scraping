import re
import pandas as pd
import time

from getpage import getpage
from name_cleener import sj_name_cleener

domain = 'https://www.superjob.ru'


def sj_page_parcer(link):
    print(f'Conneting to page {link}')
    bsObj = getpage(link)

    # создаем список элементов с названиями вакансий и  URL
    vacancy_list = []
    url_list = []

    tag = 'div'
    class_attrs = {'class': '_3mfro PlM3e _2JVkc _3LJqf'}
    vacancy_block = bsObj.findAll(tag, class_attrs)

    for vacancy in vacancy_block:
        vacancy_list.append(vacancy.getText())
        url_list.append(domain + vacancy.find('a', href=True)['href'])

    # создаем список работодателей
    employer_list = []
    employer_block = bsObj.findAll(class_='f-test-text-vacancy-item-company-name')

    for i, employer in enumerate(employer_block):
        employer_list.append(employer_block[i].getText())

    # создаем список ссылок на источник данных
    source_name_list = [domain] * 20

    # создаем список элементов с информациям по зарплатам
    salary_list = []
    tag = 'span'
    class_attrs = {'class': '_3mfro _2Wp8I PlM3e _2JVkc _2VHxz'}
    salary_block = bsObj.findAll(tag, class_attrs)

    for i, salary in enumerate(salary_block):
        salary_list.append(salary.getText())
        salary_list[i] = re.sub("\xa0", "", salary_list[i])

    min_salary = []
    max_salary = []
    currency_list = []

    for salary in salary_list:
        if salary == 'По договорённости':
            salary_min = None
            salary_max = None
            currency = None

        else:
            if salary[:2] == 'от':
                salary_min = int(''.join(re.findall(r'[0-9]', salary)))
                salary_max = None
                currency = re.findall('[\D]+$', salary)[-1]

            elif salary[:2] == 'до':
                salary_min = None
                salary_max = int(''.join(re.findall(r'[0-9]', salary)))
                currency = re.findall('[\D]+$', salary)[-1]

            else:
                currency = re.findall('[\D]+$', salary)[-1]
                salary = re.split(r'—', salary)

                if len(salary) == 1:
                    salary_min = int(''.join(re.findall(r'[0-9]', salary[0])))
                    salary_max = int(''.join(re.findall(r'[0-9]', salary[0])))

                else:
                    salary_min = int(''.join(re.findall(r'[0-9]', salary[0])))
                    salary_max = int(''.join(re.findall(r'[0-9]', salary[-1])))

        min_salary.append(salary_min)
        max_salary.append(salary_max)
        currency_list.append(currency)

    # Создаем результирующий датaфрейм
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


def sj_parcer(vacancy_name):
    # Запускаем проход по страницам:
    df = pd.DataFrame()
    link_suffix = '/vacancy/search/?keywords='
    link = domain + link_suffix + sj_name_cleener(vacancy_name)
    res, link = sj_page_parcer(link)
    df = pd.concat([res, df], ignore_index=True)
    while link:
        res, link = sj_page_parcer(link)
        df = pd.concat([res, df], ignore_index=True)
    print(f'{len(df)} vacancies was found')
    return df
