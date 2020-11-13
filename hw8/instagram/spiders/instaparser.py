import scrapy
from scrapy.http import HtmlResponse
import hw8.instagram.insta_auth as insta_auth
import re

class InstaparserSpider(scrapy.Spider):
    name = 'instaparser'
    allowed_domains = ['instagram.com']
    start_urls = ['https://www.instagram.com/']
    insta_login = insta_auth.USER
    insta_pwd = insta_auth.PASSWORD_HASH
    inst_login_link = 'https://www.instagram.com/accounts/login/ajax/'
    parse_user = 'ai_machine_learning'  # Пользователь, у которого собираем посты. Можно указать список

    def parse(self, response:HtmlResponse):
        csrf_token = self.fetch_csrf_token(response.text)
        yield scrapy.FormRequest(
            self.inst_login_link,
            method='POST',
            callback=self.auth(),
            formdata={'username': self.insta_login,
                      'enc_password': self.insta_pwd},
            headers={'X-CSRFToken': csrf_token}
        )

    def auth(self, response: HtmlResponse):
        jdata = response.json()
        if jdata.get('authenticated'):
            yield response.follow(
                f'/{self.parse_user}',
                callback=self.user_data_parse,
                cb_kwargs={'username':self.parse_user}
            )
    def user_data_parse(self, response: HtmlResponse, username):
        print()




    #Получаем токен для авторизации
    def fetch_csrf_token(self, text):
        matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return matched.split(':').pop().replace(r'"', '')
