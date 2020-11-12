# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def price_correction(value):
    return float(value.replace(' ', ''))


class LeroymerlinItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    characters = scrapy.Field()
    link = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(price_correction),
                         output_processor=TakeFirst())
    _id = scrapy.Field(output_processor=TakeFirst())
