from scrapy import cmdline

# cmdline.execute("scrapy crawl qsbk_spider".split())   #等价于下面一行
cmdline.execute(['scrapy','crawl','qsbk_spider'])