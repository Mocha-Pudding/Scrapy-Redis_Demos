# 【BeautifulSoup库】bs4拾遗

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
<div>
我是div中的文本
</div>
<p><!-- 我是注释字符串 --></p>
"""

# 这是注释

from bs4.element import Tag
from bs4.element import NavigableString
from bs4.element import Comment
soup = BeautifulSoup(html,'lxml')
# print(type(soup))
# div = soup.find('div')
# print(type(div.string))
# p = soup.find('p')
# print(type(p.string))

div = soup.find('div')
print(div.contents)
print(type(div.contents))
print(type(div.children))

table = soup.find('tbody')
for element in table.contents:
    print(element)
    print('='*30)
