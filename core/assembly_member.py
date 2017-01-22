import requests
from bs4 import BeautifulSoup
import re


url = "http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=300"

html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

for tag_member in soup.select('.memberna_list dl dt a'):
    name = tag_member.text
    link = tag_member['href'].replace('javascript:jsMemPop(','').replace(')','')
    print(name,link)

