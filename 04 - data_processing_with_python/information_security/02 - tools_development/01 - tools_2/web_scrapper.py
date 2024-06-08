"""
    Programa que utiliza as bibliotecas 'requests' e 'BeautifulSoup' para fazer um scraping
    de páginas web, minerando informações a respeito de sites.
"""
import requests
from bs4 import BeautifulSoup

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

news = soup.find("h3", class_="-bold -font-18 -gray-dark-2")

print(soup.title.string)

print(soup.p.string)

print(news.string)
