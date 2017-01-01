from urllib.request import urlopen
from http.client import HTTPResponse
from bs4 import BeautifulSoup
from bs4.element import Tag

def getNeighborUrls():
    html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    if not isinstance(html, HTTPResponse):
        return None

    bs_object = BeautifulSoup(html, 'html.parser')
    for link in bs_object.findAll("a"):
        if not isinstance(link, Tag):
            continue
        if 'href' in link.attrs:
            print(link)
            print()
            print(link.attrs['href'])
            print()

getNeighborUrls()
