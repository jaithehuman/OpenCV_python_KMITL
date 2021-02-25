import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")

img = cv2.imread("dataset/nasa.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=2,
        minSize=(20,20)
)

print("Detected {0} faces!".format(len(faces)))

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Faces Detected",img)
cv2.waitKey(0)
cv2.destroyAllWindows