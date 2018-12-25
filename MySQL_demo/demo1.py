import pymysql

conn = pymysql.connect(host='localhost',user='root',password='password',database='pymysql_demo',port='3306')

cursor = conn.cursor()

cursor.excute("select 1")
result = cursor.fetchone()
print(result)

conn.close()