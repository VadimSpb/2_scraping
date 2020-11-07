import scrapy
from scrapy.http import HtmlResponse
from hw6.booksparser.items import BooksparserItem


class LabirintruSpider(scrapy.Spider):
    name = 'labirintru'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/%D1%81%D0%B5%D0%BA%D1%81/']

    def parse(self, response: HtmlResponse):
        main_link = 'https://www.labirint.ru'
        links = response.xpath("//a[@class='product-title-link']/@href").extract()
        next_page = response.xpath("//a[@class='pagination-next__text']/@href").extract_first()
        for link in links:
            yield response.follow(url=main_link + link, callback=self.book_parse)
        if next_page:
            next_page = self.start_urls[0] + next_page
            yield response.follow(url=next_page, callback=self.parse)

    def book_parse(self, response: HtmlResponse):
        link = response.url
        name = response.xpath("//h1/text()").extract_first()
        author = response.xpath("//div[@class='authors']/a[@data-event-label='author']/text()").extract()
        reg_price = response.xpath("//span[contains(@class, 'number')]/text()").extract_first()
        promo_price = response.xpath("//span[@class='buying-pricenew-val-number']/text()").extract_first()
        rating = response.xpath("//div[@id='rate']/text()").extract_first()
        isbn = response.xpath("//div[@class='isbn']/text()").extract_first()
        yield BooksparserItem(_id=isbn,
                              link=link,
                              name=name,
                              author=author,
                              reg_price=reg_price,
                              promo_price=promo_price,
                              rating=rating)
