# 数据库插入数据

import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='pymysql_demo',
    port=3306
)

cursor = db.cursor()

# 插入数据方法一
# 一般格式：insert into table(id,username,age,password) value(3,'Mocha-Pudding',22,'333333')
# sql = """
# insert into user(id,username,age,password) value(3,'Mocha-Pudding',22,'333333')
# """
#
# cursor.execute(sql)
# db.commit()    # 提交到数据库

# 插入数据方法一  不写死数据，用%s站位，再用元组提交到数据库
sql = """
insert into user(id,username,age,password) value(null,%s,%s,%s)
"""

username = 'JS6'
age = 2
password = '444444'

cursor.execute(sql, (username,age,password))  #用元组传递参数
db.commit()    # 提交到数据库

db.close()