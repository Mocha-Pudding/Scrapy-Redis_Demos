# 数据库的链接

import pymysql

db = pymysql.connect(host='localhost',user='root',password='password',database='pymysql_demo',port=3306)

cursor = db.cursor()

cursor.execute('select 1')   # 执行sql语句
result = cursor.fetchone()
print(result)

db.close()