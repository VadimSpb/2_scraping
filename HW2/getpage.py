from bs4 import BeautifulSoup as BS
import requests

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/76.0.3809.100 Safari/537.36 OPR/63.0.3368.53'}

def getpage(url, headers=headers, params=None):
	responce = requests.get(url, headers=headers, params=params)

	# проверяем доступность страницы
	if responce.status_code is not requests.codes.ok:
		print('Страница ' + html.url + ' не доступна')


	# делаем объект bs
	soup = BS(responce.text, 'lxml')

	return soup