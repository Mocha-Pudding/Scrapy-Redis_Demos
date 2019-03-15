# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=Python&page=1']

    rules = (
        # 匹配职位列表页的规则
        Rule(LinkExtractor(allow=r'.+\?query=Python&page=\d'), follow=True),
        # 匹配职位详情页的规则
        Rule(LinkExtractor(allow=r'.+job_detail/[a-z\d._-~]+/.html'), callback="parse_job", follow=False)
    )

    # 解析职位详情的数据
    def parse_job(self, response):
        pass
