from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


words = []
def noswear_parsing(c):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    url1 = "https://www.noswearing.com/dictionary/" + c
    req = Request(url=url1, headers=headers) 
    page = urlopen(req).read() 
    soup = BeautifulSoup(page)
    data = soup.findAll("b")
    if (len(data) > 5):
        for i in data[5:-1]:
            words.append(i.get_text())
            print(i.get_text())

alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alpha)):
    noswear_parsing(alpha[i])

with open('noswear.csv', 'a') as d:
    for w in words:
        output = w + ", "
        d.write(output)