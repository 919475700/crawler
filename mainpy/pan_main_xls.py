from lxml import etree
from pyquery import PyQuery as pq
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from mainpy.pan_main_config import *
from openpyxl import Workbook
#设置好chrome Headless模式，这样就不用浪费cpu渲染页面，提供效率
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)
wb = Workbook()
ws = wb.active
row = ['资源名称', '网盘网址']
ws.append(row)
wait = WebDriverWait(browser, 8)
print('一切开始了')
def search():
    try:
        print('开始搜索了')
        browser.get('http://pansou.com/?q={KEY}'.format(KEY=KEY_PAN))
        wait.until(
            ec.presence_of_element_located((
                By.CSS_SELECTOR,'#res')))
        get_products()
    except TimeoutException:
        return search()

def next_page(page_number):
    print('当前爬取到第{num}页了~~'.format(num=page_number))
    try:
        wait.until(
            ec.element_to_be_clickable((
                By.CSS_SELECTOR,'#res')))
        nextpage = browser.find_element_by_css_selector('.next')
        nextpage.click()
        wait.until(
            ec.presence_of_element_located((
                By.CSS_SELECTOR, '#res')))
        get_products()
    except TimeoutException:
        next_page(page_number)

def get_products():
    wait.until(ec.presence_of_element_located((
        By.CSS_SELECTOR, '#result')))
    html = browser.page_source
    doc = pq(etree.fromstring(html))
    items = doc('.g').items()
    for item in items:
        pan_url = pq(item.html()).find('a').attr('href')
        pan_name = pq(item.html()).find('a').text()
        print(pan_name)
        print(pan_url)
        save_to_excel(pan_name, pan_url)

def save_to_excel(pan_name,pan_url):
    myrows = [pan_name,pan_url]
    ws.append(myrows)

def main():
    try:
        search()
        for i in range(2, KEY_PAGE):
            next_page(i)
        wb.save(r'C:\Users\acer\Desktop\{name}.xlsx'.format(name=KEY_PAN))
    finally:
        browser.close()

if __name__ == '__main__':
    main()