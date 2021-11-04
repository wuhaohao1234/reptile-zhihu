import requests
import re
URL = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=10'

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
  'accept-language': 'zh-CN,zh;q=0.9'
}

res = requests.get(URL, headers=headers)
print(res.text)
strFile = str(res.json())

strFile = re.sub('\'', '\"', strFile)
strFile = re.sub('True', 'true', strFile)
strFile = re.sub('False', 'false', strFile)

f = open('./test.json', 'w', encoding='utf-8')
f.write(strFile)
f.close()