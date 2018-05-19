import re
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from mainpy.mongoconfig import *
import pymongo

client =pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
browser = webdriver.Chrome() #声明浏览器对象
wait = WebDriverWait(browser, 10)
def search():
    try:
        browser.get('https://www.taobao.com/')
        input = wait.until(
            ec.presence_of_element_located((
                By.CSS_SELECTOR,'#q')))
        input.send_keys('美食')
        submit = wait.until(
            ec.element_to_be_clickable((
                By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        submit.click()
        total = wait.until(ec.presence_of_element_located((
            By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutException:
        return search()
def next_page(page_number):
    try:
        input = wait.until(
            ec.presence_of_element_located((
                By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        submit = wait.until(
            ec.element_to_be_clickable((
                By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(ec.text_to_be_present_in_element((
            By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)

def get_products():
    wait.until(
        ec.presence_of_element_located((
            By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html=browser.page_source
    doc =pq(html)
    items =doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    try:
        if db[MONFO_TABLE].insert(result):
            print('保存成功',result)
    except Exception:
        print('保存失败',result)

def main():
    total =search()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2 , total + 1):
        next_page(i)
    browser.close()

if __name__ == '__main__':
    main()