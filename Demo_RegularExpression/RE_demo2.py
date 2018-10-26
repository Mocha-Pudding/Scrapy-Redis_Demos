# 转义字符与原生字符串

import re

# 通过反斜杠\来进行对特殊字符的转义
text = "Apple iPhone Xs is $1299!"
ret = re.search("\$\d+",text)
print(ret.group())

# 原生字符串：
text = '\n'
print(text)

