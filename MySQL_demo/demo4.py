# 数据库删除数据/更新数据

import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'pymysql_demo',
    port = 3306
)
cursor = db.cursor()

############ 删除数据  ############
# sql = """
# delete from user where id=7
# """
# cursor.execute(sql)   # 执行sql语句
#
# #插入、删除、更新  都需要执行commit操作
# db.commit()   # 映射到数据库
# db.close()

############ 更新数据  ############
sql = """
update user set username='JS6',age='3' where id=4
"""
cursor.execute(sql)   # 执行sql语句

#插入、删除、更新  都需要执行commit操作
db.commit()   # 映射到数据库
db.close()