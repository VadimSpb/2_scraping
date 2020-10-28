"""Parser for lenta.ru"""
import re
from datetime import date

from getpage import get_xpath

def lenta_ru(news_date=date.today()):
    domain = 'https://m.lenta.ru'
    url = domain + news_date.strftime("/%Y/%m/%d")
    dom = get_xpath(url)
    news_dom = dom.xpath("//span[@class='time']/../../..")

    news_list = []
    for item in news_dom:
        news = {}
        title = item.xpath(".//span/text()")[-1]
        title = re.sub('\xa0', ' ', title)

        news['title'] = title
        news['link'] = domain + item.xpath(".//span/../@href")[0]
        news['date'] = news_date.strftime("%d.%m.%Y")
        news['source'] = domain
        news_list.append(news)

    print(f'{len(news_list)} news was parced from {domain}')
    return news_list

