# 行为链
#有时候在页面中的操作可能要有很多步，那么这时候可以使用鼠标行为链类ActionChains来完成。比如现在要将鼠标移动到某个元素上并执行点击事件
# 更多方法请参考：http://selenium-python.readthedocs.io/api.html

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')
submitBtn = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, 'Python')
actions.move_to_element(submitBtn)
actions.click(submitBtn)
actions.perform()


# click_and_hold(element)：点击但不松开鼠标。
# context_click(element)：右键点击。
# double_click(element)：双击。