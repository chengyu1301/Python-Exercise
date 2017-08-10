# -*- coding:utf-8 -*-

import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# to request url
htmlRequest = urlopen("http://www.google.com/")

# to get the status code
statusCode = htmlRequest.getcode()
print(statusCode)

# to get the content
content = htmlRequest.read()
print(content)

print('=====Another way=====')
#=====Another way=====#

request = urllib.request.Request('http://www.nchu.edu.tw/index1.php')
request.add_header('User-Agent', 'Mozilla/5.0')
response = urlopen(request)
content = response.read()
print(str(content, 'utf-8'))


soup = BeautifulSoup(content, 
                     'html.parser', 
                     from_encoding='utf-8')

links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())
    
linkNode = soup.find('a', href='http://www.nchu.edu.tw/')
print(linkNode.name, linkNode['href'], linkNode.get_text())

# use re
linkNode = soup.find('a', href=re.compile(r'nchu'))
print(linkNode.name, linkNode['href'], linkNode.get_text())


divNode = soup.find('div', class_='sub-nav lv1')
print(divNode.name, divNode.get_text())