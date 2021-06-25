from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")    # 가로 * 세로

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")    # 현재는 값이 비어 있으므로 0 대신 END 를 입력해도 됨

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1번째 라인부터, 0번째 column 부터 가져와라! END 까지
    print(e.get())  # entry 글자도 출력

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()