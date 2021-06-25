# f = open("test.txt", "w", encoding="utf-8")
# for i in [1, 2, 3, 4, 5]:
#     f.write(f"{i}번째 줄이에요\n")
# f.close()

# with open("test.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# text = ""
# with open("kakaotalk.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     for line in lines:
#         text += line
#
# print(text)


# 폰트 찾기
# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)



# from wordcloud import WordCloud
#
# text = ""
# with open("kakaotalk.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     for line in lines:
#         if "] [" in line:
#             text += line.split("] ")[2].replace("ㅋ", "").replace("이모티콘\n", "").replace("사진\n", "").replace("ㅜ", "").replace("ㅠ", "").replace("ㅎ", "")
#
# # print(text)
#
# wc = WordCloud(font_path="C:\\Windows\\Fonts\\NEXONFootballGothicB.ttf", background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")




from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if "] [" in line:
            text += line.split("] ")[2].replace("ㅋ", "").replace("이모티콘\n", "").replace("사진\n", "").replace("ㅜ", "").replace("ㅠ", "").replace("ㅎ", "")\
            .replace("근데", "").replace("지금", "").replace("너무", "").replace("이제", "").replace("내가", "").replace("진짜", "")

# print(text)

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path="C:\\Windows\\Fonts\\NEXONFootballGothicB.ttf", background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")