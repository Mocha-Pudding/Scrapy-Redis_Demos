# cookie & session

import requests

# response = requests.get('https://www.baidu.com/')
# print(response.cookies)
# print(response.cookies.get_dict())

url = 'http://www.renren.com/PLogin.do'
data = {
        'email': '253496831@qq.com',
        'password': 'charles253496831'
    }
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
session = requests.Session()

session.post(url,data=data,headers=headers)

response = session.get('http://www.renren.com/1192141461/profile')
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(response.text)