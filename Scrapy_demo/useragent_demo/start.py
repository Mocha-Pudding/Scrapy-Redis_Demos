#encoding: utf-8

from scrapy import cmdline

# 启动爬虫 随机请求头中间件
# cmdline.execute("scrapy crawl httpbin".split())

# 启动爬虫 ip代理池中间件
cmdline.execute("scrapy crawl ipproxy".split())
