#프로그램을 실행시키기 위해선 terminal에 pip install opencv-contrib-python 필요 

import cv2
import sys

video_path = './video/game.mp4'

# 기본 카메라 객체 생성
cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()
#첫 frame을 읽지 못 했을 시 예외처리
if not ret:
    print("Failed to read the first frame!")
    sys.exit()
tracker = cv2.legacy.TrackerCSRT_create()

#객체 선택 (드래그 하여 객체 설정 + ESC누르면 영상 재생)
# 예외 발생 시 오류 처리
try:
    bbox = cv2.selectROI("Select Ball", frame, fromCenter=False, showCrosshair=True)
except cv2.error as e:
    print("Error during ROI selection:", e)
    sys.exit()

object_position = []

# 영상이 제대로 열리지 않았을 때 예외 처리
if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 비디오 크기 설정
desired_width = 640
desired_height = 480

# 초기 추적 설정
tracker.init(frame, bbox)

while True:  # 무한 루프
    # ret - 프레임 읽으면 True, 못 읽으면 False 반환
    # frame - 읽은 프레임 이미지 저장
    ret, frame = cap.read()
    # frame을 읽지 못 했을 시 예외처리
    if not ret:
        print("Failed to read the frame!")
        break

    # 추적 업데이트
    success, bbox = tracker.update(frame)

    if success:
        object_center = (int(bbox[0] + bbox[2] / 2), int(bbox[1] + bbox[3] / 2))
        print("Object position:", object_center)

    if ret:
        # int로 변환
        bbox = tuple(map(int, bbox))
        
        # 추적 물체 사각형으로 위치 표현
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 2)

    # 읽어온 프레임 실행
    cv2.imshow('frame', frame)

    # 20ms 마다 한 프레임 세팅 + Esc누르면 while 종료
    if cv2.waitKey(40) == 27:
        break

cap.release()  # cap 객체 free시킴
cv2.destroyAllWindows()  # 창 닫기