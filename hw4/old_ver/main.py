from lenta_ru  import lenta_ru
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
list = lenta_ru(news_date=yesterday)
#list = lenta_ru()


print(list)

