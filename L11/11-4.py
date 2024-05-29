# -*- coding: utf-8 -*-
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson11 応用編 Webとネットワーク ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("11-4 Webスクレイピングしてみよう")
print("-------------------------")
print("")

print("| BeautifulSoupでWebスクレイピングしよう")
print("----------------------------------------")
print("コード/BeautifulSoupのインポート: No Output")
print("c11_4_1/HTMLの取得:")
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.python.org')
soup = BeautifulSoup(html.text)

print("----------------------------------------")
print("c11_4_2/titleタグの要素の取得:")
html = requests.get('https://www.python.org')
soup = BeautifulSoup(html.text, 'lxml')
headers = soup.find_all('h2')
print(headers)

print("----------------------------------------")
print("c11_4_3/h2タグの要素の取得:")
print(headers[0].text)

print("----------------------------------------")
print("c11_4_4/divタグのintroductionクラス要素の取得:")
intro = soup.find_all('div', {'class': 'introduction'})
print(intro)

print("----------------------------------------")
print("c11_4_5/divタグのintroductionクラス要素の取得:")
print(intro[0].text)

print("----------------------------------------")
print("11-4終了")
print("Lesson11終了")