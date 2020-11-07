# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BooksparserItem(scrapy.Item):
    _id = scrapy.Field()
    link = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    reg_price = scrapy.Field()
    promo_price = scrapy.Field()
    rating = scrapy.Field()
