# -*- coding: utf-8 -*-
import scrapy
import json

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        user_agent = json.loads(response.text)['user-agent']
        print('=' * 60)
        print(user_agent)
        print('=' * 60)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
        # dont_filter=True 的意思是不要过滤掉，不要去重