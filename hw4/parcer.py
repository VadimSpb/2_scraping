from getpage import get_xpath
from time import sleep
import re

def parcer():
    main_link = 'https://vesti365.ru'
    suffixes = [
        '/mail-ru-novosti/',
        '/yandex-novosti/',
        '/novosti-lenta-ru/'

    ]
    news_list = []
    for suffix in suffixes:
        dom = get_xpath(main_link + suffix)
        news_dom = dom.xpath("//li[@class='feed-item']")

        for item in news_dom:
            news = {}
            news['title'] = item.xpath("./a/text()")[0].replace('\xa0', ' ')
            news['link'] = item.xpath("./a/@href")[0]
            news['source'] = re.findall(r'^https:\/\/[\.a-z0-9_-]+', news['link'])[0]

            news['date'] = item.xpath(".//span[@class='feed-date']/text()")[0]
            news['date'] = re.search('[\.0-9_-]+', news['date'])[0]

            news['_id'] = str(hash(frozenset(news.items())))

            news_list.append(news)

        print(f"{len(news_list)} news was parced from {news['source']}")
        sleep(1)



    return news_list

from pprint import pprint
news = parcer()
pprint(news[-1])

collection = 'news'
database = 'news'
from MongoDb_session import push_to_MongoDb
push_to_MongoDb(news, collection)






