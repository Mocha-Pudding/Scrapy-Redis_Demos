# JSON文件处理
#
# JSON支持数据格式：
# 1.对象（字典）。使用花括号
# 2.数组（列表）。使用方括号
# 3.整型、浮点型、布尔类型、null类型
# 4.字符串类型（字符串必须用双引号，不能用单引号）
#
# 多个数据之间使用逗号分开。
# 注意：json本质上就是一个字符串
#
# JSON在线解析网站：www.json.cn

import json

# 将Python对象转换为json字符串

persons = [
    {
        'username':"Mocha-Pudding",
        'age':24,
        'country':'New Zealand'
    },
    {
        'username':"ZGreenicy",
        'age':22,
        'country':'Australia'
    },
    {
        'username':"建设六",
        'age':18,
        'country':'英国'
    }
]

######### dumps #########
# json_str = json.dumps(persons)   #dumps()函数来将Python对象（上面是列表当中的字典）转化成json字符串
# print(type(json_str))
# print(json_str)

######### dump #########
with open('person.json','w',encoding='utf-8') as fp:
    # fp.write(json_str)
    json.dump(persons,fp,ensure_ascii=False)
    # 因为json在dump的时候，只能存放ascii的字符，因此会将中文进行转义，这时候我们可以使用ensure_ascii=False关闭这个特性。
    # 在Python中。只有基本数据类型才能转换成JSON格式的字符串。也即：int、float、str、list、dict、tuple。


# class Person(object):
#     country = 'china'
#
# a = {
#     'person':Person()
# }
# json.dumps(a)                 #TypeError: Object of type 'Person' is not JSON serializable