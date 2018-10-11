# XPath语法：

#使用方法：
#1.使用//获取整个页面当中的元素，然后写标签签名，然后再写谓词进行提取。比如
#  //div[@class='abc']

#需要注意的知识点：
#1./和//的区别：/代表只获取直接子节点。  //获取子孙节点，一般//用得比较多，当然也要视情况而定
#2.contains：有时候某个属性中包含了多个值，那么可以使用"contains"函数，如：
#  //div[contains(@class,'job_detail')]
#3.谓词中的下标，是从1开始的，不是从0开始的


# lxml库的使用
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item第一个</a></li>
        <li class="item-1"><a href="link2.htm2">second item第二个</a></li>
        <li class="item-1"><a href="link3.htm3">third item第三个</a></li>
        <li class="item-inactive"><a href="link4.html">fourth item第四个</a></li>
        <li class="item-1"><a href="link5.html">fifth item第五个</a></li>
        <li class="item-0"><a href="link6.html">sixth item第六个</a>   #注意此处缺少一个</li>闭合标签
    </ul>
</div>

'''

# 使用lxml解析HTML代码：
#解析html字符串，使用'lxml.etree.HTML'进行解析，示例代码如下：
def parse_text():
    htmlElement = etree.HTML(text)
    print(type(htmlElement))  # <class 'lxml.etree._Element'>
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

#解析html文件，使用'lxml.etree.parse'进行解析，示例代码如下：
def parse_dianping_file():
    htmlElement = etree.parse('dianping.html')
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

#这个函数默认使用的是'XML'解析器，所以如果碰到一些不规范的'HTML'代码的时候，
# 就会解析错误，这个时候就要自己创建'HTML'解析器。
def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse('lagou.html',parser=parser)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    # parse_text()
    # parse_dianping_file()
    parse_lagou_file()


