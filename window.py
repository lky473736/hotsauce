'''from tkinter import *
from SoHot.library import get_button
from SoHot.library import getImage

def win3(): # 사용자가 촬영 버튼을 누르면, 윈도우3을 열어 편집 기능 선택 가능하도록 도움

    window2 = Tk()
    window2.configure(bg="white")
    window2.title("Image Editor")
    #window2.geometry("1600x800")

    l3 = Label(window2, text="사진 편집기") #윈도우 title
    l3.pack()
    
    load_button = Button(window2, text="내 이미지 불러오기", width=15, height=2) #이미지를 불러오는 버튼 생성
    load_button.pack()


    frame = Frame(window2)

    get_button(frame)  #버튼 프레임을 불러옵니다.
    getImage(frame) #이미지를 보여준다.

    frame.pack()

    window2.mainloop()

win3()
'''