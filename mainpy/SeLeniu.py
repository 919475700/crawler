from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
#最基本的使用小案例
browser = webdriver.Chrome() #声明浏览器对象
try:
    browser.get('https://www.baidu.com') #访问网址
    # browser.execute_script('document.getElementById("nr").value="50"')
    input = browser.find_element_by_id('kw') #通过ID查找元素
    input.send_keys('Python') #向元素输入内容
    input.send_keys(Keys.ENTER) #回车
    wait = WebDriverWait(browser,10)
    # 等待指定元素加载进来
    wait.until(ec.presence_of_all_elements_located((By.ID,'content_left')))
    #提取搜索引擎结果的核心代码（绝密）
    result=browser.find_elements_by_css_selector('#content_left .result.c-container .t')
    for r in result:
        print(r.text)
        print(r.find_element_by_css_selector('a').get_attribute('href'))
finally:
    browser.close()