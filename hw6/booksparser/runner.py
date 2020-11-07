from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from hw6.booksparser import settings
from hw6.booksparser.spiders.labirintru import LabirintruSpider
from hw6.booksparser.spiders.book24 import Book24ruSpider

if __name__ == '__main__':
    clawler_setting = Settings()
    clawler_setting.setmodule(settings)

    process = CrawlerProcess(settings=clawler_setting)
    process.crawl(LabirintruSpider)
    process.crawl(Book24ruSpider)

    process.start()

