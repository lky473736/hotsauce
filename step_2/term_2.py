import cv2
import mediapipe as mp

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
    
    #윈도우2 선언
    #버튼 만듦
    
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
                cv2.imwrite('img.jpg',frame) #캡쳐한 사진을 파일로 저장]
                camera.release() #카메라 해제
                cv2.destroyAllWindows() # 창 닫기
                #win3()
                break

#filter_name = win1()
filter_name = 'cat' #임시 필터 이름 / 필터는 cat, dog, pig, sunglass 총 4개로 이루어짐
win2(filter_name)