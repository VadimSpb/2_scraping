import re


def get_info(vacancy):

    # наименование вакансии
    name = vacancy.find_all('a', href=True)[0].text

    # зарплата:
    salary_tags = {'class': 'bloko-section-header-3 bloko-section-header-3_lite',
                   'data-qa': 'vacancy-serp__vacancy-compensation'}

    try:
        salaryblock = vacancy.find('span', salary_tags).text


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

        salary_min = int(salary_min)
        salary_max = int(salary_max)
        currency = salaryblock[-4:]

    except:
        salary_min = None
        salary_max = None
        currency = None

    # Ссылка
    link = vacancy.find_all('a', href=True)[0].get('href')

    #  Работодатель
    employer = vacancy.find(class_="bloko-link bloko-link_secondary").text
    print(f'{name, salary_min, salary_max, currency, link, employer} is parced')
    return name, salary_min, salary_max, currency, link, employer
