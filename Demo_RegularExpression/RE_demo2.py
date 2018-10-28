# 转义字符与原生字符串

import re

# 通过反斜杠\来进行对特殊字符的转义
text = "Apple iPhone Xs is $1299!"
ret = re.search("\$\d+",text)
print(ret.group())

# 原生字符串：
# text1 = '\\n'   # 反斜杠\ 转义字符
# text2 = r'\n'   # r表示原生  r=raw原生
# print(text1,text2)

text = "\\n"   # 等价于= '\n'
# python中： '\\n' = \n
# \\\\n => \\n
# 正则表达式中：\n =
# \\n => \n
ret = re.match('\\\\n',text)
print(ret.group())


