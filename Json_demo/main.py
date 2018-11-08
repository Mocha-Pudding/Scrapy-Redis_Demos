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

# json_str = json.dumps(persons)
# print(type(json_str))
# print(json_str)
with open('person.json','w',encoding='utf-8') as fp:
    # fp.write(json_str)
    json.dump(persons,fp,ensure_ascii=False)

# class Person(object):
#     country = 'china'
#
# a = {
#     'person':Person()
# }
# json.dumps(a)                 #TypeError: Object of type 'Person' is not JSON serializable