
#利用 http.cookiejar和request、HTTPCookieProcessor登录人人网

# 韩冲 人人网个人主页：http://www.renren.com/1192141461/profile
# 人人网登录url：http://www.renren.com/PLogin.do

from urllib import request, parse
from http.cookiejar import CookieJar

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

def get_opener():
    # 1.登录
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcessor对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步骤的handler创建一个opener
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    # 1.4 使用opener发送登录的请求（人人网的邮箱和密码）
    data = {
        'email': '253496831@qq.com',
        'password': 'charles253496831'
    }
    login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)

def visit_profile(opener):
    # 2.访问个人主页
    hanchong_url = 'http://www.renren.com/1192141461/profile'
    # 获取个人主页的是页面的时候，不用新建一个opener
    # 而应使用之前的那个opener，因为之前的那个opener已包含了登录所需的cookie信息
    req = request.Request(hanchong_url, headers=headers)
    resp = opener.open(req)
    with open('renren.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)


