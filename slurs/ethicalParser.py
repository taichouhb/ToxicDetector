#https://en.wikipedia.org/wiki/List_of_ethnic_slurs

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
url1 = "https://en.wikipedia.org/wiki/List_of_ethnic_slurs"
req = Request(url=url1, headers=headers) 
page = urlopen(req).read() 
soup = BeautifulSoup(page)
print(soup.prettify())

