# Please download modules to execute program through these commands Before you use this program.
""" 
     pip install opencv-python==4.8.1.78
     pip install opencv-contrib-python=4.5.3.56
     pip install numpy==1.21.6
"""


import cv2
import sys

debug = True # to check info in video, set True

video_path = 'game.mp4' #set file directory you want to play

# Create default camera object
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

# Actively calculates delay of frame
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)


# exception to failure of reading first frame
if not ret:
    print("Failed to read the first frame!")
    sys.exit()
tracker = cv2.legacy.TrackerCSRT_create()

# selecting object that would be tracked
# Setting object by drag mouse point
# Play video by typing ESC after setting object
try:    
    bbox = cv2.selectROI("Select Ball", frame, fromCenter=False, showCrosshair=True)
except cv2.error as e: # exception of error
    print("Error during ROI selection:", e)
    sys.exit()

# exception when opening video is failed
if not cap.isOpened():
    print("video open failed!")
    sys.exit()

# setting video size
desired_width = 640
desired_height = 480

# initialize tracker
tracker.init(frame, bbox)

while True:  # tracking video loop
    
    # ret | True: successed reading and tracking, False: failed reading
    # frame | valuse that stores new frame successed to tracking
    ret, frame = cap.read()
    # exception to failure of reading frame
    if not ret:
        print("Failed to read the frame!")
        break

    # Updating tracked object
    success, bbox = tracker.update(frame)

    if ret:
        # Convert bbox to int type
        bbox = tuple(map(int, bbox))
        
        #Info of object position
        (x,y,w,h) = bbox # x, y : point of coordinate | w, h : length of box
        center_x = int(x + w / 2)
        center_y = int(y + h / 2)
        object_center = (center_x, center_y) #center point of Box
        
        # Debugging info in video | to see these infos in video, set debug True
        # Showing box of tracked object in video
        if debug:
            cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)
            cv2.putText(frame, str(object_center), (0,100),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 0), 2, cv2.LINE_AA) #debugging coordinate of position
            cv2.circle(frame, (center_x, center_y), 5, (0,255,0), -1) #debugging center point
    
    # Update frame that are retracked object
    cv2.imshow('frame', frame)

    # Delay of frames and escaping case when typing ESC
    if cv2.waitKey(delay) == 27:
        break

cap.release()  # Free the tracking object
cv2.destroyAllWindows()  #closing video
