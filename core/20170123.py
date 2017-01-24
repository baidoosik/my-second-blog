import requests
from bs4 import BeautifulSoup as bs

#with open("foo.txt", "w") as f:
#   f.write("Life is too short, you need python")
#위와 같이 with문을 이용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close되어 편리하다. (※ with구문은 파이썬 2.5부터 지원됨)

# Session 생성, with 구문 안에서 유지

# 로그인할 유저정보를 넣어주자 (모두 문자열)
LOGIN_INFO = {
    'mb_id': 'qoentlr37',
    'mb_password': 'erunc837!!'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
    login_req = s.post('https://www.clien.net/cs2/bbs/login_check.php', data=LOGIN_INFO)
    # 로그인에 성공한 경우 nowlogin=1이 포함된 스크립트가 response로 온다.
    if not 'http://www.clien.net..?nowlogin=1' in login_req.text:
        raise Exception('로그인에 실패했습니다.')
    resp = s.get('http://www.clien.net/cs2/bbs/board.php?bo_table=park&wr_id=1068932')
    # BeautifulSoup으로 parsing을 해줍니다.
    # 이전 게시글과는 다르게 .content를 이용했는데,
    # 한국 웹 사이트의 경우 UTF-8에서도 일부 UnicodeError가 발생할 수 있어
    # 아래와 같은 resp.content 를 이용해 에러를 피했습니다.
    soup = bs(resp.content, 'html.parser')
    title = soup.select('div.view_title > div > h4 > span')
    contents = soup.select('#writeContents > p')
    # HTML을 제대로 파싱한 뒤에는 .text속성을 이용합니다.
    print(title[0].text) # 글제목
    for c in contents: # 글내용
        print(c.text)