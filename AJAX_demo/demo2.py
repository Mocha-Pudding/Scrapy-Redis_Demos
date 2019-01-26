# selenium常用操作

from selenium import webdriver
import time

driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")

time.sleep(5)

# driver.close()    #关闭当前页面。
driver.quit()    #退出整个浏览器。