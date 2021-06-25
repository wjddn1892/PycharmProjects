import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)   # soup 객체에서 처음으로 발견되는 a 태그 정보를 출력
# print(soup.a.attrs)  # a 태그의 속성 정보를 출력  딕셔너리 형태인듯
# print(soup.a["href"])   # a 태그의 href 속성 '값' 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))  # class="Nbtn_upload 인 a element를 찾아줘
# print(soup.find(attrs={"class": "Nbtn_upload"}))    # class="Nbtn_upload 인 어떤 element를 찾아줘

"""부모 형제 태그"""
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="여신강림-125화")
print(webtoon)