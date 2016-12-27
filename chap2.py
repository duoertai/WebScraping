from urllib.request import urlopen
from http.client import HTTPResponse
from bs4 import BeautifulSoup
from bs4.element import Tag
import re


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
if not isinstance(html, HTTPResponse):
    print('something wrong with the response')

bs_object = BeautifulSoup(html, 'html.parser')
images = bs_object.findAll('img', {'src': re.compile("\.\./img/gifts/img.*\.jpg")})

for image in images:
    print(image["src"])
