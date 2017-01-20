import requests
from bs4 import BeautifulSoup

url = "http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do"
params = {
    'currentPage': 1,
    'rowPerPage': 300
}

html = requests.get(url,params=params).text

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('.memberna_list dl dt a'):
    name = tag.text
    id = tag['href']
    print(name, id)
