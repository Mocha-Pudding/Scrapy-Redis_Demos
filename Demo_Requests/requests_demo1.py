# 发送GET请求

import requests

# response = requests.get('http://www.baidu.com/')
# # print(type(response.text))    #<class 'str'> unicode字符串
# # print(response.text)
#
# print(type(response.content))    #<class 'bytes'> 经过编码后的字符串 bytes 可直接存储和传输
# print(response.content.decode('utf-8'))
#
# print(response.url)
# print(response.encoding)
# print(response.status_code)

params = {
    'wd':'中国'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
response = requests.get('https://www.baidu.com/s',params=params,headers=headers)

with open('baidu.html','w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(response.url)