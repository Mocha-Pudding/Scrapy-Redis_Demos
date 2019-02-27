# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

########## 方法一 ##########
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json", "w", encoding='utf-8')
#
#     def open_spider(self, spider):
#         print('爬虫开始了……')
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.fp.write(item_json+'\n')
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()
#         print('爬虫结束了…')


########## 方法二 ##########
#### 数据量比较少的时候 可以用JsonItemExporter
from scrapy.exporters import JsonItemExporter

# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json", "wb")   #以二进制的方式写入
#         self.exportr = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exportr.start_exporting()
#
#     def open_spider(self, spider):
#         print('爬虫开始了……')
#
#     def process_item(self, item, spider):
#         # item_json = json.dumps(dict(item), ensure_ascii=False)
#         # self.fp.write(item_json+'\n')
#         self.exportr.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exportr.finish_exporting()
#         self.fp.close()
#         print('爬虫结束了…')


########## 方法三 ##########
#### 数据量比较多的时候，需要用JsonLinesItemExporter
from scrapy.exporters import JsonLinesItemExporter

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("duanzi.json", "wb")   #以二进制的方式写入
        self.exportr = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def open_spider(self, spider):
        print('爬虫开始了……')

    def process_item(self, item, spider):
        self.exportr.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束了…')