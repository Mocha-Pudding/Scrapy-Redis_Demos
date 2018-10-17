#使用CSS选择器 在BeautifulSoup中的应用

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

# 实现以下需求(Select方法:使用CSS选择器)
# 1.获取所有的tr标签
# 2.获取第2个tr标签
# 3.获取所有class等于even的tr标签
# 4.获取所有的a标签的href属性
# 5.获取所有的职位信息（纯文本）

soup = BeautifulSoup(html,'lxml')

# 1.获取所有的tr标签
# trs = soup.select("tr")
# for tr in trs:
#     print(tr)
#     print(type(tr))
#     print("="*60)

# 2.获取第2个tr标签
# tr = soup.select('tr')[1]
# print(tr)

# 3.获取所有class等于even的tr标签
# trs = soup.select("tr.even")
# trs = soup.select("tr[class='even']")
# for tr in trs:
#     print(tr)

# 4.获取所有的a标签的href属性
# aList = soup.select('a')
# for a in aList:
#     href = a['href']
#     print(href)

# 5.获取所有的职位信息（纯文本）
trs = soup.select('tr')[1:]
print(type(trs))
for tr in trs:
    infos = list(tr.stripped_strings)
    print(infos)