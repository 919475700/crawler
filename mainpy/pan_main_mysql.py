from lxml import etree
import time
from pyquery import PyQuery as pq
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from mainpy.pan_main_config import KEY_PAN,KEY_PAGE
import pymysql
db = pymysql.connect("127.0.0.1","root","qaz159753","sns",use_unicode=True, charset="utf8")
cursor = db.cursor()
#设置好chrome Headless模式，这样就不用浪费cpu渲染页面，提供效率
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 10)
def search():
    try:
        browser.get('https://www.57fx.com/search/')
        input = wait.until(
            ec.presence_of_element_located((
                By.CSS_SELECTOR,'#searchWord')))
        input.send_keys(KEY_PAN)
        submit = wait.until(
            ec.element_to_be_clickable((
                By.CSS_SELECTOR, 'body > div.main > div.header_resize > div.index_header > div.searchform > form > input.button_search')))
        submit.click()
        get_products()
        # 执行sql语句
        db.commit()
        return
    except TimeoutException:
        return search()
def next_page(page_number):
    print('当前爬取到第{num}页了~~'.format(num=page_number))
    try:
        browser.get('https://www.57fx.com/search-all-{key}-{page_number}/'.format(key=KEY_PAN,page_number=page_number))
        get_products()
        # 执行sql语句
        db.commit()
    except TimeoutException:
        next_page(page_number)

def get_products():
    wait.until(ec.presence_of_element_located((
        By.CSS_SELECTOR, 'body > div.main > div.fbg > div > div.content.col.c_r > div.content_file')))
    html=browser.page_source
    doc = pq(etree.fromstring(html))
    items =doc('.c_fn').items()
    for item in items:
        urls = pq(item.html().replace('xmlns', 'we')).find('a').attr('href')
        pan_name =pq(item.html().replace('xmlns', 'we')).find('a').text()
        if urls != None:
            browser.get('%s%s' % ('https://www.57fx.com',urls))
            wait.until(ec.presence_of_element_located((
                By.CSS_SELECTOR, 'body > div.main > div.fbg > div > div.content.col.c_r')))
            one_html = browser.page_source
            r = pq(etree.fromstring(one_html))
            pan_url = r('.toyunDown').attr('href')
            browser.execute_script('window.history.back(-1)')
            save_to_mysql(pan_name, pan_url)


def save_to_mysql(pan_name,pan_url):
    try:
        # 执行sql语句
        pan_url_spit = pan_url[23:]
        sql = """insert into pan values(0,'{a}','{b}')""".format(a=pan_name, b=pan_url_spit)
        cursor.execute(sql)

    except:
        # 发生错误时回滚
        db.rollback()

def main():
    start = time.clock()
    try:
        search()
        for i in range(2 , KEY_PAGE):
            next_page(i)
    finally:
        browser.close()
        cursor.close()
        db.close()
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))

if __name__ == '__main__':
    main()