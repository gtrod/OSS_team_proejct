import cv2
import sys

video_path = './video/game.mp4'

# 기본 카메라 객체 생성
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

while True: # 무한 루프
    # ret - 프레임 읽으면 True, 못 읽으면 False 반환
    # frame - 읽은 프레임 이미지 저장
    ret, frame = cap.read()
    if not ret:
        break

    # 읽어온 프레임 실행
    cv2.imshow('frame', frame)

    # 16ms마다 한 프레임 세팅 + Esc누르면 while 종료
    if cv2.waitKey(16) == 27:
        break

cap.release() # cap 객체 free시킴
cv2.destroyAllWindows() # 창 닫기
