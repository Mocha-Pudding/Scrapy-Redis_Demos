# re模块中的常用函数

import re

# 分组
text = "apple's price is $99, orange's price is $10"
ret = re.search('.*(\$\d+).*(\$\d+)', text)
print(ret.group(0))
# ret.group(0) = ret.group()
# print(ret.group(1))
# print(ret.group(2))
print(ret.group(1,2))
# 所有的子分组都拿出来
print(ret.groups())

# find_all函数：
text = "apple's price is $99, orange's price is $10"
ret = re.findall('\$\d+',text)
print(ret)

# sub函数：用来替换字符串
text = "apple's price is $99, orange's price is $10"
ret = re.sub('\$\d+','20',text)
print(ret)

html = """
<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div>
        <p>岗位职责：</p>
<p>1、负责公司量化交易平台的设计和开发维护</p>
<p>2、平衡需求复杂度和技术可行性，参与项目需求评估和优化设计</p>
<p>3、协助技术负责人提高团队的代码质量和工作效率，营造技术氛围</p>
<p><br></p>
<p>岗位优势：</p>
<p>1、量化策略团队实力雄厚，由知名985高校的<strong>博士</strong>、<strong>硕</strong>士组成的年轻而有活力的团队，部分成员来自<strong>百亿级</strong>私募，有丰富的大资金操作经验，能够大大拓客业务视野，更好地实现技术变现；</p>
<p>2、团队扁平，推崇<strong>创业</strong>、<strong>共赢</strong>的理念，邀请优秀的你加入我们，一起变得更好。</p>
<p><br></p>
<p>&nbsp;</p>
<p>职位要求:</p>
<p>1、1年以上Python经验，熟悉Django, Tornado, Flask框架中的至少一种，熟悉Web后端架构</p>
<p>2、熟悉Linux平台环境的开发，掌握Linux常用命令</p>
<p>3、熟悉python网络编程，能够设计和维护基于TCP/IP协议的高性能事件驱动框架程序</p>
<p>4、熟悉mysql、mongodb、redis等数据库使用</p>
<p>5、掌握基于WebSoceket的单页应用的开发思想和技术栈</p>
<p>&nbsp;</p>
<p>有下列经验的加分</p>
<p>1、有zeromq或者其他RPC框架的实际项目经验加分</p>
<p>2、有<strong>Docker Swarm</strong>、<strong>K8S</strong>等项目实际经验优先</p>
<p>3、有大型分布式websocket项目经验优先</p>
<p><br></p>
<p>我们将为您提供：</p>
<p>0、终身快速科学上网服务（全球各地有SS节点），<strong>机房专线</strong>直达办公室</p>
<p>1、薪资：我们提供行业内有竞争力的薪酬；（BTW: 试用期是 <strong>100%</strong>薪资）</p>
<p>2、奖金+提成：优秀的您可以共享公司的经营业绩，直接每月兑现公司总销售利润；</p>
<p>3、基本保障福利：公司按照国家规定为员工实额缴纳社会保险；</p>
<p>4、额外补充福利：</p>
<p>* 晋升加薪类：每年有超过行业平均的加薪幅度；</p>
<p>* 礼金礼品类: 过节费、各类礼金等；</p>
<p>* 员工关怀类: “家人生日会“(程序猿/媛的生日可以更加丰富多彩的）</p>
<p>* 团队建设类：团队月度“腐败”活动+“每天充足的零食”+<strong>设备补贴</strong>（以补贴一个15寸高配rMBP的价格来每月返还）</p>
<p>* 年度旅游+自由度大+提升空间大+快速成长期，等等!来了你就知道！</p>
<p><br></p>
<p>注意，团队马上进驻天河区<strong>珠江新城富力盈丰</strong>大厦，目前面试地点在<strong>番禺节能科技园总部中心2号楼1903</strong>。</p>
        </div>
    </dd>    
"""

ret = re.sub('<.+?>','',html)
print(ret)

# split函数：分割字符串
text = "hello world my&December"
ret = re.split(' |&',text)
print(ret)

# compile函数:
text = "the number is 20.50"
# r = re.compile('\d+\.?\d*')
# ret = re.search(r,text)
# print(ret.group())
r = re.compile(r"""
    \d+ # 小数点前面的数字
    \.? # 小数点本身
    \d  # 小数点后面的数字
""", re.VERBOSE)
ret = re.search(r, text)
print(ret.group())