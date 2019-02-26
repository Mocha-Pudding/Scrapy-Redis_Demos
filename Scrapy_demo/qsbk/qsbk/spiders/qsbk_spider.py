# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

class QsbkSpiderSpider(scrapy.Spider):
    #name：这个爬虫的名字，名字必须唯一
    name = 'qsbk_spider'
    #allowed_domains：允许的域名范围
    allowed_domains = ['qiushibaike.com']
    #start_urls：爬虫从这个变量中的url开始
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        contentLeft = response.xpath("//div[@id='content-left']")
        # SelectorList
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        for duanzidiv in duanzidivs:
            # Selector
            author = duanzidiv.xpath(".//h2/text()").get().strip()    #strip()是去除前后空白
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()    #content就变成字符串str了
            print(content)