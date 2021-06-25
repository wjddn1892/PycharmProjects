import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

# 열기, 저장 파일 이름
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):    # 파일 있으면, True, 없으면 False
        with open(filename, "r", encoding="utf") as file:
            text.delete("1.0", END)
            text.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(text.get("1.0", END))    # 모든 내용을 가져와서 저장

# 메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기(O)", command=open_file)
menu_file.add_command(label="저장(S)", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기(X)", command=root.quit)
menu.add_cascade(label="파일(F)", menu=menu_file)

menu.add_cascade(label="편집(E)")
menu.add_cascade(label="서식(O)")
menu.add_cascade(label="보기(V)")
menu.add_cascade(label="도움말(H)")

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side="left", fill="both", expand=True)
# txt.insert(END, "")

scrollbar.config(command=text.yview)

root.config(menu=menu)

root.mainloop()