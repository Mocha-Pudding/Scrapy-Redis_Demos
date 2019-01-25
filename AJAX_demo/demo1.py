# selenium + chromedriver

from selenium import webdriver

# chromedriver的绝对路径
driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"

# 初始化一个driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)

# 请求网页
driver.get('https://cn.bing.com/')

# 通过page_source获取网页源代码
print(driver.page_source)