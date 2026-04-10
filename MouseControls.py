import cv2
import mediapipe as mp
import pyautogui
import numpy as np

screen_w, screen_h = pyautogui.size() # takes the size of the screen of the desktop
mp_hands = mp.solutions.hands # uploading the solution of hands from mediapipe
hands = mp_hands.Hands(max_num_hands = 1) # can recogonize only one hand at a time
mp_draw = mp.solutions.drawing_utils # code for uploading the process of drawing the landmarks
cap = cv2.VideoCapture(0) # capturing video through the desktop's original camera
prev_x, prev_y = 0, 0 # starting x, y
smoothning = 7 # smoothning set to 7. More the value of smoothing, smoother the mouse but laggier.

while True: # forever loop
    success, img = cap.read() # reading the frame
    img = cv2.flip(img, 1) # flipping the read image
    h, w, _ = img.shape # finding height, width and the color channel of the frame
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converting the use of bgr to rgb as mediapipe uses rgb
    result = hands.process(rgb) # processing the image using 'hands' from mediapipe
    if result.multi_hand_landmarks: # if any hand detected
        for handLms in result.multi_hand_landmarks:  # iterating through the results after process
            lm_list = []
            for id, lm in enumerate(handLms.landmark): # iterating through each id, lm
                cx, cy = int(lm.x*w), int(lm.y*h) # converting x, y values so that they work in the form of pixels
                lm_list.append((id, cx, cy)) # apending id, and the coordinates in pixels.
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS) # drawing the landmarks
            if lm_list: # if there is any value in lm_list
                x1, y1 = lm_list[8][1], lm_list[8][2] # x1, y1 represent the coordinates of the index finger
                x2, y2 = lm_list[4][1], lm_list[4][2] # x2, y2 represent the coordinates of the thumb finger
                x3, y3 = lm_list[12][1], lm_list[12][2] #x3, y3 represent the coordinates of the middle finger
                screen_x = np.interp(x1,[0, w], [0, screen_w])
                screen_y = np.interp(y1,[0, h], [0, screen_h])

                curr_x = prev_x + (screen_x - prev_x)/smoothning # setting curr_x to the new coordinate after the hand moves
                curr_y = prev_y + (screen_y - prev_y)/smoothning # setting curr_y to the new coordinate after the hand moves

                pyautogui.moveTo(curr_x, curr_y) # moving to the set values
                prev_x, prev_y = curr_x, curr_y # the previous x, previous y now have the value of the current

                def distance(p1, p2):
                    return np.hypot(p1[0] - p2[0], p1[1] - p2[1]) # finding the distance between two fingers
                if distance((x1, y1), (x2, y2)) < 30: # using 'distance' func to find the distance between the index finger and the thumb
                    pyautogui.click() # if it is found out that their distance is less than 30px, it is counted as a left click
                    cv2.putText(img, 'Left Click', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) # printing 'Left Click' on screen
                if distance((x3, y3), (x2, y2)) < 30:# using 'distance' func to find the distance between the middle finger and the thumb
                    pyautogui.rightClick() # if it is found out that their distance is less than 30px, it is counted as a right click
                    cv2.putText(img, 'Right Click', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) # printing 'Right Click' on screen

    cv2.imshow('Hand Gesture Control', img) # showing the frame to users
    if cv2.waitKey(1) & 0xFF == 27: # if esc key is pressed, then the loop breaks
        break

cap.release() # the variable 'cap' doesn't record anymore
cv2.destroyAllWindows() # all the windows open due to the running of the code get closed.