from bs4 import BeautifulSoup

html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=41297&amp;keywords=Python&amp;tid=87&amp;lid=2196">WXG10-143 企业微信后台安全策略工程师（广州）</a>
            </td>
            <td>技术类</td>
            <td>1</td>
            <td>广州</td>
            <td>2018-10-16</td>
        </tr>
		<tr class="odd">
		    <td class="l square"><a target="_blank" href="position_detail.php?id=41031&amp;keywords=Python&amp;tid=87&amp;lid=2196">CSIG08-图像识别高级研究员（广州/北京）</a><span class="hot">&nbsp;</span></td>
            <td>技术类</td>
            <td>5</td>
            <td>广州</td>
            <td>2018-10-16</td>
        </tr>
		<tr class="even">
		    <td class="l square"><a target="_blank" href="position_detail.php?id=40569&amp;keywords=Python&amp;tid=87&amp;lid=2196">CSIG08-NLP算法研究（广州/北京）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>广州</td>
            <td>2018-10-16</td>
        </tr>
		<tr class="odd">
		    <td class="l square"><a target="_blank" href="position_detail.php?id=40169&amp;keywords=Python&amp;tid=87&amp;lid=2196">WXG01-117 微信Android客户端开发工程师（广州）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>广州</td>
            <td>2018-10-16</td>
        </tr>
		<tr class="even">
		    <td class="l square"><a target="_blank" href="position_detail.php?id=39973&amp;keywords=Python&amp;tid=87&amp;lid=2196">WXG01-113 微信后台开发工程师（广州）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>广州</td>
            <td>2018-10-16</td>
        </tr>
		<tr class="odd">
		    <td class="l square"><a target="_blank" href="position_detail.php?id=39885&amp;keywords=Python&amp;tid=87&amp;lid=2196">WXG10-143 企业微信后台策略安全高级工程师（广州）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>广州</td>
            <td>2018-10-16</td>
        </tr>
		<tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=39858&amp;keywords=Python&amp;tid=87&amp;lid=2196">WXG03-122 小程序算法工程师（广州）</a></td>
            <td>技术类</td>
            <td>3</td>
            <td>广州</td>
            <td>2018-10-16</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=39784&amp;keywords=Python&amp;tid=87&amp;lid=2196">CSIG08-推荐算法工程师（广州）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>广州</td>
            <td>2018-10-16</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=38309&amp;keywords=Python&amp;tid=87&amp;lid=2196">WXG01-117 微信iOS客户端开发工程师（广州）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>广州</td>
            <td>2018-10-16</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a id="test" class="test" target="_blank" href="position_detail.php?id=38311&amp;keywords=Python&amp;tid=87&amp;lid=2196">WXG01-122 微信数据挖掘工程师（广州）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>广州</td>
            <td>2018-10-16</td>
        </tr>
    </tbody>
</table>
"""

# python => C
# bs4 => lxml
# bs = BeautifulSoup(html,"lxml")
# print(bs.prettify())

# 实现以下需求
# 1.获取所有的tr标签
# 2.获取第2个tr标签
# 3.获取所有class等于even的tr标签
# 4.将所有id等于test，class也等于test的a标签提取出来
# 5.获取所有的a标签的href属性
# 6.获取所有的职位信息（纯文本）

soup = BeautifulSoup(html, 'lxml')

# 1.获取所有的tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print('='*30)

# 2.获取第2个tr标签
# tr = soup.find_all('tr',limit=2)[1]
# print(tr)

# 3.获取所有class等于even的tr标签
# # trs = soup.find_all('tr',class_='even')
# trs = soup.find_all('tr',attrs={'class':"even"})   #attribute 满足哪些属性
# for tr in trs:
#     print(tr)
#     print('=' * 60)

# 4.将所有id等于test，class也等于test的a标签提取出来
# aList = soup.find_all('a',id='test',class_='test')  #多个条件筛选，也可通过attrs
# aList = soup.find_all('a',attrs={'id':"test",'class':"test"})
# for a in aList:
#     print(a)

# 5.获取所有的a标签的href属性
# aList = soup.find_all('a')
# for a in aList:
#     # 1. 通过下标操作的方式
#     # href = a['href']
#     # print(href)
#
#     # 2. 通过attrs属性的方式
#     # href = a.attrs['href']
#     # print(href)

# 6.获取所有的职位信息（纯文本）
trs = soup.find_all('tr')[1:]
jobs = []
for tr in trs:
    job = {}
    # tds = tr.find_all('td')
    # # print(tds)
    #
    # title = tds[0].string
    # category = tds[1].string
    # nums = tds[2].string
    # city = tds[3].string
    # pubtime = tds[4].string
    #
    # job['title']=title
    # job['category']=category
    # job['nums']=nums
    # job['city']=city
    # job['pubtime']=pubtime
    #
    # # job = {
    # #     'title':title,
    # #     'category':category,
    # #     'nums':nums,
    # #     'city':city,
    # #     'pubtime':pubtime,
    # # }
    # jobs.append(job)

    infos = list(tr.stripped_strings)   # stripped_strings 获取非空白的字符
    job['title']=infos[0]
    job['category'] = infos[1]
    job['nums'] = infos[2]
    job['city'] = infos[3]
    job['pubtime'] = infos[4]
    jobs.append(job)

print(jobs)