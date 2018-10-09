# 发送POST请求

import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
data = {
    'first':'true',
    'pn':'1',
    'kd':'python'
}
headers = {
    'Referer':'https://www.lagou.com/jobs/list_python?px=default&city=%E5%B9%BF%E5%B7%9E',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
response = requests.post(url,data=data,headers=headers)
# print(response.text)
print(type(response.json()))
print(response.json())