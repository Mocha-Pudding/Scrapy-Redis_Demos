# 爬虫使用Cookie登录模拟登陆人人网
# 韩冲 人人网个人主页：http://www.renren.com/1192141461/profile
# 人人网登录url：http://www.renren.com/PLogin.do

from urllib import request

# 1.不使用cookie去请求韩冲的主页
hanchong_url = "http://www.renren.com/1192141461/profile"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'Cookie':"anonymid=jmzzmdef-zawj07; depovince=GW; _r01_=1; JSESSIONID=abc4eh9NUwraK4NW3Nszw; ick_login=d0512397-852b-46b9-9b71-08d5b20f0e8a; first_login_flag=1; ln_uact=253496831@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20140607/0420/h_main_RIvt_27bd00021e1a1986.jpg; wp_fold=0; jebecookies=a879dbae-a5e8-4272-b302-71324f6c32d0|||||; _de=77A908961935693A247380B22A94C474696BF75400CE19CC; p=e9e41ad07306ffa9c2a83ec370da38492; t=9da973e2d67324b4e0880511d7be469a2; societyguester=9da973e2d67324b4e0880511d7be469a2; id=331028322; xnsid=ad5bce08; ver=7.0; loginfrom=null; jebe_key=6beff12e-671d-4212-b3ec-7073cc4a7074%7Cb3adae2253dd3a09416f1db292555816%7C1538985444513%7C1"
}
req = request.Request(url=hanchong_url, headers=headers)
resp = request.urlopen(req)
with open('renren.html','w',encoding='utf-8') as fp:
    # write()函数必须写入一个str的数据类型
    # resp.read()读出来的是一个byte数据类型
    # bytes -> decode -> str
    # str -> encode -> bytes
    fp.write(resp.read().decode('utf-8'))
# print(resp.read().decode('utf-8'))