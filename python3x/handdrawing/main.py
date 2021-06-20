import cv2
import mediapipe as mp
import numpy as np
import math

red_color = (0, 0, 255, 255)
green_color = (0, 255, 0, 255)
blue_color = (255, 0, 0, 255)
selectedColor = red_color

ALLCOLORS = [red_color, green_color, blue_color]

ZDEEP = -0.12

def RadCollide(obj1X, obj1Y, obj1C, obj1R, obj2X, obj2Y, obj2C, obj2R):
    dx = (obj1X + obj1C) - (obj2X + obj2C)
    dy = (obj1Y + obj1C) - (obj2Y + obj2C)
    dist = math.sqrt(dx * dx + dy * dy)

    return dist < (obj2R + obj1R)

def IsPontingWithIndex(landmarks):
    return (landmarks[8].y < landmarks[6].y) \
        and (landmarks[12].y > landmarks[10].y) \
            and (landmarks[16].y > landmarks[14].y) \
                and (landmarks[20].y > landmarks[18].y)

def PrintHud(image):
    startPosition = 40
    jump = 70
    currentPosition = 0

    for color in ALLCOLORS:
        cv2.circle(image, ((startPosition + currentPosition * jump), 30), 20, color, cv2.FILLED)
        currentPosition += 1

def SwapColor(x, y):
    startPosition = 40
    jump = 70
    currentPosition = 0
    
    for color in ALLCOLORS:
        circleX = startPosition + currentPosition * jump

        if RadCollide(x, y, x, 50, circleX, 30, circleX, 50):
            return color

        currentPosition += 1
    
    return selectedColor


height, width = 1280, 720

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

#STATIC_IMAGE_MODE False
#MAX_NUM_HANDS 2
#MIN_DETECTION_CONFIDENCE 0.5
#MIN_TRACKING_CONFIDENCE 0.5
hands = mpHands.Hands(False, 1, 0.65, 0.65)

success, img = cap.read()
height, width, center = img.shape

layer1 = np.zeros((height, width, 3), np.uint8)

linePointX, linePointY = -1, -1

#screen_res = 1024, 768
#scale_width = screen_res[0] / width
#scale_height = screen_res[1] / height
#scale = min(scale_width, scale_height)
#window_width = int(width * scale)
#window_height = int(height * scale)

while True:
    success, img = cap.read()
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:

            indexFinger = handLandmarks.landmark[8]
            thumbFinger = handLandmarks.landmark[4]

            tX, tY = int(thumbFinger.x * width), int(thumbFinger.y * height)
            iX, iY = int(indexFinger.x * width), int(indexFinger.y * height)
            cv2.circle(img, (tX, tY), 3, selectedColor, cv2.FILLED)
            cv2.circle(img, (iX, iY), 3, selectedColor, cv2.FILLED)

            isPointing = IsPontingWithIndex(handLandmarks.landmark)

            if isPointing and indexFinger.z <= -0.4:
                selectedColor = SwapColor(iX, iY)

            if indexFinger and thumbFinger and not isPointing:
                isColliding = RadCollide(tX, tY, tX, 25, iX, iY, iX, 25)

                if isColliding and indexFinger.z <= ZDEEP:
                    if linePointX == -1:
                        linePointX, linePointY = tX, tY
                    
                    cv2.line(layer1, (linePointX, linePointY), (tX, tY), selectedColor, thickness=10)
                    linePointX, linePointY = tX, tY

                else:
                    linePointX, linePointY = -1, -1
                    

            #for id, lm in enumerate(handLandmarks.landmark):
            #    lmX, lmY = int(lm.x * width), int(lm.y * height)

            #    if id == 8:
                    #cv2.circle(img, (lmX, lmY), 15, (255, 0, 255), cv2.FILLED)
            #        cv2.circle(layer1, (lmX, lmY), 5, red_color, cv2.FILLED)

            #mpDraw.draw_landmarks(img, handLandmarks, mpHands.HAND_CONNECTIONS)

    imgGray = cv2.cvtColor(layer1, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, layer1)

    PrintHud(img)
    img = cv2.flip(img, 1)
    
    #cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("Image", window_width, window_height)
    cv2.imshow("Image", img)

    cv2.waitKey(1)