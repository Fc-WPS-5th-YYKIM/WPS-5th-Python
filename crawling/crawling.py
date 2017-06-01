import re
import requests

r = requests.get('http://comic.naver.com/webtoon/list.nhn?titleId=662774&weekday=wed')

try:
    pattern = r''
    source = r.text

    m_list = re.finditer(pattern, source)
    result_list = [m.group() for m in m_list]

except Exception as e:
    print(e)
else:
    print(result_list)




#with open('webtoon.html','wt') as f:
#    f.write(r.text)