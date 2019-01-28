# 操作表单元素

# 常见的表单元素：input type = 'text/password/email/number'
# button、input[type='submit']
# checkbox: input='checkbox'
# select：下拉列表


from selenium import webdriver

driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")

inputTag = driver.find_element_by_id('kw')    # 操作输入框
inputTag.send_keys('Python')