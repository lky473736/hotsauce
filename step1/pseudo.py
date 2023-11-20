'''
    2023-2 openSW 텀프로젝트 : 팀 핫소스 (임규연, 정예지, 유호찬, 임남령)
    가칭 : <OpenCV 및 tkinter를 사용하여 얼굴 필터 및 이미지 편집기 구현>
    
    NAVER LINE사에서 제작한 얼굴인식 필터 및 이미지 편집기인 SNOW에서 아이디어를 착안하여,
    본 팀은 OpenCV를 활용한 recognition과 filtering, tkinter를 활용한 GUI 개발을 진행할 예정.
    
    1단계 : pseudo-code 작성 : 임규연 작성 : 2023.11.20. 
    2단계 : 얼굴인식 및 필터링 세부 기능 구현 : 유호찬, 임남령 : 
    2.5단계 : 이미지 편집 세부 기능 구현 : 임규연 : 
    3단계 : GUI 윈도우 구현 : 정예지 :
    4단계 : 최적화 : 임규연 : 
    5단계 : 버그 픽스 : 
    
    pseudo-code는 pascal 기반으로 작성하려고 했으나, python 언어로 변환하기 어려울까봐
    python 언어로 작성하겠습니다. 
    기능을 구현하실 때 주석을 지우지 말고 코드를 작성해주세요.
'''

'''
    1) 프로그램 실행 시, 필터를 고를 수 있는 윈도우1이 등장하며, 사용자는 필터 n개 중 하나를 고른다
    2) 웹캠 화면과 촬영버튼이 있는 윈도우2가 등장하며, 웹캠 화면엔 자신이 고른 필터가 씌워진 모습이 등장.
    3) 사용자가 촬영버튼을 누르면 다양한 편집기능을 지원하는 윈도우3이 등장함.
    4) 윈도우3에서 종료버튼을 누르면 EOF
    
    윈도우2 기능 구현 : 유호찬, 임남령
    전체적인 윈도우 GUI, 버튼 구현 : 정예지
    윈도우3 기능 구현 : 임규연
    최적화 : 임규연
'''

import cv2
import tkinter 

# 우리는 tkinter (이하 tk)를 사용하여 버튼을 구현해야 합니다.
# tk 버튼은 반응식이기 때문에, 모든 세부 기능은 전부 사용자 지정 함수 (def)로 구현하셔야 합니다.

# 세부 기능 목록 : 촬영, 흑백기능, 사이즈 조절 기능, 회전기능 (90, 180, 270), 좌우/상하 대칭, 윤곽선 그리기 (contour), 경계 사각형 (boundaryRect) ...
# 각 세부 기능은 제가 구현하겠습니다. 혹시나 세부 기능이 이해가 되지 않으신다면 아래 repo를 참고해주세요.
# https://github.com/lky473736/temp-repo/tree/main/OpenCV/learning%20set

# 각 사용자 지정 함수의 parameter는 사용자가 원하는 기능의 인자와, 촬영되어 저장된 사진이 될 것입니다. 
# 하지만, parameter를 굳이 작성하지 않고 tk의 text input으로부터 GET을 해올 수 있으니 사용하지 않을 것입니다. 또한 save()에서 저장한 'img.jpg'는 global 변수로 대응시킬 예정이라서 더욱이 각 기능마다 parameter는 필요 없습니다.

    
def grayscale () : # 임규연 구현 부분
    '''
    흑백 기능을 구현
    '''
    img_gray = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    cv2.imshow ('img_gray', img_gray)
    
    
def change_size () : # 임규연 구현 부분
    '''
    사이즈 조절 기능을 구현 예시 (name : img.jpg의 global 변수)
    '''
    
    size = float(e2.get())
    
    img_ori = cv2.imread(name)
    img_dst = cv2.resize(img_ori, None, fx = size, fy = size)
    
    cv2.imshow(f'img_dst = {size}', img_dst)
    
    
def rotate () : # 임규연 구현 부분
    '''
    이미지 회전 기능을 구현 예시 (name : img.jpg의 global 변수)
    '''
    
    angle = float(e2.get())
    
    img_ori = cv2.imread(name)
    
    if angle == 90 :
        img_rot = cv2.rotate(img_ori, cv2.ROTATE_90_CLOCKWISE)
        
    else :
        img_rot = cv2.rotate(img_ori, cv2.ROTATE_180)
        
    cv2.imshow(f'img_rot = {angle}', img_rot)
    
    
def symmetric () : # 임규연 구현 부분
    '''
    좌우/상하 대칭 기능을 구현 예정
    '''
    
def contour () : # 임규연 구현 부분
    '''
    이미지 윤곽선 검출 기능을 구현 예정
    '''
    
def boundaryrect () : # 임규연 구현 부분
    '''
    객체 윤곽선 사각형 검출 기능을 구현 예정
    '''

def exit() : # 임규연 구현 부분
    exit() # 종료 버튼
    
def win3() : # 정예지, 임규연 구현 부분
    '''
        사용자가 촬영 버튼을 누르면, 윈도우3을 열어야 합니다. 
        본 부분이 윈도우3을 구현할 부분입니다.
    '''
    
    윈도우3 선언 
    textinput 만듦 (각 기능의 parameter가 될 것임)
    버튼 만듦 (버튼의 갯수 : 기능의 갯수)
    
def win2(필터 이름) : # 유호찬, 임남령, 임규연, 정예지 구현 부분
    '''
        윈도우2에선 사용자의 얼굴을 인식하는 부분, 필터를 덧대는 부분, 촬영하는 부분으로 나눠져야 할 것입니다.
        촬영은 곧 웹캠의 한 프레임을 저장하는 기능이 됩니다.
        파일명을 'img.jpg'로 저장하게끔 할 예정이고, 그 파일명을 global 변수로 만들 예정입니다.
    '''
    
    윈도우2 선언
    버튼 만듦
    
    카메라 출력 부분 (videoCapture() 사용)
    
    if 여는걸 실패하였을 때 : 
        프로그램 종료
        
    while True :
        cap.read() 함수 사용 (반환값 ret, frame)

        cv2.imshow('webcam', frame)
    
        ''' 
            여기서 얼굴인식, 필터 적용 코드 작성하시면 될 듯 합니다.
            자유롭게 하시면 될 것 같습니다.
        '''
        
        if 촬영 버튼이 눌리면 :
            현재 웹캠 화면을 캡처 
            win3() 
    
def win1() : # 임규연 구현 부분
    '''
    필터를 고르는 부분입니다. 
    필터를 고르면 고른 필터 이미지 이름을 win2에 return할 겁니다. 
    '''
    
filter_name = win1()
win2(filter_name)
