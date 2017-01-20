import  requests
from bs4 import BeautifulSoup as bs

url ='https://search.naver.com/search.naver?'
param ={
    'where':'nexearch',
    'ie':'utf8',
    'X_CSA':'address_search',
    'query':'동대동',
}

html = requests.get(url,params=param)
html = html.text

soup= bs(html, 'html.parser')

search_results = soup.select(
    'tr > td > dl > dd'
)

result = {}

for i in search_results:
     print('제목' + result.text)
    # print('링크' + result['href'])
