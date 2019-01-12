# CSV文件处理 - 读取csv文件

#CSV是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。最广泛的应用是在程序之间转移表格数据，而这些程序本身是在不兼容的格式上进行操作的（往往是私有的和/或无规范的格式）。因为大量程序都支持某种CSV变体，至少是作为一种可选择的输入/输出格式。

# 1.纯文本，使用某个字符集，比如ASCII、Unicode、EBCDIC或GB2312（简体中文环境）等
# 2.由记录组成（典型的是每行一条记录）；
# 3.每条记录被分隔符分隔为字段（典型分隔符有逗号、分号或制表符；有时分隔符可以包括可选的空格）；
# 4.每条记录都有同样的字段序列。

import csv

# 读取csv文件（两种方式）

########## 方法一 ##########
def read_csv_1():
    with open('stock.csv', 'r') as fp:
        # reader是一个迭代器
        reader = csv.reader(fp)
        next(reader)  # next对迭代器往下挪一位 去除掉第一行标题的数据
        for x in reader:
            # print(x)
            index = x[0]
            volumnB = x[2]
            volumnS = x[6]
            print({'股票索引号': index, '买入量': volumnB, '卖出量': volumnS})

########## 方法二：通过字典的方式 ##########
def read_csv_2():
    with open('stock.csv', 'r') as fp:
        # 使用DictReader创建reader对象
        # 不会包含标题那行的数据
        # reader是一个迭代器，遍历这个迭代器，返回来的是一个字典
        reader = csv.DictReader(fp)
        for x in reader:
            # print(x)    #输出的是字典
            value = {'股票索引号': x['index'], '买入量': x['volumnB'], '卖出量': x['volumnS']}
            print(value)

if __name__ == '__main__':
    read_csv_2()

