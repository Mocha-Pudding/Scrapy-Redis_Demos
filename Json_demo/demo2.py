# 将JSON数据load成Python对象

import json

######### loads #########
# json_str = '[{"username": "Mocha-Pudding", "age": 24, "country": "New Zealand"}, {"username": "ZGreenicy", "age": 22, "country": "Australia"}, {"username": "建设六", "age": 18, "country": "英国"}]'
#
# persons = json.loads(json_str)
# print(type(persons))
# for person in persons:
#     print(person)

######### load #########
#直接从文件中读取json文件load成Python对象
with open('person.json','r',encoding='utf-8') as fp:
    persons = json.load(fp)
    print(type(persons))
    for person in persons:
        print(person)


# 两个函数load和loads：load是和文件有关系的；loads是和文件没有关系的