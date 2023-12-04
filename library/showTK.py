# tkinter를 사용한 GUI 구현 함수들을 모은 라이브러리

#from tkinter import *
from tkinter import Tk, Label, Frame, Entry, Button, PhotoImage
from PIL import Image, ImageTk  # PIL 모듈을 사용하여 이미지를 읽어옴



##########이미지 불러오기
''''img.jpg'는 global 변수로 대응시킬 예정이라서 더욱이 각 기능마다 parameter는 필요 없습니다.'''

def getImage(window2):
    imgFrame = Frame(window2)
    
    # PIL 모듈을 사용하여 이미지를 읽어옴
    img_pil = Image.open('img.jpg')
    img_tk = ImageTk.PhotoImage(img_pil)

    # Label 위젯에 이미지 설정
    edit_image = Label(imgFrame, image=img_tk)
    edit_image.image = img_tk 
    edit_image.pack()

    imgFrame.pack(side="left")



############# 버튼 중 값을 받기 위한 entry생성, callback에는 value가 필요한 편집 기능을 가져오는 버튼을 불러오는 함수를 입력.
def get_entry(type, callback): #
    
    entry_window = Tk()  # 안내 윈도우
    entry_label = None  # entry_label 변수를 미리 선언

    if type=="change_size":
        entry_label =Label(entry_window, text="변경 사이즈를 입력하세요: ")
    
    elif type=="rotate":
        entry_label =Label(entry_window, text="angle을 입력하세요: ")
    
    elif type=="symmetric":
        entry_label =Label(entry_window, text="양수라면 좌우 대칭, 음수면 상하 대칭 : ")

    if entry_label:  # entry_label이 정의된 경우에만 pack
        entry_label.pack()

    entry = Entry(entry_window)
    entry.pack()

    def get_value():
        value = int(entry.get())
        callback(value) #entry에서 받은 값을 callback함수에 전달
        entry_window.destroy() #윈도우 닫음

    submit_button = Button(entry_window, text="확인", command=get_value) #버튼에 entry에서 받은 값을 전달
    submit_button.pack()

    entry_window.mainloop()


##################### 버튼 구현
def get_button(window2):

    f_button = Frame(window2)

    # 버튼 공통 속성 설정
    button_width = 15
    button_height = 2

    # 편집 버튼들
    grayscale_button = Button(f_button, text="흑백", width=button_width, height=button_height, command=grayscale, fg="gray", bg="white")
    grayscale_button.pack()

    size_button = Button(f_button, text="사이즈 변경", width=button_width, height=button_height, command=get_entry("change_size", change_size))
    size_button.pack()

    rotate_button = Button(f_button, text="이미지 회전", width=button_width, height=button_height, command=get_entry("rotate", rotate))
    rotate_button.pack()

    symmetric_button = Button(f_button, text="좌우/상하 대칭", width=button_width, height=button_height, command=get_entry("symmetric", symmetric))
    symmetric_button.pack()

    contour_button = Button(f_button, text="이미지 윤곽선", width=button_width, height=button_height, command=contour, )
    contour_button.pack()

    boundaryrect_button = Button(f_button, text="객체 윤곽선", width=button_width, height=button_height, command=boundaryrect)
    boundaryrect_button.pack()

    # 프레임을 윈도우에 팩
    f_button.pack(side="left")

win3()