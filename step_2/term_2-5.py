import cv2
import mediapipe as mp
from tkinter import * 

# win1 : 필터 선택
# win2 : 웹캠
# win3 : 편집기능 구현

def filter1() : 
    # 선택한 필터의 이름을 global variable에 저장
    win2('cat')
    
def filter2() : 
    # 선택한 필터의 이름을 global variable에 저장
    win2('dog')
    
def filter3() : 
    # 선택한 필터의 이름을 global variable에 저장
    win2('pig')
    
def filter4() : 
    # 선택한 필터의 이름을 global variable에 저장
    win2('sunglass')
    
def grayscale () : # 임규연 구현 부분
    '''
    흑백 기능을 구현
    '''
    img_gray = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow ('img_gray', img_gray)
    
    
def change_size () : # 임규연 구현 부분
    '''
    사이즈 조절 기능을 구현 
    '''
    
    size = float(entry1.get()) # 여기서 entry1은 win3에서의 entry입니다.
    
    img_ori = cv2.imread(name)
    img_dst = cv2.resize(img_ori, None, fx = size, fy = size)
    
    cv2.imshow(f'img_dst = {size}', img_dst)
    
    
def rotate () : # 임규연 구현 부분
    '''
    이미지 회전 기능을 구현 
    '''
    
    angle = float(entry1.get()) # 여기서 entry1은 win3에서의 entry입니다.
    
    img_ori = cv2.imread('img.jpg')
    
    if angle == 90 :
        img_rot = cv2.rotate(img_ori, cv2.ROTATE_90_CLOCKWISE)
        
    else :
        img_rot = cv2.rotate(img_ori, cv2.ROTATE_180)
        
    cv2.imshow(f'img_rot = {angle}', img_rot)
    
def symmetric () : # 임규연 구현 부분
    '''
    좌우/상하 대칭 기능을 구현 
    양수면 좌우대칭
    음수면 상하대칭
    '''
    
    value = int(entry1.get()) # 여기서 entry1은 win3에서의 entry입니다.
    
    img_ori = cv2.imread('img.jpg')
    
    if value < 0 : 
        flip = cv2.flip(img_ori, 0) # 무슨 이미지를, flipcode
    
    else :
        flip = cv2.flip(img_ori, 1) # 무슨 이미지를, flipcode
    
    cv2.imshow ('flip', flip)
    
def contour () : # 임규연 구현 부분
    '''
    이미지 윤곽선 검출 기능을 구현 
    '''
    
    img_ori = cv2.imread('img.jpg')
    
    gray = cv2.cvtColor (img_ori, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # 윤곽선 검출

    COLOR = (0, 256, 0)
    cv2.drawContours(img_ori, contours, -1, COLOR, 2) # 윤곽선 그리기
    
    cv2.imshow('contour', img_ori)
    
def boundaryrect () : # 임규연 구현 부분
    '''
    객체 윤곽선 사각형 검출 기능을 구현 
    '''
    
    img_ori = cv2.imread('img.jpg')
    
    gray = cv2.cvtColor (img_ori, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # 윤곽선 검출

    COLOR = (0, 256, 0)
    
    for cnt in contours :
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(img_ori, (x, y), (x + width, y + height), COLOR, 2) # 왼쪽위, 오
    
    cv2.drawContours(img_ori, contours, -1, COLOR, 2) # 윤곽선 그리기
    
    cv2.imshow('boundaryrect', img_ori)
    
def exit() : 
    exit()
    
############################################### 정예지 구현 파트
    
def win3() : 
    window2 = Tk()   
    window2.configure(bg="lightsalmon")

    ######### window3의 타이틀
    l3 = Label(window2, text = "<사진 편집 윈도우>",  bg="lightsalmon", height= 3)
    l3.pack()

    ########### 값을 받는 엔트리 프레임
    value_f = Frame(window2) 

    entry_l = Label(value_f, text="값을 입력하세요 : ",  bg="lightsalmon")
    entry = Entry(value_f, fg="beige" ,bg="lightsalmon", width=10) #사용자에게 값을 입력받는 엔트리 생성

    entry_l.pack(side=LEFT)
    entry.pack(side=LEFT)

    value_f.pack()


    ########### 현재 나의 이미지 표시
    your_img = PhotoImage(file=r"C:\Users\82108\Desktop\closeSW\SoHot\step_2\pig.png") #임시로 사진 주소 설정하였습니다. 전역객체로 변경해주세요.
    show_img= Label(window2, image=your_img)
    show_img.pack()

    ############ 버튼
    f_button = Frame(window2) 

    # 버튼 공통 속성 설정
    button_width = 15
    button_height = 2


    grayscale_button = Button(f_button, text="흑백", width=button_width, height=button_height, command=grayscale, fg="slateblue", bg="beige")
    size_button = Button(f_button, text="사이즈 변경", width=button_width, height=button_height, command=change_size, fg="mintcream", bg="hotpink")
    rotate_button = Button(f_button, text="이미지 회전", width=button_width, height=button_height, command=rotate,fg="slateblue", bg="beige")
    symmetric_button = Button(f_button, text="좌우/상하 대칭", width=button_width, height=button_height, command=symmetric, fg="mintcream", bg="hotpink")
    contour_button = Button(f_button, text="이미지 윤곽선", width=button_width, height=button_height, command=contour,fg="slateblue", bg="beige")
    boundaryrect_button = Button(f_button, text="객체 윤곽선", width=button_width, height=button_height, command=boundaryrect,fg="mintcream", bg="hotpink")
    
    grayscale_button.pack()
    size_button.pack()
    rotate_button.pack()
    symmetric_button.pack()
    contour_button.pack()
    boundaryrect_button.pack()

    f_button.pack(side="left") # 프레임을 윈도우에 팩

    window2.mainloop()

    
################################################

#필터를 화면에 오버레이하는 함수
def overlay(image, x, y, w, h, overlay_image):
    # 이미지 배열의 크기를 벗어나는지 체크
    if x - w < 0 or x + w > image.shape[1] or y - h < 0 or y + h > image.shape[0]:
        return

    # 오버레이할 이미지 크기를 조절
    overlay_image_resized = cv2.resize(overlay_image, (w * 2, h * 2))  # 크기를 (w * 2, h * 2)로 조절
    for c in range(0, 3):  # channel BGR
        image[y - h : y + h, x - w : x + w, c] = (
            overlay_image_resized[:, :, c] * (overlay_image_resized[:, :, 3] / 255.0) +
            image[y - h : y + h, x - w : x + w, c] * (1.0 - overlay_image_resized[:, :, 3] / 255.0)
        )

#이미지 배경 투명 함수
def remove_grabcut_bg(image):
    tmp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    r, g, b, a = cv2.split(image)
    rgba = [r, g, b, alpha]
    dst = cv2.merge(rgba, 4)
    return dst

#카메라 송출, 필터를 씌우고 촬영하는 창
def win2(filter_name) : # 유호찬, 임남령, 임규연, 정예지 구현 부분
    '''
        윈도우2에선 사용자의 얼굴을 인식하는 부분, 필터를 덧대는 부분, 촬영하는 부분으로 나눠져야 할 것입니다.
        촬영은 곧 웹캠의 한 프레임을 저장하는 기능이 됩니다.
        파일명을 'img.jpg'로 저장하게끔 할 예정이고, 그 파일명을 global 변수로 만들 예정입니다.
    '''
    #딕셔너리로 필터 이름에 따른 변경점 저장
    img_name = {'cat':'cat.png', 'dog':'dog.png', 'pig':'pig.png', 'sunglass':'sunglass.png'}#필터별 이미지 파일 이름
    w_overlayval = {'cat':0, 'dog':0, 'pig':-20, 'sunglass':0} #필터별 오버레이 x좌표의 증감값
    h_overlayval = {'cat':0, 'dog':0, 'pig':-80, 'sunglass':-50} #필터별 오버레이 y좌표의 증감값
    w_overlaysize = {'cat':150, 'dog':150, 'pig':150, 'sunglass':110} #필터별 오버레이 넓이의 증감값
    h_overlaysize = {'cat':200, 'dog':170, 'pig':200, 'sunglass':80} #필터별 오버레이 길이의 증감값
    
    camera = cv2.VideoCapture(0) #카메라 설정

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1600) #카메라 가로 길이
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 900) #카메라 세로 길이

    #컴퓨터 기종에 따라 가로세로 길이 설정이 안될 수 있음
    #frame = cv2.resize(frame, (1920, 1080)) #설정은 되지만 비율이 안 맞는 문제

    # 얼굴을 찾고, 찾은 얼굴에 표시를 해주기 위한 변수 정의
    mp_face_detection = mp.solutions.face_detection  # 얼굴 검출을 위한 face_detection 모듈을 사용

    # 이미지 불러오기
    filter_img = cv2.imread(img_name[filter_name], cv2.IMREAD_UNCHANGED)  # 알파 채널 포함하여 읽기

    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.7) as face_detection:
        while camera.isOpened():
            ret, frame = camera.read() #카메라 입력 (반환값 ret, frame)
            if not ret: #카메라 오류의 경우
                break

            # 성능 향상을 위해 이미지를 읽기 전용으로 적용
            frame.flags.writeable = False
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(frame)

            # frame에 얼굴 검출 주석을 그림
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            if results.detections:
                # 6개 특징 : 오른쪽 눈, 왼쪽 눈, 코 끝부분, 입 중심, 오른쪽 귀, 왼쪽 귀 (귀구슬점, 이주)
                for detection in results.detections:
                    # 특정 위치 가져오기
                    keypoints = detection.location_data.relative_keypoints
                    nose_tip = keypoints[2]  # 코 끝부분

                    h, w, _ = frame.shape  # height, width, channel :    이미지로부터 세로, 가로 크기 가져옴
                    # 이미지 내에서 실제 좌표 (x, y)
                    nose_tip = (int(nose_tip.x * w + w_overlayval[filter_name]), int(nose_tip.y * h + h_overlayval[filter_name]))

                    # 각 특징에 이미지를 오버레이
                    overlay(frame, *nose_tip, w_overlaysize[filter_name], h_overlaysize[filter_name], remove_grabcut_bg(filter_img))

            # frame을 좌우 반전 형태로 송출
            cv2.imshow('Webcam', cv2.resize(frame, None, fx=0.5, fy=0.5))

            if cv2.waitKey(1) == ord('c') : #촬영 버튼이 눌리면(임시키 c키)
                cv2.imwrite('img.jpg',frame) #캡쳐한 사진을 파일로 저장
                win3()
                camera.release() #카메라 해제
                cv2.destroyAllWindows() # 창 닫기
                break

window1 = Tk()

l0 = Label(window1, text = "자신이 원하는 필터를 선택하세요",   bg="lightsalmon", height= 2)
l0.pack()

bt2 = Button(window1, text="필터 1 : 고양이", command=filter1, fg="slateblue", bg="beige")
bt2.pack()

bt3 = Button(window1, text="필터 2 : 강아지", command=filter2, fg="tomato", bg="khaki")
bt3.pack()

bt4 = Button(window1, text="필터 3 : 돼지", command=filter3, fg="slateblue", bg="beige")
bt4.pack()

bt5 = Button(window1, text="필터 4 : 선글라스", command=filter4, fg="tomato", bg="khaki")
bt5.pack()
            
window1.mainloop()
