# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import requests
import json
from boss.models import ProxyModel

# 随机请求头下载器中间件
class UserAgentDownloadMiddleware(object):
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'
    ]

    def process_request(self,request,spider):
        user_agent = random.choice(self.USER_AGENTS)  # 从USER_AGENTS列表中随机选择一个User-Agent
        request.headers['User-Agent'] = user_agent


# 代理的下载器中间件
class IPProxyDownloadMiddleware(object):
    # 网上代理服务器生成的API，以下为芝麻代理的
    PROXY_URL = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&port=11&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='

    def __init__(self):
        super(IPProxyDownloadMiddleware, self).__init__()
        self.current_proxy = None

    def process_request(self,request,spider):
        # 判断request里面是否有设置过代理 或者 当前代理即将过期
        if 'proxy' not in request.meta or self.current_proxy.is_expiring:
            # 请求代理
            self.get_proxy()
            request.meta['proxy'] = self.current_proxy.proxy

    def process_response(self,request,response,spider):
        pass

    # process_request和process_response（如遇到403页面的时候）里面都可能需要请求代理
    # 请求代理的代码多个地方需要用到，所有单独定义一个方法 get_proxy()
    def get_proxy(self):
        response = requests.get(self.PROXY_URL)
        text = response.text  # 此处得到的text是个json格式的字符串,需要load成字典
        # 从代理池api返回回来的数据格式如下：
        # {"code":0,"success":true,"msg":"0","data":[{"ip":"223.242.123.50","port":3212,"expire_time":"2019-01-15 10:15:20"}]}
        result = json.loads(text)
        data = result['data'][0]
        proxy_model = ProxyModel(data)
        self.current_proxy = proxy_model
        return proxy_model
