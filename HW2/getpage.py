from bs4 import BeautifulSoup as BS
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}

def getpage(url, headers=headers, params=None):
	responce = requests.get(url, headers=headers, params=params)
	soup  = BS(responce.text, "html.parser")
	return soup