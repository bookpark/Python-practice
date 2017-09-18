import re
from bs4 import BeautifulSoup

f = open('sample.txt', 'rt')
source = f.read()
soup = BeautifulSoup(source, 'html.parser')

for a in soup.find_all('img'):
    print(a['title'])
