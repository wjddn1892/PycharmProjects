from tkinter import *

root = Tk()
root.title("My GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")    # padx, pady 는 text 에 의해 크기 변화됨
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn3 = Button(root, width=1, height=1, text="버튼4")  # width, height 는 고정된 크기
btn3.pack()

btn3 = Button(root, fg="red", bg="yellow", text="버튼3")
btn3.pack()

photo = PhotoImage(file="C:\\Users\\관리자\\PycharmProjects\\gui_basic\\img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()