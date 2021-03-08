import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # Take each frame
    _, image = cap.read()

    #resize video
    frame = cv2.resize(image,None,fx=0.7,fy=0.7)
    frame2 = frame.copy()
    # convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower = np.array([35,50,50])
    upper = np.array([100,255,255])
    mask = cv2.inRange(hsv,lower,upper)
    #bitwise 
    res = cv2.bitwise_and(frame,frame ,mask=mask)
    #Threshold
    _,thr = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
    #morphological
    opening = cv2.morphologyEx(
        thr,
        cv2.MORPH_OPEN,
        np.ones((3,3),
        np.uint8),
        iterations=5)

    #Drawing Contours
    contours,_ = cv2.findContours(opening,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    #Canny
    canny = cv2.Canny(opening,threshold1=0,threshold2=50)

    for i in range(len(contours)):
        cv2.drawContours(frame2,contours,i,(130,255,255),3)

    cv2.imshow('original',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('thr',thr)
    cv2.imshow('open',opening)
    cv2.imshow('bitwise',res)
    cv2.imshow('canny',canny)
    cv2.imshow('Contour',frame2)
    k = cv2.waitKey(5) & 0xFF
    if k == 27 :
        break

cv2.destroyAllWindows()
