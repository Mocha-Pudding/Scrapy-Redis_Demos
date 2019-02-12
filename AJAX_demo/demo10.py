# WebElement元素

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

submitBtn = driver.find_element_by_id('su')
print(type(submitBtn))
print(submitBtn.get_attribute("value"))
driver.save_screenshot('baidu.png')