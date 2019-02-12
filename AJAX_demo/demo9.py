# 设置代理ip
# 快代理 www.kuaidaili.com
# httpbin.org

from selenium import webdriver

driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://116.209.59.70:9999")   #代理的ip地址和对应的端口号

driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)

driver.get("http://httpbin.org/ip")
