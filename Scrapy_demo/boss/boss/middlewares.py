# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import requests
import json
from boss.models import ProxyModel
from twisted.internet.defer import DeferredLock   # 加锁操作

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
        self.lock = DeferredLock()  # 定义创建锁

    def process_request(self,request,spider):
        # 判断request里面是否有设置过代理 或者 当前代理即将过期
        if 'proxy' not in request.meta or self.current_proxy.is_expiring:
            # 请求代理
            self.update_proxy()
            request.meta['proxy'] = self.current_proxy.proxy

    def process_response(self,request,response,spider):
        # 如果返回的状态码不等于200或者跳转到验证码当中，即重新获取代理
        if response.status != 200 or "captcha" in response.url:
            if not self.current_proxy.blacked:
                self.current_proxy.blacked = True
            print("%s这个代理被识别并被加入黑名单了" % self.current_proxy.ip)
            self.update_proxy()
            # 如果来到这里，说明这个请求已经被BOSS直聘识别为爬虫
            # 所以这个请求就相当于什么都没有获取到
            # 如果不返回request，那么这个request就相当于没有获取到数据
            # 也就是说，这个请求就被废掉了，这个数据就没有被抓取到
            # 所以要重新返回request，让这个请求重新加入到调度中，下次再请求
            return request
        # 如果是正常的，那么要记得返回response
        # 如果不返回，那么这个response就不会被传到爬虫那里去，也就得不到解析
        return response

    # process_request和process_response（如遇到403页面的时候）里面都可能需要请求代理
    # 请求代理的代码多个地方需要用到，所有单独定义一个方法 get_proxy()
    def update_proxy(self):
        self.lock.acquire()   # 上锁
        # 判断如果没有或者即将过期又或者被拉黑
        if not self.current_proxy or self.current_proxy.is_expirin or self.current_proxy.blacked:
            response = requests.get(self.PROXY_URL)
            text = response.text  # 此处得到的text是个json格式的字符串,需要load成字典
            print("重新获取了一个代理：",text)
            # 从代理池api返回回来的数据格式如下：
            # {"code":0,"success":true,"msg":"0","data":[{"ip":"223.242.123.50","port":3212,"expire_time":"2019-01-15 10:15:20"}]}
            result = json.loads(text)
            if len(result['data']) > 0:
                data = result['data'][0]
                proxy_model = ProxyModel(data)
                self.current_proxy = proxy_model
                # return proxy_model
        self.lock.release()  # 解锁操作
