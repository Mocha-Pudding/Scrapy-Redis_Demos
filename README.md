# Scrapy-Redis_Demos
</br>
<h1 align="center">:whale:Python分布式爬虫学习记录:whale:</h></br>
</br>
<p align="center">🍭🍭🍭👋👋👋</p>

> <h5>生命苦短，我用Python！</h5>
> <h5>Python Scrapy-Redis Demos.</h5>

## 简易结构
学习路线
```
├─── Demo_ProxyHandler
│    ├── 实现代理登录
│    │    ├── CookieJar.py
│    │    ├── Cookie_login.py
│    │    ├── MozillaCookieJar.py
│    │    ├── ProxyHandler.py
│    │    ├── cookie.txt
│    │    └── renren.html
│    └── END 
│
├─── Demo_Requests
│    ├── Requests库基本用法
│    │    ├── requests_demo1.py
│    │    ├── requests_demo2.py
│    │    ├── requests_demo3.py
│    │    ├── requests_demo4.py
│    │    └── renren.html
│    └── END 
│
├─── Demo_XPath
│    ├── 结合xpath和lxml对html进行解析
│    │    ├── XPath_demo1.py
│    │    ├── demo_lxmlWithXPath.py
│    │    ├── dianping.html
│    │    ├── lagou.html
│    │    └── tencent.html
│    └── END
│
├─── douban_spider
│    ├── 【xpath解析：实战-豆瓣电影爬虫之正在上映电影数据爬取】
│    │    └── main.py
│    └── END
│
├─── dytt_spider
│    ├──  实战-电影天堂爬虫 ->最新电影->前七页全部电影信息
│    │    ├── main.py
│    │    ├── dytt_spider.py  加入了写入excel表输出功能，修改版本
│    │    └── films_list.xls   导出的Excel表，记录了1-7页爬取下来电影信息
│    └── END
│
├─── Demo_BeautifulSoup
│    ├── BeautifulSoup笔记和CSS选择器在BeautifulSoup中的应用
│    │    ├── BeautifulSoup.ipynb
│    │    ├── BeautifulSoup_demo1.py
│    │    └── BeautifulSoup_demo2.py
│    └── END
│
├─── Demo_RegularExpression
│    ├── 正则表达式和re模块
│    │    ├── RE_demo1.py
│    │    ├── RE_demo2.py
│    │    └── RE_demo3.py
│    └── END
│
├─── Json_demo
│    ├── 数据存储-json文件处理
│    │    ├── main.py
│    │    ├── demo2.py
│    │    └── person.json
│    └── END
│
├─── CSV_demo
│    ├── 数据存储-CSV文件处理
│    │    ├── demo1.py   （读取csv文件-两种方式）
│    │    ├── demo2.py   （写入csv文件-两种方式）
│    │    └── classroom.csv
│    └── END
│
├─── MySQL_demo
│    ├── MySQL数据库操作
│    │    ├── demo1.py
│    │    ├── demo2.py
│    │    ├── demo3.py
│    │    └── demo4.py
│    └── END
│
├─── MongoDB_demo
│    ├── MongoDB数据库操作
│    │    ├── MongoDB数据库操作.ipynb
│    │    ├── MongoDB基本操作命令.ipynb
│    │    ├── Python操作MongoDB.ipynb
│    │    └── demo1.py
│    └── END
│
├─── Thread_demo
│    ├── 多线程爬虫
│    │    ├── demo1.py （threading模块）
│    │    ├── demo2.py （使用Thread类创建多线程）
│    │    ├── demo3.py （多线程共享全局变量以及锁机制）
│    │    ├── demo4.py （Lock版本生产者和消费者模式代码实现）
│    │    ├── demo5.py （Condition版的生产者与消费者模式）
│    │    ├── demo6.py （Queue线程安全队列）
│    │    ├── 多线程爬虫-threading模块.ipynb
│    │    ├── Lock版本生产者和消费者模式.ipynb
│    │    ├── Condition版的生产者与消费者模式.ipynb
│    │    ├── Queue线程安全队列.ipynb
│    │    └── GIL全局解释器锁.ipynb
│    └── END
│
├─── AJAX_demo
│    ├── 动态网页爬虫
│    │    ├── demo1.py （selenium + chromedriver）
│    │    ├──【动态网页爬虫】AJAX介绍.ipynb
│    │    └──【动态网页爬虫】Selenium.ipynb
│    └── END
│
├─── Scrapy-Redis_Demos
│    ├── Scrapy框架
│    │    ├── Scrapy框架架构.ipynb
│    │    ├── Scrapy快速入门.ipynb
│    │    ├── Dataflow.png
│    │    ├── Scrapy_Architecture.png
│    │    ├── qsbk 【项目实战】使用Scrapy框架爬取糗事百科
│    │    │    ├── 糗事百科之爬虫编写qsbk_spider
│    │    │    ├── 糗事百科之pipeline保存数据
│    │    │    └── 糗事百科多页面抓取
│    │    ├── 【项目】使用Scrapy框架爬取糗事百科段子.ipynb
│    │    ├── Scrapy笔记.jpg
│    │    ├── qsbk_spider.jpg
│    │    ├── CrawlSpider.ipynb
│    │    ├── wxapp 【项目实战】CrawlSpider实现微信小程序社区爬虫
│    │    ├── Scrapy Shell的使用
│    │    ├── Request和Response对象.ipynb
│    │    ├── renren_login 【项目实战】Scrapy模拟登录人人网
│    │    ├── douban_login 【项目实战】Scrapy模拟登录豆瓣网，自动识别豆瓣网验证码
│    │    ├── 下载文件和图片.ipynb  【项目实战】Scrapy框架下载汽车之家 参见项目Repository：Scrapy_autoHome
│    │    ├── Downloader Middlewares（下载器中间件讲解）
│    │    │    ├── Downloader Middlewares（下载器中间件）.ipynb
│    │    │    ├── 反爬虫-设置随机请求头（随机请求头中间件）
│    │    │    ├── 反爬虫-ip代理池（ip代理池中间件）
│    │    │    ├── 【项目实战】攻克BOSS直聘反爬虫之正常爬取 bossZhipin
│    │    │    └── 【项目实战】攻克BOSS直聘反爬虫之无限爬取 zhipin
│    │    └──【Scrapy框架】
│    └── END
│
├─── .idea
│
├─── .gitattributes
│
├─── README.md
│
└─── END
```


