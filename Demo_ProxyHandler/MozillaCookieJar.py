# 保存cookie到本地

from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load(ignore_discard=True)  # 设置ignore_discard=True将过期的cookie信息加载进来
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

# resp = opener.open('http://httpbin.org/cookies/set?course=abc')
# cookiejar.save(ignore_discard=True)   # 设置ignore_discard=True保存即将过期被丢弃的cookie信息

resp = opener.open('http://httpbin.org/cookies')
for cookie in cookiejar:
    print(cookie)

