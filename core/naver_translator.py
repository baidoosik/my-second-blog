import  requests as req
import json

def naver_translator(q):
    url="https://s.search.naver.com/n/translate/translateForNx.dic?"

    params ={
        '_callback':'mycallback',
        'query':q,
        'srcLang':'ko',
        'tarLang':'en',
        'cht':0,
    }

    html = req.get(url,params=params).text
    html = html.replace(params['_callback']+'(','').replace(')','')

    result_dict = json.loads(html)
    result= result_dict['resultData']

    return result

if __name__=='__main__':
    line=input()
    print(naver_translator(line))


