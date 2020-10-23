import pandas as pd
from hh_parcer import hh_parcer
from sj_parcer import hh_parcer

if __name__=='__main__':
    vacancy = input("Введите название вакансии:")
    df_hh = hh_parcer(vacancy)
    if len(df_hh) == 0:
        print('На hh.ru не обнаружено вакансий')
    else:
        print(df.to_string())

    df_sj = sj_parcer(vacancy)
    if len(df_sj) == 0:
        print('На superjob.ru не обнаружено вакансий')
    else:
        print(df.to_string())

    df = pd.concat([df_hh, df_sj], ignore_index=True)
    df.to_csv('vacancies.csv', index=False, header=True, encoding='utf-8')
    print("итоговый файл vacancies.csv сохранён в каталоге проекта.")