# **Mouse Control Project**
This project controls the mouse by taking a video of the user and wherever the hand moves, the cursor follows. When the user joins the thumb and the index finger, it is considered as a left click and when the user joins the middle finger and the thumb, it is considered as a right click. This project ensures that manual mouse control is not used.

## **Libraries Used**
The libraries used are:-
1) pyautougui
2) cv2
3) numpy
4) mediapipe

```
import cv2
import mediapipe as mp
import pyautogui
import numpy as np
```

### **Pyautogui**
Pyautogui is a python library which helps the coder to insert human-like GUI animations. It includes scripts which can control the mouse, type letters on keyboard, click buttons, drag and drop and also take screenshots on their own. It is onlyapplicable in _Windows_, _macOS_ and _Linux_. In this prject, it has been used to move the mouse and clicks.
```
pyautogui.moveTo(curr_x, curr_y)
pyautogui.click()
pyautogui.rightClick()
```

### **CV2**
_CV2_ is an open source and free platform used for image processing, computer visions and machine learning. It enables a coder to inculcate the use of camera and pethora of tasks related to image processing. It has been used for image processing in this project.
```
cap = cv2.VideoCapture(0)
img = cv2.flip(img, 1)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

### **Mediapipe**
_Mediapipe_ is an open-source library used for creating, customizing and deploying machine learning solutions._Mediapipe_ is identifying hands, comprehending and drawing landmarks.
```
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
result = hands.process(rgb)
```

### **NumPy**
The full form of _Numpy_ is _Numerical Python_. It is being used for calculating the hypotenuse(distance) between two fingers for recogonizing a click. From, _Numpy_, we also use interpolation.

```
screen_x = np.interp(x1,[0, w], [0, screen_w])
screen_y = np.interp(y1,[0, h], [0, screen_h])

return np.hypot(p1[0] - p2[0], p1[1] - p2[1])
```
## **How It Works**
It first takes the size of the laptop/desktop screen and then uploads the hand solution from _Mediapipe_. 
After it starts capting the video, a forever while loop is started. In that the frame is read, the frame is flipped, the shape of the frame is exracted and we convert BGR to RGB as _Mediapipe_ does not use BGR.
If any hand is detected, the x, y coordinated are converted to pixel values, landmarks are drawn in the frame and different variables represent the x, y cooardinates of the index, thumb and the middle finger. After this, the interpolation takes place. Then, by using _pyautogui_, the code moves the mouse.
After you press the escape button, the video recording stops and all the open windows related to the project close.
