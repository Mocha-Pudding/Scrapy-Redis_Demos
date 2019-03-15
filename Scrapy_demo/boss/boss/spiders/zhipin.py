# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=Python&page=1']

    rules = (
        # 匹配职位列表页的规则
        Rule(LinkExtractor(allow=r'.+\?query=Python&page=\d'), follow=True),
        # 匹配职位详情页的规则
        Rule(LinkExtractor(allow=r'.+job_detail/\w+~.html'), callback="parse_job", follow=False)
    )

    # 解析职位详情的数据
    def parse_job(self, response):
        name = response.xpath("//div[@class='name']/h1/text()").get().strip()  # strip()去掉头和尾的空白字符串
        salary = response.xpath("//div[@class='name']/span/text()").get().strip()
        job_info = response.xpath(
            "//div[@class='job-primary detail-box']/div[@class='info-primary']/p//text()").getall()
        city = job_info[0]
        work_years = job_info[1]
        education = job_info[2]
        # company = response.xpath("//div[@class='company-info']/a/@title").get().strip()
        company = response.xpath("//div[@class='company-info']/div[@class='info']/text()").get().strip()
        item = BossItem(name=name, salary=salary, city=city, work_years=work_years, education=education,company=company)
        yield item
