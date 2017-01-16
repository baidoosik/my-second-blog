import requests
import json
import re

def spellchecker(q):
    url = "https://m.search.naver.com/p/csearch/dcontent/spellchecker.nhn?"

    params = {
        '_callback' : 'mycallback',
        'q' : q,
    }

    header = headers={'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36 "}

    html =requests.get(url, params=params, headers=header).text
    response =html.replace(params['_callback']+'(','')
    response =response.replace(');','')

    response_dict = json.loads(response)
    result_text = response_dict['message']['result']['html']

    result_text = re.sub(r'<\/?.*?>','',result_text)

    return result_text

if __name__ == '__main__' :
    line = input()
    print(spellchecker(line))

