# 页面等待

####################### 隐式等待 #######################
# from selenium import webdriver
#
# driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.douban.com/')
#
# driver.implicitly_wait(5)  #隐式等待
#
# driver.find_element_by_id("dsfkdjkdsfkld")


####################### 显式等待 #######################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://accounts.douban.com/passport/login')

element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,"tmpl_phone"))
)
print(element)