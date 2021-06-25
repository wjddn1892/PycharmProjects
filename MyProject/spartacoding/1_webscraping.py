# import dload
#
# dload.save("https://img.insight.co.kr/static/2020/02/20/700/5s0t60505a1t8m4pg22o.jpg")


# import dload
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
# driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
# time.sleep(2)   # 2초 동안 페이지 로딩 기다리기
#
# req = driver.page_source
# # HTML 을 BeautifulSoup 이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# # soup 이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
# soup = BeautifulSoup(req, 'html.parser')
#
# thumbnails = soup.select("#imgList > div > a > img")
#
# ###################################
# # 이제 여기에 코딩을 하면 됩니다!
# i = 1
# for thumbnail in thumbnails:
#     src = thumbnail["src"]
#     dload.save(src, f'img/{i}.jpg')
#     i += 1
# ###################################
#
# driver.quit() # 끝나면 닫아주기


import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%ED%8E%AD%EA%B7%84"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(url)
time.sleep(2)

soup = BeautifulSoup(browser.page_source, "lxml")

thumbnails = soup.select("#imgList > div > a > img")    # copy selector

for index, thumbnail in enumerate(thumbnails):
    src = thumbnail["src"]
    dload.save(src, f"imgs_homework/{index + 1}.jpg")

browser.quit()