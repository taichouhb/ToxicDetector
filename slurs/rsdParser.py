from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import codecs
import pdb


filename = 'rsd.html' #get HTML file as a string
url1 = "http://www.rsdb.org/full"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
req = Request(url=url1, headers=headers)  
page = urlopen(req).read()
#file = codecs.open(filename, mode='r', encoding='utf-8')
#file2 = file.readlines()
#html_doc = ''.join(file2)
#print(html_doc)
soup = BeautifulSoup(page)
#print(soup)
pdb.set_trace()
#print(soup.findAll('table')[0])
for row in soup.find('table').findAll('tr')[1:-1]:
	print(row.find('td').string)