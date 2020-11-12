from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from hw7.leroymerlin import settings
from hw7.leroymerlin.spiders.leroymerlinru import LeroymerlinruSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)

    process.crawl(LeroymerlinruSpider,  search='шпаклевки')
    process.start()