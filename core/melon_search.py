import requests as req
import json

#mac alfred2 lancher tool
#https://github.com/askdjango/snippets

def melon_search(q):
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

if __name__ == '__main__' :
    line =input()
    print(melon_search(line))
