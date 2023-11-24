# prototype for making GUI using tkinter
# tkinter GUI 구현을 도울 수 있는 가이드라인 입니다.

from tkinter import *

def filter1() : 
    # 선택한 필터의 이름을 global variable에 저장
    win2()
    
def filter2() : 
    # 선택한 필터의 이름을 global variable에 저장
    win2()
    
def filter3() : 
    # 선택한 필터의 이름을 global variable에 저장
    win2()
    
def filter4() : 
    # 선택한 필터의 이름을 global variable에 저장
    win2()
    
def exit() : 
    exit()
    
def win3() : 
    window4 = Tk()
    
    '''
    if shutter가 작동되면 : 
        현재 cv2 화면 캡처
        cv2 화면 종료'''
        
    l3 = Label(window4, text = "여기에 다양한 사진 편집 기능을 추가할 예정입니다.")
    l3.pack()
    
    exitbtn = Button(window4, text = "프로그램 종료", command = exit)
    exitbtn.pack()
    
def win2() : 
    window2 = Tk() 
    window3 = Tk()
    
    l1 = Label(window2, text = "실시간 웹캠이 될 화면입니다.")
    l1.pack()
    
    l2 = Label(window3, text = "사진을 촬영합니다.")
    l2.pack()
    
    shutter = Button(window3, text = "사진 촬영 버튼", command = win3)
    shutter.pack()
    
    

window1 = Tk()

l0 = Label(window1, text = "자신이 원하는 필터를 선택하세요")
l0.pack()

bt2 = Button(window1, text="필터 1", command=filter1)
bt2.pack()

bt3 = Button(window1, text="필터 2", command=filter2)
bt3.pack()

bt4 = Button(window1, text="필터 3", command=filter3)
bt4.pack()

bt5 = Button(window1, text="필터 4", command=filter4)
bt5.pack()
            
window1.mainloop()