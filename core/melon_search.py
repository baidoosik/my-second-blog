import requests as req
import json
import time
#mac alfred2 lancher tool
#https://github.com/askdjango/snippets

def melon_search(q):
    start_time =time.time()
    url ="http://www.melon.com/search/keyword/index.json?"

    param = {
        'jscallback':'jQuery191021634718864107283_1484665486657',
        'query':q,
    }
    html = req.get(url,params=param).text

    html= html.replace(param['jscallback']+'(','').replace(');','')
    response_dict = json.loads(html)

    if 'SONGCONTENTS' not in response_dict:
        print('result is not found')
    else:
        for song in response_dict['SONGCONTENTS']:
            print('''{SONGNAME} {SONGID} {ARTISTNAME}
            - http://www.melon.com/album/detail.htm?albumId={ALBUMID}'''.format(**song))
            #print(song['SONGNAME'],song['SONGID'],song['ARTISTNAME'])
    end_time=time.time()
    tac_time = end_time - start_time
    print('작업시간: %f'%tac_time)

if __name__ == '__main__' :
    line =input()
    print(melon_search(line))
