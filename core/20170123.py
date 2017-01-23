import  requests

#with open("foo.txt", "w") as f:
#   f.write("Life is too short, you need python")
#위와 같이 with문을 이용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close되어 편리하다. (※ with구문은 파이썬 2.5부터 지원됨)

# Session 생성, with 구문 안에서 유지
with requests.session() as s :
    req = s.get('http://clien.net/')
    html = req.text
    header = req.headers
    status = req.status_cod
    # HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok