# CSV文件处理 - 写入csv文件

import csv

# 写入csv文件（两种方式）

########## 方法一 ##########
###### 写入数据到csv文件，需要创建一个writer对象，主要用到两个方法。一个是writerow，这个是写入一行。一个是writerows，这个是写入多行 ######
def write_csv_1():
    headers = ['username', 'age', 'height']  # 定义表头信息
    values = [
        ('刘一', 18, 180),
        ('陈二', 22, 178),
        ('张三', 30, 168),
        ('李四', 28, 158),
        ('王五', 23, 170),
        ('赵六', 27, 188),
        ('孙七', 29, 170),
        ('周八', 49, 167),
        ('吴九', 53, 177),
        ('郑十', 20, 175)
    ]

    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)


########## 方法二 ##########
###### 使用字典的方式把数据写入进去。这时候就需要使用DictWriter了 ######
def write_csv_2():
    headers = ['username', 'age', 'height']  # 定义表头信息
    values = [
        {'username': '张三', 'age': 30, 'height': 169},
        {'username': '李四', 'age': 28, 'height': 158},
        {'username': '王五', 'age': 23, 'height': 170}
    ]
    with open('classroom2.csv','w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()      # 写入表头数据的时候，需要调用writerheader方法（一定要写）
        writer.writerows(values)

if __name__ == '__main__':
    write_csv_2()