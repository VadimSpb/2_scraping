from bs4 import BeautifulSoup as BS
import re


def get_info(vacancy):
    name = vacancy.find_all('a', href=True)[0].text  # наименование вакансии
    salaryblock = vacancy.find('div', class_="vacancy-serp-item__compensation").text

    if salaryblock[:2] == 'от':
        salary_min = ''.join(re.findall(r'[0-9]', salaryblock))
        salary_max = None

    elif salaryblock[:2] == 'до':
        salary_min = None
        salary_max = ''.join(re.findall(r'[0-9]', salaryblock))

    else:
        salary = salaryblock.split('-')

        if len(salary) == 1:
            salary_min = salary[0]
            salary_max = salary[0]

        else:
            salary_min = ''.join(re.findall(r'[0-9]', salary[0]))
            salary_max = ''.join(re.findall(r'[0-9]', salary[-1]))

    currency = salaryblock[-4:]
    link = vacancy.find_all('a', href=True)[0].get('href')
    employer = vacancy.findAll(class_="bloko-link bloko-link_secondary")
    return name, salary_min, salary_max, currency, link, employer