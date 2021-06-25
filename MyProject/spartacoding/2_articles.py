from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B6%94%EC%84%9D"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select("#main_pack > div.news.mynews.section._prs_nws > ul > li")

for article in articles:
    title = article.select_one("dl > dt > a").text
    url = article.select_one("dl > dt > a")["href"]
    comp = article.select_one("span._sp_each_source").text.split(" ")[0].replace("언론사", "")
    print(title, url, comp)

driver.quit()