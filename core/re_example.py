import re
#re library참고 http://egloos.zum.com/sweeper/v/3065126


# 아래에서 사용된 pattern은
# (\w+[\w\.]*) 2개와 ([A-Za-z]+) 총 세 개의 하위 표현식으로 작성되어 있다.
m = re.search(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)",
              "My email address is SooKkaRak@gmail.com")
print('m.group():')
print(m.group())
print('m.groups():')
print(m.groups())

result = m.groups()
name =['m.group[0]','m.group[1]','m.group[2]']

num=[0,1,2]

for i in num:
    print(name[i])
    print(result[i])

