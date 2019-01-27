# 定位元素

from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By

driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")

html = etree.HTML(driver.page_source)
html.xpath("")

# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element_by_name('wd')
# inputTag = driver.find_element_by_class_name('s_ipt')
# inputTag = driver.find_element_by_xpath("//input[@id='kw']")
inputTag = driver.find_element_by_css_selector(".quickdelete-wrap > input")
inputTag = driver.find_elements_by_css_selector(".quickdelete-wrap > input")[0]
inputTag = driver.find_elements(By.CSS_SELECTOR, ".quickdelete-wrap > input")[0]
print(inputTag)
inputTag.send_keys('python')    # 后续知识点 ：给输入框发送字符串

# 1.如果只是想解析网页中的数据，那么推荐将网页源代码扔给lxml来解析，因为lxml底层使用的是C语言，所以解析效率会更高。
# 2.如果是想要对元素进行一些操作，比如给一个文本框输入值，或是点击某个按钮，那么就必须使用selenium给我们提供的查找元素的方法。