from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

# import settings # ModuleNotFoundError: No module named '__main__.spiders'; '__main__' is not a package
# from booksparser import settings # No module named 'booksparser'
# from ..booksparser import settings #ValueError: attempted relative import beyond top-level package
# from . import settings # out:  ImportError: cannot import name 'settings' from '__main__' (/Users/vadim/GoogleDrive/Learning/geekbrains/1_parcing/homeworks_2/hw6/booksparser/runner.py)
# from .settings import settings # ModuleNotFoundError: No module named '__main__.settings'; '__main__' is not a package

from .spiders.labirintru import LabirintruSpider

if __name__ == '_main_':
    clawler_setting = Settings()
    clawler_setting.setmodule(settings)

    process = CrawlerProcess(settings=clawler_setting)
    process.crawl(LabirintruSpider)

    process.start()

