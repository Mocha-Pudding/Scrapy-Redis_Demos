# 数据库查找数据

import pymysql

# 连接数据库
db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password ='password',
    database = 'pymysql_demo',
    port = 3306
)
cursor = db.cursor()

# 查找数据
# select username,age from table where conditions...
# select * from table
# (上面语句等价于)select id,username,age,password from table

# sql = """
# select username,age from user where id=2
# """

sql = """
select * from user
"""

########### fetchon() ###########
# cursor.execute(sql)
# result = cursor.fetchone()    # fetchone()第一次调用返回第一条
# print(result)
# result = cursor.fetchone()    # fetchone()第二次调用返回第二条
# print(result)

# cursor.execute(sql)
# while True:
#     result = cursor.fetchone()
#     if result:
#         print(result)
#     else:
#         break
#
# db.close()

########### fetchall() ###########
# cursor.execute(sql)
# results = cursor.fetchall()
# for result in results:
#     print(result)
# db.close()

########### fetchmany(size) ###########
cursor.execute(sql)     # 执行sql语句
results = cursor.fetchmany(3)   # 指定获取多少条数据
for result in results:
    print(result)
db.close()