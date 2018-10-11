from lxml import etree

# 1.获取所有tr标签
# 2.获取第2个tr标签
# 3.获取所有class等于even的tr标签
# 4.获取所有a标签的href属性
# 5.获取所有职位信息(纯文本)

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html",parser=parser)

# 1.获取所有tr标签
# //tr
# xpath函数返回的是一个列表
# trs = html.xpath("//tr")
# print(type(trs))
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 2.获取第2个tr标签
# tr = html.xpath("//tr[2]")[0]
# print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 3.获取所有class等于even的tr标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 4.获取所有a标签的href属性
# aList = html.xpath("//a/@href")
# for a in aList:
#     print("https://hr.tencent.com/"+a)

# 5.获取所有职位信息(纯文本)
trs = html.xpath("//tr[position()>1]")
positions = []
for tr in trs:
    # 在某个标签下，再执行xpath函数，获取这个标签下的子孙元素，
    # 那么应该在//之前加一个点.代表在当前元素下获取
    href = tr.xpath(".//a/@href")[0]
    fullurl = "https://hr.tencent.com/" + href
    # title = tr.xpath(".//a/text()")[0]
    title = tr.xpath("./td[1]//text()")[0]
    category = tr.xpath("./td[2]/text()")[0]
    nums = tr.xpath("./td[3]/text()")[0]
    address = tr.xpath("./td[4]/text()")[0]
    pubtime = tr.xpath("./td[5]/text()")[0]

    position = {
        'url' : fullurl,
        'title' : title,
        'category' : category,
        'nums' : nums,
        'address' : address,
        'pubtime' : pubtime
    }
    positions.append(position)

print(positions)






## lxml结合xpath注意事项：

## 1.使用'xpath'语法，应该使用'Element.xpath'方法来执行xpath的选择，例如：
#    trs = html.xpath("//tr[position()>1]")
# 'xpath函数'返回来的永远是一个列表

## 2.获取某个标签的属性：
#    href = html.xpath(".//a/@href")

## 3.获取文本，是通过'xpath'中的'text()'函数，示例代码如下：
#    address = tr.xpath("./td[4]/text()")[0]

## 4.在某个标签下，再执行xpath函数，获取这个标签下的子孙元素，那么应该在斜杠/
# 之前加一个点.代表在当前元素下获取，示例代码如下：
#    title = tr.xpath("./td[1]//text()")[0]