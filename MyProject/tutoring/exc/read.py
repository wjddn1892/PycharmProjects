a = "https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=055&aid=0000779947&date=20191220&type=2&rankingSeq=1&rankingSectionId=100"

oid = print(a.split('oid=')[1].split('&')[0])
aid = print(a.split('aid=')[1].split('&')[0])