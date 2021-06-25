import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=top_sug.pre&fbm=1&acr=1&acq=%EC%84%9C%EC%9A%B8+%EB%82%A0&qdt=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

print("[오늘의 날씨]")
wtr_state = soup.find("p", attrs={"class":"cast_txt"}).get_text()
temp = soup.find("span", attrs={"class":"todaytemp"}).get_text()
temp_min = soup.find("span", attrs={"class":"min"}).get_text()
temp_max = soup.find("span", attrs={"class":"max"}).get_text()
print(wtr_state)
print("현재", temp, "℃", "( 최저", temp_min, "/ 최고", temp_max, ")")

today_info = soup.find("li", attrs={"class":"date_info today"}).get_text()
today_info_lst = today_info.split()
print("오전", today_info_lst[2], today_info_lst[3], "/ 오후", today_info_lst[4], today_info_lst[5])

indicator = soup.find("dl", attrs={"class":"indicator"}).get_text()
indicator_lst = indicator.split()
print(indicator_lst[0], indicator_lst[1])
print(indicator_lst[2], indicator_lst[3])

url = "https://news.naver.com/"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

titles = soup.find_all("div", attrs={"class":"hdline_article_tit"})
for title in titles:
    print(title)