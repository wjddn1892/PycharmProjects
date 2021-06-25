#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

# with urlopen('https://www.naver.com/') as response: 아래 코드와 같음
response = urlopen('https://www.naver.com/')
soup = BeautifulSoup(response, 'html.parser')
for anchor in soup.select("span.keyword"):
    print(anchor.get_text())