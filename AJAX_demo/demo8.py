# 页面切换

from selenium import webdriver

driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

#### 借助JavaScript语句打开一个新的页面
driver.execute_script("window.open('https://www.douban.com/')")   #JavaScript语句

print(driver.window_handles)
print('1====>>', driver.current_url)

#### 切换到新的页面中
driver.switch_to_window(driver.window_handles[1])

print('2====>>', driver.current_url)
print(driver.page_source)

# 虽然在窗口中切换到了新的页面，但是driveer中还没有切换
# 如果想要在代码中切换到新的页面，并且做一下爬虫
# 那么应该使用driver.switch_to_window来切换到指定的窗口
# 从driver.window_handles中取出具体第几个窗口
# driver.window_handles是一个列表，里面装的都是窗口句柄
# 它会按照打开页面的顺序来存储窗口的句柄