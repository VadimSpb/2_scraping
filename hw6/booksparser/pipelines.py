# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
import re
from funcy import flatten


class BooksparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client['books']

    def process_item(self, item, spider):
        collection = self.db[spider.name]

        if spider.name == 'labirintru':
            item['name'] = item['name'].split(':')[-1].lstrip()
            if item['reg_price']:
                item['reg_price'] = float(item['reg_price'])
            if item['promo_price']:
                item['promo_price'] = float(item['promo_price'])
            if item['rating']:
                item['rating'] = float(item['rating'])

        elif spider.name == 'book24ru':
            if not item['reg_price']:
                item['reg_price'] = float(re.sub('[^\d]', '', item['promo_price']))
                item['promo_price'] = None
            else:
                item['reg_price'] = float(re.sub('[^\d]', '', item['reg_price']))
                item['promo_price'] = float(re.sub('[^\d]', '', item['promo_price']))
            if item['rating']:
                item['rating'] = float(item['rating'].replace(',', '.'))

        if item['_id']:
            item['_id'] = str(hash(item['_id']))
        else:
            if item['name'] and item['author']:
                item['_id'] = str(hash(item['name'] + "".join(item['author'])))
            else:
                item['_id'] = str(hash(item['link']))

        collection.insert_one(item)
        return item