# Overview of Project
It is a basic program in which a user sets an object in a video to track an object.
You can modify this program whatever you want.
We are looking for modifying this program, for example, Camera chasing, drawing heatmap of object, etc.

---

# Video Examples of project#
You can see Examples of this project in 'Examples' Directory

---

# Info of Packages
### Built-in Module
```python
import sys
```
### Third-party Module
Please install these third-party module in bash or terminal of your system.
```bash
pip install opencv-python==4.8.1.78
pip install opencv-contrib-python==4.5.3.56
pip install numpy==1.21.6
```

---
# How to Use
### 1. Setting video
Before starting the program, enter the address of the video file in source.py you want to play.
-line 14 in source.py
```python
video_path = 'game.mp4' #set file directory you want to play
```
### 2. Set Target and play
After you start the program, drag the mouse in the 'Select Target' window to set the target to track and press the ESC key
### 3. Playing Video
If the 'Objcet Tracker' window pops up, the process is successed, 
You could end video whenever you want by Typing ESE key, or if the video plays its end, It automatically ends window.
### 4. How to Debug info
If you want to check the information of an object that are tracked on video, set the debug variable in source.py to True

-line 12 in source.py
```python
debug = True # to check info in video, set True
```
Info that would be debugged  

-line 77 in source.py
```python
        if debug:
            cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)
            cv2.putText(frame, str(object_center), (0,100),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 0), 2, cv2.LINE_AA) #debugging coordinate of position
            cv2.circle(frame, (center_x, center_y), 5, (0,255,0), -1) #debugging center point
```
---
