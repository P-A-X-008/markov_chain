import urllib2
from bs4 import *


def get_content(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()
