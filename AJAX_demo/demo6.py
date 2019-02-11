# Cookie操作

from selenium import webdriver

driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

#获取所有的cookie
for cookie in driver.get_cookies():
    print(cookie)

print('=' * 30)

#根据cookie的key获取value
print(driver.get_cookie("PSTM"))

#删除某个cookie：
driver.delete_cookie("PSTM")
print('=' * 30)
print(driver.get_cookie("PSTM"))

#删除所有的cookie：
driver.delete_all_cookies()