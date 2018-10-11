# 【xpath解析：实战-豆瓣电影爬虫之正在上映电影数据爬取】

import requests
from lxml import etree

# 1.将目标网站上的页面抓取下来
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer':'https://movie.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'
response = requests.get(url,headers=headers)
text = response.text
# print(response.text)
# response.text:返回的是一个经过编码后的字符串，是str(unicode)类型
# response.content:返回的是一个原生的字符串，就是从网页上抓取下来的，没有经过处理的字符串，是bytes类型

# 2.将抓取下来的数据，根据一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
lis = ul.xpath("./li")
movies = []
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0]

    movie = {
        'title':title,
        'score':score,
        'duration':duration,
        'region':region,
        'director':director,
        'actors':actors,
        'thumbnail':thumbnail
    }

    movies.append(movie)

print(movies)