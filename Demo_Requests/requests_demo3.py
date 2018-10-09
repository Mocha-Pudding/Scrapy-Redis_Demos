# 使用代理

import requests

url = 'http://httpbin.org/ip'

proxy = {
    'http':'125.110.107.198:9000'
}

response = requests.get(url,proxies=proxy)
print(response.text)