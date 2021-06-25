import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")    # 가로 * 세로

values = [str(i) + "일" for i in range(1, 32)]  # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, value=values)   # height 의 값만큼의 개수를 보여줌, 0과 END 이면 전체 다 보여줌
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목 설정 뿐 아니라 버튼 클릭을 통        한 값 설정도 가능

readonly_combobox = ttk.Combobox(root, height=10, value=values, state="readonly")    # 값 선택만 가능, 입력 불가
readonly_combobox.current(0)    # 초기 화면에서 0 번째 인덱스 값을 보여줌
readonly_combobox.pack()

def btncmd():
    print(combobox.get())   # 선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()