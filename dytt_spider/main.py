# 实战-电影天堂爬虫 ->最新电影->前七页全部电影信息

from lxml import etree
import requests

BASE_DOMIN = 'http://www.dytt8.net'
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

def get_detail_urls(url):
    response = requests.get(url,headers=HEADERS)
    #response.text
    #response.content
    #requests库，默认会使用自己猜测的编码方式将抓取下来的网页进行编码，然后存储到text属性上去
    #在电影天堂的网页中，因为编码方式，requests库猜错了，所以就会产生乱码
    # text = response.content.decode('gbk')
    # print(response.encoding)
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    # for detail_url in detail_urls:
    #     print(BASE_DOMIN + detail_url)
    detail_urls = map(lambda url:BASE_DOMIN + url, detail_urls)
    #上面lambda函数相当于一个匿名函数，等价于下面表达式：
    # def abc(url):
    #     return BASE_DOMIN + url
    # index = 0
    # for detail_url in detail_urls:
    #     detail_url = abc(detail_url)
    #     detail_urls[index] = detail_url
    #     index += 1
    return detail_urls

def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title  #电影标题

    zoomElement = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomElement.xpath(".//img/@src")
    poster = imgs[0]  #电影海报
    screenshot = imgs[1]  #电影截图
    movie['poster'] = poster
    movie['screenshot'] = screenshot

    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    infos = zoomElement.xpath(".//text()")
    # for info in infos:
    for index, info in enumerate(infos):
        # print(info)
        # print(index)
        # print('-'*30)
        if info.startswith("◎年　　代"):
            # info = info.replace("◎年　　代","").strip()
            info = parse_info(info,"◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            # info = info.replace("◎产　　地","").strip()
            info = parse_info(info,"◎产　　地")
            movie['contry'] = info
        elif info.startswith("◎类　　别"):
            # info = info.replace("◎类　　别", "").strip()
            info = parse_info(info,"◎类　　别")
            movie['category'] = info
        elif info.startswith("◎IMDb评分"):
            info = parse_info(info,"◎IMDb评分")
            movie['IMDb_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info,"◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info,"◎导　　演")
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info,"◎主　　演")
            actors = [info]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                if profile.startswith('【下载地址】'):
                    break
                movie[profile] = profile
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie

1
def spider():
    base_url = "http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    #获取1-7页的电影 用for循环来遍历
    for x in range(1,8):
        #第一个for循环是用来控制总共有7页
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            #第二个for循环是用来遍历一页中所有电影的详情url
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movies)
    # print(movies)

if __name__ == "__main__":
    spider()