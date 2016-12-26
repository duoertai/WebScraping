from urllib.request import urlopen
from urllib.error import HTTPError
from http.client import HTTPResponse
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError:
        print('get HTTP error, cannot open the url: ' + url)
        return None

    if not isinstance(html, HTTPResponse):
        print('cannot get an HTTP response after trying to open url')
        return None

    title = ''
    try:
        bs_object = BeautifulSoup(html.read(), 'html.parser')
        title = bs_object.body.h1.text
    except AttributeError:
        print('cannot find the attribute in the html content')

    return title

Title = get_title('http://www.pythonscraping.com/pages/page1.html')

if Title is None:
    print('Title could not be found')
else:
    print(Title)
