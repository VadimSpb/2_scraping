import re

def vac_name_cleener(vacancy_name):
    vacancy_name = re.sub('\+', "%2B", vacancy_name)
    vacancy_name = re.sub('#', "%23", vacancy_name)
    vacancy_name = re.sub(' +', "+", vacancy_name)
    return vacancy_name
