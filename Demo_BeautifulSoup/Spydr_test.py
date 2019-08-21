# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:14:48 2019

@author: Mocha-Pudding
"""

import requests
from bs4 import BeautifulSoup

BASE_DOMIN = "https://www.dytt8.net"
urllist = []
for i in range(3):
    urllist.append('https://www.dytt8.net/html/gndy/dyzz/list_23_%d.html' %(i+1))
    
u1 = urllist[0]

data_urllist = []
for url in urllist:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    div = soup.find('div',class_="co_content8")
    ul = div.find_all('ul')
    tables = soup.find_all('table', class_="tbspan")
    for table in tables:
        item_url = BASE_DOMIN + table.a['href']
        data_urllist.append(item_url)
        print(item_url)














