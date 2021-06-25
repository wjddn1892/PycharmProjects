""" openpyxl 전체 틀

from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])
ws1.append(["1", "2", "3"])

wb.save(filename='articles.xlsx')
"""

from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B6%94%EC%84%9D"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select("#main_pack > div.news.mynews.section._prs_nws > ul > li")

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

for article in articles:
    title = article.select_one("dl > dt > a").text
    url = article.select_one("dl > dt > a")["href"]
    comp = article.select_one("span._sp_each_source").text.split(" ")[0].replace("언론사", "")

    ws1.append([title, url, comp])

wb.save(filename='../articles.xlsx')
driver.quit()