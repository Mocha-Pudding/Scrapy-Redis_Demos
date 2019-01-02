# 连接MongoDB

import pymongo

# 获取连接MongoDB的对象
client = pymongo.MongoClient("127.0.0.1", port=27017)

# 获取数据库(如果没有ceshi这个数据库也没有关系)
db = client.ceshi

# 获取数据库中的集合（也就是MySQL中的表）
collection = db.qa


# "增"、“删”、“改”、“查”具体操作示例：

# 1.“增”：插入数据
collection.insert({"username":"ZGreenicy","age":"24"})
# 1.1 insert_one插入一条数据，等价于insert 如上
collection.insert_one({
    "username":"JS6",
    "age":"2"
})
# 1.2 insert_many插入多条数据到集合中，如下
collection.insert_many([
    {
        "username":"Zhujiange",
        "age":28
    },
    {
        "username":"Zengjingxin",
        "age":"24"
    }
])

# 2.“查”：查找数据
# 2.1 fing方法，获取集合中所有的数据
cursor = collection.find()
for x in cursor:
    print(x)
# 2.2 fing_one方法：获取集合中一条文档对象
result = collection.find_one({"age":28})
print(result)

# 3.“改”：更新修改数据
# 3.1 更新一条文档对象
collection.update_one({"username":"aaa"},{"Set":{"username":"ccc"}})
# 3.2 更新多条文档对象
collection.update_many({"username":"aaa"},{"Set":{"username":"bbb"}})

# 4.“删”：删除数据
# 4.1 删除一条文档对象
collection.delete_one({"username":"ccc"})

# 4.2 删除多条文档对象
collection.delete_many({"username":"ddd"})