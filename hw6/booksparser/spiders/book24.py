import scrapy
from scrapy.http import HtmlResponse
from hw6.booksparser.items import BooksparserItem


class Book24ruSpider(scrapy.Spider):
    name = 'book24ru'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/search/?q=%D1%81%D0%B5%D0%BA%D1%81']
    data = []

    def parse(self, response: HtmlResponse):
        main_link = 'https://book24.ru'
        links = response.xpath("//a[contains(@class, 'book__title-link')]/@href").extract()
        next_page = response.xpath("//a[contains(text(), 'Далее')]/@href").extract_first()
        for link in links:
            yield response.follow(url=main_link+link, callback=self.book_parse)
        if next_page:
            yield response.follow(url=main_link+next_page, callback=self.parse)

    def book_parse(self, response: HtmlResponse):
        link = response.url
        name = response.xpath("//h1/text()").extract_first()
        author = response.xpath("//a[@itemprop='author']/text()").extract_first()
        reg_price = response.xpath("//div[@class='item-actions__price-old']//text()").extract_first()
        promo_price = response.xpath("//div[@class='item-actions__price']//text()").extract()[0]
        rating = response.xpath("//span[@class='rating__rate-value']/text()").extract_first()
        yield BooksparserItem(link=link,
                              name=name,
                              author=author,
                              reg_price=reg_price,
                              promo_price=promo_price,
                              rating=rating)