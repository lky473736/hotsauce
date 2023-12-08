# hotsauce
(for teamplay on temp-repo) Implemented using OpenCV and tkinter by the face recognition and filter program
  
***2023-2 openSW 텀프로젝트 : 팀 핫소스 (임규연, 정예지, 유호찬, 임남령)  
<OpenCV 및 tkinter를 사용하여 얼굴 필터 및 이미지 편집기 구현>*** 
      
**NAVER LINE사에서 제작한 얼굴인식 필터 및 이미지 편집기인 SNOW에서 아이디어를 착안하여,  
본 팀은 OpenCV를 활용한 recognition과 filtering, tkinter를 활용한 GUI 개발을 진행. 
철저한 협업 소프트웨어 공학을 적용하여 단계적으로 version-controlling** 

--------

### 프로그램 실행 방법

1) 본 프로그램을 실행하기 전, 아래 '사용 라이브러리 및 테크' 파트에서 자신의 가상환경이 이를 충족하고 있는지를 확인하십시오.
2) 본 프로그램을 실행하기 전, filter_img 파일에 있는 4개의 png 파일을 hotsauce.py와 같은 디렉토리에 놓아주십시오.  

--------

### 프로그램 설명 

**본 프로그램이 시작되면 필터를 고를 수 있는 window가 등장합니다.** 필터는 총 4가지로, cat, dog, pig, sunglasses로 구성되어 있습니다. 필터를 고르면, **mediapipe의 얼굴 인식 모델과 웹캠이 작동하여 사용자의 얼굴에 필터가 덧대어집니다.** 키보드 **'c'키**를 누르는 순간 **화면이 캡쳐되고 이미지를 편집할 수 있는 window**가 등장합니다. 캡처된 이미지를 총 6가지의 기능을 통해 reshaping할 수 있으며, 기능은 **흑백, 사이즈 변경, 이미지 회전, 좌우/상하 대칭, 이미지 윤곽선, 이미지 윤곽선 사각형 (객체인식)** 이 있습니다. 원하는 편집 기능 버튼을 누르면 편집 기능이 적용된 이미지를 각자의 기능의 이름에 맞게끔 사용자의 현재 디렉토리에 저장됩니다.

--------

### 사용 라이브러리 및 테크  

* 테크 :
  * Visual Studio Code 2023 Community
  * Python 3.11.6
 
* 라이브러리 :
  * **mediapipe 0.10.8** : 객체 인식 
  * **cv2 4.8.1.78** : 객체 인식 엔진 (OpenCV : Computer Vision)
  * **tkinter** (Python 내장) : GUI 구현
  * **pillow 10.1.0** : GUI 내 이미지 리사이징 및 이미지 첨부
  * **time** (Python 내장) : 이미지 저장 시에 

--------

### 1단계 : 프로젝트 기획 및 시안 작성 (pseudo-code, guideline)
      
1) **1단계** : pseudo-code 작성 : 임규연 : 2023.11.20.   
전체 code의 흐름 파악을 위한 pseudo-code 작성
  
3) **1.5단계** : GUI 가이드라인 개발 : 임규연 : 2023.11.25.    
향후 tkinter를 사용한 GUI 개발을 위한 가이드라인 개발 
  
![화면-기록-2023-11-25-오전-12 18 34 (1)](https://github.com/lky473736/hotsauce/assets/84794782/ab35015c-70e7-4de9-89a9-bfcdefd7ee6e)  
  
-------  

### 2단계 : 얼굴인식 및 필터링 세부 기능 구현, 이미지 편집 기능 구현 : 유호찬, 임남령, 임규연 (face-recognition, mediapipe, editing)  

1) **2단계** : 얼굴인식 및 필터링 세부 기능 구현 : 유호찬, 임남령  
* 개발 기간 : 2023.11.20. ~ 2023.11.25.  
  참고자료 : https://github.com/lky473736/hotsauce/blob/main/source.md
    
2) **2.5단계** : 이미지 편집 세부 기능 구현 : 임규연  
* 개발 기간 : 2023.11.27.    
  
-------

### 3단계 : GUI 윈도우 구현 : 정예지 (Implementation GUI using tkinter)  
* 개발 기간 : 2023.11.27. ~ 2023.12.08.

<img width="218" alt="스크린샷 2023-12-08 오후 6 13 18" src="https://github.com/lky473736/hotsauce/assets/84794782/7e106544-6277-43df-abd0-4e774ee6f45b">

> 위의 예시 사진은 실제 얼굴 사진이 아닌 '몽글몽글 cinamoroll'로 하였음을 양해 바랍니다. (https://www.ebay.com/itm/175648586637)

-------

### 4단계 : 버그 픽스 및 최적화, 리팩터링 및 최종 프로그램 완성 : 임규연 (Bug fixing, Refactoring, Completion the project)  
* 개발 기간 : 2023.12.08 ~ 2023.12.09.  
  
  버그 픽스 내용 :  
  * GUI에 부모 창을 따로 설정하지 않아 PhotoImage의 작동 오류 발생 (다른 창에 이미지 보여지는 오류 & 아예 이미지가 보이지 않는 오류)
      -> open 함수 및 상대 경로 설정하여 해결
  * 전체적인 리펙토링 (주석 작성 및 indentation 수정)
  * 필터별 오버레이 길이의 증감값 argument 및 이목구비의 detection 좌푯값 알고리즘 수정 (효과적으로 안면인식을 할 수 있도록)
  * repository를 배포 형태로 수정
