

if __name__=='__main__':
    vacancy = input("Введите название вакансии:")
    df = hh_parcer()
    print(df.to_string())
    print('На superjob.ru не обнаружено интересующих меня вакансий')