from tkinter import *

root = Tk()
root.title("정우의 퀴즈")
root.geometry("640x480")    # 가로 * 세로

label1 = Label(root, text="안녕하세요 저를 사랑하시나요?")
label1.pack()

photo = PhotoImage(file="C:\\Users\\관리자\\PycharmProjects\\gui_basic\\question.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="저도 사랑해요❤")

    global photo2   # 함수 내에서 label 의 이미지 값을 바꾸기 위해 전역변수로 선언해야함
    photo2 = PhotoImage(file="C:\\Users\\관리자\\PycharmProjects\\gui_basic\\heart.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()