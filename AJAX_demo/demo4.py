# 操作表单元素

# 常见的表单元素：input type = 'text/password/email/number'
# button、input[type='submit']
# checkbox: input='checkbox'
# select：下拉列表


################ 操作输入框 ################
# from selenium import webdriver
# import time
#
# driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.baidu.com/")
#
# inputTag = driver.find_element_by_id('kw')    # 操作输入框
# inputTag.send_keys('Python')
#
# time.sleep(3)
#
# inputTag.clear()    #清除输入框中的内容


################ 操作CheckBox ################
# from selenium import webdriver
# import time
#
# driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("https://accounts.douban.com/passport/login")
#
# rememberBtn = driver.find_element_by_name('remember')    # 操作checkbox
# time.sleep(3)
# rememberBtn.click()
#
# time.sleep(5)
# rememberBtn.click()


################ 操作select标签 ################
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("http://ssci.whut.edu.cn/")
#
# selectBtn = Select(driver.find_element_by_name('select2'))   # 操作select标签
# # selectBtn.select_by_index(2)
# # selectBtn.select_by_value('mailto:lxyzsm@whut.edu.cn')
# # selectBtn.select_by_visible_text('学校首页')
# # selectBtn.deselect_all()


################ 操作按钮 ################
from selenium import webdriver

driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://cn.bing.com/")

inputTag = driver.find_element_by_id('sb_form_q')    # 操作输入框
inputTag.send_keys('Leica M2')

submitTag = driver.find_element_by_id('sb_form_go')
submitTag.click()
