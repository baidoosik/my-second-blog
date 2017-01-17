import requests as req

url ="http://www.melon.com/search/keyword/index.json?jscallback=jQuery191021634718864107283_1484665486657&query=%25E3%2585%258C&_=1484665486673"

print(req.get(url).text)