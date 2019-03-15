# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 写完pipelines.py后需要在settings.py文件里开启下

from scrapy.exporters import JsonLinesItemExporter

class BossPipeline(object):
    def __init__(self):
        self.fp = open('jobs.json','wb')  # 以二进制的方式写入 ‘wb’
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False)  #ensure_ascii=False设置为False才能保存中文

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    # 重写下另外一个函数
    def close_spider(self,spider):
        self.fp.close()
