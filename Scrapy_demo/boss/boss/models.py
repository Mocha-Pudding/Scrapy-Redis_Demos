#encoding:utf-8
from datetime import datetime, timedelta

class ProxyModel(object):
    def __init__(self,data):
        # 会传递代理的data进来，大致格式内容如下：
        # "ip":"223.242.123.50","port":3212,"expire_time":"2019-01-15 10:15:20"
        self.ip = data['ip']
        self.port = data['port']
        self.expire_str = data['expire_time']
        self.blacked = False   # 是否被拉黑

        # 时间格式： 2019-01-15 10:15:20
        # datetime.strptime()   # strptime()此方法为纯Python实现，执行效率不高
        date_str, time_str = self.expire_str.split(" ")
        year, month, day = date_str.split("-")
        hour, minute, second = time_str.split(":")
        self.expire_time = datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute),
                             second=int(second))

        # https://ip:port 构建好代理
        self.proxy = "https://{}:{}".format(self.ip,self.port)

    # @property
    # def expire_time(self):
    #     # 在函数expire_time()前面加上了@property装饰器，将函数变成了属性，以后在调用函数的时候，就跟调用属性是一样的
    #     # 时间格式： 2019-01-15 10:15:20
    #     # datetime.strptime()   # strptime()此方法为纯Python实现，执行效率不高
    #     date_str, time_str = self.expire_str.split(" ")
    #     year,month,day = date_str.split("-")
    #     hour,minute,second =time_str.split(":")
    #     date_time = datetime(year=int(year),month=int(month),day=int(day),hour=int(hour),minute=int(minute),second=int(second))
    #     return date_time

    @property
    def is_expiring(self):   # 判断代理是否即将过期
        now = datetime.now()
        if (self.expire_time - now) < timedelta(seconds=5):
            # 过期时间小于5秒，就请求代理
            return True
        else:
            return False
