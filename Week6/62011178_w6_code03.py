import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30,30)
    )
    
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    
    cv2.imshow("Face detection",img)
    k = cv2.waitKey(30)& 0xff
    if k ==27 :
        break
cap.release()
cv2.destroyAllWindows()